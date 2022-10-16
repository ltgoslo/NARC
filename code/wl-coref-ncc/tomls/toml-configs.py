# %% [markdown]
# ## Take the basic toml config file, and make iterations

# %%
import toml
import os
# from transformers import AutoModel, BertModel, AutoModelForMaskedLM



# %%
source = "/fp/homes01/u01/ec-egilron/wl-coref-ncc/config.toml"
toml_folder = "/fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls"
train_path = "/fp/homes01/u01/ec-egilron/ncc/wl-ncc_heads/wl-ncc_train_head.jsonl"
runpath = "/fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py"
fox_slurm_base = "/fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/fox_base.slurm"

with open(source) as rf:
    base_toml ={'DEFAULT': toml.loads(rf.read())['DEFAULT']}

defaults = base_toml['DEFAULT']
# for key, value in defaults.items():
#     print(key,":\t", value)




# %% [markdown]
# ## Changes from the default that is shared by all experiments go here

# %%

# models03: Iterate batch size for memory iussues. 4 epochs.

run_id = "models04"
defaults["rough_k"] = 50

defaults["bert_model"] = "/fp/homes01/u01/ec-egilron/transformers/nb-bert-base"
defaults["device"] = "cuda:0"
defaults["bert_finetune"] = True
defaults["train_epochs"] = 20
defaults["train_data"] = train_path
defaults["dev_data"] = train_path.replace("train", "development")
defaults["test_data"] = train_path.replace("train", "test")
out_folder = os.path.join(toml_folder, run_id)
defaults["conll_log_dir"] = os.path.join(out_folder, "conll_logs")
defaults["data_dir"] = out_folder
if not os.path.exists(out_folder):
    os.mkdir(out_folder)
    if not os.path.exists(defaults["conll_log_dir"]):
        os.mkdir(defaults["conll_log_dir"])


# %% [markdown]
# ## Create lists of what should be iterated over, and write a toml file with each of these experiments in the one file
# Start without any grid, list only

# %%
# alternatives = {"bert_models": ["/fp/homes01/u01/ec-egilron/norbert2", "xlm-roberta-base", "bert-base-multilingual-cased", "/fp/homes01/u01/ec-egilron/nb-bert-base"]}
# alternatives = {"bert_models": ["/fp/homes01/u01/ec-egilron/transformers/nb-bert-base",  "xlm-roberta-base"]}
alternatives = {"bert_model": ["/fp/homes01/u01/ec-egilron/transformers/nb-bert-base", "/fp/homes01/u01/ec-egilron/transformers/221", "xlm-roberta-base", "bert-base-multilingual-cased" ]}
exp_ids = []
out_toml = {'DEFAULT': defaults}
for param_name, alts in alternatives.items():
    for idx, alt in enumerate(alts):
        experiment_id = run_id+"_"+str(idx).zfill(3)
        out_toml[experiment_id] = {param_name: alt}
        exp_ids.append(experiment_id)
out_toml_path = os.path.join(toml_folder, run_id+".toml")
with open(out_toml_path, "w") as wf:
    toml.dump(out_toml, wf)

def check_models(m_list):

    from transformers import AutoModel
    for model in m_list:
        print("Checking model:", model)
        if model[0] == "/":
            try:
                m = AutoModel.from_pretrained(model, local_files_only=True).to("cpu")
                print("success load local")
            except (OSError, ValueError) as e:
                print("failure load local", model)
                print(e)
        
        else:
            try:
                m = AutoModel.from_pretrained(model).to("cpu")
                print("success", model)
            except OSError as e:
                print("failure", model)
        # print(e, "\n")

# check_models(alternatives["bert_models"])


# %% [markdown]
# ## Norwegian models
# Got them to run with cloned and local path, and torch=1.6 in stead of 1.4


# %% [markdown]
# ## Create script
# 


script_path = os.path.join(toml_folder, run_id+".sh")
fox_slurm_path = os.path.join(toml_folder, run_id+"_fox.slurm")
scriptlines  = ["#!/bin/sh"]
for exp in exp_ids:
    scriptlines.append(f'echo "Starting experiment {exp}" ')
    scriptlines.append(" ".join(["python", runpath, "train", exp, "--config-file", out_toml_path]))




# print(runpath)
# print("\n".join(scriptlines))

fox = True
if fox:
    print(fox_slurm_path )
    with open(fox_slurm_base) as rf:
        base = rf.read()
        with open (fox_slurm_path, "w") as wf:
            out_file = base+"\n"+"\n".join(scriptlines[1:])
            wf.write(out_file) 

else:
    with open (script_path, "w") as wf:
        wf.write("\n".join(scriptlines))
    print(script_path)

# %%
# sudo apt-get install git-lfs
# git lfs install
# git clone https://huggingface.co/ltgoslo/norbert2




# Code for narc baseline
Baseline models for the Norwegian Anaphora Resolution Corpus
This repository is the actual working repo for the experiments, probably containing imperfect and redundant code. We hope it may still be useful for anyone who wish to inspect the baseline model referenced in **NARC – Norwegian Anaphora Resolution Corpus** by Petter Mæhlum et al. 

### Setup
- Use Python up to 3.9
    - a dump of requirements is found in `code/requirements.txt`
        - you might need to install `transformers` locally using `pip install -e .`
            - https://github.com/huggingface/transformers/releases/tag/v3.2.0
- For info about the HPC environment, see `wl-coref-ncc/tomls/fox_base.slurm`.

### Preprocessing 
Run `preprocess.py`


The script gathers the texts and annotations files from NARC. Annotated files are converted to jsonlines, one file per document. This format is selected to support other processing pipelines. This code is written or collected by [Tollef Jørgensen](https://github.com/tollefj). Data is then converted to the format that wl-coref requires and head information is inserted with the SpaCy Norwegian parser. This code is written and collected by [Egil Rønningstad](https://github.com/egilron) and is based on the preprocessing scripts in [wl-coref](https://github.com/vdobrovolskii/wl-coref).  
The end result is a folder with `_heads` suffix inside the `data` folder.

## Configure and execute training
- The parameters are set in the toml config file, the wl-coref original file is `wl-coref-ncc/config.toml`
- The training is executed through `python wl-coref-ncc/run.py train <experiment within the toml> <toml-file>`
- The scripts `wl-coref-ncc/tomls/toml-configs.ipynb`and `wl-coref-ncc/tomls/toml-configs.py`can be used to create modification of the toml. These files are working tools, and not neccessarily tidy.
    - An example script can be run, as found in *code/example_run.sh*. This runs a non-cuda variant for the highest compatability
        - `python code/wl-coref-ncc/run.py train BERT_MULTILING --config-file code/wl-coref-ncc/tomls/POC_nocuda.toml`
        - to run with CUDA, use the following example:
            - `python code/wl-coref-ncc/run.py train POC_003 --config-file code/wl-coref-ncc/tomls/POC.toml`

### Notes on the configuration
- The experiments require access to high-vram gpus. Preferable `>30 GB`. `rough_k` can be set to 5 to train on 12 GB resources, for lower performance debug runs.
- Some Norwegian transformers-based models might not download with the transformers Automodel. Attempt to load models from local files instead.
- Originally, wl-coref saves the model after each epoch. This is modified in *coref_model.py*, where `save_weights` is called.


##  Evaluation and prediction
We run the prediction in wl-coref, and evaluate with coreference-eval

### Predictions
norBERT2 and XLM-roBERTa

```
python wl-coref-ncc/predict.py POC2_000 data/wl-formatted/narc_development.jsonl POC2_000_dev_predicted.jsonlines --config-file experiments/tomls/POC2.toml
Loading /fp/homes01/u01/ec-egilron/transformers/221...

python wl-coref-ncc/predict.py POC2_000 data/wl-formatted/narc_test.jsonl POC2_000_test_predicted.jsonlines --config-file experiments/tomls/POC2.toml
Loading /fp/homes01/u01/ec-egilron/transformers/221...

python wl-coref-ncc/predict.py POC2_001 data/wl-formatted/narc_test.jsonl POC2_001_test_predicted.jsonlines --config-file experiments/tomls/POC2.toml
Loading xlm-roberta-base...

python wl-coref-ncc/predict.py POC2_001 data/wl-formatted/narc_development.jsonl POC2_001_dev_predicted.jsonlines --config-file experiments/tomls/POC2.toml
Loading xlm-roberta-base...

The underlying wl-coref model can be cited as follows:
```
@inproceedings{dobrovolskii-2021-word,
title = "Word-Level Coreference Resolution",
author = "Dobrovolskii, Vladimir",
booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
month = nov,
year = "2021",
address = "Online and Punta Cana, Dominican Republic",
publisher = "Association for Computational Linguistics",
url = "https://aclanthology.org/2021.emnlp-main.605",
pages = "7670--7675"}
```
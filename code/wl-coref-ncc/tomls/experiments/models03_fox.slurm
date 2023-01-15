#!/bin/bash
#SBATCH --job-name=narc
#SBATCH --mail-type=FAIL
#SBATCH --account=ec30
#SBATCH --partition=accel    # To use the accelerator nodes
#SBATCH --gpus=a100:1
#SBATCH --time=1:00:00      # Max walltime is 14 days.
#SBATCH --mem-per-cpu=32G
#SBATCH --nodes=1

set -o errexit  # Recommended for easier debugging
source /etc/profile
## Load your modules
module purge
module load PyTorch/1.9.0-fosscuda-2020b
python3 -m venv /fp/homes01/u01/ec-egilron/venvs/trans_nopt --clear
source /fp/homes01/u01/ec-egilron/venvs/trans_nopt/bin/activate
pip install jsonlines
pip install toml
pip install transformers==3.2.0


echo "Starting experiment models03_000" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_000 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_001" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_001 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_002" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_002 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_003" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_003 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_004" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_004 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_005" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_005 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_006" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_006 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_007" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_007 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
echo "Starting experiment models03_008" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models03_008 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models03.toml
#!/bin/bash
#SBATCH --job-name=models04
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


echo "Starting experiment models04_000" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models04_000 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models04.toml
echo "Starting experiment models04_001" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models04_001 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models04.toml
echo "Starting experiment models04_002" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models04_002 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models04.toml
echo "Starting experiment models04_003" 
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models04_003 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models04.toml
#!/bin/sh

# Etter salloc --ntasks=1 --mem-per-cpu=16G --time=02:00:00  --account=ec30 --partition=accel --gres=gpu:1
source /etc/profile
module purge
module load PyTorch/1.9.0-fosscuda-2020b
python3 -m venv /fp/homes01/u01/ec-egilron/venvs/trans_nopt --clear
source /fp/homes01/u01/ec-egilron/venvs/trans_nopt/bin/activate
pip install jsonlines
pip install toml
pip install transformers==3.2.0



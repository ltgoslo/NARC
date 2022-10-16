#!/bin/bash

#SBATCH --job-name=narc
#SBATCH --account=nn9851k
#SBATCH --mail-type=FAIL
#SBATCH --partition=accel    # To use the accelerator nodes
#SBATCH --gres=gpu:1
#SBATCH --time=08:30:00
#SBATCH --mem-per-cpu=24G
#SBATCH --ntasks-per-node=4

source ${HOME}/.bashrc

# sanity: exit on all errors and disallow unset environment variables
set -o errexit
set -o nounset


module --quiet purge 
module load  Python/3.8.6-GCCcore-10.2.0
python3 -m venv $USERWORK/venvs/trans_nopt --clear 
source $USERWORK/venvs/trans_nopt/bin/activate
python3 -m pip install -r $USERWORK/wl-coref-ncc/requirements.txt

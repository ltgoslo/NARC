#!/bin/sh
echo "Starting experiment CUDA01_000" 
python /cluster/work/users/egilron/wl-coref-ncc/run.py train CUDA01_000 --config-file /cluster/work/users/egilron/wl-coref-ncc/tomls/CUDA01.toml
echo "Starting experiment CUDA01_001" 
python /cluster/work/users/egilron/wl-coref-ncc/run.py train CUDA01_001 --config-file /cluster/work/users/egilron/wl-coref-ncc/tomls/CUDA01.toml
echo "Starting experiment CUDA01_002" 
python /cluster/work/users/egilron/wl-coref-ncc/run.py train CUDA01_002 --config-file /cluster/work/users/egilron/wl-coref-ncc/tomls/CUDA01.toml
echo "Starting experiment CUDA01_003" 
python /cluster/work/users/egilron/wl-coref-ncc/run.py train CUDA01_003 --config-file /cluster/work/users/egilron/wl-coref-ncc/tomls/CUDA01.toml
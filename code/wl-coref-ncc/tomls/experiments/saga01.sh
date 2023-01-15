#!/bin/sh
echo "Starting experiment saga01_000" 
python /cluster/work/users/egilron/wl-coref-ncc/run.py train saga01_000 --config-file /cluster/work/users/egilron/wl-coref-ncc/tomls/saga01.toml
echo "Starting experiment saga01_001" 
python /cluster/work/users/egilron/wl-coref-ncc/run.py train saga01_001 --config-file /cluster/work/users/egilron/wl-coref-ncc/tomls/saga01.toml
echo "Starting experiment saga01_002" 
python /cluster/work/users/egilron/wl-coref-ncc/run.py train saga01_002 --config-file /cluster/work/users/egilron/wl-coref-ncc/tomls/saga01.toml
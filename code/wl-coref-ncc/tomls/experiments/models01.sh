#!/bin/sh
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models01_000 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models01.toml
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models01_001 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models01.toml
python /fp/homes01/u01/ec-egilron/wl-coref-ncc/run.py train models01_002 --config-file /fp/homes01/u01/ec-egilron/wl-coref-ncc/tomls/models01.toml
#!/usr/bin/env python3

import argparse
import os
import re
import subprocess


def extract_f1(proc: subprocess.CompletedProcess) -> float:
    prev_line = ""
    curr_line = ""
    for line in str(proc.stdout).splitlines():
        prev_line = curr_line
        curr_line = line
    return float(re.search(r"F1:\s*([0-9.]+)%", prev_line).group(1))

# Tampered with by Egil. Check original wl-coref if you need that
if __name__ == "__main__":


    gold = "/fp/homes01/u01/ec-egilron/narc-baseline/experiments/tomls/POC5/conll_logs/POC5-norBERT2_dev_e20.gold.conll"
    pred = "/fp/homes01/u01/ec-egilron/narc-baseline/experiments/tomls/POC5/conll_logs/POC5-norBERT2_dev_e20.pred.conll"

    part_a = ["perl", "reference-coreference-scorers/scorer.pl"]
    part_b = [gold, pred]
    kwargs = {"capture_output": True, "check": True, "text": True}

    results = []
    for metric in "muc", "ceafe", "bcub":
        results.append(
            extract_f1(subprocess.run(part_a + [metric] + part_b, **kwargs)))
        print(metric, results[-1])

    print("avg", sum(results) / len(results))

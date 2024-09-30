#!/usr/bin/env python
# coding: utf-8

import pandas as pd

## post analysis of cpptraj distance outputs

inp = "/path/to/input_dir/scheme-4/distances.csv"

col_num = 20 # column considered
ranges = [0, 5, 19, 100] # distance cutoff
step_size = 15000 # grouping the rows in column considered for analysis 

data = pd.read_csv(inp)
col_data = data.iloc[:, col_num]

step_counts = {}

for step_group in range(0, len(col_data), step_size):
    group_data = col_data.iloc[step_group:step_group + step_size]
    group_counts = {}
    
    for i in range(len(ranges) - 1):
        range_str = f"{ranges[i]}-{ranges[i + 1]}"
        range_count = ((group_data >= ranges[i]) & (group_data <= ranges[i + 1])).sum()
        group_counts[range_str] = range_count
    
    step_counts[f"Step {step_group}-{min(step_group + step_size, len(col_data))}"] = group_counts

result_df = pd.DataFrame(step_counts)
result_df = result_df.T
out_path = "/path/to/out_dir/epoch_counts.csv"
result_df.to_csv(out_path)





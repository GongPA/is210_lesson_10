#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task 01: Reading a CSV
The CSV file, the first couple words of top line are heading name of columns.
and this file structure is lines can split into words by ','
from [0]
the [10] is the data of grade.
therefore, we just need the get that data of index[10]
"""

import json
# Task-02 need to import a json module.

GRADES = {"A": 1.0, "B": 0.9, "C": 0.8,
          "D": 0.7, "F": 0.6}


def get_score_summary(file_in):
    """
    Task 01: Reading a CSV
    create a function to get the grade datas
    boro and camis_id into a dictionary.

    dict_sim = {}
    dict_sim["a1] = (2014,11)
    print dict_sim
    {'a1':(2014,11)}
    """
    dict_simple = {}

    file_open = open(file_in, "r")
    file_open.readline()
    for line in file_open.readlines():
        line_split = line.split(",")
        if len(line_split[10]) != 0 and line_split[10] != "P":
            dict_simple[line_split[0]] = (line_split[1],
                                          GRADES[line_split[10]])
    file_open.close()

    dict_summary = {}

    for val in dict_simple.itervalues():
        if val[0] not in dict_summary:
            dict_summary[val[0]] = (1, val[1])
        else:
            num = dict_summary[val[0]][0] + 1
            grade = dict_summary[val[0]][1] + val[1]
            dict_summary[val[0]] = (num, grade)

    for key, val in dict_summary.items():
        dict_summary[key] = (val[0], val[1] / val[0])
    return dict_summary


def get_market_density(file_in):
    """
    Task 02: Reading a JSON File
    """

    file_open = open(file_in, "r")
    data = json.load(file_open)
    file_open.close()
    # open file, close file are the same
    dict_summary = {}
    for line in data["data"]:
        borough = line[8].strip().upper()
        if borough not in dict_summary:
            # to find out is Boro code already in the Dict
            dict_summary[borough] = 1
        else:
            dict_summary[borough] += 1
    return dict_summary
    # this dict may have 'u' infront of key
    # reference link:
    # http://stackoverflow.com/questions/8101649/
    # python-dictionary-removing-u-chars


def correlate_data(scores_file_in, markets_file_in, file_out):
    """
    Task 03: Relating Data and Writing a File
    """
    dict_sum = {}

    score_sum = get_score_summary(scores_file_in)
    market_sum = get_market_density(markets_file_in)

    # print score_sum
    # print market_sum

    for key, val in score_sum.items():
        borough = key
        food_score = val[1]
        per_density = float(market_sum[key]) / val[0]
        dict_sum[borough] = (food_score, per_density)
    file_open = open(file_out, "w")
    json.dump(dict_sum, file_open)
    file_open.close()

if __name__ == "__main__":
    print correlate_data("inspection_results.csv",
                         "green_markets.json",
                         "results.json")

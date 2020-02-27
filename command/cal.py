#!/usr/bin/env python3
#!coding=utf-8

from statistics import mean, median
import fileinput
import argparse
import math
import numpy as np
import pandas as pd
from scipy import stats


class Calculator(object):
    def __init__(self, data):
        self.mean = mean(data)
        self.median = median(data)
        self.variance = np.var(data)
        self.stdev = np.std(data)
        self.total = sum(data)
        self.count = len(data)
        self.max_val = max(data)
        self.min_val = min(data)
        self.quant10 = math.ceil(len(data) * 0.1)
        self.quant25 = math.ceil(len(data) * 0.25)
        self.quant50 = math.ceil(len(data) * 0.5)
        self.quant75 = math.ceil(len(data) * 0.75)
        self.quant90 = math.ceil(len(data) * 0.9)
        self.conf90_bottom, self.conf90_up = self.cal_conf(data, alpha=0.9)
        self.conf95_bottom, self.conf95_up = self.cal_conf(data, alpha=0.95)
        self.conf99_bottom, self.conf99_up = self.cal_conf(data, alpha=0.99)

    def cal_conf(self, data, alpha):
        wc = pd.Series(data)
        t_dist = stats.t(loc=wc.mean(),
                         scale=np.sqrt(wc.var()/len(data)),
                         df=len(data)-1)

        bottom, up = t_dist.interval(alpha)
        return bottom, up

    def printer(self, dict_data):
        for name, val in dict_data.items():
            print(name, f'{val:.2f}')

    def choice_printer(self, dict_data, types):
        for i in str(types).strip().split(","):
            print(i, dict_data[i])


def parsers():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--types', help='choice argument')
    parser.add_argument('-v', '--view', action='store_true',
                        help='view all elements')
    parser.add_argument('files', metavar='FILE', nargs='*',
                        help='files to read, if empty, stdin is used')
    args = parser.parse_args()
    data = [int(i) for i in fileinput.input(
        files=args.files if len(args.files) > 0 else ('-', ))]
    return args, data


def main():
    opt, data = parsers()
    cal = Calculator(data)
    cal.printer(vars(cal)) if opt.view else None
    cal.choice_printer(vars(cal), opt.types) if opt.types else None


main()

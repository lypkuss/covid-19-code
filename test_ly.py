# coding:utf-8
import pandas as pd
import numpy as np
#pd.options.display.max_columns = None  # pandas显示全部列
#from tqdm import tqdm
import os
import sys
import time


def get_state_cgbs():
    state_cbgs = []
    df_cbg = pd.read_csv("/root/data/liangyi/dataset/fips/FipsStateCodes.csv")
    for idx, value in df_cbg.iterrows():
        tmp = str(value.FIPS)[:-3]
        # print(tmp)
        state_cbgs.append(int(tmp))
    state_cbgs = sorted(state_cbgs)  # 改为升序数组
    return state_cbgs

if __name__ == "__main__":
    state_cbgs = get_state_cgbs()
    print(state_cbgs)
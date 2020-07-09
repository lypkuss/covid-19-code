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


def get_pop_flow(df_origin, state_cbgs):
    pop_flow = pd.DataFrame(0, index=state_cbgs, columns=state_cbgs)
    #begin_time = time.time()
    #end_time = time.time()
    for idx, value in df_origin.iterrows():
        visit_home = eval(value.destination_cbgs)
        # print(visit_home.keys())

        cbg_go = int(str(df_origin.iloc[idx][0])[:-10])
        if cbg_go not in state_cbgs:
            continue
        for key in visit_home.keys():
            cbg_come = int(str(key)[:2])
            if cbg_come in state_cbgs:
                pop_flow.loc[cbg_go][cbg_come] += int(visit_home[key])
    return pop_flow


def write_pop_flow(csv_read_path, csv_write_path):
    df_origin = pd.read_csv(csv_read_path)
    state_cbgs = get_state_cgbs()
    pop_flow = get_pop_flow(df_origin, state_cbgs)
    pop_flow.to_csv(csv_write_path)



if __name__ == "__main__":
    file_path = "/root/data/liangyi/dataset/social-distance/04/"
    save_path = "/root/data/liangyi/dataset/popflow-state/04/"
    for file in os.listdir(file_path):
        print(file)
        if ".csv" in file:
            csv_read_path = file_path + file
            tmp = '-'.join(file.split('-')[:3])
            csv_write_path = save_path + tmp + '-state-popflow.csv'
            write_pop_flow(csv_read_path,csv_write_path)

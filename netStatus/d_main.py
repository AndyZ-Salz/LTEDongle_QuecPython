# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : main
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2021/4/1: Create

# import network_status

def status_formatted():
    # status_dic = network_status.get_status()
    status_dic = {'UTC': '2021/4/1 5:56:20', 'Operator': 'CHN-UNICOM', 'CellID': 'A0BD0B', 'CFUN': 1, 'CSQ': 29, 'earfcn': 1650, 'RSSI': -54, 'PCI': 474, 'TAC': 6178, 'CQI': 255, 'RSRP': -82, 'RSRQ': -8}
    status_list = ["CFUN",
                   "Operator",
                   "CSQ",
                   "CellID",
                   "PCI",
                   "TAC",
                   "earfcn",
                   "RSSI",
                   "RSRP",
                   "RSRQ",
                   "CQI",
                   "UTC"
                   ]
    status_str = []
    for value in status_list:
        status_str.append(value+":"+str(status_dic[value]))

    return status_str



if __name__ == '__main__':
    # print(network_status.get_status())
    print(status_formatted())
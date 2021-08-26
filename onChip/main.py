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

from usr import network_status
from usr import st7789v
import utime

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


def status_formatted(status_dic):
    status_str = []
    for value in status_list:
        status_str.append(value + ":" + str(status_dic[value]))

    return status_str


def display_on_LCD(status):
    y = 5
    for status_item in status:
        lcd_st7789v.lcd_show_ascii_str(0, y, 8, 16, status_item+"   ", fc, bc)
        y += 18


if __name__ == '__main__':
    utime.sleep(10)


    lcd_st7789v = st7789v.ST7789V(240, 240)
    fc = 0x0000  # 字体颜色 黑色 可根据需要修改
    bc = 0xffff  # 背景颜色 白色 可根据需要修改

    while(1):
        status_dic = network_status.get_status()
        status = status_formatted(status_dic)
        print(status)
        display_on_LCD(status)
        utime.sleep(1)

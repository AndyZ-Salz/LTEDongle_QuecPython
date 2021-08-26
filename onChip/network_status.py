# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : network_status
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2021/4/1: Create

import net
import utime


def get_status():
    status = {}

    status["CFUN"] = net.getModemFun()
    status["Operator"] = net.operatorName()[0]
    status["CSQ"] = net.csqQueryPoll()

    CellInfo = net.getCellInfo()[2][0]
    status["CellID"] = hex(CellInfo[1])[2:].upper()
    status["PCI"] = CellInfo[4]
    status["TAC"] = CellInfo[5]
    status["earfcn"] = CellInfo[6]

    Signal = net.getSignal()[1]
    status["RSSI"] = Signal[0]
    status["RSRP"] = Signal[1]
    status["RSRQ"] = Signal[2]
    status["CQI"] = Signal[3]

    LocalTime = utime.localtime()
    status["UTC"] = "{0}/{1:0>2d}/{2:0>2d} {3:0>2d}:{4:0>2d}:{5:0>2d}".format(LocalTime[0], LocalTime[1], LocalTime[2], LocalTime[3], LocalTime[4], LocalTime[5])

    return status


if __name__ == '__main__':
    print(get_status())

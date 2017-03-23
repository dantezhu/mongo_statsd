# -*- coding: utf-8 -*-
"""
读取gateway统计数据并解析
"""

import os
import re


class StatReader(object):

    cmd = None

    def __init__(self, cmd):
        """
        :param cmd: 统计命令
        :return:
        """
        self.cmd = cmd

    def read(self):
        """
        读取一次
        :return:
        """

        """
        connected to: 127.0.0.1
        insert  query update delete getmore command flushes mapped  vsize    res non-mapped faults            locked db idx miss %     qr|qw   ar|aw  netIn netOut  conn       time
        132     *0     *0     *0       0   184|0       0  1181g  2368g  7.38g      1187g      2 texas_statistic:0.8%          0       0|0     0|0    53k    23k  1060   10:17:56

        """

        keys = list()
        values = list()

        for line in os.popen(self.cmd):
            if line.startswith('connect'):
                continue
            if line.startswith('insert'):
                # 所有的key
                keys = re.split(r'\s+', line)
                continue

            # 最后这个一定是values
            values = re.split(r'\s+', line)
            break

        result = dict(zip(keys, values))

        return result

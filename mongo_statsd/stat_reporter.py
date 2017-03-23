# -*- coding: utf-8 -*-

"""
读取gateway统计数据，并上报数据至statsd
"""

from stat_reader import StatReader
from . import constants


class StatReporter(object):

    # 标识的名字
    name = None
    stat_reader = None
    statsd_client = None

    def __init__(self, cmd, statsd_client, name):
        """
        :param cmd: 命令
        :param statsd_client: statsd_client
        :param name: 名字
        :return:
        """

        self.stat_reader = StatReader(cmd, constants.HEADER_DICT.keys())
        self.statsd_client = statsd_client
        self.name = name

    def report(self):
        """
        上报
        :return:
        """

        result = self.stat_reader.read()

        if not result:
            return False

        for local_stat_name, local_value in result.items():
            if
            remote_stat_name = self.statsd_name_converter(local_stat_name)
            value = result.get(local_stat_name, 0)

            self.statsd_client.gauge(remote_stat_name, value)

        return True

    def statsd_name_converter(self, stat_name):
        return '%s.%s.%s' % (constants.PREFIX, self.name, stat_name)


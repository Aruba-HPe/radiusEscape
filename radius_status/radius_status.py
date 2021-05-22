#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/6/2021 10:44 PM
# @Author  : Jinlin
# @File    : radius_status.py
# @Project : radiusEscape


from mm import ping
import pysnooper


def host_status(host):
    radius_obj = ping.Ping(count=5, timeout=1)
    result = radius_obj.ping(host)
    return result
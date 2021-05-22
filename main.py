#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/29/2021 10:08 PM
# @Author  : Jinlin
# @File    : main.py
# @Project : radiusEscape
import requests

from mm import aos8_api_caller as aos8
from radius_status import radius_status
import time
import json
import pysnooper

dot1x_vap_status = True
disable_dot1x_enable_psk = [{"profile-name": "ipfix", "vap_enable": {"_action": "delete"}}, {"profile-name": "psk", "vap_enable": {"_action": "add"}}]
enable_dot1x_disable_psk = [{"profile-name": "ipfix", "vap_enable": {"_action": "add"}}, {"profile-name": "psk", "vap_enable": {"_action": "delete"}}]


if __name__ == '__main__':

    aos8_session = aos8.api_session("192.168.1.200", "admin", "Admin#123", check_ssl=False, verbose=True)
    aos8_session.login()
    while True:
        result = radius_status.host_status("192.168.1.20")
        print('Time:', time.ctime(), '---', result)
        if dot1x_vap_status and (result.get('loss_percentage') > 40.0):
            aos8_session.post('configuration/object/virtual_ap', disable_dot1x_enable_psk, '/mm/mynode')
            aos8_session.write_memory('/mm/mynode')
            dot1x_vap_status = False
        elif (not dot1x_vap_status) and (result.get('loss_percentage') <= 40.0):
            aos8_session.post('configuration/object/virtual_ap', enable_dot1x_disable_psk, '/mm/mynode')
            aos8_session.write_memory('/mm/mynode')
            dot1x_vap_status = True






















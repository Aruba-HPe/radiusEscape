#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/20/2021 8:57 PM
# @Author  : Jinlin
# @File    : radiusPoc.py
# @Project : radiusEscape

from radius_eap_mschapv2 import RADIUS




if __name__ == '__main__':
    radius = RADIUS('192.168.1.110', 'Admin#123', '192.168.1.100', 'PoC')
    code = radius._access_request_eap_mschapv2(b'admin', '123456')
    print(code)
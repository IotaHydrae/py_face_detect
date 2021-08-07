#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:29:39 2019

@author: pi
"""

import requests 

def get_token():
# client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=21WfgAaxLpaRPXbFfhq1dcVV&client_secret=XubU69kTjeQbbEB4LTIQuYM1cGnj8Sg3'
    response = requests.get(host)
    return response.json()['access_token']
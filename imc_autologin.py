#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zeroyu'

import ConfigParser
import os
import sys

import requests
import time
import base64


from header import *
from check_flow import *

_username        = ''
_password        = ''


def login(login_name,login_passwd):
                s_req = requests.Session()

                f = s_req.get(get_url,headers=get_header)

                _passwd = base64.b64encode(_password)

                postData = { 
                        'userName': _username,
                        'userPwd': _passwd,
                        'serviceTypeHIDE':'',
                        'serviceType':'',
                        'isSavePwd':'on',
                        'userurl':'',
                        'userip':'',
                        'basip':'',
                        'language': 'Chinese',
                        'usermac':'null',
                        'entrance':'null',
                        'custompath':'templatePage%2F20140225230636305',
                        'portalProxyIP':'202.117.80.138',
                        'portalProxyPort':'50200',
                        'dcPwdNeedEncrypt':'1',
                        'assignIpType':'0',
                        'appRootUrl':'http%3A%2F%2F202.117.80.138%3A8080%2Fportal%2F',
                        'manualUrl':'',
                        'manualUrlEncryptKey':''
                }

                s_req.post(post_url,data = postData,headers = post_header)


def get_item_from_ini():
    '''
    从.ini文件中载入账户密码信息
    '''
    global _username
    global _password
    cf = ConfigParser.ConfigParser()
    cf.read('config.ini')
    _username = cf.get('info', 'username')
    _password = cf.get('info', 'password')

def main():
        get_item_from_ini()
        check(_username,_password)
        while(1):
                login(_username,_password)
                time.sleep(1000)

if __name__ == '__main__':
        main()
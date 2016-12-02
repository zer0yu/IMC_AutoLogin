#!/usr/bin/env python
# -*- coding: utf-8 -*-


get_url = "http://202.117.80.138:8080/portal/templatePage/20140225230636305/login_custom.jsp"
post_url = "http://202.117.80.138:8080/portal/pws?t=li"

url = 'http://self.nwpu.edu.cn:8080/selfservice/module/scgroup/web/login_judge.jsf'
code_url = 'http://self.nwpu.edu.cn:8080/selfservice/common/web/verifycode.jsp'

get_header = {
        "Host" : "202.117.80.138:8080",
        "Cache-Control" : "max-age=0",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "zh-CN,zh;q=0.8",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With" : "XMLHttpRequest",
       
           }

post_header = {
        "Host" : "202.117.80.138:8080",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Accept" : "text/plain, */*; q=0.01",
        "Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding" : "gzip, deflate",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With" : "XMLHttpRequest",
        "Accept" : "text/plain, */*; q=0.01",
        "Referer": "http://202.117.80.138:8080/portal/templatePage/20140225230636305/login_custom.jsp",
        "Content-Length" : "370"
}

chaxun_header = {
	'Host': 'self.nwpu.edu.cn:8080',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://self.nwpu.edu.cn:8080/selfservice/module/scgroup/web/login_self.jsf',
	'Upgrade-Insecure-Requests': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '54'
}


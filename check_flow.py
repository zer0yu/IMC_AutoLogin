#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from PIL import Image
import pytesseract
import sys
import re
import cStringIO
import base64
from bs4 import BeautifulSoup
from header import *


req = requests.Session()
mistake_mark = 'verfiyError'
answer_wrong_mark = 'errorMsg'
answer_right_mark = ''

 
def decode():
	file = cStringIO.StringIO(req.get(code_url).content)
	image = Image.open(file)
	return pytesseract.image_to_string(image)
 
def check(line_name, line_pass):
	mistake = 1
	while(mistake == 1):
		code = decode()
		payload = {'verify' : code, 'password' : line_pass, 'name' : line_name, 'act' : 'add'}
		r = req.post(url, data = payload,headers=chaxun_header)
		if r.content.find(mistake_mark) == -1:
			mistake = 0
	res = req.get('http://self.nwpu.edu.cn:8080/selfservice/module/webcontent/web/content_self.jsf',headers=chaxun_header)
	try:
		soup = BeautifulSoup(res.text,"html.parser")

		flow = soup.find_all(text=re.compile("([0-9.]*)[ GB]*([0-9.]*) MB /([0-9.]*) GB ([0-9.]*) MB"))

		sys.stdout.flush()
		print flow[0].encode('utf-8')
		
	except:
		print '密码错误请修改密码后重新登录\n'
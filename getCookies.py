# from selenium import webdriver
# import json
# import requests
# import re
#
# browser = webdriver.Firefox()
# browser.get('https://www.yidaiyilu.gov.cn/info/iList.jsp?cat_id=10002')
#
# Cookie = browser.get_cookies()
# strr = ''
# for c in Cookie:
#     strr += c['name']
#     strr += '='
#     strr += c['value']
#     strr += ';'
# # strr = strr[0:-1]
# print(strr)
# # headers = {'Cookie': strr}
# # # # print(headers)
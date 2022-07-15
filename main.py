"""
pip install mitmproxy
pip install markupsafe==2.0.1
给你的应用或者系统设置代理:127.0.0.1:15732
安装证书:http://mitm.it/
"""
import os

os.system('mitmdump -p 15732 -s app.py')
# os.system('mitmweb -p 15732 -s app.py')

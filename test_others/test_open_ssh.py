# _*_coding:utf-8_*_
# 作者:duningning.ming
# 创建时间: 2022/8/19 15:44
# 文件   : test_open_ssh.py.py
# IDE   : PyCharm
import requests
import hashlib
import pytest


def test_open_ssh():
    ip = '172.17.21.8'
    r = requests.get('http://' + ip + ':9000/sys/deviceinfo').json()
    key = 'deepglint' + r['data']['id']
    token = hashlib.md5(key.encode('utf-8')).hexdigest()
    r = requests.post(
        'http://' + ip + ':9000/sys/ssh',
        json={'open':'true'=='true'},
        headers={'Authorization': token},
    )
    print(r.json())



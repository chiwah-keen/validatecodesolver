#! /usr/bin/env python
# coding: utf-8
# author:zhihua
import requests, sys, os, traceback, hashlib


captcha_url = "http://wenshu.court.gov.cn/User/ValidateCode"



def get_captcha_content(url):
    try:
        headers = {
             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        return r.content
    except:
        print traceback.format_exc()
        return None


def content_md5(content):
    if not content: return None
    m2 = hashlib.md5()
    m2.update(content)
    return m2.hexdigest()

def save_into_file(fname, content):
    with open(fname, 'w') as f:
        f.write(content)

def captcha_downloader():
    content = get_captcha_content(captcha_url)
    if not content: print "Content Error", exit()
    md5str = content_md5(content)
    fname = "./pics/" + md5str + ".png"
    save_into_file(fname, content)

for i in range(1000):
    captcha_downloader()
    exit()


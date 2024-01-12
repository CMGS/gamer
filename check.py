# coding: utf-8

import requests
import time
from buy import buy
from common import *

def check_and_buy(config:dict):
# 设置 URL 和 headers
    headers = {
        'authority': 'api.store.nvidia.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
        'dnt': '1',
        'origin': 'https://store.nvidia.com',
        'referer': 'https://store.nvidia.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-queueit-ajaxpageurl': 'https%3A%2F%2Fstore.nvidia.com%2Fen-us%2Fgeforce%2Fstore%2Fgpu%2F%3Fpage%3D1%26limit%3D9%26locale%3Den-us%26gpu%3DRTX%25204090%2CRTX%25204070%26category%3DGPU%26manufacturer%3DNVIDIA%26gpu_filter%3DRTX%25204090~1%2CRTX%25204080~1%2CRTX%25204070~1%2CRTX%25204060%2520Ti~1'
    }

    while True:
        try:
            response = requests.get(CHECK_URL, headers=headers)
            data = response.json()
            sku = data.get('listMap').pop()
            print(sku)
            if sku.get('is_active') == 'false':
                print("no stock.")
            else:
                print("buy.")
                buy(config)
        except:
            print("error")
        time.sleep(15)


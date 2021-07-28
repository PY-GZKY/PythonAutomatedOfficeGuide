import base64
import hashlib
import hmac
import time
from urllib import parse

import requests
from requests.exceptions import ConnectionError


class GetD():
    def __init__(self):
        self.headers = {
            "User-Agent": "Rexxar-Core/0.1.3 api-client/1 com.douban.frodo/7.11.1(220) Android/25 product/VOG-AL00 vendor/HUAWEI model/VOG-AL00  rom/android  network/wifi  udid/c72cfb38a040b64521255795860f17a634090668  platform/AndroidPad nd/1 com.douban.frodo/7.11.1(220) Rexxar/1.2.151  platform/AndroidPad 1.2.151",
        }

        self.r = requests.session()

    def get_html(self, url):
        t_ = int(time.time())

        params = {
            "tags": "",
            "refresh": 0,
            "selected_categories": {},
            "start": 0,
            "count": 8,
            "udid": "c72cfb38a040b64521255795860f17a634090668",
            "rom": "android",
            "apikey": "0dad551ec0f84ed02907ff5c42e8ec70",
            "s": "rexxar_new",
            "channel": "Baidu_Market",
            "timezone": "Asia/Shanghai",
            "device_id": "c72cfb38a040b64521255795860f17a634090668",
            "os_rom": "android",
            "apple": "9efa6ba99021c3c98ef09c7dd7543653",
            # "icecream": "84ced86782ed487aca374defabfd29c5",
            # "mooncake": "17145441849e2d8e8e757360917238ea",
            "sugar": 46000,
            "loc_id": 108288,
            "_sig": self.get_sig(url=url, ts=t_),
            "_ts": t_,
        }
        try:
            req = self.r.get(url, params=params, headers=self.headers)
            if req.status_code == 200:
                req.encoding = req.apparent_encoding
                return req.json()
            return None
        except ConnectionError:
            return None

    def parse_json(self, json_data):
        print(json_data)

    def get_sig(self, url: str, ts: int, method='GET') -> str:
        """
        :param url: api
        :param ts: 时间戳
        :param method: 请求方法（大写 GET POST）
        :return:
        """
        url_path = parse.urlparse(url).path
        raw_sign = '&'.join([method.upper(), parse.quote(url_path, safe=''), str(ts)])
        return base64.b64encode(
            hmac.new("bf7dddc7c9cfe6f7".encode(), raw_sign.encode(), hashlib.sha1).digest()).decode()

    def run(self):
        json_data = self.get_html(url="https://frodo.douban.com/api/v2/book/recommend")
        self.parse_json(json_data)


if __name__ == '__main__':
    G = GetD()
    G.run()

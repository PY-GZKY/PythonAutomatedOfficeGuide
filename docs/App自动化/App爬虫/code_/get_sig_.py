import hashlib
import hmac
import base64
from urllib import parse
API_SECRET_KEY = "bf7dddc7c9cfe6f7"

def gen_sign(url: str, ts: int, method='GET') -> str:
    """
    :param url: api
    :param ts: 时间戳
    :param method: 请求方法（大写 GET POST）
    :return:
    """
    url_path = parse.urlparse(url).path
    raw_sign = '&'.join([method.upper(), parse.quote(url_path, safe=''), str(ts)])
    print(raw_sign)
    return base64.b64encode(hmac.new(API_SECRET_KEY.encode(), raw_sign.encode(), hashlib.sha1).digest()).decode()

# print(gen_sign(url="https://frodo.douban.com/api/v2/book/recommend", ts=1627624168))
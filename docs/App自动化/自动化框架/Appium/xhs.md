> 对于 `app` 自动化来说，`appium` 是必须知道的一个自动化测试框架。

值得一提的是 `appium` 环境搭建比 `Airtest` 要略显麻烦些。详见`环境搭建章节`

这里假设你的 `appium` 已经安装完毕。
> 开始使用 Appium
> 
### 以小某书App为例

```shell
DRIVER_SERVER = 'http://127.0.0.1:4723/wd/hub'
DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "HUAWEI P30 Pro",
    "appPackage": "com.xingin.xhs",
    "appActivity": ".activity.SplashActivity",
    "noReset": "True",
    "unicodeKeyboard": "True",
    "resetKeyboard": "True"
}

```
首先 `appium服务`的默认端口是 `4723`，当然如果多开的话可以是`n+2` 这样往累加。

`DESIRED_CAPS` 指明了我们的连接信息。
这里来说:
- `platformName`:  平台名称，这里是`安卓`
- `deviceName`: 设备名称
- `appPackage`: `app`包名
- `appActivity`: `app activity`
- `noReset`: 是否`重置`
- `unicodeKeyboard`: 键盘`编码`

初始化代码如下
```python
# -*- coding:utf-8 -*-
import random
import re
import math
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


DRIVER_SERVER = 'http://127.0.0.1:4723/wd/hub'
DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "HUAWEI P30 Pro",
    "appPackage": "com.xingin.xhs",
    "appActivity": ".activity.SplashActivity",
    "noReset": "True",
    "unicodeKeyboard": "True",
    "resetKeyboard": "True"
}

class CrawlRedBook():
    def __init__(self):
        self.driver = webdriver.Remote(DRIVER_SERVER, DESIRED_CAPS)
        self.wait = WebDriverWait(self.driver, 6)
        self.flag = 0
```

可以看到我结合了 `selenium` 的显式等待的方法，集成到了 `appium` 中。

不出意外的话(`pc`和`移动端`网络连接无误等)，运行以上代码是可以正常工作的。

#### `appium`获取当前屏幕的大小

```python
def get_size(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return (x, y)
```

#### `appium`滑动屏幕操作

```python
def first_action(self,keys):
    # self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/l7"))).click()
    self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/a01"))).click()  # 点击搜索框
    self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/ar4"))).send_keys(keys)  # 输入关键字
    sleep(1)
    # self.driver.press_keycode(66)  # 回车键
    self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/ar6"))).click()  # 回车键
    count = 0
    l = self.get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    while 1:
        if 'THE END' in self.driver.page_source:
            break
        # TouchAction(self.driver).press(x=360, y=1100).wait(800).move_to(x=360, y=300).release().perform()
        self.driver.swipe(x1, y1, x1, y2)
        count += 1
        print(keys,"滑动次数: ", count)
        sleep(0.2)
        # TouchAction(self.driver).tap(x=684, y=1233).perform()
```

这样就可以源源不断的向上滑动屏幕，
`app` 后端的`接口`也就即时返回对应的 `response`，
我们也就能监听(`mitmproxy`)并获取其有效的数据。

#### 关闭 `appium`
```python
def close(self):
    self.driver.close_app()
```

#### 整体代码

```python
# -*- coding:utf-8 -*-
import random
import re
import math
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


DRIVER_SERVER = 'http://127.0.0.1:4723/wd/hub'
DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "HUAWEI P30 Pro",
    "appPackage": "com.xingin.xhs",
    "appActivity": ".activity.SplashActivity",
    "noReset": "True",
    "unicodeKeyboard": "True",
    "resetKeyboard": "True"
}

class CrawlRedBook():
    def __init__(self):
        self.driver = webdriver.Remote(DRIVER_SERVER, DESIRED_CAPS)
        self.wait = WebDriverWait(self.driver, 6)
        self.flag = 0

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def first_action(self,keys):
        # self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/l7"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/a01"))).click()  # 点击搜索框
        self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/ar4"))).send_keys(keys)  # 输入关键字
        sleep(1)
        # self.driver.press_keycode(66)  # 回车键
        self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/ar6"))).click()  # 回车键

        count = 0
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        while 1:
            if 'THE END' in self.driver.page_source:
                break
            # TouchAction(self.driver).press(x=360, y=1100).wait(800).move_to(x=360, y=300).release().perform()
            self.driver.swipe(x1, y1, x1, y2)
            count += 1
            print(keys,"滑动次数: ", count)
            sleep(0.2)
            # TouchAction(self.driver).tap(x=684, y=1233).perform()

    def close(self):
        self.driver.close_app()

if __name__ == "__main__":
    pass
```

#### `mitmproxy`监听数据接口

假设这里我们需要监听小某书的`笔记列表`，可以新建 `get_id.py` 脚本如下:
```python
# -*- coding:utf-8 -*-
# import sys
# sys.path.append('C:/Users/Administrator/AppData/Roaming/Python/Python37/site-packages')
import json
import re
from urllib.parse import unquote

def save_txt(filename, data):
    with open("./red_data/" + filename, "a", encoding="utf-8") as f:
        f.write(data + "\n")
        f.close()

def response(flow):
    url = "https://edith.xiaohongshu.com/api/sns/v10/search/"
    if flow.request.url.startswith(url):
        print(flow.request.url)
        keyword = re.findall(r'search/notes\?keyword=(.*?)&', flow.request.url)[0]
        print("关键字: ", unquote(keyword))

        text = flow.response.text
        items = json.loads(text)
        notes = items.get("data").get("items")

        for note in notes:
            item = {}
            try:
                item["user_id"] = note.get("note").get("user").get("userid")
                item["note_id"] = note.get("note").get("id")
                note_data_str = json.dumps(item)
                save_txt(f"{unquote(keyword)}.txt", note_data_str)
            except:
                pass
```


启动监听脚本
```shell
mitmdump -s ./get_id.py
```

默认监听 `8080` 端口，当然你也可以自行指定端口号，你需要在你的`真机`或`模拟器`上填写正确的服务器地址和监听端口号。

这样我们就能将接口返回的数据初步解析并存储到本地文件中(或者入其他`待爬队列`)。

```shell
{"user_id": "5d443c66000000001103429b", "note_id": "604cb35e0000000001026af6", }
{"user_id": "5c433242000000000603fe7e", "note_id": "5e218aab00000000010001cc", }
{"user_id": "5b17ff7af7e8b95acaf614d4", "note_id": "6018c335000000000100651b", }
{"user_id": "5b63a7da4eacab1a72a526a5", "note_id": "607c49f6000000002103d3dc", }
{"user_id": "59fc91c111be1055cd6fa82b", "note_id": "60dacd65000000000100a339", }
{"user_id": "5c433242000000000603fe7e", "note_id": "5e58d939000000000100277b", }
{"user_id": "5dda423800000000010036e8", "note_id": "5e2d344000000000010065d6", }
{"user_id": "5ba6e9b823d0e40001c7e6e0", "note_id": "5fcd715e000000000100995b", }
{"user_id": "6032103d000000000101efc4", "note_id": "6056e46f000000002103c662", }
{"user_id": "5efbf7ec0000000001006d37", "note_id": "6024c4c8000000000102a1d5", }
{"user_id": "5c091ec90000000007003966", "note_id": "5c0a01d2000000000801c8fd", }
{"user_id": "5e8732f5000000000100ae8c", "note_id": "609e7fb40000000021038b68", }
{"user_id": "5c433242000000000603fe7e", "note_id": "5e40f0b300000000010076e5", }
{"user_id": "5fa3d0c5000000000100574a", "note_id": "60725f36000000002103b66a", }
{"user_id": "606c67460000000001006aa4", "note_id": "60892cce000000000102b1f8", }
{"user_id": "60b101530000000001009f2b", "note_id": "60d94aee000000002103be7b", }
{"user_id": "6028c2620000000001005a0f", "note_id": "6094d72a00000000010294ba", }
```

然后根据获取的 `user_id` 和 `note_id` 抓取相关的博主或笔记信息。

> 代码仅供学习，切勿滥用。

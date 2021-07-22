`Puppeteer` 是一款基于 `NodeJS` 的 `web` 浏览器测试工具

`Pyppeteer` 是 `Puppeteer` 的 `Python` 实现，在用法上并无二至，可惜的是 `Pyppeteer` 如今已经无人维护。最近一次项目的更新时间还停留在 `2018年9月`


> [GitHub 项目地址](https://github.com/miyakogi/pyppeteer)

> [文档](https://miyakogi.github.io/pyppeteer)

这是一款基于异步实现的自动化框架，这也就意味 `Pyppeteer` 在性能上要比 `selenium` 要好，但是 `Pyppeteer` 是一个非官方版本，
在文档支持方面仍有欠缺，这给想入门web自动化的小伙伴造成了不小的困扰。


## `chromium`

总言之，`Chromium` 是一款独立的浏览器，你也可以认为它是 `chrome` 的开发版本，因为我们现在看到的 `chrome` 浏览器的功能都会先在 `Chromium` 上实现。

`Chromium` 是完全开源的，非常适用于 `web` 测试开发，
只不过它从外观看起来和 `chrome` 略有不同(几种不同程度的蓝色构成)

![](./images/Chromium.png ':size=70%')


## 安装 `Pyppeteer`

```shell
pip install pyppeteer
```

首次通过 `pip` 安装 `pyppeteer` 时会自动下载安装 `Chromium` 浏览器，这也太热情了。

如果由于网络原因导致下载终端，可以 [手动下载](https://chromium.en.softonic.com/)

下载完成后通过 `Pyppeteer` 查看 `Chromium` 版本和所在路径

```python
import pyppeteer
print(pyppeteer.__chromium_revision__)  # 查看版本号
print(pyppeteer.executablePath())  # 查看 Chromium 路径
```
```text
588429
C:\Users\HP\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429\chrome-win32\chrome.exe
```
> 如果在初始化 `pyppeteer` 对象的时候不指定浏览器路径，则会默认使用该路径打开 `chromium` 浏览器

## 测试 `Pyppeteer`
```python
# -*- coding: utf-8 -*-
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)  # 有头浏览器
    page = await browser.newPage() # 打开一个新的标签页
    await page.goto('https://pypi.org/project/pyppeteer/')  # 跳转
    await page.screenshot({'path': '../images/pyppeteer.png'})  # 截图
    await browser.close()  # 关闭浏览器

asyncio.get_event_loop().run_until_complete(main())
```

截图效果

![](./images/pyppeteer.png ':size=70%')

> 看起来不错，和我们预想的完全一致

> 这说明 `Pyppeteer` 已经能够正常启动并工作了
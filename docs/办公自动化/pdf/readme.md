
除了 `office` 办公三件套，这里将 `PDF` 作为一种辅助。

> 这里使用的扩展库是 `pdfminer` 以及 `pdfplumber`

```python
import pdfminer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator

# 提供初始密码
password = ''
# 没有密码可以初始密码
# document.initialize()

#打开pdf文件
fp = open('./Netease Q2 2019 Earnings Release-Final.pdf','rb')

#从文件句柄创建一个pdf解析对象
parser = PDFParser(fp)

#创建pdf文档对象，存储文档结构
document = PDFDocument(parser, password)

#创建一个pdf资源管理对象，存储共享资源
rsrcmgr = PDFResourceManager()

laparams = LAParams()

#创建一个device对象
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

#创建一个解释对象
interpreter = PDFPageInterpreter(rsrcmgr, device)

#处理包含在文档中的每一页
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for x in layout:
        # 获取文本对象
        if isinstance(x, LTTextBox):
            print(x.get_text().strip())
        # 获取图片对象
        if isinstance(x,LTImage):
            print('这里获取到一张图片')
        # 获取 figure 对象
        if isinstance(x,LTFigure):
            print('这里获取到一个 figure 对象')
```


```python
import pdfplumber
import pandas as pd
from openpyxl import Workbook
# with pdfplumber.open("1.pdf") as pdf:
#     page = pdf.pages[0]   # 第一页的信息
#     text = page.extract_text()
#     print(text)


with pdfplumber.open("Netease Q2 2019 Earnings Release-Final.pdf") as pdf:
    page = pdf.pages[9]   # 第一页的信息
    table = page.extract_table(
       table_settings= {
           "vertical_strategy":"text",
           "horizontal_strategy":"text"

        }
    )
    workbook = Workbook()
    sheet = workbook.active
    for row in table:
        sheet.append(row)

    workbook.save(filename="./toPdf.xlsx")
```
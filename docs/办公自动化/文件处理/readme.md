> `公司同事`：有一大批表格文件需要重命名，手动代价太大，有没有快速批量给文件重命名呢？

> `Python`：我都不用第三方扩展，`os` 模块可以在 `1` 秒之内帮你全部搞定

```python
# -*- coding: utf-8 -*-
import os
path = "C:\\Users\\HP\\Desktop\\test"

def rename(oldName,newName):
    filelist=os.listdir(path)
    for files in filelist:
        oldFilePath = os.path.join(path,files)
        if os.path.isdir(oldFilePath):
            continue
        print(oldFilePath)
        newFilePath = os.path.join(path, f"{os.path.splitext(files)[0].replace(oldName,newName)}{os.path.splitext(files)[1]}")
        print(newFilePath)
        os.rename(oldFilePath, newFilePath)

rename("Nice","你好")
```
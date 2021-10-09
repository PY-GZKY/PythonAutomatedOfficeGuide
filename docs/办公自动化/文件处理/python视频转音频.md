### You-Get
```shell
pip install you-get
```

#### Info
```shell
you-get -i "https://www.bilibili.com/video/BV1rq4y1V7ht"
```

#### download
```shell
you-get --format=flv720 "https://www.bilibili.com/video/BV1rq4y1V7ht"
```
首先通过 `you-get` 下载一个 `b站` 的视频
```shell
Downloading 点弦泛音高能！《江南》美爆的「指弹吉他」！林俊杰听了都想点赞！.flv ...
 100% ( 43.8/ 43.8MB) ├████████████████████████████████████████┤[1/1]  319 kB/s

Downloading 点弦泛音高能！《江南》美爆的「指弹吉他」！林俊杰听了都想点赞！.cmt.xml ...
```

- `.flv` 视频文件(指定其他格式如 `MP4`)
- .`cmt.xml` 弹幕文件

### moviepy

```shell
pip install moviepy
```

`视频`转换为`音频`文件
```python
from moviepy.editor import *

video = VideoFileClip('点弦泛音高能！《江南》美爆的「指弹吉他」！林俊杰听了都想点赞！.flv')
audio = video.audio
audio.write_audiofile('点弦泛音高能！《江南》美爆的「指弹吉他」！林俊杰听了都想点赞！.mp3')
```

```shell
MoviePy - Writing audio in 点弦泛音高能！《江南》美爆的「指弹吉他」！林俊杰听了都想点赞！.mp3
MoviePy - Done.
```
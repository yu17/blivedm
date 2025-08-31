# blivedm

Forked from [xfgryujk/blivedm](https://github.com/xfgryujk/blivedm).

Added `blivedm_xml_logger`, which records the live danmakus and writes them to a file in the bilibili danmaku xml format. Used in [yu17/bilibili-live-recorder](https://github.com/yu17/bilibili-live-recorder) to record live danmakus together with the live stream.

添加了 `blivedm_xml_logger`类，用于记录保存直播弹幕。保存格式与B站普通视频使用的XML格式相同，可以直接使用danmaku2ass转换为ass字幕。这个项目被用于我的另一个项目[yu17/bilibili-live-recorder](https://github.com/yu17/bilibili-live-recorder)，以便在录直播的同时支持录弹幕。

为了保证与danmaku2ass兼容，目前仅支持普通弹幕和SC。其中SC会显示为普通顶部弹幕，会显示发送人和金额，但不会长时间保留。

将来可能会考虑fork一下danmaku2ass，更好地支持SC和礼物。

### `readme.md` from the original repo:

Python获取bilibili直播弹幕的库，使用WebSocket协议，支持web端和B站直播开放平台两种接口

[协议解释](https://open-live.bilibili.com/document/657d8e34-f926-a133-16c0-300c1afc6e6b)

基于本库开发的一个应用：[blivechat](https://github.com/xfgryujk/blivechat)

## 使用说明

1. 需要Python 3.8及以上版本
2. 安装依赖

    ```sh
    pip install -r requirements.txt
    ```

3. web端例程在[sample.py](./sample.py)，B站直播开放平台例程在[open_live_sample.py](./open_live_sample.py)

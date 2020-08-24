# blivedm

Forked from [xfgryujk/blivedm](https://github.com/xfgryujk/blivedm).

Added `blivedm_xml_logger`, which records the live danmakus and writes them to a file in the bilibili danmaku xml format. Used in [yu17/bilibili-live-recorder](https://github.com/yu17/bilibili-live-recorder) to record live danmakus together with the live stream.

添加了 `blivedm_xml_logger`类，用于记录保存直播弹幕。保存格式与B站普通视频使用的XML格式相同，可以直接使用danmaku2ass转换为ass字幕。这个项目被用于我的另一个项目[yu17/bilibili-live-recorder](https://github.com/yu17/bilibili-live-recorder)，以便在录直播的同时支持录弹幕。

`readme.md` from the original repo:

获取bilibili直播弹幕，使用websocket协议

[协议解释](https://blog.csdn.net/xfgryujk/article/details/80306776)（有点过时了，总体是没错的）

基于本库开发的一个应用：[blivechat](https://github.com/xfgryujk/blivechat)

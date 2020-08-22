import asyncio
import os,time

import blivedm


class BLiveXMLlogger(blivedm.BLiveClient):
    def __init__(self, room_id, uid=0, heartbeat_interval=30, ssl=True, loop=None, savefile=None, inittime=int(time.time())):
        super().__init__(room_id, uid=uid, heartbeat_interval=heartbeat_interval, ssl=ssl, loop=loop)
        self.file = savefile
        self.inittime = inittime


    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def __on_vip_enter(self, command):
        print(command)
    _COMMAND_HANDLERS['WELCOME'] = __on_vip_enter  # 老爷入场

    async def _on_receive_popularity(self, popularity: int):
        print(f'当前人气值：{popularity}')

    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        print(f'{danmaku.uname}：{danmaku.msg}')
        curtime = int(time.time())
        self.file.write(f'<d p="{curtime-self.inittime},{danmaku.mode},{danmaku.font_size},{danmaku.color},{curtime},0,{danmaku.uid},0">{danmaku.msg}</d>')

    async def _on_receive_gift(self, gift: blivedm.GiftMessage):
        print(f'{gift.uname} 赠送{gift.gift_name}x{gift.num} （{gift.coin_type}币x{gift.total_coin}）')

    async def _on_buy_guard(self, message: blivedm.GuardBuyMessage):
        print(f'{message.username} 购买{message.gift_name}')

    async def _on_super_chat(self, message: blivedm.SuperChatMessage):
        print(f'醒目留言 ¥{message.price} {message.uname}：{message.message}')


async def main():
    filename = "12235923.xml"
    saving_path = "livelogs"
    xmlheader = '''<?xml version="1.0" encoding="UTF-8"?><i><chatserver>chat.bilibili.com</chatserver><chatid>219333260</chatid><mission>0</mission><maxlimit>8000</maxlimit><state>0</state><real_name>0</real_name><source>k-v</source>'''
    xmltail = '''</i>'''
    f = open(os.path.join(saving_path, filename),'w')
    client = BLiveXMLlogger(12235923, ssl=True, savefile=f)
    future = client.start()
    f.write(xmlheader)
    try:
        await future
    finally:
        f.write(xmltail)
        f.close()
        await client.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

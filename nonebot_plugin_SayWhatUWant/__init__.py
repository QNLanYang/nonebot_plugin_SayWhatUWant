from nonebot import on_message
from nonebot.rule import to_me
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageEvent
import re

__plugin_meta__ = PluginMetadata(
    name="hentai又要让本喵说什么",
    description="可以让机器人说指定的内容",
    usage='艾特机器人 + 说/say +【内容】',
    extra={
        'author':'岚漾',
        'priority': 50,
    }
)

saysth = on_message(rule = to_me(), priority=90, block=False)

@saysth.handle()
async def _(event: MessageEvent):
    # 获取消息文本
    msg = str(event.get_message())
    # 去掉带中括号的内容(去除cq码)
    msg = re.sub(r"\[.*?\][ ]?", "", msg)
    # 查询是否为"说"开头
    if msg.startswith("说") or msg.startswith("say"):
        #去掉"说"字
        msg = re.sub(r"说|say", "", msg)
        await saysth.finish(msg)

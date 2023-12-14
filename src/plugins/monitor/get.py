from typing import Optional
from src.util.subnya import *
from nonebot import on_command, on_keyword
from nonebot.params import CommandArg
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.telegram import Bot
from nonebot.adapters.telegram.event import MessageEvent

# def get_bot() -> Optional[Bot]:
#     """
#     说明：
#         获取 bot 对象
#     """
#     try:
#         return list(nonebot.get_bots().values())[0]
#     except IndexError:
#         return None


        
@on_command("get").handle()
async def _(bot: Bot, event: MessageEvent):
    if not is_tool('subnya'):
        get_tool()
    if is_command_available("subnya"):
        await bot.send(
            event,
            "subnya command is available",
            reply_to_message_id=event.message_id,
        )

    else:
        await bot.send(
            event,
            "subnya command is not available",
            reply_to_message_id=event.message_id,
         )   

@on_command("hello").handle()
async def _(bot: Bot, event: MessageEvent):
    await bot.send(event, "hola!", reply_to_message_id=event.message_id)

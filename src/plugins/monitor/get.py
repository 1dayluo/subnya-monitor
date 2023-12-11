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

command = on_command(
    "get"
)

        
@command.handle()
async def _(matcher: Matcher, event: MessageEvent):
    if is_command_available("subnya"):
        await matcher.send(
            "subnya command is available",
            reply_to_message_id=event.message_id,
        )

    else:
        await matcher.send(
            "subnya command is not available",
            reply_to_message_id=event.message_id,
         )   

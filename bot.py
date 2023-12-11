import nonebot
from nonebot.adapters.telegram import Adapter as TelegramAdapter

nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()

driver.register_adapter(TelegramAdapter)

nonebot.load_builtin_plugins("echo")

if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
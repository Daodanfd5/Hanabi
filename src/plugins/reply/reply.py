from nonebot.rule import to_me
from nonebot.plugin import on_command

weather = on_command("宵宫语录")

@weather.handle()
async def handle_function():
    pass  # do something here
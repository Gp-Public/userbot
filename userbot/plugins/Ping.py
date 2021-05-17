# rewritten by @saravanakrish

from telethon import events
from datetime import datetime

from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from userbot.manager.utils import edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TamilBot🇮🇳"


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    IMSID = bot.uid
    start = datetime.now()
    event = await edit_or_reply(event, "__**🚴🏻‍♂️ Pong!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**🚴🏻‍♂️ Pong!__**\n➥__**Ping Speed**__ {ms}\n➥ __**Bot**__ __**of**__ [{DEFAULTUSER}](tg://user?id={IMSID})"
    )

CMD_HELP.update(
    {
        "Ping": "**Plugin : **`Ping`\
        \n\n**Syntax : **`.ping`\
\n**Usage : **Check your bot status.\
"
    }
)
CMD_HELP.update(
    {
        "Broadcast": """**Plugin : ** `Broadcast`

  ╼•∘ 🅲🅼🅽🅳 ∘•╾  :`.sendto category_name`
  ╼•∘ 🆄🆂🅰️🅶🅴 ∘•╾  __will send the replied message to all the chats in give category__
"""
    }
)

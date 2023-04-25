from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from KynanRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot, OWNER_USERNAME


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"┏━━━━━━━━━━━━━━━━━━━━┓\n"
    TEXT += f"┠➣ **GUA {BOT_NAME}.** \n"
    TEXT += f"┠➣ **LIBRARY VERSION :** `{telever}` \n"
    TEXT += f"┠➣ **TELETHON VERSION :** `{tlhver}` \n"
    TEXT += f"┠➣ **PYROGRAM VERSION :** `{pyrover}` \n"
    TEXT += "┗━━━━━━━━━━━━━━━━━━━━┛\n\n"
    TEXT += "**THANKS YOO UDAH NAMBAHIN SI ARAB ROBOT DI GC LU❤️**"
    BUTTON = [
        [
            InlineKeyboardButton("HELP", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
        [
            InlineKeyboardButton("TUAN GUA", url=f"t.me/{OWNER_USERNAME}"),
        ]
    ]
    await message.reply_photo(
        photo=START_IMG,
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )

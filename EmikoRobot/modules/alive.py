import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot
from telegram.ext import CallbackContext, CallbackQueryHandler

PHOTO = "https://telegra.ph/file/09d6c7cc130bec60767f2.jpg"

async def awake(event):
    TEXT = "¤¤ 𝐇𝐞𝐲 𝐌𝐚𝐞𝐬𝐭𝐫𝐨, 𝐈'𝐦 ╚»𝐎𝐬𝐦𝐚𝐧𝐢 𝐂𝐡𝐚𝐭𝐛𝐨𝐭«╝! ¤¤\n\n"
    TEXT += f"ø 𝐘𝐞𝐚𝐡!! 𝐃𝐨𝐧'𝐭 𝐛𝐨𝐭𝐡𝐞𝐫 𝐚𝐛𝐨𝐮𝐭 𝐦𝐲 𝐬𝐩𝐞𝐞𝐝 𝐟𝐨𝐫 𝐧𝐨𝐰 ø\n\n"
    TEXT += f"ø 𝐎𝐬𝐦𝐚𝐧𝐢 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 : 𝐋𝐀𝐓𝐄𝐒𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 ø\n\n"
    TEXT += f"ø 𝐌𝐲 𝐌𝐚𝐞𝐬𝐭𝐫𝐨 (𝐂𝐫𝐞𝐚𝐭𝐨𝐫) : [𝗥 𝗶 𝗯 𝗮 𝗷](http://t.me/ribajosmani) ø\n\n"
    TEXT += f"ø ᴀɴʏ ɪ𝓼𝓼ᴜᴇ𝓼 ᴄᴏɴᴛᴀᴄᴛ us ʜᴇʀᴇ : @salmanhelp ø\n\n"
    TEXT += "♥ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ♥ (っ◔◡◔)っ "
    BUTTON = [
        [
            Button.url("🥺 Me Global", "https://t.me/mribaj"),
            Button.url("❤️ Love Store", "https://t.me/osmanilovestore"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)


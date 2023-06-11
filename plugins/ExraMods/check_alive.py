import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝖧𝖾𝗒 𝖡𝖴𝖣𝖣𝖸! 𝖨𝗆 𝖠𝖫𝖨𝖵𝖤 𝖺𝗇𝖽 𝗄𝗂𝖼𝗄𝗂𝗇𝗀 𝖧𝗂𝗍 <code>/start</code> 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

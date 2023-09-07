from config import DEV, STUFF
from .data import RadhaX
from YashuAlpha.Database.echo import *
from .verify import verify
from pyrogram import Client, filters

hl = STUFF.COMMAND_HANDLER

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + RadhaX

@Client.on_message(filters.command("addecho", hl))
async def addecho(_, m):
    x = await verify(m.from_user.id)
    if not x:
        return
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"`{hl}addecho [username|id|reply]`")
    if await verify(id):
        return await m.reply("`CAN'T ECHO THEM !`")
    if await is_echo(id):
        return await m.reply("`ECHO IS ALREADY ACTIVATED TO THIS USER !`")
    await add_echo(id)
    await m.reply(f"`ECHO ACTIVATED TO THE USER` <code>{id}</code>")

@Client.on_message(filters.command("rmecho", hl))
async def rmecho(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"`{hl}rmecho [username|id|reply]`")
    if not await is_echo(id):
        return await m.reply("`USER NOT IN ECHO LIST !`")
    await del_echo(id)
    await m.reply(f"`ECHO DEACTIVATED TO THE USER` <code>{id}</code>")

@Client.on_message(group=1)
async def echo_cwf(_, m):
    if m.from_user:
        if await is_echo(m.from_user.id):
            if m.text:
                txt = m.text
                await m.reply(txt)
            elif m.sticker:
                id = m.sticker.file_id
                await m.reply_sticker(id)
            elif m.photo:
                id = m.photo.file_id
                caption = m.caption if m.caption else ""
                await m.reply_photo(id, caption=caption)
            elif m.video:
                id = m.video.file_id
                caption = m.caption if m.caption else ""
                await m.reply_video(id, caption=caption)
            elif m.animation:
                id = m.animation.file_id
                caption = m.caption if m.caption else ""
                await m.reply_animation(id, caption=caption)
            elif m.document:
                id = m.document.file_id
                caption = m.caption if m.caption else ""
                await m.reply_document(id, caption=caption)
            elif m.audio:
                id = m.audio.file_id
                caption = m.caption if m.caption else ""
                await m.reply_audio(id, caption=caption)
            elif m.voice:
                id = m.voice.file_id
                caption = m.caption if m.caption else ""
                await m.reply_voice(id, caption=caption)
            else:
                pass

@Client.on_message(filters.command("echos", hl))
async def echos(_, m):
    if not await verify(m.from_user.id):
        return
    x = await get_echos()
    if not x:
        return await m.reply("`No user is added to echo !`")
    txt = "**Echo Users :**\n\n"
    for y in x:
        txt += f"`{y}`\n"
    txt += "\n"
    txt += f"**Count : {len(x)}**"
    await m.reply(txt)

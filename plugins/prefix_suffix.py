from pyrogram import Client, filters, enums
from helper.database import roheshbots


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Prefix__\n\nExample:- `/set_prefix @Rohesh_Bots`**")
    prefix = message.text.split(" ", 1)[1]
    Rohesh_Gavit = await message.reply_text("Please Wait ...")
    await roheshbots.set_prefix(message.from_user.id, prefix)
    await Rohesh_Gavit.edit("**Prefix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    Rohesh_Gavit = await message.reply_text("Please Wait ...")
    prefix = await roheshbots.get_prefix(message.from_user.id)
    if not prefix:
        return await Rohesh_Gavit.edit("**You Don't Have Any Prefix ❌**")
    await roheshbots.set_prefix(message.from_user.id, None)
    await Rohesh_Gavit.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    Rohesh_Gavit = await message.reply_text("Please Wait ...")
    prefix = await roheshbots.get_prefix(message.from_user.id)
    if prefix:
        await Rohesh_Gavit.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await Rohesh_Gavit.edit("**You Don't Have Any Prefix ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Suffix__\n\nExample:- `/set_suffix @Rohesh_Bots`**")
    suffix = message.text.split(" ", 1)[1]
    Rohesh_Gavit = await message.reply_text("Please Wait ...")
    await roheshbots.set_suffix(message.from_user.id, suffix)
    await Rohesh_Gavit.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    Rohesh_Gavit = await message.reply_text("Please Wait ...")
    suffix = await roheshbots.get_suffix(message.from_user.id)
    if not suffix:
        return await Rohesh_Gavit.edit("**You Don't Have Any Suffix ❌**")
    await roheshbots.set_suffix(message.from_user.id, None)
    await Rohesh_Gavit.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    Rohesh_Gavit = await message.reply_text("Please Wait ...")
    suffix = await roheshbots.get_suffix(message.from_user.id)
    if suffix:
        await Rohesh_Gavit.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await Rohesh_Gavit.edit("**You Don't Have Any Suffix ❌**")
       
      
     
    
   
   

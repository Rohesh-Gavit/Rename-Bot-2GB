from pyrogram import Client, filters 
from helper.database import roheshbots


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await roheshbots.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**You Don't Have Any Thumbnail ❌**") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await roheshbots.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Thumbnail Deleted Successfully 🗑️**")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    roheshbots = await message.reply_text("Please Wait ...")
    await roheshbots.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await roheshbots.edit("**Thumbnail Saved Successfully ✅️**")



from handlers.database.users_sql import Users, num_users
from handlers.database.chats_sql import num_chats
from handlers.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(~filters.edited & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


async def check_for_users(user_ids):
    if isinstance(user_ids, int):
        user_ids = [user_ids]
    elif isinstance(user_ids, list):
        pass
    for user_id in user_ids:
        q = SESSION.query(Users).get(user_id)
        if not q:
            SESSION.add(Users(user_id))
            SESSION.commit()
        else:
            SESSION.close()

@Client.on_message(~filters.edited & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(1946995626) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    chats = await num_chats()
    await msg.reply(f"Total Users : {users} \n\nTotal Chats : {chats}", quote=True)

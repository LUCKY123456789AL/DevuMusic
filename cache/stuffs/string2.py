from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


button1 = [
    [
        InlineKeyboardButton(text="🥀𝐁𝐀𝐁𝐘✨", url=f"https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton(text="🤎𝐊𝐈𝐃𝐍𝐀𝐏💚", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="🌷𝐏𝐀𝐏𝐀 𝐉𝐈🍁", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="🌟𝐑𝐄𝐏𝐎✨", callback_data="repo_k"),
    ],                
    [                    
        InlineKeyboardButton(text="🙀𝐎𝐖𝐒𝐌 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒😻", callback_data="help_"),
    ],
]


button2 = [
    [
        InlineKeyboardButton(text="🙊𝐁𝐀𝐒𝐈𝐂🙈", callback_data="basic_"),
        InlineKeyboardButton(text="🍸𝐀𝐃𝐕𝐀𝐍𝐂𝐄🥂", callback_data="admin_cmd"),
    ],
    [
        InlineKeyboardButton(text="☀️𝐎𝐅𝐅☀️", callback_data="close_"),
        InlineKeyboardButton(text="🔥𝐁𝐀𝐂𝐊🔥", callback_data="HOME"),
    ],
]



button3 = [
    [
        InlineKeyboardButton(text="🐿️𝐀𝐀 𝐉𝐀🐒", url="https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton(text="🥱𝐁𝐀𝐂𝐊🥱", callback_data="HOME"),
    ],
]


button4 = [
    [
        InlineKeyboardButton(text="💛𝐎𝐅𝐅💛", callback_data="close_"),
        InlineKeyboardButton(text="💔𝐁𝐀𝐂𝐊💔", callback_data="help_"),
    ],
]






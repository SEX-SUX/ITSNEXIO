from pyrogram.types import InlineKeyboardButton

import config
from NEXIOMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [ InlineKeyboardButton(text="❖ sᴀɴᴀᴛᴀɴɪ ᴛᴇᴄʜ ❖", url=f"https://t.me/ALL_SANATANI_BOT")],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true",)
        ],
        [
            InlineKeyboardButton(text="ᴧησηʏϻσᴜs", url=f"HTTPS://T.ME/ITS_NEXIO"),
            InlineKeyboardButton(text="sᴧᴄʜɪη", url=f"HTTPS://T.ME/V_VIP_OWNER"),
        ],
        [
            InlineKeyboardButton(text="侖 ᶦϻͣ ⁣⁤⚚ 𝗦𝝙𝗡𝝙𝗧𝝙𝗡𝗜 侖", url=f"https://t.me/II_SANATANI_II")
        ],
    ]
    return buttons

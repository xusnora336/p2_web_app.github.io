from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiohttp import web

web_app = WebAppInfo(url="https://xusnora336.github.io/p2_web_app.github.io/")
web_app_btn=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Web App", web_app=web_app)],
    ]
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiohttp import web

web_app = WebAppInfo(url="https://google.com")
web_app_btn=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Web App", web_app=web_app)],
    ]
)
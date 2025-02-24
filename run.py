import asyncio

import uvicorn
from aiogram import Dispatcher
from fastapi import FastAPI

import app.handlers
from app.database.models import async_main
from app.payments import router
from app.bot import bot



app_api = FastAPI()
app_api.include_router(router)


async def main():
    await async_main()
    dp = Dispatcher()
    dp.include_router(router=app.handlers.router)
    print("✅ Bot Started!")

    await dp.start_polling(bot)

async def start():
    asyncio.create_task(main())

    config = uvicorn.Config(app_api, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print("Exit.")
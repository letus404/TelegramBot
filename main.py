# main.py

import asyncio
from bot.bot import run_bot
from bot.scheduler import start_scheduler 
from bot.database import init_db

async def main():
    init_db()
    await asyncio.gather(
        run_bot(),
        start_scheduler() 
    )

if __name__ == "__main__":
    asyncio.run(main())

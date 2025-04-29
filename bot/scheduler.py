# scheduler.py

import asyncio
import random
from bot.database import get_message_by_id, get_all_messages, get_all_chat_ids
from bot.bot import send_message

# Loop individual que recarga los datos del mensaje desde la DB en cada iteración
async def schedule_message_loop(msg_id):
    while True:
        # Obtener la versión más reciente del mensaje desde la base de datos
        msg = get_message_by_id(msg_id)
        if not msg:
            print(f"Mensaje ID {msg_id} no encontrado. Reintentando en 60s...")
            await asyncio.sleep(60)
            continue

        _, content, enabled, interval_min, interval_max = msg

        if enabled:
            chat_ids = get_all_chat_ids()
            for chat_id in chat_ids:
                await send_message(chat_id, content)
                print(f"Mensaje '{content}' enviado a {chat_id}")

            wait_time = random.randint(interval_min, interval_max)
            print(f"Esperando {wait_time} segundos antes del próximo envío del mensaje ID {msg_id}...")
            await asyncio.sleep(wait_time)
        else:
            print(f"Mensaje ID {msg_id} está deshabilitado. Reintentando en 60s...")
            await asyncio.sleep(60)

# Lanzador de todos los loops
async def start_scheduler():
    messages = get_all_messages()
    tasks = [schedule_message_loop(msg[0]) for msg in messages]  # Pasamos solo el msg_id
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(start_scheduler())

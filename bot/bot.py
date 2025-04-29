# bot.py
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from config import BOT_TOKEN
from bot.database import save_chat_id, get_all_chat_ids

# Setup básico
logging.basicConfig(level=logging.INFO)

# Instancias principales
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Manejador del comando /start
@router.message(lambda msg: msg.text and msg.text.startswith("/start"))
async def start_handler(message: Message):
    await message.answer("He despertado 👽. Empezaré a enviarte mensajes cada dos minutos 😅 ")

# Guarda chat_id y responde con info básica
@router.message()
async def get_chat_id(message: Message):
    chat_id = message.chat.id
    save_chat_id(chat_id)
    await message.answer(f"¡Hola! Soy un bot que envía mensajes programados. ✨, para iniciarme escribe /start")

# Comando para enviar un mensaje automático a todos los registrados
@router.message(lambda msg: msg.text and msg.text.startswith("/enviar"))
async def enviar_handler(message: Message):
    chat_ids = get_all_chat_ids()
    texto = "📢 Este es un mensaje automático para todos los usuarios registrados."

    enviados = 0
    for chat_id in chat_ids:
        try:
            await bot.send_message(chat_id, texto)
            enviados += 1
        except Exception as e:
            logging.warning(f"No se pudo enviar mensaje a {chat_id}: {e}")

    await message.answer(f"Mensaje enviado a {enviados} usuarios.")

# Función para lanzar el bot
async def run_bot():
    await dp.start_polling(bot)

# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Token del bot de Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "8014426023:AAGWtM9TSUFnyVR-Zs9yXEvWzD34auHkU9E")

# URL o path de la base de datos (usaremos SQLite para algo simple)
DB_PATH = os.getenv("DB_PATH", "messages.db")

# Tiempo mínimo entre publicaciones (en segundos)
MIN_INTERVAL = int(os.getenv("MIN_INTERVAL", 60))

# Tiempo máximo entre publicaciones (en segundos)
MAX_INTERVAL = int(os.getenv("MAX_INTERVAL", 300))

# Nombre del administrador o grupo autorizado
ADMIN_USERNAMES = os.getenv("ADMIN_USERNAMES", "").split(",")

# Agregar validación para las variables de entorno
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN no está configurado")

if not DB_PATH:
    raise ValueError("DB_PATH no está configurado")

if MIN_INTERVAL < 0 or MAX_INTERVAL < 0:
    raise ValueError("MIN_INTERVAL y MAX_INTERVAL deben ser números positivos")

if MIN_INTERVAL > MAX_INTERVAL:
    raise ValueError("MIN_INTERVAL no puede ser mayor que MAX_INTERVAL")

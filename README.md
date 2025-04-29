Telegram Bot Proyecto

Este proyecto implementa un bot de Telegram que envía mensajes programados a una lista de chats o usuarios registrados, y cuenta con un panel web para gestionar contenido e intervalos sin necesidad de editar código.

Características

Envío de mensajes automáticos a intervalos configurables (mínimo y máximo).

Panel web (Flask + Tailwind) para:

Agregar nuevos mensajes.

Editar contenido e intervalos.

Activar/desactivar mensajes.

Eliminar mensajes.

Registro automático de chat_id cuando un usuario inicia conversación.

Posibilidad de envío manual (“Enviar ahora”) desde el panel.

Almacenamiento en SQLite (messages.db) con dos tablas: messages y users.

Requisitos Previos

Python 3.8 o superior.

Git (para control de versiones y despliegue).

Token de bot de Telegram (obtenido de @BotFather).

(Opcional) Heroku CLI o Railway CLI para despliegue.

Instalación

Clonar el repositorio: git clone https://github.com/tu_usuario/telegram-bot.git

Entrar al directorio del proyecto: cd telegram-bot

Crear y activar un entorno virtual:

Windows: python -m venv venv venv\Scripts\activate

Linux/Mac: python -m venv venv source venv/bin/activate

Instalar dependencias: pip install -r requirements.txt

Crear archivo .env en la raíz con: BOT_TOKEN=tu_token_de_telegram DB_PATH=messages.db (y cualquier otra variable necesaria)

Inicializar la base de datos (solo la primera vez): python

from database import init_db init_db() exit()

Uso Local

Ejecutar el bot + scheduler: python main.py

Ejecutar solo el panel: python run.py Abrir en el navegador: http://localhost:5000

Interactuar en Telegram:

Enviar /start para registrarte.

Usar el panel para agregar y gestionar mensajes.
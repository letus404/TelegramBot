from bot.database import init_db, add_message, get_all_messages

init_db()
add_message("Mensaje de prueba - Envio de mensajes automático activado . ", 90, 180)
print(get_all_messages())
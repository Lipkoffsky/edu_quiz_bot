from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

# ADMINS = [836221909]
# BOT_TOKEN = "5046040497:AAEBQ39u5EtDnhSc7YOOHcIVHvDt5nMwXVc"
# IP = "127.0.0.1"


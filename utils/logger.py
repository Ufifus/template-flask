from dotenv import load_dotenv
import os
import logging

load_dotenv()

# Логирование всех операций

# получение пользовательского логгера и установка уровня логирования
logger = logging.getLogger('DEBUG-LOGGER')
logger.setLevel(logging.DEBUG)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
handler = logging.FileHandler(f"debug.log", mode='w')
handler.setLevel(logging.WARNING)
formatter = logging.Formatter("%(name)s %(asctime)s [ %(levelname)s ] %(message)s")

# добавление форматировщика к обработчику
handler.setFormatter(formatter)
# добавление обработчика к логгеру
logger.addHandler(handler)
logger.addHandler(logging.StreamHandler())
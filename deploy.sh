#!/bin/bash

# Перейти в директорию проекта
cd /path/to/your/project

# Обновить код из репозитория
git pull origin master

# Активировать виртуальное окружение
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Выполнить миграции базы данных (для Django)
python manage.py migrate

# Собрать статические файлы (для Django)
python manage.py collectstatic --noinput

# Перезапустить сервис (например, через systemd)
sudo systemctl restart your-app.service
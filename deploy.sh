#!/bin/bash

# Установка переменной окружения для совместимости с OpenSSL
export NODE_OPTIONS=--openssl-legacy-provider

# Сборка React-приложения
npm run build

# Создание директории для статических файлов, если она не существует
mkdir -p static
mkdir -p staticfiles

# Копирование собранных файлов в директорию static Django
cp -r build/* static/

# Выполнение миграций и сборка статических файлов Django
python3 manage.py collectstatic --noinput

# Деплой на GitHub Pages
npm run deploy

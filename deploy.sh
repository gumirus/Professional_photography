#!/bin/bash

# Сборка React-приложения
npm run build

# Копирование собранных файлов в директорию static Django
cp -r build/* path/to/your/django/static/

# Выполнение миграций и сборка статических файлов Django
python3 manage.py collectstatic --noinput

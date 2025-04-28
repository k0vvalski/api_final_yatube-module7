# API для Yatube.
## Другие проекты (Яндекс Backend):
### Блогикум (1 часть) <- https://github.com/k0vvalski/blogicum-1pt;
### Блогикум (2 часть) <- https://github.com/k0vvalski/blogicum-2pt;
### Блогикум (3 часть) <- https://github.com/k0vvalski/blogicum-3pt.

## Технологии:
```
Python 3.11.0
Django 3.2.16
Django REST framework 3.12.4
Simple JWT
```
## Установка (macOS):
### 1. Клонирование репозитория
Откройте терминал и выполните команду: 
```
  git clone https://github.com/k0vvalski/api_final_yatube-module7.git
```
### 2. Переход в директорию проекта:
После клонирования перейдите в директорию проекта: 
```
  cd api_final_yatube-module7
```
### 3. Создание и активация виртуального окружения:
```
  python3.11 -m venv venv  
  source venv/bin/activate
```
### 4. Обновите pip:  
```
  python3.11 -m pip install --upgrade pip
```
### 5. Установка зависимостей:
```
  pip install -r requirements.txt
```
### 6. Перейти в папку проекта и запустить его:
```
  python3.11 yatube_api/manage.py migrate  
  python3.11 yatube_api/manage.py runserver 8001
```
### 7. Документация будет доступна:
```
  http://localhost:8001/
```

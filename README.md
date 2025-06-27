# Описание проекта

Проект представляет собой консольное приложение для поиска записей в базе данных по заданному шаблону. Приложение анализирует переданные аргументы, определяет их типы и ищет совпадения в TinyDB.



# Form Template Finder

Приложение для поиска шаблонов форм по переданным полям и определения типов полей.

# Установка 

Клонирование репозитория

git clone https://github.com/TolstovaDA21/form_recognizer.git
cd form_recognizer

# Функциональность

Определение типов данных (email, телефон, дата, текст)
Парсинг аргументов командной строки
Работа с базой данных TinyDB
Поиск записей по шаблону

# Тестирование

python -m unittest discover tests

# Cтруктура 

form_recognizer/
|                
├── app/
│   ├── __init__.py
│   ├── form_finder.py    
│   └── type_checker.py   
├── database/
│   └── forms.json        
├── tests/
│   └── test_form_finder.py
├── .gitignore
├── requirements.txt      
├
└── README.md

# Структура БД
 database/forms.json



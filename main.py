#!/usr/bin/env python3
from app.form_finder import FormFinder
from app.type_checker import TypeChecker
import json
import sys

def main():
    try:
        # Инициализация поисковика форм
        finder = FormFinder('database/forms.json')
        
        print("=== Form Recognizer ===")
        print("Введите данные для поиска шаблона (Ctrl+D для завершения):")
        
        # Чтение входных данных из stdin
        input_data = {}
        for line in sys.stdin:
            try:
                # Парсинг в формате "ключ=значение"
                key, value = line.strip().split('=', 1)
                input_data[key] = value
            except ValueError:
                print(f"Ошибка: неверный формат строки '{line.strip()}'. Используйте key=value")

        if not input_data:
            print("Ошибка: не введены данные")
            return

        # Определение типов полей (для демонстрации)
        print("\nОпределенные типы полей:")
        for field, value in input_data.items():
            field_type = TypeChecker(value).type
            print(f"- {field}: {value} => {field_type}")

        # Поиск совпадений в БД
        print("\nПоиск совпадающих шаблонов...")
        matched_forms = finder.find_matching_forms(input_data)

        # Вывод результатов
        if matched_forms:
            print("\nНайдены совпадающие шаблоны:")
            for form in matched_forms:
                print(f"\nНазвание формы: {form.get('form_name', 'N/A')}")
                print("Поля:")
                for field, field_type in form.items():
                    if field != 'form_name':
                        print(f"  {field}: {field_type}")
        else:
            print("\nСовпадающих шаблонов не найдено.")
            print("Определенные типы полей:", {f: TypeChecker(v).type for f, v in input_data.items()})

    except Exception as e:
        print(f"\nОшибка: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
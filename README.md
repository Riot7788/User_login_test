# Login Tests

Автотесты для проверки логина на сайте https://www.saucedemo.com/ с использованием Python.

## Проект содержит:
- Python 3.10
- Selenium
- Pytest
- Allure
- Page Object Model
- .env
- Docker
- README с инструкцией 

## Установка:

```bash
  pip install -r requirements.txt
```
## Запуск тестов локально
1. Запуск автотестов:
```bash
  pytest
```
2. Запуск с Allure:
```bash
  allure serve allure-results
```
## Запуск тестов через Docker

1. Сборка Docker образа:
```bash
  docker build -t login_tests .
```
2. Запуск контейнера и выполнение тестов:
```bash
  docker run --rm login_tests
```
## Были реализованы тесты:
1. Тест открытие страницы
2. Тест успешный логин standard_user
3. Логин с неверным паролем
4. Логин заблокированного пользователя
5. Логин с пустыми полями
6. Логин пользователем PERFORMANCE_USER
7. Логин с пустым паролем
8. Логин с пустым username
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
## Настройка:
1. Репозиторий: git clone https://github.com/Riot7788/User_login_test
2. Создайте файл .env в корневой директории:
```
  BASE_URL=https://www.saucedemo.com/
  STANDARD_USER=standard_user
  STANDARD_PASSWORD=secret_sauce
  LOCKED_USER=locked_out_user
  PERFORMANCE_USER=performance_glitch_user
  WRONG_PASSWORD=wrong_password
```
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
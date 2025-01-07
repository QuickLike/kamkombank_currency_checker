# [Курсы валют "КАМКОМБАНКа"](https://github.com/QuickLike/kamkombank_currency_checker)

## Описание проекта:

Парсер курсов валют сайта [КАМКОМБАНК](https://www.kamkombank.ru/).

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/QuickLike/kamkombank_currency_checker) и перейдите в него в командной строке:
```bash
git clone https://github.com/QuickLike/kamkombank_currency_checker

cd kamkombank_currency_checker
```
Создайте виртуальное окружение и активируйте его

Windows
```bash
python -m venv venv
venv/Scripts/activate
```

Linux/Ubuntu/MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```
Обновите pip:
```bash
python -m pip install --upgrade pip
```
Установите зависимости:
```bash
pip install -r requirements.txt
```
Создайте файл .env и добавьте переменные
```dotenv
CITY=<Москва,Санкт-Петербург,Набережные Челны>
DELAY=<задержка_между_отправкой_курсов_валют_в_минутах>
```

(Опционально)Для получения информации о курсах валют в Telegram, нужно добавить в файл .env переменные:
```dotenv
BOT_TOKEN=<токен_вашего_бота>
CHAT_ID=<ваш_id>
```


## Запуск парсера.

```
python main.py
```


## Автор

[Власов Эдуард](https://github.com/QuickLike)

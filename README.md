# Транслятор cpp to go

## Описание транслятора

**Синтаксический анализатор**, как и **оптимизатор**
идёт под капотом у парсера.

## Как запустить

На машине, на которой вы запускаете программу,
должен быть установлен python.

### Гайд по установке python3

#### Проверяем установлен ли python

```sh
python3 --version
```

#### Установка python3

_Linux:_

```sh
sudo apt update
sudo apt install python3
```

[**MacOs или Windows**](https://www.python.org/downloads/)

### Запуск приложения

#### Виртуальное окружение

_Unix, MacOS:_

```sh
virtualenv venv -p python3
source venv/bin/activate
```

#### Установка зависимостей

```sh
python3 -m pip install -r requirements.txt
```

#### Запуск

```sh
python3 main.py
```

> _P.S._ После `main.py` можно указать название файла 
без расширения из директории `test_case` 
для передачи транслятору файла отличного от `main.cpp`
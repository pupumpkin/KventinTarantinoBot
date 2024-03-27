# Бот-сценарист Квентин Тарантино

Телеграм-бот, который на основе выбранных пользователем жанра, персонажа и сеттинга создает 
уникальный сценарий.

## Описание

Проект представляет собой бота-сценариста, который предлагает на
выбор три жанра(комедия, романтика, фэнтези), четыре персонажа(два персонажа
женского пола и два персонажа мужского пола), три сеттинга(Ведьмак, GTA 5, Breathedge).
В зависимости от выбора пользователя бот отвечает различно, генерируя сценарий, в котором
выбранный персонаж находится в выбранной вселенной и производит какие-либо действия.

## Инструкции по использованию
- Начало:
  - Найдите бота в Telegram: @tarantinokvenbot
  - Запустите бота командой /start.
  - Бот готов к работе!
- Режим ответа на вопросы:
  - Бот предоставляет выбор жанра.
  - Бот предоставляет выбор персонажа с описанием.
  - Бот предоставляет выбор сеттинга с описанием.
  - Бот распознает текст от пользователя, который обязательно должен начинаться со "Сгенерируй сценарий,
в котором..". 
  - Бот выводит ответ от GPT.
- Режим объяснения:
  - После просьбы объяснить бот выводит продолжение ответа от GPT.
- Режим отладки(для тестировщиков):
  - По команде /debug бот отправляет файл с логами.
  - По команде /debug_mode_on бот переходит в режим отладке, в котором пользователю выводятся все
логи и состояние запроса к нейросети.
  - По команде /debug_mode_off бот переходит в режим ответа на вопросы.

## Контакты
Для связи с разработчиком можно использовать следующие контакты:

- [Telegram](https://t.me/mrisxxs)
- [Почта](atrosenko596@gmail.com)
- [Vk](https://vk.com/shinepg)
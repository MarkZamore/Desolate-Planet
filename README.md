# Desolate Planet

Подготовка сборки 1.8.6.0 для LANMinecraft. [Авторский клиентский выпуск](https://www.curseforge.com/minecraft/modpacks/desolate-planet/files/8267330)

`tools/upstream-client-lock.json` фиксирует SHA256 и размер оригинального ZIP, ссылки на официальный источник, записи зависимостей и SHA256 файлов внутри авторских overrides. Minecraft и загрузчик взяты из оригинального манифеста. Java в `portable-pack.json` соответствует выбору текущего лаунчера для этой версии Minecraft и проверяется при запуске.

## Восстановление авторского клиента

Из корня LANMinecraft используйте `tools/PackData/CurseForge/prepare.py` с `--project-id 1318843` и `--file-id 8267330`. Укажите этот lock через `--expect` и новый каталог внутри своего стенда через `--output`. Полная подготовка проверяет все заявленные зависимости. Отдельный lock поставки и метаданные карточки готовятся после запуска и проверки фактического состава.

## Публикация

У сборки CC BY-NC-SA 4.0. В манифесте закреплён JourneyMap, CF 32274/5789363. Его условия ограничивают перепубликацию JAR. [Условия](https://teamjm.github.io/journeymap-docs/latest/about/licensing/)

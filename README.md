# Desolate Planet

Подготовка сборки 1.8.6.0 для LANMinecraft. [Авторский клиентский выпуск](https://www.curseforge.com/minecraft/modpacks/desolate-planet/files/8267330)

`tools/upstream-client-lock.json` фиксирует SHA256 и размер оригинального ZIP, ссылки на официальный источник, записи зависимостей и SHA256 файлов внутри авторских overrides. Minecraft и загрузчик взяты из оригинального манифеста. Java в `portable-pack.json` соответствует выбору текущего лаунчера для этой версии Minecraft и проверяется при запуске.

## Восстановление авторского клиента

Закреплённый авторский клиент CurseForge использует project ID 1318843 и file ID 8267330.
Для подготовки текущего кандидата из корня LANMinecraft запустите:

```powershell
python -B tools/PackData/CurseForge/release_overlay.py stage --pack-source LocalSources/Desolate-Planet --output $stage
```

`tools/overlay.json` сохраняет политику открытия мира через Steam. Для нового авторского выпуска снимите отдельную квитанцию через `prepare.py --client-only` и проверьте её командой `release_overlay.py review-update`. При изменении защищённого входа пересмотрите рецепт и закрепите новые точные байты. После нативной проверки сохраните полный `tools/upstream-lock.json` и выполните `release_overlay.py verify` по готовому манифесту.

Оригинальный e4mc `849519/8225255` проверяется и остаётся в авторском lock. Рецепт исключает его JAR из игровой поставки для совместимости с e4steam и закрепляет `hostEnabled = false`.

## Публикация

У сборки CC BY-NC-SA 4.0. В манифесте закреплён JourneyMap, CF 32274/5789363. Его условия ограничивают перепубликацию JAR. [Условия](https://teamjm.github.io/journeymap-docs/latest/about/licensing/)

Пользователь подтвердил наличие разрешения на перезалив. Публикация следует после проверки полного состава и нативной приёмки.

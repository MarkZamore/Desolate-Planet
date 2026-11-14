---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоматическая печь
  icon: minecraft:furnace
---

# Автоматическая печь

В этой схеме используется поставщик шаблонов <ItemLink id="pattern_provider" />, поэтому она рассчитана на подключение к [автокрафту](../ae2-mechanics/autocrafting.md).
Для автономной печи хватит воронок и сундуков.

Автоматизировать печь <ItemLink id="minecraft:furnace" /> сложнее, чем простой механизм вроде [зарядника](../example-setups/charger-automation.md).
У печи два входа и один выход. Предметы для переплавки подаются сверху,
топливо сбоку. Результат извлекается снизу.

Можно поставить поставщик шаблонов <ItemLink id="pattern_provider" />
сверху, шину экспорта <ItemLink id="export_bus" /> сбоку для непрерывной подачи топлива и шину импорта <ItemLink id="import_bus" />
снизу для вывода результатов в сеть. Для этого нужны три [канала](../ae2-mechanics/channels.md).

Как обойтись одним каналом:

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/furnace_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) Поставщик шаблонов. Направленный вариант, настроенный гаечным ключом из истинного кварца. Вставлены шаблоны обработки.

        ![Шаблон плавки железа](../assets/diagrams/furnace_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (2) Интерфейс. Настройки по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="1.3 2 1">
        (3) Шина хранения № 1. Принимает только уголь.
        <ItemImage id="minecraft:coal" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 2 0" max="1 2.3 1">
        (4) Шина хранения № 2. Исключает уголь с помощью карты-инвертера.
        <Row><ItemImage id="minecraft:coal" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* Поставщик шаблонов <ItemLink id="pattern_provider" /> (1) используется с настройками по умолчанию и нужными шаблонами <ItemLink id="processing_pattern" />.
    Сделайте его направленным с помощью ключа <ItemLink id="certus_quartz_wrench" />.

  ![Шаблон плавки железа](../assets/diagrams/furnace_pattern.png)

* Интерфейс <ItemLink id="interface" /> (2) используется с настройками по умолчанию.
* Первая шина хранения <ItemLink id="storage_bus" /> (3) отфильтрована по углю или другому выбранному топливу.
* Вторая шина хранения <ItemLink id="storage_bus" /> (4) исключает выбранное топливо за счёт карты <ItemLink id="inverter_card" />.

## Как это работает

1. Поставщик шаблонов <ItemLink id="pattern_provider" /> отправляет ингредиенты в интерфейс <ItemLink id="interface" />.
   (Для экономии операций поставщик работает сразу через подключённые шины хранения, как через собственные грани. Предметы во внутренний инвентарь интерфейса не попадают.)
2. Интерфейс настроен не держать запас, поэтому отправляет ингредиенты в [хранилище сети](../ae2-mechanics/import-export-storage.md).
3. Единственные хранилища зелёной подсети — шины <ItemLink id="storage_bus" />. Шина с фильтром на уголь подаёт его в боковой слот для топлива.
    Шина, отфильтрованная на всё, кроме угля, подаёт предметы в верхний слот для плавки.
4. Печь переплавляет предметы.
5. Воронка извлекает результат снизу и кладёт в слоты возврата поставщика, откуда он попадает в основную сеть.

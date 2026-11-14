---
navigation:
  parent: example-setups/example-setups-index.md
  title: Пополнение запаса по сигналу уровня
  icon: level_emitter
---

# Пополнение запаса по сигналу уровня

Как поддерживать заданный запас предмета и создавать новые экземпляры по мере расхода?

Шина экспорта <ItemLink id="export_bus" />, излучатель уровня <ItemLink id="level_emitter" /> и карта изготовления <ItemLink id="crafting_card" /> позволяют заказывать предмет
через [автокрафт](../ae2-mechanics/autocrafting.md). Такая схема подходит для большого запаса одного предмета.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/level_emitter_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (1) Шина экспорта. Фильтр на нужный предмет, установлены редстоуновая карта и карта изготовления.
        Режим красного камня — «Активируется сигналом», режим создания — «Не использовать имеющиеся в наличии предметы».
        <Row><ItemImage id="redstone_card" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.7 1 0" max="1 2 1">
        (2) Излучатель уровня. Заданы нужный предмет и количество. Включает сигнал, когда запас ниже порога.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (3) Интерфейс. Настройки по умолчанию.
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* В шине экспорта <ItemLink id="export_bus" /> (1) выберите нужный предмет для фильтра. Вставьте карту <ItemLink id="redstone_card" /> и карту <ItemLink id="crafting_card" />.
  Установите режим красного камня «Активируется сигналом» и режим создания «Не использовать имеющиеся в наличии предметы».
* В излучателе уровня <ItemLink id="level_emitter" /> (2) задайте предмет и количество, затем включите подачу сигнала при запасе ниже порога.
* Интерфейс <ItemLink id="interface" /> (3) используется с настройками по умолчанию.

## Как это работает

1. Если в [хранилище сети](../ae2-mechanics/import-export-storage.md) осталось меньше предметов, чем задано в
   излучателе уровня <ItemLink id="level_emitter" />, он подаёт сигнал красного камня.
2. По сигналу благодаря карте <ItemLink id="crafting_card" /> и режиму «Не использовать имеющиеся в наличии предметы»
   шина экспорта <ItemLink id="export_bus" /> заказывает недостающее через [автокрафт](../ae2-mechanics/autocrafting.md),
   затем экспортирует созданные предметы.
3. Интерфейс <ItemLink id="interface" /> не настроен хранить запас, поэтому передаёт поступившие в него предметы в хранилище сети.

---
navigation:
  parent: example-setups/example-setups-index.md
  title: Подсеть для передачи предметов и жидкостей
  icon: storage_bus
---

# Подсеть для передачи предметов и жидкостей

[Устройства AE2](../ae2-mechanics/devices.md) могут работать как предметная или жидкостная труба.
Например, такая подсеть возвращает результат обработки в поставщик шаблонов <ItemLink id="pattern_provider" />.

Есть две основные схемы.

## Шина импорта → шина хранения

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_storage_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        (1) Шина импорта. Можно настроить фильтр.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        (2) Шина хранения. Можно настроить фильтр. Эта шина и остальные шины назначения
        должны быть единственными хранилищами подсети.
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
        Источник
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
        Приёмник
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Шина импорта <ItemLink id="import_bus" /> (1) извлекает предметы или жидкость из источника и отправляет их в [хранилище подсети](../ae2-mechanics/import-export-storage.md).
Единственное хранилище подсети — шина <ItemLink id="storage_bus" /> (2). Поэтому ресурсы попадают в подключённый к ней приёмник.
Питание подаётся через кварцевое волокно <ItemLink id="quartz_fiber" />.
Фильтры можно настроить на обеих шинах. Без фильтров схема переносит все доступные ресурсы.
Можно подключить несколько шин импорта и несколько шин хранения.

## Шина хранения → шина экспорта

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/storage_export_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        (1) Шина хранения. Можно настроить фильтр. Эта шина и остальные шины-источники
        должны быть единственными хранилищами подсети.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        (2) Шина экспорта. Требуется фильтр.
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
        Источник
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
        Приёмник
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Шина экспорта <ItemLink id="export_bus" /> на приёмнике запрашивает ресурсы из [хранилища подсети](../ae2-mechanics/import-export-storage.md) по своему фильтру.
Единственное хранилище подсети — шина <ItemLink id="storage_bus" />, поэтому ресурсы поступают из подключённого к ней источника.
Питание подаётся через кварцевое волокно <ItemLink id="quartz_fiber" />.
Без фильтра на шине экспорта схема не работает.
Можно подключить несколько шин хранения и несколько шин экспорта.

## Нерабочая схема. Шина импорта → шина экспорта

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_export_pipe.snbt" />

<BoxAnnotation color="#dd3333" min="3.7 0 0" max="4 1 1">
        Шина импорта. В подсети нет хранилища, поэтому ей некуда отправить ресурсы.
  </BoxAnnotation>

<BoxAnnotation color="#dd3333" min="1 0 0" max="1.3 1 1">
        (2) Шина экспорта. В подсети нет хранилища, поэтому ей неоткуда извлечь ресурсы.
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#ff0000">
        Источник
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#ff0000">
        Приёмник
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Соединить шины импорта и экспорта напрямую не получится. Шина импорта пытается забрать ресурсы из источника
и отправить их в хранилище. Шина экспорта пытается извлечь из хранилища ресурсы и поместить их в приёмник.
**Хранилища в такой подсети нет**, поэтому шины ничего не переместят.


## Ввод и вывод через одну грань

Если механизм принимает и отдаёт предметы через одну грань, как зарядник <ItemLink id="charger" />,
совместите обе схемы. Так можно подавать ингредиенты и забирать результат через ту же грань.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_storage_export_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="4 1 1" max="5 1.3 2">
        (1) Шина импорта. Можно настроить фильтр.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 1 1" max="3 1.3 2">
        (2) Шина хранения. Можно настроить фильтр. Эта шина и остальные шины, через которые нужно передавать ресурсы в обе стороны,
        должны быть единственными хранилищами подсети.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0 1" max="3 1 2">
        (3) Механизм, которому нужна и подача, и извлечение ресурсов. Здесь это зарядник.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 1" max="1 1.3 2">
        (4) Шина экспорта. Требуется фильтр.
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 1.5" color="#00ff00">
        Источник
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 1.5" color="#00ff00">
        Приёмник
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Интерфейсы

Кроме шин импорта и экспорта есть другие [устройства](../ae2-mechanics/devices.md), которые могут отправлять предметы в
[хранилище сети](../ae2-mechanics/import-export-storage.md) и извлекать их оттуда.
Интерфейс <ItemLink id="interface" /> отправляет в хранилище предметы, для которых не задан запас.
Это можно использовать так же, как пару из шины импорта и шины хранения.
Интерфейс, настроенный поддерживать запас, забирает запрошенные предметы из хранилища, как в схеме со шинами хранения и экспорта.
Интерфейс может держать запас одних предметов и пропускать другие. Так через шины хранения можно удалённо передавать предметы в обе стороны.

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/interface_pipes.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        Интерфейс
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        Шина хранения
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.7 0 2" max="4 1 3">
        Шина хранения
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 2" max="1 1.3 3">
        Шина хранения
  </BoxAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Несколько источников или приёмников

В одной подсети можно использовать несколько шин импорта <ItemLink id="import_bus" />, экспорта <ItemLink id="export_bus" /> или хранения <ItemLink id="storage_bus" />.

<GameScene zoom="3" background="transparent">
<ImportStructure src="../assets/assemblies/many_to_many_pipe.snbt" />

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

## Подача ингредиентов в несколько мест

С одной грани поставщика шаблонов <ItemLink id="pattern_provider" /> можно отправлять ингредиенты
к нескольким механизмам или на разные грани одного механизма.

Обычные пары шин здесь не помогут: поставщик шаблонов <ItemLink id="pattern_provider" /> не хранит ингредиенты,
а выталкивает их в соседние инвентари. Значит, рядом нужен инвентарь,
который сам может передавать предметы дальше.

Для этого подходит интерфейс <ItemLink id="interface" />.
Сделайте поставщик направленным или плоским. Другой вариант — использовать плоский интерфейс.
Поставщик и интерфейс не должны образовывать сетевое соединение.

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        Интерфейс. Используйте плоскую версию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        Шины хранения
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        Точки подачи ингредиентов: разные механизмы или грани одного механизма
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

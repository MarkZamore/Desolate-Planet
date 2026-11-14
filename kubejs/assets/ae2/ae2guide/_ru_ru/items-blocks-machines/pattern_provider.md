---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Поставщик шаблонов
  icon: pattern_provider
  position: 210
categories:
- devices
item_ids:
- ae2:pattern_provider
- ae2:cable_pattern_provider
---

<a name="the-pattern-provider" />

# Поставщик шаблонов

<Row gap="20">
<BlockImage id="pattern_provider" scale="8" />
<BlockImage id="pattern_provider" p:push_direction="up" scale="8" />
<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_pattern_provider.snbt" />
</GameScene>
</Row>

Поставщики шаблонов связывают [автокрафт](../ae2-mechanics/autocrafting.md) с оборудованием. Они отправляют ингредиенты из
[шаблонов](patterns.md) в соседние инвентари и принимают предметы обратно в сеть. Канал часто можно сэкономить:
верните результат по трубам в ближайший поставщик, например в тот же, который выдал ингредиенты. Тогда отдельная
<ItemLink id="import_bus" /> на выходе из машины не понадобится.

Поставщик отправляет ингредиенты прямо из [хранилища создания](crafting_cpu_multiblock.md#crafting-storage) процессора.
В собственном инвентаре он их не держит, поэтому труба не сможет их извлечь. Сначала отправьте ингредиенты
в соседний инвентарь, например бочку, и подсоедините трубу к нему.

Поставщик выдаёт сразу всю партию ингредиентов. Частями он её отправлять не может. Этим можно воспользоваться в схемах.

Если поставщик подключён к МЭ-интерфейсу [подсети](../ae2-mechanics/subnetworks.md), у которого все ячейки запроса пусты,
ингредиенты идут прямо в [хранилище](../ae2-mechanics/import-export-storage.md) подсети. Они не занимают ячейки интерфейса,
а новая партия ждёт, пока в станке освободится место. В режиме блокировки поставщик проверяет наличие ингредиентов
в ячейках станка.

Например, в схеме ниже и переплавляемый предмет, и топливо идут прямо в нужные ячейки печи. Так можно подавать
ингредиенты с нескольких сторон одного станка или сразу в несколько станков.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/furnace_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) Поставщик шаблонов: направлен кварцевым ключом и содержит нужные шаблоны обработки.

        ![Шаблон переплавки железа](../assets/diagrams/furnace_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (2) Интерфейс: с настройками по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="1.3 2 1">
        (3) Шина хранения № 1: фильтр разрешает уголь.
        <ItemImage id="minecraft:coal" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 2 0" max="1 2.3 1">
        (4) Шина хранения № 2: фильтр с картой инверсии исключает уголь.
        <Row><ItemImage id="minecraft:coal" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Общая схема подачи ингредиентов в несколько станков:

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        Плоский интерфейс
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        Шины хранения
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        Станки, которым поставщик выдаёт ингредиенты
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

Несколько поставщиков с одинаковыми шаблонами работают параллельно. Каждый поставщик по очереди проверяет все
свои грани, чтобы задействовать подключённые станки одновременно.

<a name="variants" />

## Варианты

Поставщик бывает обычным, направленным и плоским, в виде [кабельного модуля](../ae2-mechanics/cable-subparts.md).
От варианта зависит, с каких сторон он выдаёт ингредиенты, принимает предметы и подключается к сети.

*   Обычный поставщик выдаёт ингредиенты, принимает предметы и подключается к сети со всех сторон.

*   Чтобы направить обычный поставщик, примените <ItemLink id="certus_quartz_wrench" />. Он будет выдавать ингредиенты
    только с выбранной стороны, а принимать предметы со всех. На выбранной стороне нет сетевого соединения, поэтому
    поставщик можно подвести к оборудованию отдельной МЭ-подсети.

*   Плоские поставщики — [кабельные модули](../ae2-mechanics/cable-subparts.md). Несколько таких модулей можно разместить
    на одном кабеле. Их лицевая сторона выдаёт ингредиенты и принимает предметы, но не соединяет сети.

Обычный и плоский варианты можно преобразовать друг в друга в сетке верстака.

<a name="settings" />

## Настройки

*   **Режим блокировки** задерживает подачу следующей партии, пока в станке остаются ингредиенты.
*   **Блокировка создания** может приостановить поставщика по условию красного камня или до возврата результата
    предыдущего рецепта в этот поставщик.
*   Поставщик можно показать или скрыть в <ItemLink id="pattern_access_terminal" />.

<a name="priority" />

## Приоритет

Нажмите на ключ в правом верхнем углу окна поставщика. Если для предмета доступно несколько [шаблонов](patterns.md),
сеть сначала попробует поставщика с более высоким приоритетом. Если для его шаблона не хватает ингредиентов,
сеть использует доступный вариант с меньшим приоритетом.

<a name="a-common-misconception" />

## Частая ошибка

Иногда между поставщиком и станком ставят <ItemLink id="export_bus" />, думая, что поставщик сам не выдаёт ингредиенты.
Такая схема не заработает. Как объясняется в разделе [«Кабели»](cables.md), кабель служит для соединения сети
и не имеет инвентаря для приёма предметов.

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_1.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        Это не плавильная печь
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

Рядом с поставщиком нет инвентаря, которому он мог бы отправить ингредиенты. В этой схеме он работает только
как соединение между <ItemLink id="export_bus" /> и сетью.

Поставщик не передаёт <ItemLink id="export_bus" /> указания о том, что экспортировать. Шина выводит предметы,
заданные в её собственном фильтре.

На деле эта схема равнозначна следующей:

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_2.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        Это не плавильная печь
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

Чтобы отправить ингредиенты из шаблона в станок, поставьте поставщик вплотную к нему:

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_3.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        Это не плавильная печь
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

<a name="recipes" />

## Рецепты

<RecipeFor id="pattern_provider" />

<RecipeFor id="cable_pattern_provider" />

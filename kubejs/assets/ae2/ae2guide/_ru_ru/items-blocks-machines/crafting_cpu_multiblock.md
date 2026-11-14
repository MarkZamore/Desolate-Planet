---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Процессор создания"
  icon: 1k_crafting_storage
  position: 210
categories:
- devices
item_ids:
- ae2:1k_crafting_storage
- ae2:4k_crafting_storage
- ae2:16k_crafting_storage
- ae2:64k_crafting_storage
- ae2:256k_crafting_storage
- ae2:crafting_accelerator
- ae2:crafting_monitor
- ae2:crafting_unit
---

<a name="the-crafting-cpu" />

# Процессор создания

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<Row>
  <BlockImage id="1k_crafting_storage" scale="4" />

  <BlockImage id="crafting_accelerator" scale="4" />

  <BlockImage id="crafting_monitor" scale="4" />

  <BlockImage id="crafting_unit" scale="4" />
</Row>

Процессор выполняет запросы на создание предметов. Он хранит промежуточные ингредиенты при выполнении
многоэтапных заданий. От процессора зависит, какие по объёму задания можно запустить и как быстро они выполнятся.
Подробнее в разделе [«Автокрафт»](../ae2-mechanics/autocrafting.md).

Один процессор выполняет одно задание за раз. Чтобы одновременно заказать вычислительный процессор и 256 блоков
гладкого камня, понадобятся два отдельных процессора создания.

Процессор можно настроить на запросы игроков, устройств автоматизации или обоих источников.

Нажмите ПКМ по процессору, чтобы открыть окно выполнения текущего задания.

<a name="settings" />

## Настройки

*   Можно принимать только запросы игроков, только запросы автоматизации, например от <ItemLink id="export_bus" />
    с <ItemLink id="crafting_card" />, или оба вида запросов.

<a name="construction" />

## Сборка

Процессор собирается из блоков в сплошной прямоугольный параллелепипед без пустот.

Нужно хотя бы одно хранилище создания. Простейший рабочий процессор может состоять из одного хранилища на 1К.

<a name="crafting-unit" />

# Блок создания

<BlockImage id="crafting_unit" scale="4" />

Необязательный блок. Заполняет пустоты в процессоре, если других компонентов не хватает для прямоугольной формы.
Также входит в рецепты остальных компонентов.

<RecipeFor id="crafting_unit" />

<a name="crafting-storage" />

# Хранилище создания

<Row>
  <BlockImage id="1k_crafting_storage" scale="4" />

  <BlockImage id="4k_crafting_storage" scale="4" />

  <BlockImage id="16k_crafting_storage" scale="4" />

  <BlockImage id="64k_crafting_storage" scale="4" />

  <BlockImage id="256k_crafting_storage" scale="4" />
</Row>

Обязательный блок. Хранилища на 1К, 4К, 16К, 64К и 256К содержат исходные и промежуточные ингредиенты задания.
Для заданий с большим числом ингредиентов поставьте больше блоков хранилища или возьмите блоки большей ёмкости.

<Column>
  <Row>
    <RecipeFor id="1k_crafting_storage" />

    <RecipeFor id="4k_crafting_storage" />

    <RecipeFor id="16k_crafting_storage" />
  </Row>

  <Row>
    <RecipeFor id="64k_crafting_storage" />

    <RecipeFor id="256k_crafting_storage" />
  </Row>
</Column>

<a name="crafting-co-processing-unit" />

# Блок совместной обработки изготовления

<BlockImage id="crafting_accelerator" scale="4" />

Необязательный блок. С ним <ItemLink id="pattern_provider" /> чаще выдаёт партии ингредиентов.
Например, если вокруг одного поставщика установлено несколько <ItemLink id="molecular_assembler" />, сеть сможет
выдавать партии быстрее, чем их обрабатывает один сборщик. Тогда поставщик распределит партии между сборщиками.

<RecipeFor id="crafting_accelerator" />

<a name="crafting-monitor" />

# Монитор создания

<BlockImage id="crafting_monitor" scale="4" />

Необязательный блок. Показывает текущее задание процессора. Для окраски экрана используйте <ItemLink id="color_applicator" />.

<RecipeFor id="crafting_monitor" />

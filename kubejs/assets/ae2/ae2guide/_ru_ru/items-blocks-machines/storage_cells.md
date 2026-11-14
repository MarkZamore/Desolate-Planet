---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Ячейки хранения
  icon: item_storage_cell_1k
  position: 410
categories:
- tools
item_ids:
- ae2:item_cell_housing
- ae2:fluid_cell_housing
- ae2:cell_component_1k
- ae2:cell_component_4k
- ae2:cell_component_16k
- ae2:cell_component_64k
- ae2:cell_component_256k
- ae2:item_storage_cell_1k
- ae2:item_storage_cell_4k
- ae2:item_storage_cell_16k
- ae2:item_storage_cell_64k
- ae2:item_storage_cell_256k
- ae2:fluid_storage_cell_1k
- ae2:fluid_storage_cell_4k
- ae2:fluid_storage_cell_16k
- ae2:fluid_storage_cell_64k
- ae2:fluid_storage_cell_256k
---

<a name="storage-cells" />

# Ячейки хранения

<Column>
  <Row>
    <ItemImage id="item_storage_cell_1k" scale="4" />

    <ItemImage id="item_storage_cell_4k" scale="4" />

    <ItemImage id="item_storage_cell_16k" scale="4" />

    <ItemImage id="item_storage_cell_64k" scale="4" />

    <ItemImage id="item_storage_cell_256k" scale="4" />
  </Row>

  <Row>
    <ItemImage id="fluid_storage_cell_1k" scale="4" />
    <ItemImage id="fluid_storage_cell_4k" scale="4" />
    <ItemImage id="fluid_storage_cell_16k" scale="4" />
    <ItemImage id="fluid_storage_cell_64k" scale="4" />
    <ItemImage id="fluid_storage_cell_256k" scale="4" />
  </Row>
</Column>

Ячейки — один из основных способов хранения в Applied Energistics. Они вставляются в <ItemLink id="drive" />
или <ItemLink id="chest" />.

Как рассчитывается вместимость в байтах и типах, объясняется в разделе [«Байты и типы»](../ae2-mechanics/bytes-and-types.md).

Чтобы извлечь компонент из корпуса пустой ячейки, возьмите её в руку и нажмите Shift + ПКМ.

<a name="storage-capacity-with-varying-type-count" />

## Как число типов влияет на вместимость

Часть байтов тратится на [хранение сведений о типах](../ae2-mechanics/bytes-and-types.md). При одном типе
в ячейку помещается почти вдвое больше предметов, чем при заполнении всех 63 типов.

| Ячейка | Предметов при одном типе | Предметов при 63 типах |
| ---- | ----: | ----: |
| <ItemLink id="item_storage_cell_1k" /> | 8 128 | 4 160 |
| <ItemLink id="item_storage_cell_4k" /> | 32 512 | 16 640 |
| <ItemLink id="item_storage_cell_16k" /> | 130 048 | 66 560 |
| <ItemLink id="item_storage_cell_64k" /> | 520 192 | 266 240 |
| <ItemLink id="item_storage_cell_256k" /> | 2 080 768 | 1 064 960 |

<a name="partitioning" />

## Фильтрация

Ячейку можно настроить на приём определённых предметов, как <ItemLink id="storage_bus" />. Настройку выполняют
в <ItemLink id="cell_workbench" />.

Предметы можно перетащить в ячейки фильтра из JEI или REI, даже если их нет в инвентаре.

<a name="upgrades" />

## Улучшения

Вставляйте [карты улучшения](upgrade_cards.md) в <ItemLink id="cell_workbench" />:

*   <ItemLink id="fuzzy_card" /> позволяет фильтровать по степени износа или игнорировать NBT предмета. Для жидкостей карта недоступна.
*   <ItemLink id="inverter_card" /> меняет список разрешённых предметов на список запрещённых.
*   <ItemLink id="equal_distribution_card" /> отводит одинаковое число байтов каждому типу. Один тип не заполнит всю ячейку.
*   <ItemLink id="void_card" /> уничтожает новые предметы, если ячейка заполнена. При равномерном распределении
    это касается выделенного места конкретного типа. Такая карта помогает фермам не забиваться. Сначала настройте фильтр.
*   В переносную ячейку можно поставить <ItemLink id="energy_card" />, чтобы увеличить заряд встроенной батареи.

<a name="coloring" />

## Окрашивание

Переносные ячейки для предметов и жидкостей можно окрасить, объединив их с красителем в сетке крафта, как кожаную броню.

<a name="housings" />

# Корпуса

Ячейку собирают из компонента хранения и готового корпуса либо по рецепту, в котором материалы корпуса сразу выкладываются
вокруг компонента:

<Row>
  <Recipe id="network/cells/item_storage_cell_1k" />

  <Recipe id="network/cells/item_storage_cell_1k_storage" />
</Row>

Рецепты отдельных корпусов:

<Row>
  <RecipeFor id="item_cell_housing" />

  <RecipeFor id="fluid_cell_housing" />
</Row>

<a name="storage-components" />

# Компоненты хранения

Компонент определяет вместимость ячейки. Каждый следующий уровень вмещает в четыре раза больше и требует три компонента
предыдущего уровня.

<Column>
  <Row>
    <RecipeFor id="cell_component_1k" />

    <RecipeFor id="cell_component_4k" />

    <RecipeFor id="cell_component_16k" />
  </Row>

  <Row>
    <RecipeFor id="cell_component_64k" />

    <RecipeFor id="cell_component_256k" />
  </Row>
</Column>

<a name="item-storage-cells" />

# Ячейки хранения предметов

Такая ячейка хранит до 63 типов предметов. Доступны все стандартные уровни вместимости.

<Column>
  <Row>
    <Recipe id="network/cells/item_storage_cell_1k_storage" />

    <Recipe id="network/cells/item_storage_cell_4k_storage" />

    <Recipe id="network/cells/item_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/item_storage_cell_64k_storage" />

    <Recipe id="network/cells/item_storage_cell_256k_storage" />
  </Row>
</Column>

<a name="portable-item-storage" />

## Переносные ячейки для предметов

Переносная ячейка работает как карманный <ItemLink id="chest" />. Её можно зарядить в <ItemLink id="charger" />.

У переносных ячеек вдвое меньше байтов, чем у обычных ячеек того же уровня. При переходе на следующий уровень
число доступных типов предметов уменьшается.

Кроме стандартных карт улучшения, они поддерживают <ItemLink id="energy_card" /> для увеличения ёмкости батареи.

<Column>
  <Row>
    <RecipeFor id="portable_item_cell_1k" />

    <RecipeFor id="portable_item_cell_4k" />

    <RecipeFor id="portable_item_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_item_cell_64k" />

    <RecipeFor id="portable_item_cell_256k" />
  </Row>
</Column>

<a name="fluid-storage-cells" />

# Ячейки хранения жидкостей

Такая ячейка хранит до пяти типов жидкостей. Доступны все стандартные уровни вместимости.

<Column>
  <Row>
    <Recipe id="network/cells/fluid_storage_cell_1k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_4k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/fluid_storage_cell_64k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_256k_storage" />
  </Row>
</Column>

<a name="portable-fluid-storage" />

## Переносные ячейки для жидкостей

Переносная ячейка работает как карманный <ItemLink id="chest" />. Её можно зарядить в <ItemLink id="charger" />.

У переносных ячеек вдвое меньше байтов, чем у обычных ячеек того же уровня. При переходе на следующий уровень
число доступных типов жидкостей уменьшается.

Кроме стандартных карт улучшения, они поддерживают <ItemLink id="energy_card" /> для увеличения ёмкости батареи.

<Column>
  <Row>
    <RecipeFor id="portable_fluid_cell_1k" />

    <RecipeFor id="portable_fluid_cell_4k" />

    <RecipeFor id="portable_fluid_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_fluid_cell_64k" />

    <RecipeFor id="portable_fluid_cell_256k" />
  </Row>
</Column>

<a name="creative-item-and-fluid-cells" />

# Творческие ячейки для предметов и жидкостей

<Row>
  <ItemImage id="creative_item_cell" scale="2" />

  <ItemImage id="creative_fluid_cell" scale="2" />
</Row>

Творческая ячейка работает как бесконечный источник и поглотитель выбранного предмета или жидкости.
Тип содержимого задаётся [фильтром](cell_workbench.md).

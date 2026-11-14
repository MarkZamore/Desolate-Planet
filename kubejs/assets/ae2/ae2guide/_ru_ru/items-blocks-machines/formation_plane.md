---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Плоскость формирования"
  icon: formation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:formation_plane
---

<a name="the-formation-plane" />

# Плоскость формирования

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/formation_plane.snbt" />
</GameScene>

Плоскость формирования ставит блоки и выбрасывает предметы. Она работает как <ItemLink id="storage_bus" /> с доступом только на ввод: когда [устройства](../ae2-mechanics/devices.md), например <ItemLink id="import_bus" /> и <ItemLink id="interface" />, помещают предметы в [сетевое хранилище](../ae2-mechanics/import-export-storage.md), плоскость может вывести их прямо в мир.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/formation_plane_demonstration.snbt" />
  <IsometricCamera yaw="255" pitch="30" />
</GameScene>

Это [устройство](../ae2-mechanics/devices.md) использует тот же принцип, что шина хранения в [транспортной подсети](../example-setups/pipe-subnet.md). Вместо вывода в соседний инвентарь плоскость размещает блоки или выбрасывает предметы в мир.

Плоскость устанавливается на [грань кабеля](../ae2-mechanics/cable-subparts.md).

**Разрешите действия псевдоигроков в настройках привата чанка.**

<a name="filtering" />

## Фильтрация

Без фильтра плоскость пытается разместить или выбросить всё, что получает. Укажите в слотах фильтра ресурсы, которые ей разрешено выводить.

Перетащить предметы или жидкости в слоты фильтра можно из JEI или REI, даже если их нет у вас в инвентаре.

Чтобы выбрать жидкость вместо её ёмкости, нажмите ПКМ по ведру или баку в слоте фильтра.

<a name="priority" />

## Приоритет

Приоритет задаётся кнопкой с гаечным ключом в правом верхнем углу окна. Сеть сначала направляет входящие предметы в хранилище с наивысшим приоритетом.

<a name="settings" />

## Настройки

*   В настройках выберите, будет плоскость размещать блоки или выбрасывать предметы.

<a name="upgrades" />

## Улучшения

Плоскость формирования поддерживает следующие [карты улучшений](upgrade_cards.md):

*   <ItemLink id="capacity_card" /> добавляет слоты фильтра.
*   <ItemLink id="fuzzy_card" /> позволяет фильтровать по степени износа и игнорировать данные NBT.
*   <ItemLink id="inverter_card" /> меняет режим фильтра с разрешающего на запрещающий.

<a name="recipe" />

## Рецепт

<RecipeFor id="formation_plane" />

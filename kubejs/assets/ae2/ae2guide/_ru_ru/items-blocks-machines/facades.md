---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Кабельные фасады"
  icon: facade
  icon_nbt: '{item: "minecraft:stone"}'
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:facade
---

<a name="facades" />

# Кабельные фасады

Кабельные фасады скрывают проводку. Они подходят для обычных и плотных кабелей и воспроизводят внешний вид разных блоков.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/facades_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Фасады можно поставить со всех сторон кабеля. Установленные на кабель [компоненты](../ae2-mechanics/cable-subparts.md) и соединения останутся видимыми.

<GameScene zoom="6"  interactive={true}>
  <ImportStructure src="../assets/assemblies/facades_2.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

С их помощью можно спрятать проводку или сделать стороны одного блока похожими на разные материалы.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/facades_3.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<a name="hiding-facades" />

## Скрытие фасадов

Фасады скрываются, пока вы держите в любой руке <a href="network_tool.md">сетевой инструмент</a>.

Пока фасад скрыт, можно взаимодействовать с блоком за ним, не снимая фасад.

<a name="recipe" />

## Рецепт

Поместите нужный блок в центр сетки создания и окружите его четырьмя <ItemLink id="cable_anchor" />.

![Рецепт фасада](../assets/diagrams/facade_recipe.png)

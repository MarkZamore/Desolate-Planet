---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Ускоритель роста"
  icon: growth_accelerator
  position: 310
categories:
- machines
item_ids:
- ae2:growth_accelerator
---

<a name="the-growth-accelerator" />

# Ускоритель роста

<BlockImage id="growth_accelerator" p:powered="true" scale="8"/>

Ускоритель заметно ускоряет [рост кристаллов](../ae2-mechanics/certus-growth.md) истинного кварца или аметиста, если установить его рядом с растущим блоком.

Он *также* ускоряет рост некоторых растений.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/growth_accelerator.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Для ручного привода установите <ItemLink id="crank" /> сверху или снизу и нажимайте по ней ПКМ.

Кабель можно подключить только к граням с розовыми флюисовыми контактами.

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/accelerator_connections.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

<a name="recipe" />

## Рецепт

<RecipeFor id="growth_accelerator" />

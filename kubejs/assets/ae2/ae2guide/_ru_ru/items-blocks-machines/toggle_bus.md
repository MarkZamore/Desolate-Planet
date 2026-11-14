---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "МЭ шина переключения"
  icon: toggle_bus
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:toggle_bus
- ae2:inverted_toggle_bus
---

# МЭ шина переключения

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/assemblies/toggle_bus.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

Шина работает примерно как <ItemLink id="fluix_glass_cable" /> или другой кабель. Сигнал редстоуна позволяет управлять соединением и отключать часть [МЭ-сети](../ae2-mechanics/me-network-connections.md).

Обычная шина при подаче сигнала соединяет участки сети. <ItemLink id="inverted_toggle_bus" /> при подаче сигнала разъединяет их.

Когда шина переключается, сеть может перезапуститься и пересчитать подключённые устройства.

Шины переключения относятся к [кабельным компонентам](../ae2-mechanics/cable-subparts.md).

## Рецепты

<RecipeFor id="toggle_bus" />

<RecipeFor id="inverted_toggle_bus" />

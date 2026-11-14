---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Резонирующая камера"
  icon: vibration_chamber
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:vibration_chamber
---

# Резонирующая камера

<BlockImage id="vibration_chamber" p:active="true" scale="8" />

Обычно сеть получает [энергию](../ae2-mechanics/energy.md) через <ItemLink id="energy_acceptor" />. Резонирующая камера сама вырабатывает небольшое или среднее количество AE.

При стандартных настройках и без [улучшений](upgrade_cards.md) камера производит 40 AE за такт.

Если запас [энергии](../ae2-mechanics/energy.md) сети полон, камера снижает скорость сжигания топлива, но не останавливается полностью.

## Настройки

*   В интерфейсе камеры можно выбрать общую единицу измерения энергии: AE или E/FE.

## Улучшения

Камера поддерживает следующие [улучшения](upgrade_cards.md):

*   <ItemLink id="energy_card" /> повышает КПД на 50%. С тремя картами КПД составляет 250% от базового.
*   <ItemLink id="speed_card" /> ускоряет сжигание топлива на 50%. С тремя картами мощность составляет 250% от базовой.

## Конфигурация

Параметры камеры можно изменить в файле `config/ae2/common.json` в каталоге `.minecraft`.

*   `baseEnergyPerFuelTick` задаёт базовый КПД без улучшений.
*   `minEnergyPerGameTick` задаёт минимальную выработку. Камера понемногу расходует топливо, даже когда сети энергия не нужна.
*   `maxEnergyPerGameTick` задаёт максимальную выработку и скорость работы без улучшений.

## Рецепт

<RecipeFor id="vibration_chamber" />

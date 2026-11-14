---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Зарядник"
  icon: charger
  position: 310
categories:
- machines
item_ids:
- ae2:charger
---

<a name="the-charger" />

# Зарядник

<BlockImage id="charger" scale="8" />

Зарядник заряжает совместимые инструменты и <ItemLink id="certus_quartz_crystal" />.

Энергия подаётся через верхнюю или нижнюю грань. Подойдут [кабели AE2](cables.md) с энергией AE и кабели других модов с энергией Forge (FE). Предметы можно подавать и извлекать с любой стороны. Извлекается только результат, поэтому фильтр, отделяющий незаряженные кристаллы от заряженных, не нужен. Для удобства автоматизации зарядник можно повернуть с помощью <ItemLink id="certus_quartz_wrench" />.

Зарядник превращает <ItemLink id="certus_quartz_crystal" /> в <ItemLink id="charged_certus_quartz_crystal" />, а <ItemLink id="minecraft:compass" /> в <ItemLink id="meteorite_compass" />.

Для ручной зарядки установите <ItemLink id="crank" /> сверху или снизу и нажимайте по ней ПКМ, пока предмет не зарядится.

Зарядник также служит рабочим блоком для деревенского жителя AE2.

<a name="simple-automation" />

## Простая автоматизация

Возможность поворачивать зарядник позволяет собирать такие полуавтоматические установки:

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/charger_hopper.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<a name="recipe" />

## Рецепт

<RecipeFor id="charger" />

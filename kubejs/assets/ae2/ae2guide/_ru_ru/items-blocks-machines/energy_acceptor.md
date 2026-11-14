---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Приёмщик энергии"
  icon: energy_acceptor
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_acceptor
---

<a name="the-energy-acceptor" />

# Приёмщик энергии

<Row gap="20">
<BlockImage id="energy_acceptor" scale="8" />

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_energy_acceptor.snbt" />
</GameScene>
</Row>

Приёмщик преобразует энергию других технических модов во внутренние [единицы энергии](../ae2-mechanics/energy.md) AE2. <ItemLink id="controller" /> тоже умеет принимать энергию, но его грани удобнее оставить для подключения каналов.

Коэффициенты преобразования энергии Forge и Fabric:

*   2 FE = 1 AE (Forge)
*   1 E = 2 AE (Fabric)

Скорость преобразования зависит от ёмкости энергетического буфера сети. Причина описана в [разделе об энергии](../ae2-mechanics/energy.md).

<a name="variants" />

## Варианты

Приёмщик бывает обычным, в форме полного блока, и плоским, для установки на [грань кабеля](../ae2-mechanics/cable-subparts.md). Плоский вариант удобен для компактных схем.

Преобразовать один вариант в другой можно в сетке создания.

<a name="recipe" />

## Рецепт

<RecipeFor id="energy_acceptor" />

<RecipeFor id="cable_energy_acceptor" />

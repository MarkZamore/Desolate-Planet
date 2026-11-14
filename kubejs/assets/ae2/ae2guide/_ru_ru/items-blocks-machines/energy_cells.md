---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Энергохранилища"
  icon: energy_cell
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_cell
- ae2:dense_energy_cell
- ae2:creative_energy_cell
---

<a name="energy-cells" />

# Энергохранилища

<Row gap="20">
  <BlockImage id="energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="dense_energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="creative_energy_cell" scale="8" />
</Row>

Энергохранилища увеличивают запас [энергии](../ae2-mechanics/energy.md) сети. Небольшой буфер помогает справляться с пиками расхода при массовом вводе и выводе предметов. Большой запас позволяет продолжать работу при остановке генерации, например ночью при питании от солнечных панелей, или выдержать высокий мгновенный расход [пространственного хранилища](../ae2-mechanics/spatial-io.md).

<a name="fill-bars" />

## Индикаторы заряда

<Row>
<BlockImage id="energy_cell" scale="4" p:fullness="0" />
<BlockImage id="energy_cell" scale="4" p:fullness="1" />
<BlockImage id="energy_cell" scale="4" p:fullness="2" />
<BlockImage id="energy_cell" scale="4" p:fullness="3" />
<BlockImage id="energy_cell" scale="4" p:fullness="4" />
</Row>

Полосы на боку блока показывают уровень заряда:

*   0 полос при заряде ниже 25%.
*   1 полоса при заряде от 25% до 50%.
*   2 полосы при заряде от 50% до 75%.
*   3 полосы при заряде от 75% до 99%.
*   4 полосы при заряде выше 99%.

<a name="types-of-cell" />

## Виды энергохранилищ

*   <ItemLink id="energy_cell" /> хранит до 200 000 AE. Обычно одного блока хватает,
    чтобы сгладить пики расхода в повседневной работе сети.
*   <ItemLink id="dense_energy_cell" /> хранит до 1 600 000 AE. Он нужен, чтобы запитать сеть от накопленной энергии
    или справиться с мгновенным расходом крупного [пространственного хранилища](../ae2-mechanics/spatial-io.md).
*   <ItemLink id="creative_energy_cell" /> даёт неограниченную энергию. Предназначен для тестирования в творческом режиме.

<a name="recipes" />

## Рецепты

<Row>
  <RecipeFor id="energy_cell" />

  <RecipeFor id="dense_energy_cell" />
</Row>

---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Растущий истинный кварц"
  icon: flawless_budding_quartz
  position: 010
categories:
- misc ingredients blocks
item_ids:
- ae2:flawless_budding_quartz
- ae2:flawed_budding_quartz
- ae2:chipped_budding_quartz
- ae2:damaged_budding_quartz
- ae2:small_quartz_bud
- ae2:medium_quartz_bud
- ae2:large_quartz_bud
- ae2:quartz_cluster
---

<a name="budding-certus-quartz" />

# Растущий истинный кварц

(См. также [выращивание истинного кварца](../ae2-mechanics/certus-growth.md).)

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_blocks.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Почки истинного кварца вырастают на растущих блоках истинного кварца, как почки аметиста. Эти блоки можно найти в [метеоритах](../ae2-mechanics/meteorites.md). У них четыре ступени качества: безупречный, дефектный, со сколами и повреждённый. Узнать ступень помогут Jade, HWYLA, The One Probe или экран F3.

Если почка переходит на следующую стадию роста, блок под ней может потерять ступень качества. Это относится к дефектным, сколотым и повреждённым блокам, которые со временем могут стать обычным <ItemLink id="quartz_block" />.

Безупречные блоки при росте почек не изнашиваются, поэтому служат возобновляемым источником истинного кварца.

При добыче обычной киркой блок теряет одну ступень качества. «Шёлковое касание» предотвращает это для всех ступеней, кроме безупречной. **Перенести безупречный блок киркой не получится.** Чтобы перенести его целиком, воспользуйтесь [пространственным хранилищем](../ae2-mechanics/spatial-io.md).

<a name="recipes" />

## Рецепты

Чтобы получить растущий блок нужного качества, бросьте в воду блок на ступень ниже или обычный <ItemLink id="quartz_block" /> вместе с одним или несколькими <ItemLink id="charged_certus_quartz_crystal" />.

Безупречный блок можно найти только в мире. Изготовить его нельзя.

<Row>
  <RecipeFor id="damaged_budding_quartz" />

  <RecipeFor id="chipped_budding_quartz" />

  <RecipeFor id="flawed_budding_quartz" />
</Row>

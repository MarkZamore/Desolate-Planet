---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: Выращивание истинного кварца
  icon: quartz_cluster
---

# Выращивание истинного кварца

## Повторяем материал из раздела «Первые шаги»

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/budding_certus_1.snbt" />
</GameScene>

Почки истинного кварца растут на [цветущих блоках истинного кварца](../items-blocks-machines/budding_certus.md), как аметисты. Из маленькой, средней или большой почки выпадает только кварцевая пыль (<ItemLink id="certus_quartz_dust" />) в количестве одной единицы. Зачарование «Удача» на это не влияет. Из взрослой друзы выпадают четыре кристалла (<ItemLink id="certus_quartz_crystal" />), и «Удача» увеличивает их число.

У цветущих блоков четыре уровня: безупречный, дефектный, надколотый и повреждённый.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_blocks.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Каждый раз, когда почка переходит на следующую стадию роста, цветущий блок может потерять один уровень. Со временем он превратится в обычный блок истинного кварца. Чтобы восстановить цветущий блок или получить новый, бросьте в воду цветущий или обычный блок истинного кварца вместе с одним или несколькими <ItemLink id="charged_certus_quartz_crystal" />.

<RecipeFor id="damaged_budding_quartz" />

Безупречные цветущие блоки не изнашиваются и дают кварц бесконечно. Их невозможно изготовить или добыть киркой, даже с «Шёлковым касанием». Переместить их можно с помощью [пространственного хранилища](../ae2-mechanics/spatial-io.md).

Сами по себе почки истинного кварца растут очень медленно. <ItemLink id="growth_accelerator" />, установленный вплотную к цветущему блоку, значительно ускоряет их рост. Сделайте несколько ускорителей в первую очередь.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_certus_2.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Если кварца не хватает на <ItemLink id="energy_acceptor" /> или <ItemLink id="vibration_chamber" />, изготовьте <ItemLink id="crank" /> и установите его на торец ускорителя.

О том, как автоматически собирать истинный кварц, рассказано [в этом разделе](../example-setups/simple-certus-farm.md).

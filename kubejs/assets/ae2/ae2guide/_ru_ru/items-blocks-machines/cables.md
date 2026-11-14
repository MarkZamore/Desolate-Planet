---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Кабели"
  icon: fluix_glass_cable
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:white_glass_cable
- ae2:orange_glass_cable
- ae2:magenta_glass_cable
- ae2:light_blue_glass_cable
- ae2:yellow_glass_cable
- ae2:lime_glass_cable
- ae2:pink_glass_cable
- ae2:gray_glass_cable
- ae2:light_gray_glass_cable
- ae2:cyan_glass_cable
- ae2:purple_glass_cable
- ae2:blue_glass_cable
- ae2:brown_glass_cable
- ae2:green_glass_cable
- ae2:red_glass_cable
- ae2:black_glass_cable
- ae2:fluix_glass_cable
- ae2:white_covered_cable
- ae2:orange_covered_cable
- ae2:magenta_covered_cable
- ae2:light_blue_covered_cable
- ae2:yellow_covered_cable
- ae2:lime_covered_cable
- ae2:pink_covered_cable
- ae2:gray_covered_cable
- ae2:light_gray_covered_cable
- ae2:cyan_covered_cable
- ae2:purple_covered_cable
- ae2:blue_covered_cable
- ae2:brown_covered_cable
- ae2:green_covered_cable
- ae2:red_covered_cable
- ae2:black_covered_cable
- ae2:fluix_covered_cable
- ae2:white_covered_dense_cable
- ae2:orange_covered_dense_cable
- ae2:magenta_covered_dense_cable
- ae2:light_blue_covered_dense_cable
- ae2:yellow_covered_dense_cable
- ae2:lime_covered_dense_cable
- ae2:pink_covered_dense_cable
- ae2:gray_covered_dense_cable
- ae2:light_gray_covered_dense_cable
- ae2:cyan_covered_dense_cable
- ae2:purple_covered_dense_cable
- ae2:blue_covered_dense_cable
- ae2:brown_covered_dense_cable
- ae2:green_covered_dense_cable
- ae2:red_covered_dense_cable
- ae2:black_covered_dense_cable
- ae2:fluix_covered_dense_cable
- ae2:white_smart_cable
- ae2:orange_smart_cable
- ae2:magenta_smart_cable
- ae2:light_blue_smart_cable
- ae2:yellow_smart_cable
- ae2:lime_smart_cable
- ae2:pink_smart_cable
- ae2:gray_smart_cable
- ae2:light_gray_smart_cable
- ae2:cyan_smart_cable
- ae2:purple_smart_cable
- ae2:blue_smart_cable
- ae2:brown_smart_cable
- ae2:green_smart_cable
- ae2:red_smart_cable
- ae2:black_smart_cable
- ae2:fluix_smart_cable
- ae2:white_smart_dense_cable
- ae2:orange_smart_dense_cable
- ae2:magenta_smart_dense_cable
- ae2:light_blue_smart_dense_cable
- ae2:yellow_smart_dense_cable
- ae2:lime_smart_dense_cable
- ae2:pink_smart_dense_cable
- ae2:gray_smart_dense_cable
- ae2:light_gray_smart_dense_cable
- ae2:cyan_smart_dense_cable
- ae2:purple_smart_dense_cable
- ae2:blue_smart_dense_cable
- ae2:brown_smart_dense_cable
- ae2:green_smart_dense_cable
- ae2:red_smart_dense_cable
- ae2:black_smart_dense_cable
- ae2:fluix_smart_dense_cable
---

<a name="cables" />

# Кабели

<GameScene zoom="3" background="transparent">
  <ImportStructure src="../assets/assemblies/cables.snbt" />
  <IsometricCamera yaw="180" pitch="30" />
</GameScene>

МЭ-устройства соединяются и напрямую, но растянуть сеть на большие расстояния проще всего кабелями.

Соседние кабели разных цветов не соединяются. Это помогает распределять [каналы](../ae2-mechanics/channels.md).
Цвет кабеля также задаёт цвет подключённых терминалов. Изменчивый кабель без красителя соединяется
с кабелем любого цвета.

**Цвет кабеля не влияет на число каналов.**

<a name="an-important-note" />

## Важно для начинающих

**Если вы только знакомитесь с каналами, по возможности используйте умные кабели, обычные и плотные.
По их индикаторам видны маршруты каналов в сети.**

<a name="another-note" />

## Как работают кабели

Кабели соединяют [устройства AE2](../ae2-mechanics/devices.md) в сеть. У кабеля нет инвентаря для приёма предметов,
поэтому поставщик шаблонов и станок не могут отправлять в него содержимое, как в трубу.

<a name="glass-cable" />

## Стеклянный кабель

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/fluix_glass_cable.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="fluix_glass_cable" /> проще всего изготовить. Он передаёт питание и до восьми [каналов](../ae2-mechanics/channels.md).
У него 17 вариантов: исходный изменчивый цвет и 16 цветов красителей.

В сетке верстака окружите краситель восемью кабелями одного типа. Исходные цвета можно смешивать, но типы — стеклянные,
умные и другие — должны совпадать. Уже установленные кабели можно красить любой кистью, совместимой с Forge.

Чтобы смыть цвет, положите окрашенный кабель и ведро воды в сетку крафта.

Из шерсти и стеклянного кабеля можно сделать <ItemLink id="fluix_covered_cable" />.
Для наблюдения за [каналами](../ae2-mechanics/channels.md) пригодится <ItemLink id="fluix_smart_cable" />.

<RecipeFor id="fluix_glass_cable" />

<RecipeFor id="blue_glass_cable" />

<a name="covered-cable" />

## Покрытый кабель

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

По функциям покрытый кабель совпадает с <ItemLink id="fluix_glass_cable" />. Покрытие меняет внешний вид.

Красится так же, как <ItemLink id="fluix_glass_cable" />. Из четырёх <ItemLink id="fluix_covered_cable" />,
красного камня и светокамня получится <ItemLink id="fluix_covered_dense_cable" />.

<Recipe id="network/cables/covered_fluix" />

<RecipeFor id="blue_covered_cable" />

<a name="dense-cable" />

## Плотный кабель

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Плотный кабель передаёт 32 канала вместо восьми. Шины и панели к нему напрямую не крепятся.
Для них сделайте ответвление через <ItemLink id="fluix_glass_cable" /> или <ItemLink id="fluix_smart_cable" />.

Плотный кабель влияет на маршрутизацию. Каналы идут кратчайшим путём до плотного кабеля, а затем
кратчайшим путём по нему до контроллера.

<Recipe id="network/cables/dense_covered_fluix" />

<RecipeFor id="blue_covered_dense_cable" />

<a name="smart-cable" />

## Умный кабель

<Row>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
</Row>

Внешне похожи на <ItemLink id="fluix_covered_cable" />, но вдоль чёрной полосы горят индикаторы каналов.
На обычном умном кабеле первые четыре канала отображаются цветом кабеля, следующие четыре — белым.
На плотном умном кабеле каждая линия соответствует четырём каналам.

В сети с <ItemLink id="controller" /> индикаторы показывают точный маршрут каналов.

В сети без контроллера умный кабель показывает, сколько каналов используется во всей сети.

Красится так же, как <ItemLink id="fluix_glass_cable" />.

<Recipe id="network/cables/smart_fluix" />

<Recipe id="network/cables/dense_smart_fluix" />

<RecipeFor id="blue_smart_cable" />

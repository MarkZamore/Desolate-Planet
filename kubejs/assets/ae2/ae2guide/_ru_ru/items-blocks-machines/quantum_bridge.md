---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Квантовый мост"
  icon: quantum_ring
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:quantum_link
- ae2:quantum_ring
---

# Квантовый сетевой мост

![Собранный квантовый сетевой мост](../assets/diagrams/quantum_bridge_demonstration.png)

Квантовый сетевой мост позволяет протянуть [сеть](../ae2-mechanics/me-network-connections.md) на любое расстояние и даже между измерениями. Всего он пропускает 32 канала независимо от того, к каким граням подсоединены кабели. По сути, это беспроводной [плотный кабель](cables.md#dense-cable).

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_2.snbt" />

  <BoxAnnotation color="#33dd33" min="1 1 1" max="6 2 3">
        Воображаемый кабель между двумя концами моста
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

**Чанки на обеих сторонах должны быть загружены.** Если стороны находятся далеко друг от друга, используйте <ItemLink id="spatial_anchor" /> или другой загрузчик чанков.

# МЭ квантовое кольцо

<BlockImage id="quantum_ring" scale="8" />

Восемь блоков кольца вокруг <ItemLink id="quantum_link" /> образуют квантовый сетевой мост. Подключать кабель можно только к четырём блокам <ItemLink id="quantum_ring" />, которые прилегают к <ItemLink id="quantum_link" />. Четыре угловых блока кабели не принимают.

## Рецепт

<RecipeFor id="quantum_ring" />

# МЭ камера квантовой связи

<BlockImage id="quantum_link" scale="8" />

Камера в центре <ItemLink id="quantum_ring" /> образует квантовый сетевой мост. Сама камера не подключается к кабелям и появляется в сети только как часть собранного моста.

В её инвентаре помещается одна <ItemLink id="quantum_entangled_singularity" />. Предметы можно подавать и извлекать автоматически.

## Рецепт

<RecipeFor id="quantum_link" />

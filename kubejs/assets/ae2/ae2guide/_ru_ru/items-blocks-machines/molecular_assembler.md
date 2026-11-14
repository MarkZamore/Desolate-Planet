---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Молекулярный сборщик"
  icon: molecular_assembler
  position: 310
categories:
- machines
item_ids:
- ae2:molecular_assembler
---

# Молекулярный сборщик

<BlockImage id="molecular_assembler" scale="8" />

Молекулярный сборщик принимает ингредиенты и выполняет операцию, которую задаёт соседний <ItemLink id="pattern_provider" /> или вставленный шаблон: <ItemLink id="crafting_pattern" />, <ItemLink id="smithing_table_pattern" /> либо <ItemLink id="stonecutting_pattern" />. Затем сборщик отправляет результат в соседний инвентарь.

В сборщик на схеме вставлен шаблон, по которому из одного дубового бревна получаются четыре дубовые доски. Бревно поступает из верхней воронки, а готовые доски отправляются в нижнюю.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/standalone_assembler.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Основное применение

Обычно рядом со сборщиком ставят <ItemLink id="pattern_provider" />. В этом случае поставщик передаёт соседним сборщикам рецепт вместе с ингредиентами. Сборщики автоматически отправляют результат в соседние инвентари, в том числе в слоты возврата поставщика. Для автоматизации рецепта достаточно поставить сборщик рядом с поставщиком.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Улучшения

Молекулярный сборщик поддерживает следующие [улучшения](upgrade_cards.md):

*   <ItemLink id="speed_card" />

## Рецепт

<RecipeFor id="molecular_assembler" />

## Примечание

OptiFine нарушает передачу готовых предметов в соседние инвентари, поэтому с ним большинство схем со сборщиками не работает.

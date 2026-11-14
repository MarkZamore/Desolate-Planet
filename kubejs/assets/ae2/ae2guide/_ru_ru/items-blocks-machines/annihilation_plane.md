---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "Плоскость уничтожения"
  icon: annihilation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:annihilation_plane
---

<a name="the-annihilation-plane" />

# Плоскость уничтожения

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/annihilation_plane.snbt" />
</GameScene>

Плоскость уничтожения разбивает блоки и подбирает предметы. Подобно <ItemLink id="import_bus" />, она отправляет их в [сетевое хранилище](../ae2-mechanics/import-export-storage.md). Предмет должен коснуться лицевой стороны плоскости: она подбирает только то, что находится прямо перед ней.

На плоскость уничтожения можно наложить любые чары для кирки. Если сборка позволяет увеличить уровень «Удачи», зачаруйте плоскости и [автоматизируйте добычу из руды](../example-setups/ore-fortuner.md). «Шёлковое касание» работает как обычно, «Эффективность» уменьшает расход энергии на разрушение блока, а «Прочность» даёт шанс разрушить его без затрат энергии.

Плоскость устанавливается на [грань кабеля](../ae2-mechanics/cable-subparts.md).

**Разрешите действия псевдоигроков в настройках привата чанка.**

<a name="filtering" />

## Фильтрация

Плоскость уничтожения разбивает блок или подбирает предмет только тогда, когда её сеть может принять добычу. Поэтому для фильтрации *ограничьте содержимое сетевого хранилища*, например выделите устройству [подсеть](../ae2-mechanics/subnetworks.md). Настройте фильтр на <ItemLink id="storage_bus" /> или [ограничьте содержимое](cell_workbench.md) [ячейки](../items-blocks-machines/storage_cells.md).

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/annihilation_filtering.snbt" />

  <DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        Настройте фильтр на предметы, выпадающие из нужного блока.
  </DiamondAnnotation>

  <DiamondAnnotation pos=".5 0.5 2.5" color="#00ff00">
        Ограничьте содержимое ячейки предметами, выпадающими из нужного блока.
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Фильтр проверяет *выпадающие предметы*. Например, чтобы плоскость разбивала только зрелые аметистовые друзы <ItemLink id="minecraft:amethyst_cluster" />, потребуется «Шёлковое касание». Без этих чар из незрелых почек ничего не выпадает, поэтому сеть может принять их пустую добычу, и плоскость сломает и их.

<a name="recipe" />

## Рецепт

<RecipeFor id="annihilation_plane" />

---
navigation:
  parent: example-setups/example-setups-index.md
  title: Простая ферма истинного кварца
  icon: certus_quartz_crystal
  position: 110
---

# Простая ферма истинного кварца

Как описано в разделе [о росте истинного кварца](../ae2-mechanics/certus-growth.md), для автоматического сбора кристаллов <ItemLink id="certus_quartz_crystal" />
нужны плоскости уничтожения <ItemLink id="annihilation_plane" /> и шины хранения <ItemLink id="storage_bus" />.
Ускорители роста <ItemLink id="growth_accelerator" /> сильно ускоряют рост зародышей. Плоскости ломают
выросшие друзы <ItemLink id="quartz_cluster" />. Фильтрация использует особенность незрелых зародышей кварца:
с них выпадает пыль <ItemLink id="certus_quartz_dust" />, а не пустой результат.

С безупречным цветущим блоком <ItemLink id="flawless_budding_quartz" /> ферма работает сама. Потресканные, сколотые и повреждённые
блоки нужно заменять вручную или автоматизировать замену по примеру [полуавтоматической](semiauto-certus-farm.md)
или [полностью автоматической фермы](advanced-certus-farm.md).

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/simple_certus_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="3.7 1 1" max="4 2 2">
        (1) Плоскость уничтожения. Настроек нет, можно зачаровать на «Удачу».
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 1" max="3.3 2 2">
        (2) Шина хранения № 1. Фильтр на кристалл истинного кварца.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 .7" max="2 2 1">
        (3) Шина хранения № 2. Фильтр на кристалл истинного кварца. Приоритет выше основного хранилища.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* Первую плоскость уничтожения <ItemLink id="annihilation_plane" /> (1) нельзя настроить, но можно зачаровать на «Удачу».
* Первая шина хранения <ItemLink id="storage_bus" /> (2) отфильтрована по предмету <ItemLink id="certus_quartz_crystal" />.
* Вторая шина хранения <ItemLink id="storage_bus" /> (3) отфильтрована по предмету <ItemLink id="certus_quartz_crystal" />. Её
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) выше, чем у основного хранилища.

## Как это работает

1. Плоскость уничтожения <ItemLink id="annihilation_plane" /> пытается сломать блок перед собой, но ломает только выросшую друзу <ItemLink id="quartz_cluster" />,
   поскольку единственное хранилище подсети — шина <ItemLink id="storage_bus" />, принимающая только кристаллы <ItemLink id="certus_quartz_crystal" />.
4. Первая шина хранения <ItemLink id="storage_bus" /> складывает кристаллы в бочку.
5. Вторая шина хранения <ItemLink id="storage_bus" /> даёт основной сети доступ к кристаллам в бочке.
   Высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) направляет кристаллы
   сначала обратно в бочку, а затем в основное хранилище.

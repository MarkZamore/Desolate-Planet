---
navigation:
  parent: example-setups/example-setups-index.md
  title: Полуавтоматическая ферма истинного кварца
  icon: certus_quartz_crystal
  position: 115
---

# Полуавтоматическая ферма истинного кварца

Для полной автоматизации [простой кварцевой ферме](simple-certus-farm.md) нужен безупречный цветущий блок <ItemLink id="flawless_budding_quartz" />.
Чтобы использовать такой блок, либо перенесите его через [пространственный ввод-вывод](../ae2-mechanics/spatial-io.md), либо постройте ферму у [метеорита](../ae2-mechanics/meteorites.md).

AE2 умеет ставить и ломать блоки. Можно поручить ферме
*заменять цветущие блоки самостоятельно*. Вам останется время от времени добавлять
потресканные цветущие блоки <ItemLink id="flawed_budding_quartz" /> во входную бочку и вынимать обычные блоки кварца <ItemLink id="quartz_block" />
из бочки для отработанных блоков.

Полный автомат описан на странице [полностью автоматической кварцевой фермы](advanced-certus-farm.md).

Эта ферма сложнее [простой](simple-certus-farm.md), поскольку в ней
соединены три отдельных схемы.

**ЧАСТЬ БЛОКОВ СКРЫТА. ПОВОРАЧИВАЙТЕ СЦЕНУ, ЧТОБЫ РАССМОТРЕТЬ СХЕМУ СО ВСЕХ СТОРОН.**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/semiauto_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) Плоскость уничтожения № 1. Настроек нет, можно зачаровать на «Удачу».
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1" max="2.3 3 2">
        (2) Шина хранения № 1. Фильтр на кристалл истинного кварца.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    Подсеть сбора друз
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) Плоскость уничтожения № 2. Настроек нет, требуется «Шёлковое касание».
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1" max="2.3 2 2">
        (4) Шина хранения № 2. Фильтр на блок истинного кварца.
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    Подсеть демонтажа кварцевого блока
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) Плоскость формирования. Настройки по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0 1" max="2.3 1 2">
        (6) Шина импорта. Настройки по умолчанию.
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    Подсеть установки цветущего блока
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="0.7 2 1" max="1 3 2">
        (7) Шина хранения № 3. Фильтр на кристалл истинного кварца. Приоритет выше основного хранилища.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

    <DiamondAnnotation pos="1.5 0.5 1.5" color="#00ff00">
        Вручную добавляйте потресканные цветущие блоки истинного кварца.
        <BlockImage id="flawed_budding_quartz" scale="2" />
    </DiamondAnnotation>

    <DiamondAnnotation pos="1.5 1.5 1.5" color="#00ff00">
        Вручную извлекайте обычные блоки истинного кварца.
        <BlockImage id="quartz_block" scale="2" />
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="165" pitch="5" />
</GameScene>

## Настройки

### Сбор друз

* Первую плоскость уничтожения <ItemLink id="annihilation_plane" /> (1) нельзя настроить, но можно зачаровать на «Удачу».
* Первая шина хранения <ItemLink id="storage_bus" /> (2) отфильтрована по предмету <ItemLink id="certus_quartz_crystal" />.

### Демонтаж кварцевого блока

* Вторую плоскость уничтожения <ItemLink id="annihilation_plane" /> (3) нельзя настроить. Зачаруйте её на «Шёлковое касание».
* Вторая шина хранения <ItemLink id="storage_bus" /> (4) отфильтрована по предмету <ItemLink id="quartz_block" />.

### Установка цветущего блока

* Плоскость формирования <ItemLink id="formation_plane" /> (5) оставьте с настройками по умолчанию.
* Шина импорта <ItemLink id="import_bus" /> (6) используется с настройками по умолчанию.

### Основная сеть

* Третья шина хранения <ItemLink id="storage_bus" /> (7) отфильтрована по предмету <ItemLink id="certus_quartz_crystal" />. Её
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) выше, чем у основного хранилища.

## Как это работает

### Сбор друз

Подсеть сбора друз работает так же, как в [простой кварцевой ферме](simple-certus-farm.md).

1. Плоскость уничтожения <ItemLink id="annihilation_plane" /> пытается сломать блок перед собой, но ломает только выросшую друзу <ItemLink id="quartz_cluster" />,
   поскольку единственное хранилище подсети — шина <ItemLink id="storage_bus" />, принимающая только кристаллы <ItemLink id="certus_quartz_crystal" />.
2. Шина хранения <ItemLink id="storage_bus" /> складывает кристаллы в бочку.

### Демонтаж кварцевого блока

Подсеть ломает истощённый цветущий блок, когда он становится обычным блоком кварца <ItemLink id="quartz_block" />.
Она работает по тому же принципу, что и подсеть сбора друз.

1. Плоскость уничтожения <ItemLink id="annihilation_plane" /> пытается сломать блок перед собой, но ломает только кварцевый блок <ItemLink id="quartz_block" />,
   поскольку единственное хранилище — шина <ItemLink id="storage_bus" />, принимающая только блоки <ItemLink id="quartz_block" />.
   С «Шёлковым касанием» цветущий блок при разрушении сохранил бы свой тип, поэтому фильтр не даёт плоскости сломать его раньше времени.
2. Шина хранения <ItemLink id="storage_bus" /> складывает обычный кварцевый блок в бочку для отработанных блоков.
   Чтобы восстановить цветущий блок, бросьте его в воду вместе с заряженным кристаллом <ItemLink id="charged_certus_quartz_crystal" />.

### Установка цветущего блока

Эта подсеть ставит новый цветущий блок <ItemLink id="flawed_budding_quartz" />, когда отработанный блок удалён.

1. Шина импорта <ItemLink id="import_bus" /> забирает цветущий блок из входной бочки.
2. Единственное хранилище — плоскость формирования <ItemLink id="formation_plane" />. Она ставит блок.

### Основная сеть

* Шина хранения <ItemLink id="storage_bus" /> даёт основной сети, в том числе [автоматической зарядке](charger-automation.md), доступ к кристаллам в бочке.
  Высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) направляет кристаллы
  сначала обратно в бочку, а затем в основное хранилище.

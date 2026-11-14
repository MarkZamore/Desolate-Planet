---
navigation:
  parent: example-setups/example-setups-index.md
  title: Полностью автоматическая ферма истинного кварца
  icon: certus_quartz_crystal
  position: 120
---

# Полностью автоматическая ферма истинного кварца

Это [полуавтоматическая ферма истинного кварца](semiauto-certus-farm.md), полностью подключённая к МЭ-сети.


Вместо запаса цветущих блоков, которые нужно восстанавливать вручную,
здесь используются [автоматическая зарядка](charger-automation.md) и [автоматизация рецептов в воде](throw-in-water-automation.md).


**ЧАСТЬ БЛОКОВ СКРЫТА. ПОВОРАЧИВАЙТЕ СЦЕНУ, ЧТОБЫ РАССМОТРЕТЬ СХЕМУ СО ВСЕХ СТОРОН.**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/advanced_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) Плоскость уничтожения № 1. Настроек нет, можно зачаровать на «Удачу».
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1.7" max="3 3 2">
        (2) Шина хранения № 1. Фильтр на кристалл истинного кварца.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    Подсеть сбора друз
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) Плоскость уничтожения № 2. Настроек нет, требуется «Шёлковое касание».
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1.7" max="3 2 2">
        (4) Шина хранения № 2. Фильтр на блок истинного кварца.
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    Подсеть демонтажа кварцевого блока
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) Плоскость формирования. Настройки по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0.7 2" max="3 1 3">
        (6) Шина импорта. Фильтр на потресканный цветущий блок истинного кварца.
        <BlockImage id="flawed_budding_quartz" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    Подсеть установки цветущего блока
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="1.7 2 2" max="2 3 3">
        (7) Шина хранения № 3. Фильтр на кристалл истинного кварца. Приоритет выше основного хранилища.
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#aaaadd" min="2 1 2" max="3 2 3">
        (8) Интерфейс. Поддерживает запас в один потресканный цветущий блок истинного кварца. Установлена карта изготовления.
        <Row><BlockImage id="flawed_budding_quartz" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="1.5 0.5 0" color="#00ff00">
        К основной сети, автоматической зарядке и рецептам в воде
        <Row>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/charger_automation.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/throw_in_water.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        </Row>
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
* Шина импорта <ItemLink id="import_bus" /> (6) отфильтрована по предмету <ItemLink id="flawed_budding_quartz" />.

### Основная сеть

* Третья шина хранения <ItemLink id="storage_bus" /> (7) отфильтрована по предмету <ItemLink id="certus_quartz_crystal" />. Её
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) выше, чем у основного хранилища.
* Интерфейс <ItemLink id="interface" /> хранит один потресканный цветущий блок. В нём установлена карта <ItemLink id="crafting_card" />.

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
2. Шина хранения <ItemLink id="storage_bus" /> помещает обычный блок кварца в интерфейс <ItemLink id="interface" />.
   [Рецепт в воде](throw-in-water-automation.md) превращает его в новый цветущий блок <ItemLink id="flawed_budding_quartz" />.

### Установка цветущего блока

Эта подсеть ставит новый цветущий блок <ItemLink id="flawed_budding_quartz" />, когда отработанный блок удалён.

1. Шина импорта <ItemLink id="import_bus" /> забирает цветущий блок из интерфейса <ItemLink id="interface" /> в [хранилище подсети](../ae2-mechanics/import-export-storage.md).
2. Единственное хранилище — плоскость формирования <ItemLink id="formation_plane" />. Она ставит блок.

### Основная сеть

* Шина хранения <ItemLink id="storage_bus" /> даёт основной сети, в том числе [автоматической зарядке](charger-automation.md), доступ к кристаллам в бочке.
  Высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) направляет кристаллы
  сначала обратно в бочку, а затем в основное хранилище.
* Интерфейс <ItemLink id="interface" /> выдаёт новый цветущий блок <ItemLink id="flawed_budding_quartz" /> подсети установки
    и позволяет подсети демонтажа вернуть отработанный блок в основную сеть.
    Карта <ItemLink id="crafting_card" /> позволяет запросить новый цветущий блок через [автокрафт](../ae2-mechanics/autocrafting.md) основной сети.

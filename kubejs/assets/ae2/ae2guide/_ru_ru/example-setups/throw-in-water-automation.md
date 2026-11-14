---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоматизация рецептов в воде
  icon: fluix_crystal
---

# Автоматизация рецептов в воде

В этой схеме используется поставщик шаблонов <ItemLink id="pattern_provider" />, поэтому она рассчитана на подключение к [автокрафту](../ae2-mechanics/autocrafting.md).


В некоторых рецептах предметы бросают в воду. Похожая схема может выбрасывать предметы и в другое место.
Для этого подойдут плоскость формирования <ItemLink id="formation_plane" /> и плоскость уничтожения <ItemLink id="annihilation_plane" />
в двух модифицированных [подсетях-трубах](pipe-subnet.md).

Используйте [автоматическую зарядку](charger-automation.md), чтобы получать заряженные кристаллы <ItemLink id="charged_certus_quartz_crystal" />.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/throw_in_water.snbt" />

<BoxAnnotation color="#dddddd" min="2 0 1" max="3 1 2">
        (1) Поставщик шаблонов. Настройки по умолчанию и нужные шаблоны обработки.

        ![Шаблон флюисового кристалла](../assets/diagrams/fluix_pattern_small.png) ![Шаблон цветущего кварца](../assets/diagrams/flawed_budding_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1.7 0 1" max="2 1 2">
        (2) Интерфейс. Настройки по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 .7 1" max="2 1 2">
        (3) Плоскость формирования. Выбрасывает полученные предметы.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 2 1" max="2 2.3 2">
        (4) Плоскость уничтожения. Настроек нет.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 1 1" max="3 1.3 2">
        (5) Шина хранения. Фильтр на результаты шаблонов.
        <Row><ItemImage id="fluix_crystal" scale="2" /><BlockImage id="flawless_budding_quartz" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="3.9 0.5 1.5" color="#00ff00">
        К основной сети и автоматической зарядке
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/charger_automation.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
    </DiamondAnnotation>

  <IsometricCamera yaw="180" pitch="0" />
</GameScene>

## Настройки и шаблоны

* Поставщик шаблонов <ItemLink id="pattern_provider" /> (1) используется с настройками по умолчанию. Вставьте нужные шаблоны <ItemLink id="processing_pattern" />.
  * Для кристалла <ItemLink id="fluix_crystal" /> подходит обычный рецепт из JEI/REI:

    ![Шаблон флюисового кристалла](../assets/diagrams/fluix_pattern.png)

  * Для блока <ItemLink id="flawed_budding_quartz" /> лучше взять обычный кварцевый блок <ItemLink id="quartz_block" />.
    Тогда ингредиент одного рецепта не окажется результатом другого, и шина хранения сможет отличить входные предметы от готовых:

    ![Шаблон цветущего кварца](../assets/diagrams/flawed_budding_pattern.png)

* Интерфейс <ItemLink id="interface" /> (2) используется с настройками по умолчанию.
* Плоскость формирования <ItemLink id="formation_plane" /> (3) настроена выбрасывать полученные предметы.
* Плоскость уничтожения <ItemLink id="annihilation_plane" /> (4) не имеет интерфейса настройки.
* Шина хранения <ItemLink id="storage_bus" /> (5) отфильтрована по результатам шаблонов.

## Как это работает

1.  Поставщик шаблонов <ItemLink id="pattern_provider" /> отправляет ингредиенты в интерфейс <ItemLink id="interface" /> сбоку, в зелёную подсеть.
2.  Интерфейс по умолчанию не держит запаса и отправляет предметы в [хранилище подсети](../ae2-mechanics/import-export-storage.md).
3.  Единственное хранилище зелёной подсети — плоскость формирования <ItemLink id="formation_plane" />. Она выбрасывает ингредиенты в воду.
4.  Плоскость уничтожения <ItemLink id="annihilation_plane" /> оранжевой подсети пытается подобрать ингредиенты, но
    шина хранения <ItemLink id="storage_bus" /> над поставщиком, единственное хранилище оранжевой подсети, принимает только результаты этих рецептов.
5.  В воде ингредиенты превращаются в готовые предметы.
6.  Теперь плоскость уничтожения может подобрать их, поскольку фильтр шины хранения пропускает результат.
7.  Шина хранения кладёт готовые предметы в поставщик шаблонов, возвращая их в сеть.

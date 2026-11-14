---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоматическое создание процессоров
  icon: inscriber
---

# Автоматическое создание процессоров

Это один из способов автоматизировать создание [процессоров](../items-blocks-machines/processors.md).

Для этой схемы подойдут предметные трубы, каналы или другие средства транспортировки из разных модов,
если у них есть фильтры.

![Схема производственного процесса](../assets/diagrams/processor_flow_diagram.png)

Ниже показано, как обойтись средствами AE2, используя [подсети-трубы](pipe-subnet.md).

В этой схеме есть поставщик шаблонов <ItemLink id="pattern_provider" />, поэтому она рассчитана на подключение к [автокрафту](../ae2-mechanics/autocrafting.md).
Для автономной работы замените поставщик ещё одной бочкой и сами складывайте ингредиенты в верхнюю бочку.

Схема совместима и с предыдущими версиями AE2.
Даже если у вырезателей <ItemLink id="inscriber" /> подача и извлечение возможны только с определённых сторон,
подсети подключены к нужным граням.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/processor_automation.snbt" />

  <BoxAnnotation color="#dddddd" min="5 1 0" max="6 2 1" thickness=".05">
        (1) Поставщик шаблонов. Настройки по умолчанию и нужные шаблоны обработки.

        <Row>
            ![Шаблон логического процессора](../assets/diagrams/logic_pattern_small.png)
            ![Шаблон вычислительного процессора](../assets/diagrams/calculation_pattern_small.png)
            ![Шаблон инженерного процессора](../assets/diagrams/engineering_pattern_small.png)
        </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.7 2 0" max="5 3 1" thickness=".05">
        (2) Шина хранения № 1. Настройки по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="4.3 2 1" thickness=".05">
        (3) Шина экспорта № 1. Фильтр на кремний, две карты ускорения.
        <Row><ItemImage id="silicon" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="4.3 3 1" thickness=".05">
        (4) Шина экспорта № 2. Фильтр на золотой слиток, две карты ускорения.
        <Row><ItemImage id="minecraft:gold_ingot" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="4.3 4 1" thickness=".05">
        (5) Шина экспорта № 3. Фильтр на кристалл истинного кварца, две карты ускорения.
        <Row><ItemImage id="certus_quartz_crystal" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 6 0" max="4.3 5 1" thickness=".05">
        (6) Шина экспорта № 4. Фильтр на алмаз, две карты ускорения.
        <Row><ItemImage id="minecraft:diamond" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 0" max="2 2 1" thickness=".05">
        (7) Шина экспорта № 5. Фильтр на красную пыль, две карты ускорения.
        <Row><ItemImage id="minecraft:redstone" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="3 2 1" thickness=".05">
        (8) Вырезатель № 1. Настройки по умолчанию. Установлены пресс для кремния и четыре карты ускорения.
        <Row><ItemImage id="silicon_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 3 0" max="3 4 1" thickness=".05">
        (9) Вырезатель № 2. Настройки по умолчанию. Установлены логический пресс и четыре карты ускорения.
        <Row><ItemImage id="logic_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="3 5 1" thickness=".05">
        (10) Вырезатель № 3. Настройки по умолчанию. Установлены вычислительный пресс и четыре карты ускорения.
        <Row><ItemImage id="calculation_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="3 6 1" thickness=".05">
        (11) Вырезатель № 4. Настройки по умолчанию. Установлены инженерный пресс и четыре карты ускорения.
        <Row><ItemImage id="engineering_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 0" max="1 3 1" thickness=".05">
        (12) Вырезатель № 5. Настройки по умолчанию. Установлены четыре карты ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 2 0" max="3 1 1" thickness=".05">
        (13) Шина импорта № 1. Настройки по умолчанию, две карты ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 4 0" max="3 3 1" thickness=".05">
        (14) Шина импорта № 2. Настройки по умолчанию, две карты ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 5 0" max="3 4 1" thickness=".05">
        (15) Шина импорта № 3. Настройки по умолчанию, две карты ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 6 0" max="3 5 1" thickness=".05">
        (16) Шина импорта № 4. Настройки по умолчанию, две карты ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 3 0" max="1 3.3 1" thickness=".05">
        (17) Шина хранения № 2. Настройки по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1.7 0" max="1 2 1" thickness=".05">
        (18) Шина хранения № 3. Настройки по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 0" max="0.7 3 1" thickness=".05">
        (19) Шина импорта № 5. Настройки по умолчанию, две карты ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="5 0.7 0" max="6 1 1" thickness=".05">
        (20) Шина хранения № 4. Настройки по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.3 2.7 0.3" max="3.7 3 0.7" thickness=".05">
        Кварцевое волокно питает все три вырезателя. Вырезатели передают энергию, как кабели.
  </BoxAnnotation>

<DiamondAnnotation pos="7 1.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="185" pitch="5" />
</GameScene>

## Настройки

* Поставщик шаблонов <ItemLink id="pattern_provider" /> (1) используется с настройками по умолчанию и нужными шаблонами <ItemLink id="processing_pattern" />.

  ![Шаблон логического процессора](../assets/diagrams/logic_pattern.png)
  ![Шаблон вычислительного процессора](../assets/diagrams/calculation_pattern.png)
  ![Шаблон инженерного процессора](../assets/diagrams/engineering_pattern.png)

* Шины хранения <ItemLink id="storage_bus" /> (2, 17, 18, 20) используются с настройками по умолчанию.
* Шины экспорта <ItemLink id="export_bus" /> (3–7) отфильтрованы по соответствующим ингредиентам. В каждой по две карты <ItemLink id="speed_card" />.
    <Row>
      <ItemImage id="silicon" scale="2" />
      <ItemImage id="minecraft:gold_ingot" scale="2" />
      <ItemImage id="certus_quartz_crystal" scale="2" />
      <ItemImage id="minecraft:diamond" scale="2" />
      <ItemImage id="minecraft:redstone" scale="2" />
    </Row>
* Шины импорта <ItemLink id="import_bus" /> (13–16, 19) используются с настройками по умолчанию. В каждой по две карты <ItemLink id="speed_card" />.
* Вырезатели <ItemLink id="inscriber" /> используются с настройками по умолчанию. В каждом установлен подходящий [пресс](../items-blocks-machines/presses.md)
   и четыре карты <ItemLink id="speed_card" />.
   <Row>
     <ItemImage id="silicon_press" scale="2" />
     <ItemImage id="logic_processor_press" scale="2" />
     <ItemImage id="calculation_processor_press" scale="2" />
     <ItemImage id="engineering_processor_press" scale="2" />
   </Row>

## Как это работает

1. Поставщик шаблонов <ItemLink id="pattern_provider" /> отправляет ингредиенты в бочку.
2. Первая [подсеть-труба](pipe-subnet.md) оранжевого цвета забирает кремний, красную пыль и материал для нужного процессора
   (золотой слиток, кристалл истинного кварца или алмаз) и подаёт их в соответствующий вырезатель <ItemLink id="inscriber" />.
3. Первые четыре вырезателя <ItemLink id="inscriber" /> печатают кремний <ItemLink id="printed_silicon" /> и подходящую схему: логическую <ItemLink id="printed_logic_processor" />,
   вычислительную <ItemLink id="printed_calculation_processor" /> или инженерную <ItemLink id="printed_engineering_processor" />.
4. Вторая и третья [подсети-трубы](pipe-subnet.md), отмеченные зелёным, забирают напечатанные схемы из первых четырёх вырезателей <ItemLink id="inscriber" />
    и подают их в пятый вырезатель <ItemLink id="inscriber" />, где идёт окончательная сборка.
5. Пятый вырезатель <ItemLink id="inscriber" /> собирает [процессор](../items-blocks-machines/processors.md).
6. Четвёртая [подсеть-труба](pipe-subnet.md), отмеченная фиолетовым, кладёт процессор в поставщик шаблонов и возвращает его в основную сеть.

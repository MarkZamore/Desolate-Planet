---
navigation:
  parent: example-setups/example-setups-index.md
  title: Загрузка и разгрузка ячеек
  icon: io_port
---

# Загрузка и разгрузка ячеек

Как быстро выгрузить ячейку в сундук, блоки хранения или рюкзак? А как заполнить её из такой ёмкости?

Поместите порт ввода-вывода <ItemLink id="io_port" /> в подсеть, чтобы ограничить источник или место назначения.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/cell_dumper_filler.snbt" />

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 1">
        (1) Порт ввода-вывода. Кнопка со стрелкой по центру переключает между «Передать данные в сеть»
        и «Передать данные в камеру хранения». Вставлены три карты ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0.7 0" max="1 1 1">
        (2) Шина хранения. Настройки по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#33dd33" min="0 1 0" max="1 2 1">
        Поместите сюда ёмкость, которую хотите заполнить или опустошить.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0.35 0.35" max="2.3 0.65 0.65">
        Кварцевое волокно требуется только при питании от другой сети.
  </BoxAnnotation>

<DiamondAnnotation pos="3 0.5 0.5" color="#00ff00">
        К источнику энергии, например другой сети или приёмщику энергии.
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* Порт ввода-вывода <ItemLink id="io_port" /> (1) переключается кнопкой со стрелкой между передачей в сеть
  и передачей в ячейку. Три карты ускорения дают максимальную скорость.
* Шина хранения <ItemLink id="storage_bus" /> (2) используется с настройками по умолчанию.

## Как это работает

### Передача в сеть

1. Порт ввода-вывода <ItemLink id="io_port" /> отправляет содержимое вставленной [ячейки хранения](../items-blocks-machines/storage_cells.md)
    в [хранилище сети](../ae2-mechanics/import-export-storage.md).
2. Единственное хранилище подсети — шина <ItemLink id="storage_bus" />. Она помещает предметы, жидкости и другие ресурсы в ёмкость,
    к которой её подключили.
* Энергохранилище <ItemLink id="energy_cell" /> запасает достаточно [энергии](../ae2-mechanics/energy.md),
    чтобы сеть выдерживала передачу большого количества ресурсов за тик.

### Передача в ячейку

1. Порт ввода-вывода <ItemLink id="io_port" /> переносит содержимое [хранилища сети](../ae2-mechanics/import-export-storage.md)
   во вставленную [ячейку хранения](../items-blocks-machines/storage_cells.md).
2. Единственное хранилище подсети — шина <ItemLink id="storage_bus" />. Она забирает предметы, жидкости и другие ресурсы из ёмкости,
   к которой её подключили.
* Энергохранилище <ItemLink id="energy_cell" /> запасает достаточно [энергии](../ae2-mechanics/energy.md),
  чтобы сеть выдерживала передачу большого количества ресурсов за тик.

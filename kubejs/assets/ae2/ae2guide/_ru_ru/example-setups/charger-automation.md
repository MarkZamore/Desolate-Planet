---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоматическая зарядка
  icon: charger
---

# Автоматическая зарядка

В этой схеме используется поставщик шаблонов <ItemLink id="pattern_provider" />, поэтому она рассчитана на подключение к [автокрафту](../ae2-mechanics/autocrafting.md).
Для автоматизации зарядника <ItemLink id="charger" /> без МЭ-сети хватит воронок и сундуков.

Поставщик шаблонов <ItemLink id="pattern_provider" /> подаёт ингредиент в зарядник <ItemLink id="charger" />, а [подсеть-труба](pipe-subnet.md)
или обычная предметная труба возвращает результат в поставщик.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/charger_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) Поставщик шаблонов. Настройки по умолчанию и нужные шаблоны обработки. Также питает зарядник.

        ![Шаблон зарядки](../assets/diagrams/charger_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="1 1.3 1">
        (2) Шина импорта. Настройки по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (3) Шина хранения. Настройки по умолчанию.
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* Поставщик шаблонов <ItemLink id="pattern_provider" /> (1) используется с настройками по умолчанию и нужными шаблонами <ItemLink id="processing_pattern" />.
  Он же подаёт [энергию](../ae2-mechanics/energy.md) в зарядник <ItemLink id="charger" />, поскольку действует как [кабель](../items-blocks-machines/cables.md).

    ![Шаблон зарядки](../assets/diagrams/charger_pattern.png)

* Шина импорта <ItemLink id="import_bus" /> (2) используется с настройками по умолчанию.
* Шина хранения <ItemLink id="storage_bus" /> (3) используется с настройками по умолчанию.

## Как это работает

1. Поставщик шаблонов <ItemLink id="pattern_provider" /> отправляет ингредиенты в зарядник <ItemLink id="charger" />.
2. Зарядник заряжает предмет.
3. Шина импорта <ItemLink id="import_bus" /> зелёной подсети забирает заряженный предмет и пытается поместить его
   в [хранилище сети](../ae2-mechanics/import-export-storage.md).
4. Единственное хранилище зелёной подсети — шина <ItemLink id="storage_bus" />. Через неё предмет возвращается в поставщик шаблонов основной сети.

---
navigation:
  parent: example-setups/example-setups-index.md
  title: Пополнение запасов через интерфейс
  icon: interface
---

# Пополнение запасов через интерфейс

Как держать заданное количество разных предметов и автоматически создавать недостающие?

Интерфейс <ItemLink id="interface" /> с картой изготовления <ItemLink id="crafting_card" /> может автоматически заказывать предметы
через [автокрафт](../ae2-mechanics/autocrafting.md). Эта схема удобна, если нужно хранить
понемногу разных предметов.

Демонстрационная схема сокращена, чтобы её проще было осмотреть. Лучше использовать четыре интерфейса <ItemLink id="interface" /> и четыре шины хранения <ItemLink id="storage_bus" />,
чтобы занять все восемь [каналов](../ae2-mechanics/channels.md) обычного [кабеля](../items-blocks-machines/cables.md).

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_autostocking.snbt" />

<BoxAnnotation color="#dddddd" min="0 0 0" max="2 1 1">
        (1) Интерфейсы. Поддерживают запас выбранных предметов. Установлены карты изготовления.
        <ItemImage id="crafting_card" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="2 1.3 1">
        (2) Шины хранения. Режим ввода и вывода установлен на «Только извлекать».
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* Интерфейсы <ItemLink id="interface" /> (1) настроены хранить заданные предметы. Нажмите нужным предметом по одному из верхних слотов
   или перетащите его туда из JEI, затем задайте количество кнопкой с гаечным ключом над слотами. Установите карты <ItemLink id="crafting_card" />.
* Для шин хранения <ItemLink id="storage_bus" /> (2) выберите режим ввода и вывода «Только извлекать».

## Как это работает

1. Если интерфейс <ItemLink id="interface" /> не находит достаточно предметов в [хранилище сети](../ae2-mechanics/import-export-storage.md),
   карта <ItemLink id="crafting_card" /> позволяет ему заказать недостающее через [автокрафт](../ae2-mechanics/autocrafting.md).
2. Шины хранения <ItemLink id="storage_bus" /> дают сети доступ к содержимому интерфейсов.

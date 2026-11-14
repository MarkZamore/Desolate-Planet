---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "МЭ-интерфейс"
  icon: interface
  position: 210
categories:
- devices
item_ids:
- ae2:interface
- ae2:cable_interface
---

<a name="the-interface" />

# МЭ-интерфейс

<Row gap="20">
<BlockImage id="interface" scale="8" />
<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_interface.snbt" />
</GameScene>
</Row>

Интерфейс работает как небольшой сундук и резервуар. Он пополняет заданный запас из [сетевого хранилища](../ae2-mechanics/import-export-storage.md)
и возвращает туда излишки. За один игровой такт он может принять или выдать до девяти стопок. Это удобно для быстрого
импорта и экспорта, если трубы успевают передавать предметы.

В интерфейсе можно хранить до девяти типов жидкостей и предметы. Если отключить его от сети, останется обычное
небольшое хранилище для разных ресурсов.

<a name="how-an-interface-works-internally" />

## Как устроен интерфейс

Интерфейс можно представить как сундук и резервуар, к которым подключены быстрые <ItemLink id="import_bus" /> и
<ItemLink id="export_bus" />, а запас контролирует набор <ItemLink id="level_emitter" />.

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_internals.snbt" />

  <BoxAnnotation color="#dddddd" min="1.3 0.3 1.3" max="9.7 1 1.7">
        Излучатели уровня контролируют заданный запас.
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/level_emitter.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 4 1.3" max="9.7 4.7 1.7">
        Излучатели уровня контролируют заданный запас.
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/level_emitter.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 1.3 1.3" max="9.7 2 1.7">
        Шины импорта передают по одной стопке за игровой такт.
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/import_bus.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 3 1.3" max="9.7 3.7 1.7">
        Шины экспорта передают по одной стопке за игровой такт.
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/export_bus.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 1" max="10 3 2">
        Девять внутренних ячеек.
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="15" />
</GameScene>

<a name="special-interactions" />

## Взаимодействие с другими устройствами

Интерфейсы по-особому работают с некоторыми [устройствами AE2](../ae2-mechanics/devices.md).

Если подключить <ItemLink id="storage_bus" /> к интерфейсу без настроек, вся его [сеть хранения](../ae2-mechanics/import-export-storage.md)
станет доступна сети шины, как один большой сундук. Если указать запас хотя бы одного предмета в ячейках фильтра,
это поведение отключится.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_storage.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Если поставщик шаблонов подключён к ненастроенному интерфейсу [подсети](../ae2-mechanics/subnetworks.md), он отправляет
ингредиенты прямо в [хранилище](../ae2-mechanics/import-export-storage.md) подсети. Они не занимают ячейки интерфейса.
Следующая партия поступит, когда в хранилище появится место.

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        Плоский интерфейс
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        Шины хранения
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        Места подачи ингредиентов: несколько станков или несколько граней одного станка.
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

<a name="variants" />

## Варианты

Интерфейс бывает обычным и плоским, в виде [кабельного модуля](../ae2-mechanics/cable-subparts.md). От варианта зависит,
с каких сторон доступны инвентарь и сетевое соединение.

*   Обычный интерфейс принимает и выдаёт содержимое со всех сторон. Он подключается к сети любой гранью.

*   Плоские интерфейсы — [кабельные модули](../ae2-mechanics/cable-subparts.md). Несколько таких модулей можно разместить
    на одном кабеле. Лицевая сторона принимает и выдаёт содержимое, но не соединяет сети.

Обычный и плоский интерфейсы можно преобразовать друг в друга в сетке крафта.

<a name="settings" />

## Настройки

В верхних ячейках укажите, что должно быть в запасе интерфейса. Когда вы положите туда предмет или перетащите его из
JEI или REI, появится кнопка с ключом. Нажмите её, чтобы задать количество.

Нажмите ПКМ по ячейке, держа ёмкость с жидкостью, например ведро или резервуар. Фильтр запомнит саму жидкость.

<a name="upgrades" />

## Улучшения

Интерфейс поддерживает следующие [улучшения](upgrade_cards.md):

*   <ItemLink id="fuzzy_card" /> позволяет фильтровать предметы по степени износа или игнорировать их NBT.
*   <ItemLink id="crafting_card" /> позволяет пополнять запас через [автокрафт](../ae2-mechanics/autocrafting.md).
    Интерфейс сначала пытается взять предметы из хранилища. Если их нет, он отправляет запрос на создание.

<a name="priority" />

## Приоритет

Нажмите на ключ в правом верхнем углу окна. Интерфейс с высоким приоритетом пополнит запас раньше интерфейса
с низким приоритетом.

<a name="recipes" />

## Рецепты

<Recipe id="network/blocks/interfaces_interface" />

<RecipeFor id="cable_interface" />

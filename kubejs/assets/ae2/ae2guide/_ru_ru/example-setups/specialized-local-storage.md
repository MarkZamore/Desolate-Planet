---
navigation:
  parent: example-setups/example-setups-index.md
  title: Отдельное хранилище для фермы
  icon: drive
---

# Отдельное хранилище для фермы

Благодаря [особенностям интерфейса](../items-blocks-machines/interface.md#special-interactions)
[подсеть](../ae2-mechanics/subnetworks.md) может открыть основной сети доступ к своему хранилищу, не получая доступа к хранилищу основной сети.
Для подключения нужен всего один [канал](../ae2-mechanics/channels.md).

Так можно хранить продукцию фермы отдельно, чтобы она не заполнила основное хранилище.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/local_storage.snbt" />

<BoxAnnotation color="#dddddd" min="4 0 0" max="5 2 1">
        (1) Приём предметов. Здесь это интерфейс.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 0 0" max="4 1 1">
        (2) МЭ-накопитель. Ячейки отфильтрованы по продукции фермы.
        В ячейки можно установить карты равного распределения и уничтожения излишков.
        <Row><ItemImage id="item_storage_cell_4k" scale="2" /> <ItemImage id="equal_distribution_card" scale="2" /> <ItemImage id="void_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 1 0" max="4 2 0.3">
        (3) Терминал создания. Видит содержимое МЭ-накопителя подсети. Хранилище основной сети ему недоступно.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0 0" max="2.3 1 1">
        (4) Интерфейс № 2. Настройки по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1.7 0 0" max="2 1 1">
        (5) Шина хранения. Приоритет выше основного хранилища. Можно отфильтровать по продукции фермы.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 0.3">
        Терминал создания. Видит содержимое основной сети и подсети.
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* Первый интерфейс <ItemLink id="interface" /> (1) принимает продукцию фермы и передаёт её в подсеть.
* В МЭ-накопитель <ItemLink id="drive" /> (2) вставьте [ячейки](../items-blocks-machines/storage_cells.md),
  [отфильтрованные](../items-blocks-machines/cell_workbench.md) по предметам, которые даёт ферма.
  В ячейки можно установить карты <ItemLink id="equal_distribution_card" /> и <ItemLink id="void_card" />.
* Второй интерфейс <ItemLink id="interface" /> (4) используется с настройками по умолчанию.
* У шины хранения <ItemLink id="storage_bus" /> [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) должен быть выше,
  чем у основного хранилища. Можно настроить фильтр на продукцию фермы.

## Как это работает

* Интерфейс <ItemLink id="interface" /> в подсети открывает шине хранения <ItemLink id="storage_bus" /> основной сети доступ
к МЭ-накопителю <ItemLink id="drive" />. Шина может напрямую записывать предметы в его ячейки и извлекать их.
* Высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) шины хранения означает, что предметы сначала идут
  в подсеть, а уже затем в основное хранилище.
* Когда ячейки подсети заполняются, продукция фермы не переполняет основную сеть.
Если заполнение останавливает ферму, карты <ItemLink id="void_card" /> позволяют удалять лишние предметы.
* Если ферма производит несколько предметов, карты <ItemLink id="equal_distribution_card" /> распределяют место,
чтобы один вид продукции не занял ячейки целиком.

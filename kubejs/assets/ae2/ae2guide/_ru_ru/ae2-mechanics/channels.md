---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: Каналы
  icon: controller
---

# Каналы

В [МЭ-сетях](me-network-connections.md) Applied Energistics 2 каналы нужны [устройствам](../ae2-mechanics/devices.md), которые используют сетевое хранилище или другие услуги сети.

Представьте компьютер с ограниченным числом портов USB. У большинства механизмов, полноблочных устройств и обычных кабелей есть место для восьми каналов. [Плотный кабель](../items-blocks-machines/cables.md#dense-cable) пропускает до 32. Столько же могут передать <ItemLink id="me_p2p_tunnel" /> и [квантовый сетевой мост](../items-blocks-machines/quantum_bridge.md). Канал, который заняло устройство, уже нельзя отдать другому устройству ниже по линии.

<GameScene zoom="7" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_demonstration_1.snbt" />

  <LineAnnotation color="#33ff33" from="1 .4 .7" to="2.4 .4 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .7" to="2.4 .6 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .6" to="2.6 .4 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.4 .6 .7" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .4 .7" to="2.4 .4 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .6 .6" to="2.6 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 .6" to="2.6 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.1 .6 1.5" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 1.5" to="2.9 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.6 .6 1.5" to="2.6 .9 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .1 1.5" to="2.4 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .4" to="3.5 .6 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="3.5 .6 .4" to="3.5 .9 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="3.5 .1 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .3" to="1.5 .6 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1.5 .6 .3" to="1.5 .9 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1.5 .1 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#ff3333" from="3.5 .5 .5" to="5.5 .5 .5" alwaysOnTop={true}>
  Все восемь каналов кабеля заняты. Накопителю канал не достался.
  </LineAnnotation>

  <LineAnnotation color="#993333" from="1 .5 .5" to="1.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="1.5 .5 .5" to="1.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2 .5 .5" to="2.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2.5 .5 .5" to="2.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="3 .5 .5" to="3.25 .5 .5" alwaysOnTop={true}/>

  <DiamondAnnotation pos="3.6 0.5 0.5" color="#ff0000">
        Все восемь каналов кабеля заняты. Накопителю канал не достался.
    </DiamondAnnotation>

  <IsometricCamera yaw="15" pitch="30" />
</GameScene>

[Умные кабели](../items-blocks-machines/cables.md) показывают, сколько каналов занято и по каким участкам они проходят.

Канал расходует 1⁄128 AE за такт на каждый узел, через который проходит. Если в сети восемь устройств и более 96 узлов, установка <ItemLink id="controller" /> может снизить потребление энергии благодаря изменению маршрутов.

Цвет кабеля позволяет управлять соединениями между соседними кабелями. На вместимость каналов он не влияет.

<a name="channel-routing" />

## Маршрутизация каналов

В сети с <ItemLink id="controller" /> маршрут строится в три шага. Сначала ищется кратчайший путь через соседние механизмы к ближайшему [обычному кабелю](../items-blocks-machines/cables.md): стеклянному, покрытому или умному. Затем — кратчайший путь по обычным кабелям к [плотному кабелю](../items-blocks-machines/cables.md). Наконец, по плотным кабелям выбирается кратчайший маршрут к <ItemLink id="controller" />.

Если на кратчайшем пути все каналы заняты, некоторым [устройствам](devices.md) не хватит каналов. Направляйте их по нужным веткам, меняя цвета кабелей и используя кабельные крепления или туннели.

На этой схеме части накопителей не хватает каналов. Вместимости кабелей в целом достаточно, но алгоритм выбирает кратчайший путь, перегружая одни участки и оставляя другие пустыми.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 3.6" to="1.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.4 0.5 3.6" to="1.4 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 1.6" to="0.6 .5 1.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 1.6" to="0.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 3.4" to="1.4 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 3.4" to="1.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <BoxAnnotation color="#dddddd" min="1.2 0.2 3.2" max="1.8 0.8 3.8" alwaysOnTop={true} thickness="0.05">
        Через этот участок пытаются провести больше восьми каналов. Часть оборудования останется без связи.
  </BoxAnnotation>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

Исправить схему можно, ограничив возможные пути. Сеть проще прокладывать в форме дерева или куста. Старайтесь избегать петель и неоднозначных маршрутов.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue_fix.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 5.6" to="1 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

## Сети без контроллера

В сети без <ItemLink id="controller" /> может работать до восьми устройств, которым нужны каналы. Если таких устройств станет больше восьми, все они отключатся. Уберите лишние устройства или добавьте <ItemLink id="controller" />.

[Умные кабели](../items-blocks-machines/cables.md) в такой сети показывают число занятых каналов во всей сети. С контроллером они показывают число каналов на конкретном участке.

Каждое устройство в сети без контроллера занимает один из общих каналов. <ItemLink id="controller" /> распределяет каналы по кратчайшим маршрутам.

## Проектирование

Как описано в разделе [о маршрутизации](channels.md#channel-routing), стройте сеть в форме дерева. От контроллера идут плотные кабели, от них — обычные, к которым подключены группы из восьми [устройств](../ae2-mechanics/devices.md) или меньше.

Пример неудачной схемы. Проследим путь каналов от контроллера:

1. Справа от контроллера стоит накопитель. Он пропускает столько же каналов, сколько обычный кабель, поэтому из 32 доступно только восемь. Без умного кабеля это сужение не видно.
2. Накопитель занимает канал. Осталось семь.
3. Два канала уходят вверх к терминалам. Осталось пять.
4. Правее интерфейс занимает ещё один канал. Осталось четыре.
5. Канал уходит вверх к поставщику шаблонов. Осталось три.
6. Правее канал уходит вверх к шине импорта. Осталось два.
7. У группы из четырёх поставщиков, работающих со сборщиками, осталось только два канала. Два поставщика не смогут работать.

Проблема в слишком узком участке сразу после контроллера и в том, как по нему распределяются каналы.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/bad_network_structure.snbt" />

<LineAnnotation color="#33ff33" from="6.5 .5 1.5" to="6 .5 1.5" alwaysOnTop={true} thickness="0.4">
  32 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="6 .5 1.5" to="5.5 .5 1.5" alwaysOnTop={true} thickness="0.2">
  8 каналов
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 1.5 1.5" alwaysOnTop={true} thickness="0.1">
  2 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 1.5 1.5" to="5.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 2.5 1.5" to="5.5 2.5 1.1" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="4.5 .5 1.5" alwaysOnTop={true} thickness="0.158">
  5 каналов
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 1.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="3.5 .5 1.5" alwaysOnTop={true} thickness="0.122">
  3 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="3.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 2.5 1.5" to="3.7 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="1.5 .5 1.5" alwaysOnTop={true} thickness="0.1">
  2 канала
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="1.5 0.3 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="0.5 0.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#33ff33" from="0.5 0.5 1.5" to="0.5 0.5 0.5" alwaysOnTop={true} thickness="0.071">
  1 канал
</LineAnnotation>

<LineAnnotation color="#ff3333" from="0.5 1.5 1.5" to="0.5 1.3 1.5" alwaysOnTop={true} thickness="0.071">
  Нет каналов
</LineAnnotation>

<LineAnnotation color="#ff3333" from="1.5 1.5 0.5" to="1.5 1.3 0.5" alwaysOnTop={true} thickness="0.071">
  Нет каналов
</LineAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

---

Пример удачной схемы:

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/treelike_network_structure.snbt" />

    <BoxAnnotation color="#dddddd" min="6.9 0 4.9" max="9.1 4 7.1" thickness="0.05">
        Поставщики шаблонов подключены отдельными группами по восемь.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 4 4" max="8 5 5" thickness="0.05">
        Если сходятся два обычных кабеля, в которых заняты все каналы, после соединения нужен плотный кабель.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 0 13" max="8 1 14" thickness="0.05">
        Кабели разных цветов не соединяются между собой даже вплотную.
    </BoxAnnotation>


  <IsometricCamera yaw="315" pitch="30" />
</GameScene>

## Режимы каналов

Начиная с AE2 10.0.0 для Minecraft 1.18, поведение каналов можно менять параметром `channels` в общем разделе конфигурации. Оператор может узнать текущий режим командой `/ae2 channelmode` или изменить его командой `/ae2 channelmode <mode>`. При смене режима существующие сети сразу перезапустятся с новыми правилами.

Эта настройка развивает вариант из Minecraft 1.12. С ней можно упростить прокладку сетей, сохранив механику каналов.

| Режим | Как работает |
| --- | --- |
| `default` | Обычная пропускная способность кабелей и сетей без контроллера. |
| `x2` | Вместимость удваивается: 16 каналов у обычного кабеля, 64 у плотного и 16 у сети без контроллера. |
| `x3` | Вместимость утраивается: 24 канала у обычного кабеля, 96 у плотного и 24 у сети без контроллера. |
| `x4` | Вместимость увеличивается в четыре раза: 32 канала у обычного кабеля, 128 у плотного и 32 у сети без контроллера. |
| `infinite` | Каналы без ограничений. Контроллер всё равно заметно снижает потребление энергии. Умные кабели либо погашены, если каналов нет, либо светятся целиком. |

---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Туннели P2P
  icon: me_p2p_tunnel
  position: 210
categories:
- devices
item_ids:
- ae2:me_p2p_tunnel
- ae2:redstone_p2p_tunnel
- ae2:item_p2p_tunnel
- ae2:fluid_p2p_tunnel
- ae2:fe_p2p_tunnel
- ae2:light_p2p_tunnel
---

<a name="point-to-point-tunnels" />

# Туннели P2P

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_tunnels.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Туннели P2P передают предметы, жидкости, сигналы красного камня, энергию, свет или [каналы](../ae2-mechanics/channels.md)
через сеть без взаимодействия с самой сетью. Каждый тип туннеля работает с одним видом ресурсов или сигналов.
Туннель действует как прямое соединение между гранями блоков на расстоянии. У него есть заданные вход и выход,
поэтому передача идёт только в одну сторону.

![Прямое соединение через туннель](../assets/assemblies/p2p_portal.png)

Например, воронка напротив входа предметного туннеля работает так, будто подсоединена прямо к бочке.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_hopper_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

А две бочки не передают предметы друг другу, как и соседние бочки без туннеля.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_barrel_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Так же можно соединять устройства с сигналами красного камня:

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_redstone.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<a name="types-of-p2p-tunnel-and-attunement" />

## Типы туннелей и их настройка

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_tunnels.snbt" />
  <IsometricCamera yaw="180" pitch="90" />
</GameScene>

Создать по рецепту можно только туннель МЭ P2P. Чтобы выбрать другой тип, нажмите ПКМ по туннелю нужным предметом.

- МЭ-каналы — любой [кабель](../items-blocks-machines/cables.md).
- Сигнал красного камня — один из компонентов схем на красном камне.
- Предметы — сундук или воронка.
- Жидкости — ведро или бутылочка.
- Энергия — почти любой предмет, в котором хранится энергия.
- Свет — факел или светокамень.

У отдельных типов есть ограничения. Каналы одного туннеля МЭ P2P не проходят через другой туннель того же типа.
Туннели FE отнимают 2,5 % от проходящей энергии, увеличивая собственное [потребление](../ae2-mechanics/energy.md).

<a name="the-most-used-form-of-p2p" />

## Перенос большого числа каналов

Туннели МЭ P2P позволяют провести много [каналов](../ae2-mechanics/channels.md) по одному плотному кабелю
вместо нескольких отдельных кабелей.

В примере восемь входов МЭ P2P принимают 256 каналов (8 × 32) от <ItemLink id="controller" /> основной сети,
а восемь выходов передают их дальше. Каждый вход и выход занимает по одному каналу, поэтому через тонкий
кабель можно провести много каналов. Туннели работают в отдельной [подсети](../ae2-mechanics/subnetworks.md)
и не занимают каналы основной сети. Их можно ставить вплотную к контроллеру или подключить через
[плотный умный кабель](../items-blocks-machines/cables.md#smart-cable), чтобы видеть распределение каналов.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/p2p_compact_channels.snbt" />

  <BoxAnnotation color="#dddddd" min="1.3 1.3 6.3" max="2 2.7 6.7">
        Кварцевое волокно передаёт энергию между основной сетью и подсетью P2P.
  </BoxAnnotation>

  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

Ещё один пример, в том числе с [квантовыми мостами](quantum_bridge.md):

![Туннели P2P и квантовые мосты](../assets/diagrams/p2p_quantum_network.png)

<a name="nesting" />

## Вложенные туннели

Провести бесконечное число каналов по одному кабелю нельзя. Канал самого туннеля МЭ P2P не проходит
через другой туннель МЭ P2P. На схеме внешние туннели на красных кабелях отключены. Ограничение касается
только туннелей МЭ: например, туннели красного камня могут работать через туннель МЭ P2P.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_nesting.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<a name="linking" />

## Соединение входа и выхода

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_linking_frequency.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Чтобы связать концы туннеля, используйте <ItemLink id="memory_card" />. Частота показана цветными квадратами
2 × 2 на задней стороне модуля.

- Shift + ПКМ создаёт новую частоту связи.
- ПКМ применяет записанные настройки, карты улучшений или частоту связи.

Туннель, на котором вы нажали Shift + ПКМ, становится входом, а туннель, на котором нажали ПКМ, — выходом.
Выходов может быть несколько. У туннелей МЭ P2P каналы делятся между выходами: продублировать их нельзя.

<a name="recipe" />

## Рецепт

<RecipeFor id="me_p2p_tunnel" />

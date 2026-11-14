---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: Соединения в сети
  icon: fluix_glass_cable
---

# Соединения в сети

## Что такое сеть?

Сеть — группа [устройств](../ae2-mechanics/devices.md), соединённых блоками, по которым проходят [каналы](../ae2-mechanics/channels.md). Это могут быть [кабели](../items-blocks-machines/cables.md) или полноблочные механизмы и [устройства](../ae2-mechanics/devices.md), например <ItemLink id="charger" />, <ItemLink id="interface" /> и <ItemLink id="drive" />. Даже отдельный кабель технически уже сеть.

## Где ставить устройства

Для [устройств](../ae2-mechanics/devices.md), которые работают со всей сетью, расположение неважно. Например, <ItemLink id="interface" /> получает и передаёт предметы [сетевому хранилищу](../ae2-mechanics/import-export-storage.md), <ItemLink id="level_emitter" /> следит за его содержимым, а <ItemLink id="drive" /> предоставляет место для хранения.

**Важно, к какой сети подключено устройство.** Расстояние до накопителя или интерфейса само по себе ничего не меняет.

## Как проверить соединения

Узнать, что подключено к сети, поможет <ItemLink id="network_tool" />. Он покажет каждый компонент. Если там появилось лишнее устройство или какого-то не хватает, проверьте соединения.

Например, здесь две отдельные сети.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        Сеть 1
  </BoxAnnotation>

<BoxAnnotation color="#915dcd" min="2 0 0" max="3 2 2">
        Сеть 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Здесь тоже две сети. <ItemLink id="quartz_fiber" /> передаёт [энергию](../ae2-mechanics/energy.md), но не связывает сети между собой.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        Сеть 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="1.3 0 0" max="3 2 2">
        Сеть 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

А здесь одна сеть. [Квантовый мост](../items-blocks-machines/quantum_bridge.md) работает как беспроводной [плотный кабель](../items-blocks-machines/cables.md#dense-cable), поэтому соединяет обе стороны.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="7 3 3">
        Одна сеть
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Здесь тоже одна сеть. [Кабели](../items-blocks-machines/cables.md) разных цветов напрямую не соединяются, но кабель без красителя соединяется с кабелями любого цвета.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        Одна сеть
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Неочевидные соединения

Это одна сеть. Полноблочный <ItemLink id="pattern_provider" /> соединяет компоненты подобно кабелю, и <ItemLink id="inscriber" /> тоже пропускает соединение. Поэтому сеть проходит через оба блока.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        Одна сеть
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

В схемах автокрафта с [подсетями](../ae2-mechanics/subnetworks.md) такое соединение иногда нужно разорвать. Нажмите правой кнопкой мыши на поставщик шаблонов с <ItemLink id="certus_quartz_wrench" />, чтобы сделать его направленным. Тогда через одну сторону каналы проходить не будут.

<Row gap="40">
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="2 2 2">
        Сеть 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="2 0 0" max="4 2 2">
        Сеть 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_directional_connection.snbt" />

  <BoxAnnotation color="#ee3333" min="1 .3 .3" max="1.3 .7 .7">
        Здесь кабель не подключается.
  </BoxAnnotation>

  <IsometricCamera yaw="255" pitch="30" />
</GameScene>
</Row>

Большинство [устройств](../ae2-mechanics/devices.md) в виде [кабельных частей](../ae2-mechanics/cable-subparts.md) тоже не пропускают соединение насквозь. Это относится к <ItemLink id="import_bus" />, <ItemLink id="storage_bus" /> и <ItemLink id="cable_interface" />.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/subpart_no_connection.snbt" />

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

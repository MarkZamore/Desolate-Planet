---
navigation:
  parent: example-setups/example-setups-index.md
  title: Пример основной сети
  icon: controller
---

# Пример основной сети

В других схемах часто упоминается «основная сеть». Здесь показано, как разные [устройства](../ae2-mechanics/devices.md) соединяются в одну рабочую систему.

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/treelike_network_structure.snbt" />

    <BoxAnnotation color="#dddddd" min="3.9 0 1.9" max="9.1 5 7.1" thickness="0.05">
        Большая группа поставщиков шаблонов и сборщиков даёт место для обычных рецептов, камнереза и кузнечного стола.
        Шахматное расположение позволяет поставщикам использовать несколько сборщиков параллельно и экономит место.
        Группы по восемь устройств предотвращают проблемы с маршрутизацией каналов.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="3.9 0 9.9" max="5.1 3 12.1" thickness="0.05">
        Механизмы с отдельной подсетью для передачи результатов поставщикам шаблонов.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="-0.1 0 8.9" max="1.1 3 13.1" thickness="0.05">
      Терминалы и вспомогательные устройства. Обычно достаточно терминала создания, который выполняет и функции обычного терминала.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="-0.1 0 -0.1" max="2.1 3 8.1" thickness="0.05">
      Ряд процессоров создания. У части много памяти, у остальных меньше.
      Для реальной сети может пригодиться больше сопроцессоров, чем помещается в сцене.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5.9 0 13.9" max="7.1 1 15.1" thickness="0.05">
      Контроллер лучше ставить в центре базы. Для крупной сети можно сделать его больше, собрав блоки в линию.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="11.9 0 7.9" max="13.1 4 13.1" thickness="0.05">
        Хранилища на МЭ-накопителях и шинах хранения. Устройства собраны группами по восемь.
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="10.9 0 0.9" max="13.1 2 7.1" thickness="0.05">
        Ещё один вариант хранилищ на МЭ-накопителях и шинах хранения, также группами по восемь.
    </BoxAnnotation>

  <IsometricCamera yaw="315" pitch="30" />
</GameScene>

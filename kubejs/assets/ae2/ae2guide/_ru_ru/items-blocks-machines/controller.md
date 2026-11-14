---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "МЭ-контроллер"
  icon: controller
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:controller
---

<a name="the-controller" />

# МЭ-контроллер

<BlockImage id="controller" p:state="online" scale="8" />

МЭ-контроллер распределяет каналы [МЭ-сети](../ae2-mechanics/me-network-connections.md). Без контроллера сеть автономна и поддерживает не более восьми [устройств](../ae2-mechanics/devices.md), которым нужны каналы.

В одной [МЭ-сети](../ae2-mechanics/me-network-connections.md) может быть только один контроллер. Он может состоять из нескольких блоков.

Каждая грань контроллера выдаёт до 32 [каналов](../ae2-mechanics/channels.md).

Каждый блок контроллера расходует 6 AE/такт и хранит до 8000 AE. Крупной сети может понадобиться дополнительный буфер. Подробнее об [энергии](../ae2-mechanics/energy.md).

Многоблочный контроллер можно собрать в разных формах.

<GameScene zoom="2" background="transparent">
  <ImportStructure src="../assets/assemblies/controllers.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

При сборке соблюдайте три правила:

1.  Все блоки контроллера в [МЭ-сети](../ae2-mechanics/me-network-connections.md) должны соприкасаться гранями и образовывать одну конструкцию. Иначе блоки загорятся красным.
2.  Контроллер должен помещаться в объём 7×7×7 блоков. Иначе он загорится красным.
3.  Блок контроллера может иметь соседей с обеих противоположных сторон только по одной оси. При нарушении этого условия он отключится и загорится красным.

<GameScene zoom="2" background="transparent">
  <ImportStructure src="../assets/assemblies/controller_rules.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Правильно собранный контроллер при подаче питания светится и меняет цвет.

ПКМ по контроллеру открывает то же окно, что и <ItemLink id="network_tool" />.

<a name="recipe" />

## Рецепт

<RecipeFor id="controller" />

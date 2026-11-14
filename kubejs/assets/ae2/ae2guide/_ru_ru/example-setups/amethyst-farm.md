---
navigation:
  parent: example-setups/example-setups-index.md
  title: Аметистовая ферма
  icon: minecraft:amethyst_shard
---

# Выращивание аметиста

Ускоритель роста <ItemLink id="growth_accelerator" /> действует и на аметист. Однако способ фильтрации [зародышей истинного кварца](../items-blocks-machines/budding_certus.md)
с помощью плоскости уничтожения <ItemLink id="annihilation_plane" /> здесь не подходит. Незрелые зародыши кварца оставляют
пыль <ItemLink id="certus_quartz_dust" />, а незрелые зародыши аметиста ничего не оставляют. Поэтому плоскость всегда ломает их:
в сети есть место для «ничего».

Зачаруйте плоскость на «Шёлковое касание». Тогда с незрелого аметиста будет выпадать
сам блок зародыша соответствующей стадии. Его можно отфильтровать.

Затем плоскость формирования <ItemLink id="formation_plane" /> ставит друзу <ItemLink id="minecraft:amethyst_cluster" />.
Вторая плоскость уничтожения <ItemLink id="annihilation_plane" /> без «Шёлкового касания» разбивает её на осколки <ItemLink id="minecraft:amethyst_shard" />.

Напротив плоскости формирования нужна сплошная грань блока, к которой прикрепится друза.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/amethyst_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 1 1" max="3 2 2">
        (1) Плоскость уничтожения № 1. Настроек нет, требуется «Шёлковое касание».
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1 1" max="2.3 2 2">
        (2) Плоскость формирования. Принимает только аметистовую друзу.
        <ItemImage id="minecraft:amethyst_cluster" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 0.7 1" max="2 1 2">
        (3) Плоскость уничтожения № 2. Настроек нет, можно зачаровать на «Удачу».
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 1" max="1.3 1 2">
        (4) Шина хранения № 1. Принимает только осколки аметиста.
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 .7" max="1 1 1">
        (5) Шина хранения № 2. Принимает осколки аметиста с приоритетом выше основного хранилища.
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

* Первую плоскость уничтожения <ItemLink id="annihilation_plane" /> (1) нельзя настроить. Зачаруйте её на «Шёлковое касание».
* Плоскость формирования <ItemLink id="formation_plane" /> (2) отфильтрована по блоку <ItemLink id="minecraft:amethyst_cluster" />.
* Вторую плоскость уничтожения <ItemLink id="annihilation_plane" /> (3) нельзя настроить, но можно зачаровать на «Удачу».
* Первая шина хранения <ItemLink id="storage_bus" /> (4) отфильтрована по предмету <ItemLink id="minecraft:amethyst_shard" />.
* Вторая шина хранения <ItemLink id="storage_bus" /> (5) отфильтрована по предмету <ItemLink id="minecraft:amethyst_shard" />. Её
  [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) выше, чем у основного хранилища.

## Как это работает

1. Первая плоскость уничтожения <ItemLink id="annihilation_plane" /> пытается сломать блок перед собой. Ломается только зрелая друза <ItemLink id="minecraft:amethyst_cluster" />,
    поскольку единственное хранилище подсети — плоскость формирования <ItemLink id="formation_plane" />, которая принимает только друзу.
«Шёлковое касание» обязательно, иначе плоскость сломает и незрелые зародыши, с которых ничего не выпадет.
2. Плоскость формирования <ItemLink id="formation_plane" /> ставит друзу на грань блока напротив.
3. Вторая плоскость уничтожения <ItemLink id="annihilation_plane" /> разбивает друзу на осколки <ItemLink id="minecraft:amethyst_shard" />.
4. Первая шина хранения <ItemLink id="storage_bus" /> складывает осколки в бочку. Фильтр необязателен,
поскольку ко второй плоскости попадают только выросшие друзы.
5. Через вторую шину хранения <ItemLink id="storage_bus" /> основная сеть получает доступ ко всем осколкам.
Высокий [приоритет](../ae2-mechanics/import-export-storage.md#storage-priority) означает, что осколки сначала будут возвращаться
в бочку, а уже затем попадут в основное хранилище.

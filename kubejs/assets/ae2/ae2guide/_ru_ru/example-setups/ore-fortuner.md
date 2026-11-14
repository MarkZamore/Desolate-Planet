---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоматическая добыча руды с «Удачей»
  icon: minecraft:raw_iron
---

# Автоматическая добыча руды с «Удачей»

Плоскость уничтожения <ItemLink id="annihilation_plane" /> поддерживает все зачарования для кирок, включая «Удачу».
Зачаруйте несколько плоскостей и объедините плоскости формирования <ItemLink id="formation_plane" /> с плоскостями уничтожения <ItemLink id="annihilation_plane" />,
чтобы быстро ставить и ломать рудные блоки.

Шины импорта <ItemLink id="import_bus" /> набирают скорость постепенно, поэтому схема выйдет на полную производительность через несколько секунд.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/ore_fortuner.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 0 2" max="3 1 3">
        (1) Шина импорта. Установлено несколько карт ускорения.
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 2" max="2 1 2.3">
        (2) Плоскости формирования. Настройки по умолчанию.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 0.7" max="2 1 1">
        (3) Плоскости уничтожения. Настроек нет, требуется «Удача».
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 0 0" max="3 1 1">
        (4) Шина хранения. Настройки по умолчанию.
  </BoxAnnotation>

<DiamondAnnotation pos="3.5 0.5 2.5" color="#00ff00">
        Вход
    </DiamondAnnotation>

<DiamondAnnotation pos="3.5 0.5 0.5" color="#00ff00">
        Выход
    </DiamondAnnotation>

<DiamondAnnotation pos="4 0.5 1.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Настройки

*   В шине импорта <ItemLink id="import_bus" /> (1) установлено несколько карт <ItemLink id="speed_card" />. Чем больше плоскостей формирования в линии,
    тем больше карт нужно, чтобы забирать больше предметов за раз.
*   Плоскости формирования <ItemLink id="formation_plane" /> (2) используются с настройками по умолчанию.
*   Плоскости уничтожения <ItemLink id="annihilation_plane" /> (3) не имеют интерфейса настройки. Зачаруйте их на «Удачу».
*   Шина хранения <ItemLink id="storage_bus" /> (4) используется с настройками по умолчанию.

## Как это работает

1.  Шина импорта <ItemLink id="import_bus" /> зелёной подсети забирает блоки из первой бочки в [хранилище подсети](../ae2-mechanics/import-export-storage.md).
2.  Единственное хранилище зелёной подсети — плоскость формирования <ItemLink id="formation_plane" />. Она ставит блоки.
3.  Плоскость уничтожения <ItemLink id="annihilation_plane" /> оранжевой подсети ломает блоки с зачарованием «Удача».
4.  Шина хранения <ItemLink id="storage_bus" /> оранжевой подсети складывает добычу во вторую бочку.

---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: "МЭ-порт ввода-вывода"
  icon: io_port
  position: 210
categories:
- devices
item_ids:
- ae2:io_port
---

<a name="the-me-i/o-port" />

# МЭ-порт ввода-вывода

<BlockImage id="io_port" p:powered="true" scale="8" />

Порт ввода-вывода быстро переносит содержимое [ячеек хранения](../items-blocks-machines/storage_cells.md)
в [сетевое хранилище](../ae2-mechanics/import-export-storage.md) или обратно.

Чтобы повернуть блок, используйте <ItemLink id="certus_quartz_wrench" />.

<a name="settings" />

## Настройки

*   Укажите, когда переносить ячейку на выход: после опустошения, заполнения или окончания переноса.
*   <ItemLink id="redstone_card" /> открывает настройки сигнала красного камня.
*   Стрелка в центре окна задаёт направление: из ячейки в [сетевое хранилище](../ae2-mechanics/import-export-storage.md)
    или из хранилища в ячейку.

<a name="upgrades" />

## Улучшения

Порт ввода-вывода поддерживает следующие [улучшения](upgrade_cards.md):

*   <ItemLink id="speed_card" /> увеличивает количество ресурсов, перемещаемых за операцию.
*   <ItemLink id="redstone_card" /> даёт три режима управления: при наличии сигнала, без сигнала и один раз на импульс.

<a name="recipe" />

## Рецепт

<RecipeFor id="io_port" />

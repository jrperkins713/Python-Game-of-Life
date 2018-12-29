# The Game of Life #

## Introduction ##

**The Game of Life** is a cellular automation, which is basically a grid of cells and a set of rules
governing how the cells' values change over time. In particular, in
[Conway's Game of Life][game_of_life] there is a 2D grid, and the cells are *on* or *off*. A cell's
value is determined by it's neighbors: The eight cells adjacent and diagonal, also known as the
[Moore neighborhood][neighborhood]. The rules are simple:

  1. If a cell has fewer than two live neighbors, it dies (under-population)
  2. If a cell has two or three live neighbors, it lives on
  3. If a cell has more than three live neighbors, it dies (over-population)
  4. If a dead cell has exactly three live neighbors, it becomes alive (reproduction)

All rules are applied to all cells simultaneously. At each time step, the old grid
is frozen, and a new grid is calculated from the old grid.

## Instructions ##
* Click buttons on the grid to toggle them on or off
* Click the PLAY button to advance the grid one step
* Arrange cells in patterns to achieve interesting results
* Experiment!

## Screenshot ##
!["Gameplay Screenshot"](GameOfLifeGameplay.png?raw=true "Title")





[game_of_life]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
[neighborhood]: https://en.wikipedia.org/wiki/Moore_neighborhood
[glider]: https://en.wikipedia.org/wiki/Glider_%28Conway%27s_Life%29


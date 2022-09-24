import math
import random

"""
Maze Solver
First attempt to solve a maze. Will try to do BFS.

This program creates a representation of a maze by
creating an undirected graph
connecting nodes i and j if i is reachable from j and vice-versa
The representation is stored in an adjacency matrix of size n^2*n^2

TODO:
1. Generate a maze with atleast one possible solution
2. Implement BFS
3. Research more advanced solving algorithms
4. Benchmark and report
"""
# A solution is a list of nodes with startNode as the beginning and the endNode as the ending such that endNode is reachable from startNode
# An optimal solution is a solution that minimizes the path from startNode to endNode

class Maze():
  def __init__(self, n=3, connectedness=1):
    """
    n: number of rows = number of cols
    """
    self.n = n
    self.cells = self.n ** 2
    self.adj = [[0 for i in range(n**2)] for j in range(n**2)]
    self.connectedness = connectedness
    self.generateRandomMaze()

    # the percentage of connections in the maze.
    # connectedness = 1 => all cells reachable from all other
    # connectedness = 0 => no cell is reachable from any other

  def getBlock(self, block):
    output = []
    if block[0]:
      output.append(['***'])
      # print("***", end='')
    else:
      output.append(['* *'])
      # print("* *", end='')

    if block[1]:
      if block[3]:
        output.append(['* *'])
        # print('* *', end='')
      else:
        output.append(['  *'])
        # print('  *', end='')
    else:
      if block[3]:
        output.append(['*  '])
        # print('*  ', end='')
      else:
        output.append(['   '])
        # print('  ', end='')

    if block[2]:
      # print('***', end='')
      output.append(['***'])
    else:
      output.append(['* *'])
      # print('* *', end='')

    return output

  def printMaze(self):
    """
    read the adjacency matrix to print the nXn maze

    matrix keeps tracks of the four "walls" around a cell.
    True represents a wall.
    False represents absence of wall

    """

    # top, right, bottom, left
    matrix = [[True, True, True, True] for i in range(self.cells)]

    for i in range(self.cells):
      for j in range(self.cells):
        if self.adj[i][j] == 1:
          # cells i and j are connected
          row_i = i // self.cells
          col_i = i % self.cells

          row_j = j // self.cells
          col_j = j % self.cells


          # WARNING: potentially buggy code
          # this is the wall breaking code
          if row_i == row_j + 1 and col_i == col_j:
            matrix[i] = [False, True, True, True]
            matrix[j] = [True, True, True, False]

          elif row_i == row_j and col_i == col_j + 1:
            matrix[i] = [True, True, True, False]
            matrix[j] = [True, False, True, True]

    # prints a "block"
    # a "block" is an ASCII-equivalent of a cell with a star "*" missing for a passage / no-wall
    #
    for i in range(self.n):
      row = [[], [], []]
      for j in range(self.n):
        block = self.getBlock(matrix[i*self.n + j])
        row[0] = row[0] + block[0]
        row[1] = row[1] + block[1]
        row[2] = row[2] + block[2]
      for k in row:
        print(''.join(k))



    # for i in range(self.cells):
    #   for j in range(self.cells):
    #     print(self.adj[i][j], end='')
    #   print()

  def _isAdjacent(self, i, j):
    # WARNING: potentially buggy code
    row_i = i // self.cells
    col_i = i % self.cells

    row_j = j // self.cells
    col_j = j % self.cells

    if abs(row_i - row_j) > 1 or abs(col_i - col_j) > 1:
      return False
    return True

  def generateRandomMaze(self):
    """
    conveniently generate a random maze with atleast once certain solution
    """
    for i in range(self.n**2):
      for j in range(self.n**2):
        if self._isAdjacent(i, j):
          if random.random() <= self.connectedness:
            self.adj[i][j] = 1


def main():
  # n = int(input("Enter number of rows: "))
  maze = Maze()
  maze.printMaze()
  # print(
  #   m.getBlock([True, True, True, True])
  # )
  # print("done")
  # print(
  # m.getBlock([False, True, True, True])
  # )
  # print("done")
  # print(
  # m.getBlock([True, False, False, True])
  # )
  # print("done")

if __name__ == "__main__":
  main()
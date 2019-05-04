#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:01:25 2019

@author: dylan
"""
from Tile import Tile
import math

class Board:
    
    def __init__(self, difficulty, size):
        self.size = size
        self.tiles = []
        for i in range(size):
            self.tiles.append([Tile(difficulty, (i,j)) \
                               for j in range(size)])
        for i in range(self.size):
            for j in range(self.size):
                self.tiles[i][j].set_adjacent_mines(
                        self.__get_adjacent_mines(i,j))

    def __get_adjacent_mines(self, i, j):
        x_range = [x for x in range(i-1, i+2) if x >= 0 and x < self.size]
        y_range = [y for y in range(j-1, j+2) if y >= 0 and y < self.size]
        mines = 0
        for x in x_range:
            mines += sum([1 for y in y_range if self.tiles[x][y].is_mine and (
                    (i,j) != (x,y))])
        return mines
        
    def __str__(self):
        max_row_size = int(math.log10(self.size))
        top_legend = ' '.join([str(x) for x in range(1, self.size+1)])
        board_string = '+' + ' '*max_row_size + '| ' + top_legend +'\n'
        board_string += '-' + '-'*max_row_size + \
        '|' + '-'*(len(top_legend)+1) + '\n'
        for i, row in enumerate(self.tiles):
            row_size = int(math.log10(i+1))+1
            board_string += str(i+1)+ ' '*(max_row_size + 1 - row_size) + "| "
            for j, tile in enumerate(row):
                col_size = int(math.log10(j+1))+1
                if tile.is_revealed:
                    if tile.is_mine:
                        board_string += '*'*col_size
                    else:
                        board_string += str(tile.adjacent_mines) + \
                        ' '*(col_size-1)
                else:
                    if tile.is_marked:
                        board_string += '#'*col_size
                    else:
                        board_string +=  '~'*col_size
                board_string += ' '
            board_string += '\n'
        return board_string
                        



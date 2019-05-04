#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:30:34 2019

@author: dylan
"""
import random

class Tile:
    
    def __init__(self, difficulty, location):
        self.location = location
        self.is_revealed = False
        self.is_marked = False
        self.is_mine = random.random() < difficulty
        self.adjacent_mines = 0
    
    def get_location(self):
        return str(self.location[0]+1) + '-' + str(self.location[1]+1)
    
    def set_adjacent_mines(self, adjacent_mines):
        self.adjacent_mines = adjacent_mines
    
    def mark(self):
        if self.is_marked:
            return "This tile is already marked"
        if self.is_revealed:
            return f"Tile {self.get_location()} has already been mined"
        self.is_marked = True
        return f"You marked tile {self.get_location()}"
        
    def unmark(self):
        if not self.is_marked:
            return "This tile is not marked"
        if self.is_revealed:
            return f"Tile {self.get_location()} has already been mined"
        self.is_marked = False
        return f"You unmarked tile {self.get_location()}"
    
    def mine(self):
        if self.is_marked:
            return "You cannot mine a marked tile"
        if self.is_revealed:
            return f"Tile {self.get_location()} has already been mined"
        self.is_revealed = True
        if self.is_mine:
            return "You hit a mine! You lost"
        return f"You mined tile {self.get_location()}"
        
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:46:42 2019

@author: dylan
"""

from Board import Board
from collections import deque
    
class Minesweeper:
    
    __diff_dict = {'easy': .05, 'medium': .1, 'hard': .2}
    __diff_msg =  "Please enter your desired difficulty.\n" + \
        "Options are 'Easy', 'Medium', and 'Hard': "
    __size_dict = {'tiny': 5, 'small': 10, 'medium': 25, 'large': 50}
    __size_msg = "Please enter your desired minefield size.\n" + \
        "Options are 'Tiny', 'Small', 'Medium', and 'Large': "
    __bad_input_msg = "Please enter a valid input"
    
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.__new_game()
        
        
    def __new_game(self):
        print("Welcome to Minesweeper!", end='\n\n')
        self.game_over = False
        self.winner = None
        self.difficulty = self.__set_difficulty()
        self.board_size = self.__set_board_size()
        self.board = Board(self.difficulty, self.board_size)
        print("Let's get started!",end='\n\n')
        self.__help()
        while not self.game_over:
            self.__take_turn()
        self.__game_over_screen()
    
    def __game_over_screen(self):
        print(f"Thanks for playing. You have {self.wins} win" + \
              f"{'s' if self.wins != 1 else ''} and {self.losses} loss" + \
              f"{'es' if self.losses != 1 else ''}.\n\n")
        play_again = input(
                "Press Enter to play again or anything else to exit: ").lower()
        if play_again == '':
            self.__new_game()
    
    def __take_turn(self):
        user_input = input('What do you do?').lower()
        if user_input == 'help':
            self.__help()
            return
        user_input = user_input.split(' ')
        if len(user_input) != 2:
            print(Minesweeper.__bad_input_msg)
            return
        loc = self.__check_coords(user_input[1].split('-'))
        move = user_input[0]
        if loc == None:
            print(Minesweeper.__bad_input_msg)
            return
        if move == 'mark':
            print(self.board.tiles[loc[0]][loc[1]].mark(), end='\n\n')
        elif move == 'unmark':
            print(self.board.tiles[loc[0]][loc[1]].unmark(), end='\n\n')
        elif move != 'mine':
            print(Minesweeper.__bad_input_msg)
        else:
            mine = self.board.tiles[loc[0]][loc[1]].mine()
            if mine == "You hit a mine! You lost":
                self.losses += 1
                self.game_over = True
                self.winner = False
            elif mine == f"You mined tile {user_input[1]}":
                if self.board.tiles[loc[0]][loc[1]].adjacent_mines == 0:
                    self.__mine_adjacent_tiles(loc[0], loc[1])
                self.__check_win_condition()
            print(mine, end='\n\n')
        print(self.board, end='\n\n')
        if self.winner != None and self.winner:
            print("Congrats! You won!")
            
    
    def __mine_adjacent_tiles(self, i, j):
        stack = deque()
        x_range = [x for x in range(
                i-1, i+2) if x >= 0 and x < self.board_size]
        y_range = [y for y in range(
                j-1, j+2) if y >= 0 and y < self.board_size]
        for x in x_range:
            for y in y_range:
                if not self.board.tiles[x][y].is_revealed:
                    stack.append(self.board.tiles[x][y])
        for tile in stack:
            tile.mine()
            if tile.adjacent_mines == 0:
                self.__mine_adjacent_tiles(
                        tile.location[0], tile.location[1])
                
    def __check_win_condition(self):
        win = True
        for row in self.board.tiles:
            for tile in row:
                if not (tile.is_mine or tile.is_revealed):
                    win = False
        if win:
            self.game_over = True
            self.winner = True
            self.wins += 1
                
        
    def __check_coords(self, coords):
        if len(coords) != 2:
            return None
        try:
            coordinates = (int(coords[0])-1, int(coords[1])-1)
            for coord in coordinates:
                if coord < 0 or coord >= self.board_size:
                    return None
        except:
            return None
        return coordinates
    
      
    def __help(self):
        print("Coordinates start at 1-1 in the top left " + \
              f"corner and go to {self.board_size}-{self.board_size} in " + \
              "the bottom right.\nYour possible moves are 'Mine', 'Mark', " + \
              "'Unmark' and 'Help'.\nTo complete a move, type <Move> " + \
              "<Coordinate>.\nFor example 'Mine 3-4' will mine the tile " + \
              "3rd from the top and 4th from the left.\nType 'Help' to " + \
              "see this again.", end='\n\n')
        
        
    def __set_difficulty(self):
        return self.__set_parameter_by_input(
                Minesweeper.__diff_dict, Minesweeper.__diff_msg)
        
    
    def __set_board_size(self):
        return self.__set_parameter_by_input(
                Minesweeper.__size_dict, Minesweeper.__size_msg)
         
    
    def __set_parameter_by_input(
            self, valid_values, message, user_input='', bad_input=False):
        if user_input in valid_values:
            return valid_values[user_input]
        if bad_input:
            print(Minesweeper.__bad_input_msg)
        user_input = input(message).lower()
        return self.__set_parameter_by_input(
                valid_values, message, user_input, True)
    
def main():
    Minesweeper()
    
if __name__ == '__main__':
    main()
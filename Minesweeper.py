#!/usr/bin/env python
# coding: utf-8

# In[59]:


# Installs
import numpy as np
import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows=10, columns=10, mines=10): 
        self.master = master 
        self.rows = rows 
        self.columns = columns  
        self.mines = mines  # Number of mines in the grid.
        self.buttons = []  # Initializes a list to hold button widgets.
        self.mine_locations = []  # Initialize a list to store mine locations.
        self.create_tiles()  # Creates the grid of buttons.
        self.place_mines()  # Places mines on the grids
        
    def create_tiles(self):
        for r in range(self.rows):
            row_tiles = []
            for c in range(self.columns):
                button = tk.Button(self.master, width=2, height=1, command=lambda r=r, c=c: self.reveal_tile(r, c))
                # Create a button widget, set its size, and bind it to the reveal_cell function.
                button.grid(row=r, column=c)  # Place the button on the grid.
                button.bind("<Button-3>", self.on_right_click)
                row_tiles.append(button)  # Add the button
            self.buttons.append(row_tiles)
            
    # Places mines on start-up
    def place_mines(self):
        while len(self.mine_locations) < self.mines:
            r = random.randint(0, self.rows - 1) 
            c = random.randint(0, self.columns - 1)  

            # No duplicate mine locations
            if (r, c) not in self.mine_locations:
                self.mine_locations.append((r, c))  # Add the mine location to the list.
                #self.buttons[r][c].config(text="M")  # For testing: shows where mines are placed
                
    # returns number of surrounding mines            
    def surrounding_mines(self, r, c):
        surrounding_tiles = [(r-1, c-1), (r-1, c), (r-1, c+1),
                            (r, c-1),           (r, c+1),
                            (r+1, c-1), (r+1, c), (r+1, c+1)]
        number = 0
        
        for tile in surrounding_tiles:
            tr, tc = tile  # Unpack the row and column indices
            if 0 <= tr < self.rows and 0 <= tc < self.columns:  # Ensures the tile is within the grid boundaries
                if (tr, tc) in self.mine_locations:  # Check if this tile is a mine
                    number += 1  # Increment the count if it's a mine

        return number
    
    # reveals the tile when you click it
    def reveal_tile(self, r, c):
        # If there is a mine
        if(r, c) in self.mine_locations:
            self.buttons[r][c].config(text='*', bg='red')
            self.game_over()
            
        # If there isn't a mine, checks if it's in the range and it wasn't already revealed
        elif r in range (0, 10) and c in range(0, 10) and self.buttons[r][c].cget('state') == 'normal':
            if self.surrounding_mines(r, c) == 0:
                self.buttons[r][c].config(text=self.surrounding_mines(r, c), state='disabled')
                self.reveal_zeros_area(r, c)
            
            else:
                self.buttons[r][c].config(text=self.surrounding_mines(r, c), state='disabled')
    
    # In real minesweeper, if you click a zero then all of the surrounding area is revealed, this creates a recursive
    # loop that reveals all tiles until the first surrounding non zero is hit
    def reveal_zeros_area(self, r, c):
        # Row 1 in surrounding error
        self.reveal_tile(r-1,c-1)
        self.reveal_tile(r-1, c)
        self.reveal_tile(r-1, c+1)
        # Row 2 in surrounding error
        self.reveal_tile(r, c-1)
        self.reveal_tile(r, c+1)
        # Row 3 in surrounding error
        self.reveal_tile(r+1, c-1)
        self.reveal_tile(r+1, c)
        self.reveal_tile(r+1, c+1)
    
    # Turns button blue on right click, acts as a flag like in the real game
    def on_right_click(self, event):
        button = event.widget
        if button.cget('state') == "disabled":
            button.config(state='normal', bg='#F0F0F0')
        elif button.cget('state') == 'normal':
            button.config(state='disabled', bg="blue")
            
    def game_over(self):
        for(r, c) in self.mine_locations:
            self.buttons[r][c].config(text='*', bg='red')
        print("Game Over!") # Game over printed

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window.
    game = Minesweeper(root, rows=10, columns=10, mines=10)  # Initializes the Minesweeper game. master = root
    root.mainloop()  # Start the Tkinter event loop.


# In[ ]:





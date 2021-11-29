# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:35:40 2021

@author: Evan Benitez
"""

test_matrix = [
    [0,3,2,5,4,7,6,9,8],
    [3,0,1,2,3,4,5,6,7],
    [2,1,0,3,2,5,4,7,6],
    [5,2,3,0,1,2,3,4,5],
    [4,3,2,1,0,3,2,5,4],
    [7,4,5,2,3,0,1,2,3],
    [6,5,4,3,2,1,0,3,2],
    [9,6,7,4,5,2,3,0,1],
    [8,7,6,5,4,3,2,1,0]
    ]

out_matrix = []

# return the proper value of surrounding pixel based on placement relative to main pixel
def Pixel_Val(rel_val, rel_row, rel_col):
    # return 0 for lest than zero values
    if rel_val < 0:
        return 0
    
    if rel_row > 0:
        if rel_col == -1:
            return 32
        if rel_col == 0:
            return 64
        else:
            return 128
        
    if rel_row == 0:
        if rel_col == -1:
            return 16
        else:
            return 1
        
    else:
        if rel_col == -1:
            return 8
        if rel_col == 0:
            return 4
        else:
            return 2
        

if __name__ == "__main__":
    row_max = len(test_matrix) - 1
    
    # go through ever row of matrix
    for row in range(len(test_matrix)):
        col_max = len(test_matrix[row]) - 1
        list_row = []
        
        # go through every column in each row
        for col in range(len(test_matrix[row])):
            code_value = 0
            
            # cycle through adjacent neighbors
            for r in range(row - 1, row + 2):
                adjusted_r = r
                
                # adjust for out of bounds using mirroring
                if r < 0:
                    adjusted_r = 1
                elif r > row_max:
                    adjusted_r = row_max - 1
                        
                for c in range(col + 1, col - 2, -1):
                    
                    # skip if central element
                    if r == row and c == col:
                        continue
                    adjusted_c = c
                    
                    # adjust for out of bounds using mirroring
                    if c < 0:
                        adjusted_c = 1
                    elif c > col_max:
                        adjusted_c = col_max - 1
                    
                    val = test_matrix[adjusted_r][adjusted_c]
                            
                    code_value += Pixel_Val(val - test_matrix[row][col], r - row, c - col)
                    
            # add to new list_row
            list_row.append(code_value)
            
        # add to out_matrix
        out_matrix.append(list_row)
        
    # print new matrix
    print(out_matrix)
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:43:51 2021

@author: Evan Benitez
"""

import sys

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

def Code(matrix):
    out_matrix = []
    row_max = len(matrix) - 1
    
    # go through ever row of matrix
    for row in range(len(matrix)):
        col_max = len(matrix[row]) - 1
        list_row = []
        
        # go through every column in each row
        for col in range(len(matrix[row])):
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
                    
                    val = matrix[adjusted_r][adjusted_c]
                            
                    code_value += Pixel_Val(val - matrix[row][col], r - row, c - col)
                    
            # add to new list_row
            list_row.append(code_value)
            
        # add to out_matrix
        out_matrix.append(list_row)
        
    return out_matrix

def Check_Row_Size(matrix):
    if len(matrix) > 1:
        for i in range(len(matrix)):
            if len(matrix) - 1 <= i:
                return True
            if len(matrix[i]) != len(matrix[i+1]):
                return False
    return True
        

# test function
if __name__ == "__main__":
    print("Enter your 2D matrix (all rows must be the same size):")
    row_count = 1;
    entry = "start"
    input_matrix = []
    while entry != "":
        entry = input("enter row " + str(row_count) + " (leave empty when finish): ")
        if entry != "":
            row_count += 1
            parse = entry.split()
            parse = [int(num) for num in parse]
            input_matrix.append(parse)
            if not Check_Row_Size(input_matrix):
                print("Row are not the same size")
                sys.exit()
    print(Code(input_matrix))
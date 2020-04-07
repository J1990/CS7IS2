import sys
from PIL import Image
import pandas as pd

data = pd.read_csv("input.csv", header=None)

rows, columns = 2, 2
width, height = 28, 28

total_width = columns * width
max_height = rows * height

new_im = Image.new('RGB', (total_width, max_height))

y_offset = 0
filename=''
for rowNumber in range(0, rows):
    x_offset = 0
    for columnNumber in range(0, columns):
        imageNum = str(data.at[rowNumber, columnNumber])
        filename = filename + imageNum
        im = Image.open(('mnist/' + imageNum + '.jpg'))        
        new_im.paste(im, (x_offset,y_offset))
        x_offset += width
    
    y_offset += height

new_im.save(filename+'.jpg')
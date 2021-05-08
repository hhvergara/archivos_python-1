import csv
import re

with open (r'C:\Users\Francisco Pch\Desktop\Python\inove\Curso 1 Inove\unidad_5\archivos_python-master\propiedades.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        col_amb = 0
        print(reader[9])
        
        
        
       # for row in reader:
       #     col_amb = int(row['ambientes'])
       # print (col_amb)


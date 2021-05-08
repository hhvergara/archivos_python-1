import csv


with open (r'C:\Users\Francisco Pch\Desktop\Python\inove\Curso 1 Inove\unidad_5\archivos_python-master\stock.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['tornillos'], row['arandelas'])

print(row)



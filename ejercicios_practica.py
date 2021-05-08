#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

import csv
import re


def ej1():
    print('Ejercicios con diccionarios \n')
    print ("Ejercicio 1:\n")
    # Crear un diccionario vacio que luego completaremos
    # con el stock de elementos de ferreteris
    # el diccionario vacio debe llamarse "stock"

    stock = {"tornillos": 300, "tuercas": 150, "arandelas":300}
    print (stock,"\n")

    print ("_______________________________________\n")

    # stock = ....

    # Luego de crear el diccionario completelo
    # con el siguiente stock:
    # tornillos = 100
    # tuercas = 150
    # arandelas = 300

    # Los nombres tornillos, tuercas y arandelas
    # son las claves (keys) del diccionario
    # mientras que las cantidades son los valores (values)

    # Una vez armado el diccionario imprimirlo en pantalla con print


def ej2():
    print('Ejercicio con diccionarios \n')
    print ("Ejercicio 2:\n")

    # Basado en el ejemplo anterior, deseamos tener un stock mes a mes
    # de los items tornillos, tuerca y arandelas.

    # Crear un diccionario por cada mes, cada diccionario se llamara "mes"
    # Cada uno que se genere debe tener los tres campos
    # tornillos, tuerca y arandelas y su respectivo stock
    # # Cada diccionario deberá almacenarse en una lista llamada stock

    

    # Paso 1:
    # Generar un bucle de 3 iteraciones, solo generaremos el stock de
    # tres meses ok

    # Paso 2:
    # En cada iteracion del bucle solicitar por consola cuando
    # stock se desea informar de cada uno de los 3 elementos ok

    # Paso 3:
    # Generar un diccionar llamado "mes" con los tres valores
    # de stock ingresados por consola

    # Paso 4:
    # Almacenar ese diccionario generado en una lista
    # llamada "stock"

    # Paso 5:
    # Repetir el proceso nuevamente en la siguiente
    # iteracion del bucle
    # Cuando finalice el bucle su lista debera contener los tres
    # diccionarios almacenados.

    # Paso 6:
    # Imprimir en pantalla el resultado, deberá verse como
    # el siguiente ejemplo:

    # [{'tornillos': 30, 'tuercas': 20, 'arandelas': 5}, {'tornillos': 100, 'tuercas': 50, 'arandelas': 15}, {'tornillos': 80, 'tuercas': 70, 'arandelas': 10}]

    # NOTA: Este ejercicio es exactamente lo mismo que armar
    # el edificio viste en clase, con los departamentos por piso
    # pero los valores para cada diccionario en cada mes
    # son ingresados por consola

    meses = ["enero", "febrero", "marzo"]
    for i in meses:
        mes_stock= input("Ingresa el mes que deseas cargar stock")
        
        if mes_stock in meses:
            tornillos = input ("Idique el stock de tornillos segun el mes:") 
            arandelas = input ("Idique el stock de arandelas segun el mes:")
            tuercas = input ("Idique el stock de tuercas segun el mes:")
            mes_ingresado = (mes_stock)
            stock_mes = {"tornillos":(tornillos), "arandelas":(arandelas), "tuercas":(tuercas)}
            print("El stock correspondiente al mes de",mes_ingresado, "es de", stock_mes,"\n") # En esta linea tendrías que hacer un append del diccionario
            # a una lista para obtener la lista de diccionarios:
            #  [{'tornillos': 30, 'tuercas': 20, 'arandelas': 5}, {'tornillos': 100, 'tuercas': 50, 'arandelas': 15}, {'tornillos': 80, 'tuercas': 70, 'arandelas': 10}]
            # Y luego, fuera del bucle hacer el print de los 3. Me gustó el  detalle de los meses!
            
        else:
            print("El mes ingresado no es valido")
    print ("_______________________________________\n") # Recordá que en el print no hace falta el \n, ya viene por defecto!
    

def ej3():
    print('Ejercicio de archivos CSV \n')
    print ("Ejercicio 3:\n")

    '''
    Realice un programa que abra el archivo 'stock.csv'
    y cuente el stock total de tornillos a lo largo
    de todo el archivo, sumando el stock en cada
    fila del archivo
    '''
    with open (r'C:\Users\Francisco Pch\Desktop\Python\inove\Curso 1 Inove\unidad_5\archivos_python-master\stock.csv', newline='') as csvfile:
        # Para que no tengas que poner toda la ruta, abrí el visual studio code en la carpeta donde está el .csv :D
        reader = csv.DictReader(csvfile)
        col_tor = 0
        for row in reader:
            col_tor += int(row['tornillos'])
        print ("El total de tornillos en la matriz es:", col_tor,'\n')

    print ("_______________________________________\n")



def ej4():
    print('Ejercicios con archivos CSV \n')
    print ("Ejercicio 4:\n")
    
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    with open (r'C:\Users\Francisco Pch\Desktop\Python\inove\Curso 1 Inove\unidad_5\archivos_python-master\propiedades.csv', newline='') as csvfile:
        # Para que no tengas que poner toda la ruta, abrí el visual studio code en la carpeta donde está el .csv :D

        reader = csv.DictReader(csvfile)
        reader = list(reader)
        filas = len(reader)
        columnas = len(reader[0])
        
        #para conocer el largo de filas y columnas#
        print ("El archivo tiene", filas,"filas y tiene", columnas, "columnas \n")

        
        # para conocer los titulos de las comlumnas#
        print(" Los titulos de las columnas son:")
        columnas = (reader[0])
        for col in columnas:
            columnas = (col)
            print(columnas, '\n')
        

        # para resolver el ejercicio#
        
        col_ambi_2 = 0
        col_ambi_3 = 0

        for i in range (len(reader)):
            columna = reader[i]
            for k, v in columna.items():
                if (k=='ambientes') and (v == "2"):
                    col_ambi_2 += 1
                if (k=='ambientes') and (v == "3"):
                    col_ambi_3 += 1
        print ("La cantidad de departamentos con 3 ambientes es:",col_ambi_2, "\n")
        print ("La cantidad de departamentos con 3 ambientes es:",col_ambi_3, "\n")
            




if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()

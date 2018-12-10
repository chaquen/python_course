#encoding: utf-8
import os, sys

print("EJEMPLO DE FUNCIONALIDAD DE FUNCION JOIN QUE SIRVE PARA UNIR UNA CADENA DE TEXTO POR ALGUN CARACTER EN ESPECIAL JOIN")
lista_de_libros=["señor de los anillos","ensayo sobre la ceguera","el tunel","sobre heroes y tumbas"]
lista_de_libros_2=["el médico","los karamasov","it","el resplandor","el cerebro y el mito del yo entre otros."];

print("Mis libros favoritos son: "+", ".join(lista_de_libros)+"y aún hay más "+", ".join(lista_de_libros_2))

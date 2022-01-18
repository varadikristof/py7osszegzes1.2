'''
1.2 Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!

A program csak a páros számokat adja össze!
'''
import random 

lista = [random.randint(1,10) for _ in range(5)]

osszeg = 0
for szam in lista:
  if szam % 2 == 0:
     osszeg += szam
print(osszeg,lista)
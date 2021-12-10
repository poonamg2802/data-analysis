# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:21:46 2021

@author: DELL
"""
hindi=int(input ("Enter the mark of Hindi"))
eng=int(input ("enter the mark of English"))
math=int (input("Ener the mark of Maths"))
Sci=int (input("Enter the mark of Science "))
comp=int(input("Enter the mark of Computer"))
total= (hindi + eng + math + Sci + comp)
print("Total marks of 5 subject is Total")
per=(total*100)/500
print("Pecentage is",per)
if hindi>=33 and eng>=33 and math>=33 and Sci>=33 and comp>=33:
    print("Student is Pass")
else:
    print ("Student is Fail")

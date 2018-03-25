# coding=utf-8
'''
Created on 2 март. 2018 г.
@author: Dim
'''
import functions

print('ITIB Laboratory work #1. Investigation of single-layer neural networks by example Simulation of boolean expressions Var0')

for inc in range(2):
    #print('AF ', inc + 1 , ': ')
    if inc==0: print('Threshold activation function')
    else: print('Logical activation function')
    af = inc
    functions.learning(inc)
    print('________________________________________________')

print('Learning on min sets: ')
functions.learning_sets()
print('________________________________________________')
#!/usr/bin/env python
"""
Name: Michael Anthony Borchardt
Date Created: 3-29-23
File: gpacalc.py
"""
class gpacalc(object):
    def __init__(self, numOfValues):
        self.__numOfValues = numOfValues
    def getNumOfValues(self):
        return self.__numOfValues
    def setNumOfValues(self, numOfValues):
        self.__numOfValues = numOfValues
        print('Number of values:',self.__numOfValues)
    def welcome(self):
        print(format('-','-<20'), ' Welcome to GPA Calculator ', format('-','->20'))
        print('What you need to know:\n1. How many GPA values you have.' \
              ,'\n2. The GPA score of each value.')
    def promptForNumOfValues(self):
        inputOne = int(input('Enter number of values: '))
        return inputOne
    def calculateGPA(self, numOfValues):
        gpaList = []
        value = 0
        while numOfValues > 0:
            inputOne = float(input('Enter GPA: '))
            gpaList.append(inputOne)
            print('GPA: ', inputOne, ' -- Entered into record -- ')
            numOfValues -= 1
        for index in gpaList:
            value += index
        print('Overall GPA: ', value/len(gpaList))
            
            
            
obj = gpacalc(5)
obj.welcome()
obj.setNumOfValues(obj.promptForNumOfValues())
obj.calculateGPA(obj.getNumOfValues())



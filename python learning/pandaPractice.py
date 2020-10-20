# student_details = {
#     "name" : ["Minhaz","Lipon","Sayem","Rumman"],
#     #"course_taken" :["Machine Learning","Data Mining","Fuzzy","SQA"],
#     "machine learning":[4,3,3.3,4],
#     "Data Mining":[4,2.75,2.5,3.75],
#     "Fuzzy":[4,3,3.3,4],
#     "SQA":[4,4,3.0,3.3]
    
#     }
# student_details["CGPA"] = []

# i = 0
# for result in student_details["name"]:
#     student_details["CGPA"].append( (student_details["machine learning"][i]*3
#     +student_details["Data Mining"][i]*3
#     +student_details["Fuzzy"][i]*3
#     +student_details["SQA"][i]*3)/12 )
#     i+=1
# #student_details["CGPA"] =int(student_details.get("Data Mining"))*3

import pandas as pd

# brick = pd.DataFrame(student_details)
# print(brick)

# covid = pd.read_csv('./covid data set/worldometers_snapshots_April18_to_August1.csv')
# print(covid.columns)
# print(covid[['Date','Country','Total Deaths']])

# import random

# def lotary():
#     for i in range(5):
#         yield random.randint(10, 150)

# for randomNumber in lotary():
#     print(randomNumber)

#1 1 2 3 5
# def getFibonacci(n):
#     a = 1
#     b = 1
#     for i in range(1,n):
#         #print(i)
#         if i<3:
#             yield 1
#         else:
#             yield (a+b)
#             a,b = b,(a+b)

# for value in getFibonacci(5):
#     print(value)
# import types       
# if type(getFibonacci(1)) == types.GeneratorType:
#     print("OK")

# List practice:

# sentence = "Rashed sir is a very strict person"
# words = sentence.split()
# word_length = []
# for word in words:
#     if word!='is':
#         word_length.append(len(word))

# print(word_length)

# integer_numbers = [10,-5,10,-5,6,7,8]
# positive_integers = []
# print("All numbers",integer_numbers)
# for number in integer_numbers:
#     if number>-1:
#         positive_integers.append(number)
# print("Integer Numbers",positive_integers)

# Any number of Argument

# def functionWithVariableArgument(a,b,**options):
#     if options.get("action") == "sum":
#                 return a+b
#     if options.get("action") == "subtract":
#         return a-b

# print(functionWithVariableArgument(1, 2, action ="sum"))

# Exception Handling

# student = {"name":"Abdul Motaleb", "Dept":"CSE"}

# def getLastName():
#     words = student["name"].split()
#     try:
#         print(words[-1])
#     Exception(IndexError(args)):
#         print("Index out of bound error")
# getLastName()

#-- sets: list without duplicate value if we write any duplicate value it will 
# appear once only--

# departments = set(["IT","CSE","IT"])
# print(departments)

#-- JSON in python
# There are two basic format of JSON data one is string and another is object 
# Data strcutures ---

# import pickle

# pickled_string = pickle.dumps([1,2,3,'a',"string element"])
# print(pickle.loads(pickled_string))

#-- PARTIAL FUNCTION -- 

# from functools import partial

# def func(u,v,w,x):
#     return  u*4 + v*3 + w*2 + x
# partial_function = partial(func,5,5,5)

# print(partial_function(15)) #this argument is for last parameter
 
# -- Code Introspection --
# class Student:
#     name = ""
#     id = 123
#     def getDetails(self,name):
#         self.name = name
#         print(self.name,self.id)
# AML = Student()
# AML.getDetails("Abdul Motaleb")
# print(dir(Student))

#--Clousers--

# def outerFunction(message):
   
#     #self.message = message
#     def innerFunction():
#         #print(message)
#         nonlocal message
#         message = "Salam"
#         print(message)
#     innerFunction()

# outerFunction("Assalamualaikum")


def outerFunction(message):
   
    #self.message = message
    def innerFunction():
        #print(message)
        nonlocal message
        message = "Salam"
        print(message)
    return innerFunction

ref_fun = outerFunction("Assalamualaikum")

ref_fun()
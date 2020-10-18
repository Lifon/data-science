student_details = {
    "name" : ["Minhaz","Lipon","Sayem","Rumman"],
    #"course_taken" :["Machine Learning","Data Mining","Fuzzy","SQA"],
    "machine learning":[4,3,3.3,4],
    "Data Mining":[4,2.75,2.5,3.75],
    "Fuzzy":[4,3,3.3,4],
    "SQA":[4,4,3.0,3.3]
    
    }
student_details["CGPA"] = []

i = 0
for result in student_details["name"]:
    student_details["CGPA"].append( (student_details["machine learning"][i]*3
    +student_details["Data Mining"][i]*3
    +student_details["Fuzzy"][i]*3
    +student_details["SQA"][i]*3)/12 )
    i+=1
#student_details["CGPA"] =int(student_details.get("Data Mining"))*3

import pandas as pd

brick = pd.DataFrame(student_details)
print(brick)
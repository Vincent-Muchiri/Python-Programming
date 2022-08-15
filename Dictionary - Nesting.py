#Nesting a list in a dictoinary
import random

travel_log = {
    "Kenya" : ["Nairobi", "Mombasa", "Kisumu"],
    "South Africa": ["Durban", "Joburg", "Cape Town"]
}

#Nesting a dictionary inside another dictionary
cities_visited = {
    "Kenya": "Naivasha",
    "South Africa": "Pritoria"
}
travel_log = {
    "Kenya" : ["Nairobi", "Mombasa", "Kisumu"],
    "South Africa": ["Durban", "Joburg", "Cape Town"],
    "cities_visited" : cities_visited
}

# print(travel_log)

#Nesting a dictionary inside a list
travel_log = [
    {
        "country" : "Kenya",
        "cities_visited" : ["Nairobi", "Mombasa", "Kisumu"],
        "no_of_visits" : 12
    },
    {
        "country": "South Africa",
        "cities_visited": ["Durban", "Joburg", "Cape Town"],
        "no_of_visits" : 12
    }
]

#Adding new entries
def add_new_country (country, times_visited, cities_visited): 
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["no_of_visits"] = times_visited
    
    # travel_log.append(new_country)
    travel_log[-1] = new_country


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# print(travel_log[0]["country"])

class_list = ["North", "East", "West", "South"]
student_list = ["Vincent", "Diana", "Siz"]
subjects = ["Math", "English", "Kiswahili", "Science", "Social Studies", "C.R.E"]

class_name = ""
student_name = ""

# class_marks = {}

class_marks = {
    class_name: {
        student_name: {
            "Math": 0.0,
            "English": 0.0,
            "Kiswahili": 0.0,
            "Science": 0.0,
            "Social studies": 0.0,
            "C.R.E.": 0.0
        }
    }
}

for classes in class_list:
    class_name = classes
    for student in student_list:
        student_name = student
        # class_marks = {
        #     class_name: {
        #         student_name: {
        #             "Math": 0.0,
        #             "English": 0.0,
        #             "Kiswahili": 0.0,
        #             "Science": 0.0,
        #             "Social studies": 0.0,
        #             "C.R.E.": 0.0
        #         }
        #     }
        # }

        # class_marks[class_name][student_name]['Math'] = random.randint(0, 100)
        # class_marks[class_name][student_name]['English'] = random.randint(0, 100)
        # class_marks[class_name][student_name]['Kiswahili'] = random.randint(0, 100)
        # class_marks[class_name][student_name]['Science'] = random.randint(0, 100)
        # class_marks[class_name][student_name]['Social Studies'] = random.randint(0, 100)
        # class_marks[class_name][student_name]['C.R.E.'] = random.randint(0, 100)

# print(class_marks)

class_list = ['North', 'East', 'West']
teacher_list = ['Elon', 'Amber', 'Johnny']
prefect_list = ['Musk', 'Heard', 'Depp']
student_list = ['Student1', 'Student2', 'Student3','Student4', 'Student5']
subjects = ['Math', 'English', 'Science']
grade = random.randint(0, 100)
# Use this dict and loops through the above lists to create a subject dict nested inside a student dict,
# nested inside a class dict
class_dict = {
    'Class Name': class_name,
    'Class Teacher': class_teacher,
    'Class Prefect': class_prefect,
    'Students': {
        student_name: {
            subject: grade
        }
    }
}
# Output
sadfsaf = {
    {
        'Class Name': class_name,
        'Class Teacher': class_teacher,
        'Class Prefect': class_prefect,
        'Students': {
            student1: {
                subject: grade,
                subject2: grade2,
                subject3: grade3
            },
            student2: {
                subject: grade,
                subject2: grade2,
                subject3: grade3
            },
            student3: {
                subject: grade,
                subject2: grade2,
                subject3: grade3
            }
        }
    },
    {
        'Class Name': class_name,
        'Class Teacher': class_teacher,
        'Class Prefect': class_prefect,
        'Students': {
            student1: {
                subject: grade,
                subject2: grade2,
                subject3: grade3
            },
            student2: {
                subject: grade,
                subject2: grade2,
                subject3: grade3
            },
            student3: {
                subject: grade,
                subject2: grade2,
                subject3: grade3
            }
        }
    }
}
# (p4.py) The dictionary contains the names of subjects and the grades obtained. 
# Create a function f(subjects) that, for the given subjects and their grades, returns the name of the subject for which the average grade is the highest. 
# Example:
# f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) -> "comp"

def f(subjects):
    highest_avarage_grade = 0.0
    highest_avarage_subject = None

    for subject, grades in subjects.items():
        avarage_grade = sum(grades)/len(grades) if len(grades) > 0 else 0.0

        if avarage_grade > highest_avarage_grade:
            highest_avarage_grade = avarage_grade
            highest_avarage_subject = subject

    return highest_avarage_subject



if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
    print(f({"math":[3,4,4],"pe":[5,4,5],"it":[5,4,3]}))
    print(f({"chem":[6,6,6],"eng":[5,4,4,4],"comp":[5,4]}))
    
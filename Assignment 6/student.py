#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:
    def __init__(self, name, student_id, year, major, gpa):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.gpa = gpa

    def honors(self):
        if self.gpa > 3.5:
            return True
        else:
            return False

    def food_raffle(self):
        import random
        rand_id = random.randrange(1111,9999)
        if self.student_id == rand_id:
            return("winner! student (name) gets free lunch!")
        else:
            return("Looooser!")
    

def main():
    #create three students and check if they get free lunch and if they qualify for honors
    student1 = student("Amanda", 4567, "sophomore", "computer science", 4.0)
    student2 = student("Liz", 2983, "sophomore", "psychology", 3.2)
    student3 = student("Maddy", 3498, "sophomore", "cybersecurity", 3.5)

    #prints whether each student wins free lunch
    print("Did you win the food raffle?")
    print(student1.name, str(student1.food_raffle()))
    print(student2.name, str(student2.food_raffle()))
    print(student3.name, str(student3.food_raffle()))

    #prints whether students 1,2, and 3 are eligible for honors
    print("\nAre you eligible for honors?")
    print(student1.name, str(student1.honors()))
    print(student2.name, str(student2.honors()))
    print(student3.name, str(student3.honors()))
    
main()

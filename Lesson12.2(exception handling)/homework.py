def get_grade(number):
    while True:
        try:
            grade = float(input(f"Grade {number}: ")) #hello
            if grade < 0 or grade > 100:
                raise ValueError
            return grade
        except ValueError:
            print("Enter a number between 0 and 100.")
        except:
            print("Something went wrong!")
 
 
def calculate_average(grades):
    return sum(grades) / len(grades)
 
 
def main():
    name = input("Student name: ")
    grades = [get_grade(i) for i in range(1, 4)]
    print(f"{name}: average {calculate_average(grades):.2f}")
 
 
main()
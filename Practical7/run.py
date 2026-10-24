
# Import classes from our package
from staff_app import Department, Developer


def main():

    # Create a department
    engineering = Department("Engineering")

    # Create a developer object
    dev = Developer("Riya", "EMP101", engineering, "Python")

    # Set the developer's salary
    dev.salary = 65000

    # Display developer details
    print(dev.describe())
    print("Salary:", dev.salary)

    # Test invalid salary
    try:
        dev.salary = -100
    except ValueError as error:
        print("Validation:", error)


# Run the program
if __name__ == "__main__":
    main()

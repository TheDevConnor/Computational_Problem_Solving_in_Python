def letter_to_number(letter_grade):
    grade_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    
    letter_grade = letter_grade.upper().strip()
    return grade_scale.get(letter_grade)


def find_lowest_grade(grades):
    return min(grades)


def calculate_average(grades):
    return sum(grades) / len(grades)


def number_to_letter(number_grade):
    if number_grade >= 4.0:
        return 'A'
    elif number_grade >= 3.0:
        return 'B'
    elif number_grade >= 2.0:
        return 'C'
    elif number_grade >= 1.0:
        return 'D'
    else:
        return 'F'


def get_valid_grade(prompt):
    valid_grades = ['A', 'B', 'C', 'D', 'F']
    while True:
        grade = input(prompt).upper().strip()
        if grade in valid_grades:
            return grade
        else:
            print(f"Invalid grade. Please enter A, B, C, D, or F.")


def main():
    print("=" * 50)
    print("Grade Calculator - Enter 4 Letter Grades")
    print("=" * 50)
    
    # Collect 4 letter grades from user
    letter_grades = []
    for i in range(1, 5):
        grade = get_valid_grade(f"Enter grade {i} (A, B, C, D, F): ")
        letter_grades.append(grade)
    
    # Convert letter grades to numerical values
    numerical_grades = [letter_to_number(grade) for grade in letter_grades]
    
    # Calculate lowest grade and average
    lowest_grade = find_lowest_grade(numerical_grades)
    average_grade = calculate_average(numerical_grades)
    
    # Convert back to letter grades for display
    lowest_letter = number_to_letter(lowest_grade)
    average_letter = number_to_letter(average_grade)
    
    # Display results
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"Grades entered: {', '.join(letter_grades)}")
    print(f"Numerical values: {numerical_grades}")
    print(f"\nLowest grade: {lowest_letter} ({lowest_grade})")
    print(f"Average grade: {average_letter} ({average_grade:.2f})")
    print("=" * 50)


if __name__ == "__main__":
    main()

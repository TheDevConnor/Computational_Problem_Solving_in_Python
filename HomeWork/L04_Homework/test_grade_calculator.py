from grade_calculator import (
    letter_to_number,
    number_to_letter,
    find_lowest_grade,
    calculate_average
)


def test_letter_to_number():
    print("Testing letter_to_number():")
    test_cases = ['A', 'B', 'C', 'D', 'F']
    for grade in test_cases:
        result = letter_to_number(grade)
        print(f"  {grade} -> {result}")
    print()


def test_number_to_letter():
    print("Testing number_to_letter():")
    test_cases = [4.0, 3.0, 2.0, 1.0, 0.0, 3.5, 2.5]
    for grade in test_cases:
        result = number_to_letter(grade)
        print(f"  {grade} -> {result}")
    print()


def test_find_lowest():
    print("Testing find_lowest_grade():")
    test_grades = [4.0, 3.0, 2.0, 3.0]
    lowest = find_lowest_grade(test_grades)
    print(f"  Grades: {test_grades}")
    print(f"  Lowest: {lowest}")
    print()


def test_calculate_average():
    print("Testing calculate_average():")
    test_grades = [4.0, 3.0, 2.0, 3.0]
    average = calculate_average(test_grades)
    print(f"  Grades: {test_grades}")
    print(f"  Average: {average:.2f}")
    print()


def run_sample_calculation():
    print("=" * 50)
    print("Sample Calculation with Grades: A, B, C, B")
    print("=" * 50)
    
    sample_grades = ['A', 'B', 'C', 'B']
    numerical = [letter_to_number(g) for g in sample_grades]
    
    print(f"Letter grades: {sample_grades}")
    print(f"Numerical values: {numerical}")
    
    lowest = find_lowest_grade(numerical)
    average = calculate_average(numerical)
    
    print(f"\nLowest grade: {number_to_letter(lowest)} ({lowest})")
    print(f"Average grade: {number_to_letter(average)} ({average:.2f})")
    print("=" * 50)


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("GRADE CALCULATOR TESTS")
    print("=" * 50 + "\n")
    
    test_letter_to_number()
    test_number_to_letter()
    test_find_lowest()
    test_calculate_average()
    run_sample_calculation()

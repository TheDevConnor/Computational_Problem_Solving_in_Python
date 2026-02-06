# Grade Calculator
## Description
This Python application calculates the lowest grade and average grade from 4 letter grades entered by the user.

## Files Included
- `grade_calculator.py` 
- `test_grade_calculator.py` 
- `README.md`

## Features
- Converts letter grades (A, B, C, D, F) to numerical values (4.0, 3.0, 2.0, 1.0, 0.0)
- Validates user input to ensure only valid letter grades are accepted
- Calculates the lowest grade from 4 grades
- Calculates the average of 4 grades
- Displays results in both letter and numerical format

## How to Run

### Running the Main Program
```bash
python grade_calculator.py
```

The program will prompt you to enter 4 letter grades. After entering all grades, it will display:
- The grades you entered
- Their numerical values
- The lowest grade
- The average grade

### Running the Test File
```bash
python test_grade_calculator.py
```

This will run automated tests on all functions and display a sample calculation.

## Functions

### `letter_to_number(letter_grade)`
Converts a letter grade to a numerical value.
- **Parameters:** letter_grade (str) - A letter grade (A, B, C, D, F)
- **Returns:** float - Numerical value of the grade

### `number_to_letter(number_grade)`
Converts a numerical grade back to a letter grade.
- **Parameters:** number_grade (float) - Numerical grade value
- **Returns:** str - Letter grade

### `find_lowest_grade(grades)`
Finds the lowest numerical grade from a list of grades.
- **Parameters:** grades (list) - List of numerical grades
- **Returns:** float - The lowest grade value

### `calculate_average(grades)`
Calculates the average of a list of grades.
- **Parameters:** grades (list) - List of numerical grades
- **Returns:** float - The average grade

### `get_valid_grade(prompt)`
Prompts user for a valid letter grade and validates input.
- **Parameters:** prompt (str) - The prompt message to display
- **Returns:** str - Valid letter grade


# use_pathlib.py

from pathlib import Path

# Create relative path to data/text.d directory
data_folder = Path("../Computational_Problem_Solving_in_Python/text.d/")

# Join folder with filename
file_to_open = data_folder / "some_text.txt"

# Read and print contents
print(file_to_open.read_text())

# read_text() should not be used for very large files

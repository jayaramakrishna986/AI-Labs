from langchain_text_splitters import RecursiveCharacterTextSplitter,Language


text="""
import random
import shutil
import time

# Get the width of your terminal screen
columns, _ = shutil.get_terminal_size()

# Characters to drop (mixing Katakana, letters, and numbers)
chars = ["1", "0", "A", "B", "Z", "X", "Y", "々", "〆", "ｱ", "ｲ", "ｳ", "ｴ", "ｵ", "*", "#", "$"]

# Initialize columns with spaces
grid = [" " for _ in range(columns)]

try:
    print("\033[92m")  # Switch terminal text colour to bright green
    while True:
        # Pick a random column and populate it with a random character
        for _ in range(random.randint(1, 5)):
            random_col = random.randint(0, columns - 1)
            grid[random_col] = random.choice(chars)
            
        # Print the current row of falling code
        print("".join(grid))
        
        # Randomly fade out/clear random columns to create trailing gaps
        for i in range(columns):
            if random.random() > 0.85:
                grid[i] = " "
                
        time.sleep(0.05)  # Frame rate pause

except KeyboardInterrupt:
    print("\033[0m\nMatrix execution stopped safely.")  # Reset text colour
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

chunks=splitter.split_text(text)
print(chunks)
print(len(chunks))
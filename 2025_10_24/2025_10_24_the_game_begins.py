file_path = "hyperskill-dataset-117317545.txt"

file = open(file_path, "r")
content = file.read().strip()
file.close()

letters = {}

for letter in content:
    if not letter in letters:
        letters[letter] = 0

    letters[letter] += 1

unique_letters = [letter for letter in letters if letters[letter] == 1]

print("".join(unique_letters))
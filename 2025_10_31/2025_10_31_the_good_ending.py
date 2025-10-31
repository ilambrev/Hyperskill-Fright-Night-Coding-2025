file_path = "hyperskill-dataset-117518928.txt"

file = open(file_path, "r")
rows = file.read().strip().split("\n")
file.close()

pairless_letters = []

for row in rows:
    letters = {}

    for letter in row:
        if not letter in letters:
            letters[letter] = 0

        letters[letter] += 1

    row_pairless_letters = "".join(l for l in letters if letters[l] == 1)
    pairless_letters.append(row_pairless_letters)

print("".join(pairless_letters))
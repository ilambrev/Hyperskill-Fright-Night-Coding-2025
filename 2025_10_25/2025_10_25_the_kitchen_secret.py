file_path = "hyperskill-dataset-117346754.txt"

file = open(file_path, "r")
content_rows = file.read().split("\n")
file.close()

keypad = [
    "ABCD",
    "EFGH",
    "IJKL",
    "MNOP"
]

result = []

for content_row in content_rows:
    row = 0
    col = 0
    moves = content_row.split(",")

    for move in moves:
        if move == "UP":
            if row > 0:
                row -= 1
        elif move == "RIGHT":
            if col < len(keypad[0]) - 1:
                col += 1
        elif move == "DOWN":
            if row < len(keypad) - 1:
                row += 1
        elif move == "LEFT":
            if col > 0:
                col -= 1

    result.append(keypad[row][col])

print("".join(result))
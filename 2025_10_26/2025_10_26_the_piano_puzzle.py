file_path = "hyperskill-dataset-117369737.txt"

file = open(file_path, "r")
content = file.read().strip()
file.close()

seven_notes = "ABCDEFG"
shortest_sequence = content

def isSequenceContainsNotes(sequence):
    for char in seven_notes:
        if not char in sequence:
            return False

    return True

for i in range(1 + len(content) - len(seven_notes)):
    sequence = content[i:i+len(seven_notes)]

    if isSequenceContainsNotes(sequence):
        shortest_sequence = sequence
        break
    else:
        for j in range(i + len(seven_notes), len(content)):
            sequence = content[i:j + 1]

            if isSequenceContainsNotes(sequence):
                if len(sequence) < len(shortest_sequence):
                    shortest_sequence = sequence
                    break

print(shortest_sequence)
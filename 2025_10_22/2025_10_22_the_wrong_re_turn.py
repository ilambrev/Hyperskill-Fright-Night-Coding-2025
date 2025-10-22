file_path = "hyperskill-dataset-117254506.txt"

file = open(file_path, "r")
content = file.read().strip()
file.close()

digits = {}

for symbol in content:
    digit = int(symbol)
    if not digit in digits:
        digits[digit] = 0
    
    digits[digit] += 1

sorted_digits = {val[0] : val[1] for val in sorted(digits.items(), key = lambda x: (-x[1], -x[0]))}

print("".join([str(digit) for digit in list(sorted_digits.keys())[:4]]))
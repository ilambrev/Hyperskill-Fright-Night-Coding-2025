file_path = "hyperskill-dataset-117432315.txt"

file = open(file_path, "r")
content = file.read().strip()
file.close()

phone_number = int(content)
binary_string = format(phone_number, "b")
overflows = int(binary_string[0:(len(binary_string) - 32)], 2)
phone_number_remainder = format(phone_number % 2 ** 32, "b")

print(overflows, phone_number_remainder, sep=",")
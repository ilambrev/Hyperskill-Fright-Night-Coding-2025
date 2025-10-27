from math import ceil, sqrt, pow

file_path = "hyperskill-dataset-117397474.txt"

file = open(file_path, "r")
content_rows = file.read().strip().split("\n")
file.close()

distances = []

for i in range(1, len(content_rows)):
    p = [int(number) for number in content_rows[i - 1].split(",")]
    q = [int(number) for number in content_rows[i].split(",")]

    distance = ceil(sqrt(
        pow(p[0] - q[0], 2) +
        pow(p[1] - q[1], 2) +
        pow(p[2] - q[2], 2) +
        pow(p[3] - q[3], 2)))

    distances.append(distance)

print(sum(distances))
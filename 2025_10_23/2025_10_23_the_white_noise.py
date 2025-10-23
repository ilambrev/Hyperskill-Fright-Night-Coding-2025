file_path = "hyperskill-dataset-117286718.txt"

file = open(file_path, "r")
content = file.read().strip()
file.close()

degrees = 0
settings = [int(movement) for movement in content.split(",")]

for setting in settings:
    if setting > 0:
        degrees = (degrees + setting) % 360
    elif setting < 0:
        degrees = (360 + (degrees + setting)) % 360

print(degrees)
file_path = "hyperskill-dataset-117463078.txt"

file = open(file_path, "r")
words = file.read().strip().split()
file.close()

words_with_sorted_letters = {}

for word in words:
    word_with_sorted_letters = "".join(sorted([letter for letter in word]))

    if not word_with_sorted_letters in words_with_sorted_letters:
        words_with_sorted_letters[word_with_sorted_letters] = 0

    words_with_sorted_letters[word_with_sorted_letters] += 1

print([word for word in words if
       words_with_sorted_letters["".join(sorted([letter for letter in word]))] == 1][0])
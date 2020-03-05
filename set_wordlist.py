word_list = []

with open("allwords.txt", "r") as word_file:
    for line in word_file.readlines():
        word_list.append(line.strip())

word_list = list(set(word_list))

print(len(word_list))

word_list = '\n'.join(word_list)

print(word_list)

with open("allwords.txt", "w") as word_file:
    word_file.write(word_list)

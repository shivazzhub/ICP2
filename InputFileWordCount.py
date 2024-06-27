input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
word_count = {}
lines = input_file.readlines()
for line in lines:
    output_file.write(line)
    words = line.strip().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
output_file.write("\nWord_Count:\n")
for word, count in word_count.items():
    output_file.write(f"{word}: {count}\n")
input_file.close()
output_

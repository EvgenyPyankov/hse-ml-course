def print_answer(num, line):
    f = open("answers/" + str(num) + ".txt", "w+")
    f.write(line)
    print(line)
    f.close()

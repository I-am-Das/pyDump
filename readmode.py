with open("DAS.txt","r") as f:
    data =f.readlines()
    for line in data:
        print(line)
        word=line.strip()
        print(word)


with open("poem.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    result = 0
    for i in range(0, len(lines)):
        result += int(lines[i].split(" ")[2])

print(result / len(lines))
    

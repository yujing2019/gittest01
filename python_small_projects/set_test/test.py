data=set()
with open("input.txt") as fin:
    for line in fin:
        if len(line.strip())>0:
            line=line.strip().split("\t")
            name=line[0]
            data.add(name)

for name in data:
    print(name)


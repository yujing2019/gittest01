#example1
result=[]
for i in range(10):
    if i%2 ==0:
        result.append(i*i)
print(result)

result2=[i*i for i in range(10) if i%2==0]
print(result2)

#example2
data=[1,2,3,4]
print(data)
result3="\t".join([str(d)for d in data])
print(result3)

fin=open("fin.txt")
stu_id=[line.strip().split("\t")[0] for line in fin if len(line.strip())>0]
stu_name=[str(line).split("\t")[1].strip()for line in fin if len(line.strip())>0]
s=f"stuid {stu_id}"
print(s)

fin.close()
fin=open("read.txt")

smin=10000
smax=0
sumv=0
countv=0

for line in fin:
    number=int(line.strip())
    if number >smax:
        smax=number
    if number <smin:
        smin=number
    sumv += number
    countv += 1

avg=sumv/countv

print("max_value",smax)
print("min_value",smin)
print("avg_value",avg)

fout=open('fout.txt','w')
fout.write("max_value: "+str(smax)+'\n')
fout.write("min_value: "+str(smin)+'\n')
fout.write("avg_value: "+str(avg)+'\n')


fin.close()
fout.close()

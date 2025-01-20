sgrades=[(1005,95),(1006,86),(1007,98),(1008,81)]
new_list=sorted(sgrades,key=lambda x:x[1],reverse=True)
print(new_list)
print(sgrades)
sgrades.sort(key=lambda x:x[1])
print(sgrades)
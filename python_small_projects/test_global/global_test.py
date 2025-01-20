x=100
def vari():
    global x
    #x=200
    while x <200:
        if  not bool(x%2 or x%3 or x%5  ):
            print(x)
        x+=1

vari()
print(x)
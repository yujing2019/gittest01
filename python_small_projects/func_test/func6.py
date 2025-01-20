x=123
"""
    def func():
        print(x)
    
    func()
    
    def func1():
        x=100
        print(x)
    
    func1()
    print(x)
"""
def func2():
    global x
    x=200
    print(x)

print(x)
func2()
print(x)
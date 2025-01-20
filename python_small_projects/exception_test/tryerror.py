try:
    print("hello 01")
    print(10/0)
    print("hello 02")
except ValueError as e:
    print("exception",e)
except ZeroDivisionError as e:
    print("exception",e)
finally:
    print("finally")
print("hello 03")


def set_price(c):
    if c.year < 5 and c.mileage < 30000:
        if c.brand == "Bmw":
           price = 60000
        elif c.brand == "Toyoto":
            price = 20000
        elif c.brand == "Bnz":
            price = 40000
        else:
            price = 10000
    elif c.year < 10 and c.mileage < 100000:
        if c.brand == "Bmw":
            price = 30000
        elif c.brand == "Toyoto":
            price = 10000
        elif c.brand == "Bnz":
            price = 5000
        else:
            price = 3000
    else:
        price = 2000
    return price



class Car:
    cnt=0
    def __init__(self,owner,brand,mileage,year):
        self.owner=owner
        self.brand=brand
        self.mileage=mileage
        self.year=year





car1=Car('tommy','Toyoto',27877,3)
print(set_price(car1))

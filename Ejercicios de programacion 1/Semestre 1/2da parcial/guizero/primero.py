def suma01(a:int | float, b:int|float)->int:
    return a + b
    
def suma_float(a:float, b:int)->float:
    return a + b
print(suma01(4,5))
print(suma01(4.5,5))
print(suma01(4,5.4))

def divideCalc(d1:int, d2:int):
    divideValue = d1/d2
    return divideValue

def multiplyCalc(d1:int, d2:int):
    multiplyValue = d1*d2
    return multiplyValue

def additionCalc(d1:int, d2:int):
    additionValue = d1+d2
    return additionValue

def subtractionCalc(d1:int, d2:int):
    subtractionValue = d1-d2
    return subtractionValue

d1 = int(input("Enter the first number : "))
d2 = int(input("Enter the second number : "))

print(divideCalc(d1,d2))
print(multiplyCalc(d1,d2))
print(additionCalc(d1,d2))
print(subtractionCalc(d1,d2))
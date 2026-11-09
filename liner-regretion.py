import math

def inputData():
    x = eval(input("Enter the data separated by comas for x: "))
    y = eval(input("Enter the data separated by comas for y: "))
    
    count_x = len(x)
    count_y = len(y)
    
    if count_y != count_x:
        return "the count of the data of x and y are not matching reEnter the data points"
    
    data = {}
    
    sumOfX = sum(x)
    sumOfY = sum(y)
    
    
    sum_xy = 0
    i = 0
    squreOfXi = 0
    for it in x:
        squreOfXi += it ** 2
        
        
    while i < count_x:
        sum_xy += x[i] * y[i]
        i += 1
        
    data["sumSqureOfXi"] = squreOfXi
    data["sum_xy"] = sum_xy
    data["sum_of_x"] = sumOfX
    data["sum_of_y"] = sumOfY
    data["count"] = count_x
    data["squreSumOfX"] = sumOfX ** 2
    data['y'] = y
    data['x'] = x
    
    
    return data


def findM(data):
    return (
        (
            (data["count"] * data["sum_xy"]) - (data["sum_of_x"] * data["sum_of_y"])
        )/
        (
            (data["count"] * data["sumSqureOfXi"]) - data["squreSumOfX"]
        )
    )
    
    
def findC(data,m):
    return (
        (
            data["sum_of_y"] - (data["sum_of_x"] * m)
        )/
        (
            data["count"] 
        )
    )


def calculateMandC():
    data = inputData()
        
    m = findM(data)
    c = findC(data,m)
    
    return m,c

def predictedY(m,c,x):
    pred_y = []
    for it in x:
        pred_y.append(it*m + c)
    
    return pred_y
    
def error(y, pred_y):
    errors = []
    for it in range(0, len(y)):
        errors.append(y[it],pred_y[it])
    return errors



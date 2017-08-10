import math
def main():
    x = [100 + 100*math.cos(theta*math.pi) for theta in [0.01*i for i in range(200)]]
    y = [100 + 100*math.sin(theta*math.pi) for theta in [0.01*i for i in range(200)]]


    data = {}
    data.setdefault("lableX", x)
    data.setdefault("lableY", y)

    jsonData = {}
    jsonData.setdefault("data", data)

    print(jsonData)


main()
def c_to_f(c):
    return (c * 1.8)+32
def f_to_c(f):
    return (f-32)*0.5555

print ("Welcome to Farenheit-404 ")

while True:
    print("1. Convert Celcuis to Fahrenheit")
    print("2. Convert Fahrenheit to Celcuis")

    choice = input("Enter 1 or 2")
    if choice == "1":
        Celcuis = input("Enter temprature in Celcuis:")
        Celcuis = float(Celcuis)
        Fahrenheit = c_to_f(Celcuis)
        print(Celcuis,"degrees Celcuis is", Fahrenheit, "degrees Fahrenheit")
    elif choice == "2":
        Fahrenheit = input("Enter temprature in Fahrenheit:")
        Fahrenheit = float(Fahrenheit)
        Celcuis = f_to_c(Fahrenheit)
        print(Fahrenheit,"degrees Fahrenheit is", Celcuis,"degrees Celsius")
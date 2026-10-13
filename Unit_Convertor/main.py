# Banner
print("=-="*20)
print("-=-"*20)
print("              UNIT CONVERTOR")
print("-=-"*20)
print("=-="*20)

# ------------------------Functions------------------------

# 1
def m_to_km(data):
    return data / 1000
# 2
def km_to_m(data):
    return data * 1000
# 3
def g_to_kg(data):
    return data / 1000
# 4
def kg_to_g(data):
    return data * 1000 
# 5
def c_to_k(data) :
    return data + 273.15
# 6 
def c_to_f(data):
    return (data * (9 / 5)) + 32

# 7
def f_to_k(data):
    return (data - 32)* 5/9 + 273.15

# 8
def f_to_c(data):
    return (data - 32) * 5/9

# 9 
def k_to_c(data):
    return data - 273.15

# 10 
def k_to_f(data):
    return (data - 273.15) * 9/5 +32


# This is a unit convertor

print("Hi! \nThis is a simple unit convertor")
while True:
    print("\n Choose conversion:")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Gram to Kilogram")
    print("4. Kilogram to Gram")
    print("5. Celsius to Kelvin")
    print("6. Celsius to Fahrenheit")
    print("7. Fahrenheit to Kelvin")
    print("8. Fahrenheit to Celsius")
    print("9. Kelvin to Celsius")
    print("10. Kelvin to Fahrenheit")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0" :
        break
    
    try:
        data = float(input("Enter the value: "))
    except:
        print('INvalid value , Cannot give any other input only numbers')
        continue
    # 1. Meter to Kilometer 
    if choice == "1":
        r = m_to_km(data)
        u = "Km"
    # 2. Kilometer to Meter       
    elif choice == "2":
        r = km_to_m(data)
        u = "m"
    # 3. Gram to Kilogram
    elif choice == "3":
        r = g_to_kg(data)
        u = "Kg"
    # 4. Kilogram to gram   
    elif choice == "4":
        r = kg_to_g(data)
        u = "g" 
    # 5. Celsius to Kelvin    
    elif choice == "5":       
        r = c_to_k(data)
        u = "K"
    # 6. Celsius to Fahrenheit
    elif choice == "6":
        r = c_to_f(data)
        u = "F"
    # 7. Fahrenheit to Kelvin 
    elif choice == "7":
        r = f_to_k(data)
        u = "K" 
    # 8. Fahrenheit to Celsius
    elif choice == "8":
        r = f_to_c(data)
        u = "C"
    # 9. Kelvin to Celsius     
    elif choice == "9":
        r = k_to_c(data)
        u = "C" 
    # 10.Kelvin to Fahrenheit
    elif choice == "10":
        r = k_to_f(data)
        u = "F"
    # For another choice
    else:
        print("Invalid choice")
        continue
    print(f"Result: {r:.2f}{u}")

print("\nThanks for using Unit Converter!")

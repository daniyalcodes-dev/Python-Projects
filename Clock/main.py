from clock_functions import clock

print("==== Clock ====")
print("\nMenu:\n\u2022 Clock\n\u2022 Timer\n\u2022 Stopwatch")
while True:
    try:
        choice = input("Choice: ").lower()
        if choice =="exit":break
        elif choice == "clock":clock.Clock()
        elif choice == "timer":clock.Timer()
        elif choice == "stopwatch":clock.Stopwatch()
        else:raise TypeError
    except:
        raise ValueError
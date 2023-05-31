import time
cel = 10
while cel <= 100:
    time.sleep(0.09)
    fah = (cel * 9/5) + 32
    print(f"Celsius {cel} - Fahrenheit {fah}")
    cel += 10
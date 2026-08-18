price = r"$ 99.99"


# IndexError ValueError

try:
    float(price.split("1")[0])
except (ValueError, IndexError):
    print("No price found")
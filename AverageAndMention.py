a, b, c = map(int, input("Enter three exam results: ").split())

avg = (a + b + c) / 3

if avg < 10:
    print("Insufficient")
elif avg < 12:
    print("Passable")
elif avg < 14:
    print("Assez bien")
elif avg < 16:
    print("Bien")
else:
    print("Très bien")

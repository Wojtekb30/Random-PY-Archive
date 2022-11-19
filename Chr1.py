print("Start")
for i in range(0,100):
    znak = chr(i)
    print(znak, end=" ")
    if i % 16 == 15:
        print()
print()
print("Done")
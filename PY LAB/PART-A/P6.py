print("Demonstrating Break:")
for num in range(1,10):
    if num==5:
        break
    print(num,end=" ")
print("\n")

print("Demonstrating Continue:")
for num in range(1,10):
    if num==5:
        continue
    print(num,end=" ")
print("\n")

print("Demonstrating Pass:")
for num in range(1,10):
    if num==5:
        pass
    print(num,end=" ")
print("\n")

size = int(input("Enter the size of the array: "))

print("Enter the elements of the array:")
arr = []
for _ in range(size):
    element = float(input())
    arr.append(element)

index = int(input("Enter the index of the element to print: "))

try:
    print(f"Element at index {index}: {arr[index]:.2f}")
except IndexError:
    print(f"Index {index} is invalid.")
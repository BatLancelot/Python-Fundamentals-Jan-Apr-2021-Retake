n = int(input())

positives = []
negatives = []

for _ in range(n):
    digit = int(input())
    if digit >= 0:
        positives.append(digit)
    else:
        negatives.append(digit)

print(positives)
print(negatives)
print(
    f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")

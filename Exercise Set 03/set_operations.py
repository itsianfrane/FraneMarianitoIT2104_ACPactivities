set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

diff_set1_set2 = set1 - set2
diff_set2_set1 = set2 - set1

union_set = set1 | set2

symmetric_diff1 = set1 ^ set2
symmetric_diff2 = set2 ^ set1

intersection1 = set1 & set2
intersection2 = set2 & set1

print("Set Difference (set1 - set2):", diff_set1_set2)
print("Set Difference (set2 - set1):", diff_set2_set1)
print("\nUnion of sets (set1 | set2):", union_set)
print("\nSymmetric Difference (set1 ^ set2):", symmetric_diff1)
print("Symmetric Difference (set2 ^ set1):", symmetric_diff2)
print("\nSet Intersection (set1 & set2):", intersection1)
print("Set Intersection (set2 & set1):", intersection2)
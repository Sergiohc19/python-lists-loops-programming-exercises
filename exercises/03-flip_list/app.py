sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below
new_list = []

# for items in reversed(sample_list):
#     new_list.append(items)

for items in sample_list[::-1]:
    new_list.append(items)

   

print(sample_list)
print(new_list)

students = ["john", "doe", "mark", "tyson"]

print(students)

# print no. of items
print(len(students))

# print the 1st item
print(students[0])


# print the last item
last = len(students) -1
print(students[last])


# add an item at a certain index
students.insert(1, "Alex")
print(students)

students.insert(3, "larry")
print(students)

# add a name at the end
students.append("wanjiru")
print(students)

# change value
students[0] = "Alice"
print(students)



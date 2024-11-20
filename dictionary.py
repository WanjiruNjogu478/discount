# teacher = dict{}
customer = {
    "name": "wanjiru",
    "age": 20,
    "year": "3"
}
print(customer)

# add more items
customer['weight'] =60,
customer['bought'] ="jersey"
print(customer)

# print out a specific item
print(customer["name"])
# or
print(customer.get("age"))

for customer in customer:
    print(customer)

for key,value in customer.items():
    print(f"key: (key), value: (value)")
    print("---------------")

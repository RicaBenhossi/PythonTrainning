my_dict = {
    "Name": "Natalia",
    "Age": 31,
    "BDFL": True
}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

teste git cloud

test git at home for 10000 times

for key in my_dict:
    print(key, my_dict[key])

cubes_by_four = [(x ** 3) for x in range(1, 11) if ((x ** 3) % 4 == 0)]
print(cubes_by_four)

def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

a = [5, 10, 15, 20, 25]
b = list_ends(a)
# c = [x for x in a if ]
c = [a[0], a[-1]]

print(a)
print(b)
print(c)

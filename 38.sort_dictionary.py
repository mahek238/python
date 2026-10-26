d = {'a': 3, 'b': 1, 'c': 2}
# Ascending
asc = dict(sorted(d.items(), key=lambda item: item[1]))
print("Ascending:", asc)
# Descending
desc = dict(sorted(d.items(), key=lambda item: item[1],
reverse=True))
print("Descending:", desc)
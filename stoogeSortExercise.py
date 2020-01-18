x = 93
y = 68
z = 88
tmp = max(x, y)
x = min(x, y)
y = tmp
tmp = max(y, z)
y = min(y, z)
z = tmp
tmp = max(x, y)
y = tmp
x = min(x, y)
print('"X", is', x, ', "Y" , is', y, 'and "Z", is', z);

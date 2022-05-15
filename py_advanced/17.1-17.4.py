# ----------------- 1 --------------------

file = open(input(), 'r')
print(file.read())
file.close()

# ----------------- 2 --------------------

with open(input()) as output:
    print(output.readlines()[-2])
output.close()
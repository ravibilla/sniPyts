# print pyramid
def print_pyramid(n, sym):
    for i in range(1, n+1):
        print((n-i) * " " + i * (sym+" "))

print_pyramid(10, "$")
def is_solution(expr, x):
    return eval(expr) == 0

# Thay range(-10, 10) bằng range(-5, 5)
A = {x for x in range(-5, 5) if x**2 + x - 6 == 0}
print("A:", A)  # -> {-3, 2}


# Thay điều kiện: x**2 + x - 2 == 0
A = {x for x in range(-5, 5) if x**2 + x - 2 == 0}
print("A mới:", A)

# Kiểm tra từng phần tử có là nghiệm không
for x in A:
    print(f"x = {x}, là nghiệm:", x**2 + x - 2 == 0)

# Gợi ý nâng cao: dùng hàm kiểm tra với chuỗi biểu thức
for x in A:
    print(f"x = {x}, is_solution:", is_solution("x**2 + x - 2", x))
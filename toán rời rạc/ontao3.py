from sympy import FiniteSet
S = FiniteSet(1, 2, 3, 4)
ps = S.powerset()
print("Tổng số tập con của S:", len(ps))  
empty_set = FiniteSet()
print("Tập rỗng có là tập con không?", empty_set in ps)
print("Các tập con có đúng 2 phần tử:")
for subset in ps:
    if len(subset) == 2:
        print(subset)
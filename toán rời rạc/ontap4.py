from sympy import FiniteSet
S = FiniteSet('a', 'b')
P = S ** 2
print("Các bộ 2 từ S x S:")
for item in P:
    print(item)
P3 = S ** 3
print("\nCác bộ 3 từ S x S x S:")
for item in P3:
    print(item)
print("\nSố phần tử trong S x S:", len(P))
print("Số phần tử trong S x S x S:", len(P3))

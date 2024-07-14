# 在Python中，常見的條件語句有 if、else 和 elif（else if）。

x = 3
if x > 5 or x < 10:
    print("x")
elif x > 0 and x < 4: # elif是else if的縮寫
    print("y")
else:
    print("z")

'''
A.邏輯運算：使用 and 和 or 來處理布林值。這些運算符在條件判斷中更常見。
常見的邏輯運算符有：and、or 和 not。
等同於java中的&&、||、！

B.位元運算：使用 & 和 | 來處理整數的位元。這些運算符在處理低階資料或進行位元操作時更常見。
ex:
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a & b  # 0001 in binary, which is 1 in decimal
print(result)  # 1
常見的位元運算符有：&（AND）、|（OR）、^（XOR）和 ~（NOT）。
'''

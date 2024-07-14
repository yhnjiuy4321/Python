# for迴圈用於遍歷序列（如列表、元組、字串等）中的每個元素，或者執行固定次數的操作。
# 一維陣列
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 二維陣列
fruits = [["apple", "banana", "cherry"], ["orange", "lemon", "lime"]]
for fruit in fruits:
    for f in fruit:
        print(f + "\n")

for a in ['x', 'y', 'z']:
    for b in [1, 2, 3]:
        print(f'{a}{b}')  # f-string

# range() 函數
for i in range(5): # 5代表結束值(5不包含)
    print(i)

for i in range(2, 5):  # 2代表起始值，5代表結束值(5不包含)
    print(i)

for i in range(2, 10, 2):  # 2代表起始值，10代表結束值(10不包含)，2代表間隔值
    print(i)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print("{}*{}={}\t".format(j, i, i * j), end="") # end=""表示不換行
    print() # 換行

"""
"{}*{}={}".format(j, i, i * j)

{} 代表占位符，format() 函數將後面的變數依次填入占位符中。
j 代表乘數，i 代表被乘數，i * j 代表積。
"""

# break 語句用來跳出當前循環
for i in range(5):
    if i == 3:
        break
    print(i)

# continue 語句用來跳過當前循環中的剩餘語句，然後繼續進行下一輪循環。
for i in range(5):
    if i == 3:
        continue
    print(i)

# pass 語句是空操作，是為了保持程序結構的完整性。
for i in range(5):
    if i == 3:
        pass  # 沒有任何操作
    print(i)

"""
與java的for迴圈的差異:

java:
for迴圈三寶---開頭,條件(限制),怎麼跑
for (開頭; 條件(限制); 怎麼跑) {
}

python:
for 變數 in 序列:
for 變數 in range(起始值, 結束值(不包含), 間隔值):

java的for迴圈是用分號隔開，python的for迴圈是用冒號隔開。

"""

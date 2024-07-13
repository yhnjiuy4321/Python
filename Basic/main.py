name = "Kevin"
age = 26
country = "Taiwan"
print("my name is ", name , ", I am ", age, " years old, I come from ", country)

user_name = input("Enter your name: ")  # 等同java的Scanner
print("Hello,", user_name)

age = input("Enter your age: ") # 這裡的age是字串
age = int(age)  # 將age轉換成整數(才可以進行做運算)
age = age + 1
print("You are", age, "years old", sep="-")  # sep="-"是指定分隔符號

"""
1.可以直接宣告變數，不需要事先宣告變數型態
2.input()是用來接收使用者輸入的資料，括號內可以加入提示字元
3.input()接收到的資料是字串(String)，若要進行數值運算或其他操作，需要先轉換成對應的型態

    轉換範例:
    age = input("Enter your age: ") # 這裡的age是字串
    age = int(age) # 將age轉換成整數(才可以進行做運算)

4.在print()中，可以直接使用逗點分隔不同的變數，也可以使用sep參數指定分隔符號(比如:sep="-")
5.第一段與第三段都有age，但兩者不會干擾，正確來說，當重新賦值時，新的值會覆蓋舊的值，而不會引發任何衝突。若要有區分，可以使用不同的變數名稱。
"""

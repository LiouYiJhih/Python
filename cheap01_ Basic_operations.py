
# 註解的重要性
hourly_salary = 125                         # 設定時薪
annual_salary = hourly_salary * 8 * 300     # 計算年薪
monthly_fee = 9000                          # 設定每月花費
annual_fee = monthly_fee * 12               # 計算每月花費
annual_savings = annual_salary - annual_fee # 計算每年儲存金額
print(annual_savings)                       # 列出每年儲存金額
print("=====================")

print("認識底線開頭或結尾的變數")
# 變數名稱有前單底線，例如: _test
### 一種私有變數、函數或方法，可能是在測試中或一般應用在不想直接被調用的方法可以使用。
# 變數名稱有後單底線，例如: dict_
### 主要目的是避免與Python的關鍵字或內建函數有相同名稱。
### 舉例: max是求較大值函數、min是求較小值函數，若想建立max和min變數可以命名為max_和min_。
# 變數名稱前後有雙底線，例如: __test__
### 保留給Python內建的變數或方法使用。
# 變數名稱有錢雙底線，例如: __test
### 這也是私有方法或變數命名，無法直接使用本名存取。
print("=====================")

# 基本運算 四則運算
a = 5 + 6
print(a)
b = 80 -10
print(b)
c = 5 * 9
print(c)
d = 9 / 5
print(d)
# 餘數和整除
x = 9 % 5   # 餘數設定給變數x
print(x)
y = 9 // 2  # 整數結果設定給變數y
print(y)
x = 3 ** 2  # 3的平方
print(x)
y = 3 ** 3  # 3的次方
print(y)
# 多重指定
x = y = z = 10
print(x, y, z)
a, b, c = 10, 20, 30
print(a, b, c)
# 變數交換
x, y = 70, 80
print("Before:",x, y)
x, y = y, x
print("After:",x, y)
# divmod(): 一次獲得商和餘數
z = divmod(9, 5)    # 獲得元組值(1, 4)，元組(Tuple)
print(z)
x, y = z            # 將元組值設定給x和y
print(x, y)
# 刪除變數 
del x
# print(x)
# 將一個敘述分成多行
a = b = c = 10
x = a + b + c + 12
print(x)
y = a + \
    b + \
    c + \
    12
print(y)
z =( a + 
     b + 
     c + 
     12 )
print(z)
print("=====================")

# 複利計算
money = 50000 * (1 + 0.015) ** 5
print("本金合是:", money)
# 計算園面積和圓周長
PI = 3.14159
r = 5
print("圓面積:單位是平方公分")
area = PI * r * r
print(area)
circumference = 2 * PI * r
print("圓周長:單位是公分")
print(circumference) 
print("=====================")




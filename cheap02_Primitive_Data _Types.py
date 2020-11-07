
# 數值資料型態(numeric type): 整數(int)、浮點數(float)、複數(complex number)
# 布林值(boolean): 也被視為"數值"資料型態
# 文字序列(text sequence type): 字串(striing)
# 字元組(bytes): 二進位的資料型態，長度是8個位元。
# 序列型態(sequence type): list、tuple 
# 對映型態(mapping type): dict
# 集合型態(set type): 集合(set)、凍結集合(forzenset)
# list、tuple、dict、set又稱作是容器(container)

# type(): 列出變數的資料型態
x = 10
y = x / 3
print(x)
print(type(x))
print(y)
print(type(y))  # 帶有小數點的數字稱為浮點數
y = x + 5.5
print(y)
print(type(y))  # 帶有小數點的數字稱為浮點數
print("=====================")

# 自然數(int可以任意大小的數值)
googol = 10 ** 100
print("自然數:", googol)
print("=====================")

# 2進位整數和函數bin()
x = 0b1101      # 2進位整數
print(x)        # 列出10進位結果
y = 13          # 10進位整數
print(bin(y))   # 列出轉換2進位結果
# 8進位整數和函數oct()
x = 0o57        # 8進位整數
print(x)        # 列出10進位結果
y = 47          # 10進位整數
print(oct(y))   # 列出轉換8進位結果
# 16進位整數和函數hex()
x = 0x5D        # 16進位整數
print(x)        # 列出10進位結果
y = 93          # 10進位整數
print(hex(y))   # 列出轉換16進位結果
print("=====================")

# 數值運算常用的函數
### abs(): 計算絕對值
### pow(x,y): 返回x的y次方
### round(): 奇數使用四捨五入，偶數使用五捨六入
print(round(1.5))       # round(1.5) = 2
print(round(2.5))       # round(2.5) = 2
# 處理小數時，第二個參數代表取到小數第幾位，小數位數的下一個小數位數採用"5"以下捨去
print(round(2.15,1))    # round(2.15,1) = 2
print(round(2.25,1))    # round(2.25,1) = 2
print(round(2.151,1))   # round(2.151,1) = 2
print(round(2.251,1))   # round(2.251,1) = 2
print("=====================")

# 科學記號表示法 
x = 1.23456E+5
print(x)
y = 1.23e-4
print(y)
print("=====================")

# 複數(complex number)
### 複數由實數和虛數(都是浮點數)，a + bj 或 complex(a,b)
print(3 + 5j)
print(complex(3,5))
### 虛數單位值是根號-1，可使用real和imag分別獲得實數和虛數
x = 6 + 9j
print(x.real)
print(x.imag)
print("=====================")

# 布林值(True = 1、False = 0)
x = True
print(x)
print(type(x))
y = False
print(y)
print(type(y))

print(int(x))   # 強制轉換為整數
print(type(x))
print(int(y))   # 強制轉換為整數
print(type(y))

xt = True
x = 1 + xt      # 布林當作數值資料
print(x)
print(type(x))
yt = False
y = 1 + yt      # 布林當作數值資料
print(y)
print(type(y))
# 下列情況也視為False
### 布林值 False
### 整數 0
### 浮點數 0.0
### 空字串 ''
### 空串列 []
print("=====================")

# 字串(string)資料是指兩個單引號(')或兩個雙引號(")之間，資料型態為str
x = 'DeepStone means Deep Learning'
print(x)
y = "深石數位"
print(y)
# 字串連接
num1 = 222
num2 = 333
num3 = num1 + num2
print("數值相加:", num3)
num1 = "222"
num2 = "333"
num3 = num1 + num2
print("數值組成的字串相加:", num3)
str1 = "DeepStone"
str2 = "Deep Learning"
str3 = str1 + str2
print("一般字串相加:", str3)
print("=====================")

# str()
### 設定空字串
x = str()
print(x)
### 設定字串
x = str('ABC')
print(x)
### 強制將數值資料轉換為字串資料
x = 123
y = str(x)
print(y)
print(type(y))
num1 = 222
num2 = 333
num3 = num1 + num2
print("數值相加:", num3)
str1 = str(num1) + str(num2)
print("強制轉換為字串相加:", str1)
#將字串轉換為整數
x1 = "22"
x2 = "33"
x3 = x1 + x2
print(x3)   # 列印字串相加
x4 = int(x1) + int(x2)
print(x4)   # 列印整數相加
# 字串與整數相乘產生字串複製效果
x1 = "A"
x2 = x1 * 10
print(x2)
x3 = "ABC"
x4 = x3 * 5
print(x4)
# 聰明的使用字串加法和換行字元\n
str1 = "台灣加油"
str2 = "大家幸福"
str3 = "找到工作"
str4 = str1 + "\n" + str2 + "\n" + str3
print(str4)
# 字串前加r，可以防止逸出字元(Escape Character)被轉譯
str1 = "Hello!\nPython"
print("不含r字元輸出:", str1)
str2 = r"Hello!\nPython"
print("含r字元輸出:", str2)
print("=====================")

# ASCII碼: 使用8個位元定義一個字元
### chr(): 可以傳回函數x值的ASCII或Unicode字元
# Unicode碼: 使用16個位元定義文字
### ord(): 可以傳回函數字元參數x的Unicode碼值
# utf-8編碼: 針對Unicode字符級的可變長度編碼方式，目前網際網路遵循編碼方式
## ASCII使用utf-8編碼規則
### ASCII使用1個byte儲存ASCII字元，utf-8編碼方式為byte的第一個位元為0，其他7個位元則是字元ASCII的碼值
## Unicode使用utf-8編碼規則
### 對於需要n個byte編碼的Unicode中文字元，例如需要3個byte編碼，第一個byte的前n(3)位元皆設為1，n+1(4)設為0。
### 後面第二個和第三個byte前2位元是10，其它則是此中文字元的Unicode碼
### 1110xxxx 10xxxxxx 10xxxxxx
x1 = 97
x2 = chr(x1)
print(x2)
x3 = ord(x2)
print(x3)
x4 = '魁'
print(hex(ord(x4)))
print("=====================")

# bytes資料
### 字串轉成bytes資料，稱為編碼(encode)
string = 'abc'
print(len(string))
stringBytes = string.encode('utf-8')
print(len(stringBytes))
print(type(stringBytes))
print(stringBytes)
name = '劉益智'
print(len(name))
nameBytes = name.encode('utf-8')
print(len(nameBytes))
print(type(nameBytes))
print(nameBytes)
### bytes資料轉成Unicode字串，稱為解碼(decode)
stringUcode = stringBytes.decode('utf-8')
print(len(stringBytes))
print(stringUcode)
nameUcode = nameBytes.decode('utf-8')
print(len(nameBytes))
print(nameUcode)
print("=====================")

# 計算地球到月球所需時間
### 馬赫(Mach number)紀念奧地利科學家恩斯特馬赫(Ernst Mach)，約每小時1225公里
### 地球到月球距離約384400公里
dist = 384400                   # 地球到月球距離
speed = 1225                    # 馬赫每小時1225公里
total_hours = dist // speed     # 計算小時數
# 方法一
days = total_hours // 24        # 商 = 計算天數
hours = total_hours % 24        # 餘數 = 計算小時數
# 方法二
days, hours = divmod(total_hours, 24)
print("總共需要", days, "天", hours, "小時")
# 計算座標軸2個點之間距離，(1, 8)和(3, 10)
### **0.5相當於開根號
x1 = 1
y1 = 8
x2 = 3
y2 = 10
dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print("兩點距離: ", dist)
print("=====================")



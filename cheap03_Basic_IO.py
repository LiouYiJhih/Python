import math

# help(): 列出Python指令使用說明
print(help(print))
print("=====================")

# 格式化輸出
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
### value: 表示想輸出的資料，用逗號隔開
### sep: 插入各筆資料的分隔字元，預設為空白字元
### end: 當資料輸出結束時所插入的字元，預設為換行字元
### file: 資料輸出位置，預設為sys.stdout(也就是螢幕)。也可以將輸出導入其他檔案和設備
### flush: 是否清除資料流的緩衝區，預設為不清除
num1 = 222
num2 = 333
num3 = num1 + num2
print("數值相加: ", num3)
print("數值相加: ", num3, end="\t")
str1 = str(num1) + str(num2)
print("強制轉換為字元相加: ", str1, sep=" $$$ ")
print("=====================")

# 格式化輸出
# print("...輸出格式區..." % (變數系列區, ...))
'''
%d: 整數
%f: 浮點數
%x: 16進位整數
%X: 大寫16進位整數
%o: 8進位整數
%s: 字串
%e: 科學符號e的輸出
%E: 科學符號大寫E的輸出
'''
score = 90
name = "劉益智"
count = 1
formaster = " %s 你的第 %d 次物理考試成績是 %d "
print(" %s 你的第 %d 次物理考試成績是 %d " % (name, count, score))
print(formaster % (name, count, score))
x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))
x = 10
print("整數%d \t浮點數%f \t字串%s" % (x, x, x))
y = 9.9
print("整數%d \t浮點數%f \t字串%s" % (y, y, y))
print("%x" % x)
print("%X" % x)
x = 10000000
print("%e" % x)
print("%E" % x)
print("=====================")

# 經穩控制格式化輸出
'''
%(+|-)nd: 整數
%(+|-)m.nf: 浮點數
%(+|-)nx: 16進位整數
%(+|-)nX: 大寫16進位整數
%(+|-)no: 8進位整數
%(-)ns: 字串
%(-)m.ns: 字串(m輸出字串寬度、n顯示字串長度)，n小於字串長度時會有裁減字串效果
%(+|-)e: 科學符號e的輸出
%(+|-)E: 科學符號大寫E的輸出
'''
x = 100
print("x = /%6d/" % x)
y = 10.5
print("y = /%6.2f/" % y)
s = "Deep"
print("s = /%6s/" % s)
print("保留格數空間不足的實例")
print("x = /%2d/" % x)
print("y = /%3.2f/" % y)
print("s = /%2s/" % s)
# 靠左對齊
print("x = /%-6d/" % x)
print("y = /%-6.2f/" % y)
print("s = /%-6s/" % s)
# 出現正號(+)
print("x = /%+6d/" % x)
print("y = /%+6.2f/" % y)
string = "abcdefg"
print("/%10.3s/" % string)
print("=====================")

# format(): 輸出格式區內的變數使用"{}"表示
# print("...輸出格式區...".format(變數系列區, ...))
score = 90
name = "劉益智"
count = 1
# 方法一
print(" {} 你的第 {} 次物理考試成績是 {} ".format(name, count, score))
# 方法二
string = " {} 你的第 {} 次物理考試成績是 {} "
print(string.format(name, count, score))
# 方法三
print(" {0} 你的第 {1} 次物理考試成績是 {2} ".format(name, count, score))
# 方法四
print(" {n} 你的第 {c} 次物理考試成績是 {s} ".format(n="劉益智", c=1, s=90))
r = 5
PI = 3.14159
area = PI * r ** 2
print("/半徑 {0:3d}，圓面積 {1:10.2f}".format(r, area))
# 輸出對齊方式應用
print("/半徑 {0:3d}，圓面積 {1:10.2f}".format(r, area))
print("/半徑 {0:>3d}，圓面積 {1:>10.2f}".format(r, area))   # >: 靠右對齊
print("/半徑 {0:<3d}，圓面積 {1:<10.2f}".format(r, area))   # <: 靠左對齊
print("/半徑 {0:^3d}，圓面積 {1:^10.2f}".format(r, area))   # ^: 置中對齊
title = "南極旅遊講座"
print("/{0:*^20s}/".format(title))
print("/{0:*>20s}/".format(title))
print("/{0:*<20s}/".format(title))
print("=====================")

# format()優點，使用Python應用在爬蟲時，可能要處理下列格式的字串
'''
"https://maps.apis.com/json?city=taipei&radius=1000&type=school"
如果使用print()設計可能如下:
url = "https://maps.apis.com/json?city="
city = "taipei"
radius = 1000
type = "shcool"

url + city + '&radius=' + str(radius) + '&type=' + type
如果使用format，則上述一行設計可以如下
url + "{}&radius={}&type={}".format(city, radius, type)

'''
url = "https://maps.apis.com/json?city="
city = "taipei"
radius = 1000
type = "shcool"
# 方法一
print(url + city + '&radius=' + str(radius) + '&type=' + type)
# 方法二
print(url + "{}&radius={}&type={}".format(city, radius, type))

# Python3.6x版，有一個改良format格式化方法，稱為f-strings。
name = "劉益智"
message = f"我是{name}"
print(message)
my_url = url + f"{city}&radius={radius}&type={type}"
print(my_url)
score = 95.5
message = f"我的成績是 {score:10.2f}"
print(message)
print("=====================")

# 有趣信件排版應用
sp = " " * 40
print("%s   1231 Delta Rd" % sp)
print("%s   Oxford, Mississippi" % sp)
print("%s   USA\n\n\n" % sp)
print("Dear Ivan")
print("I am pleased to inform you that your application for fall 2020 has")
print("been favorably reviewed by the Electrical and Computer Engineering")
print("Office.\n\n")
print("Best Regards")
print("Peter Malong")
print("=====================")

# 開啟一個檔案 open()
# file_Obj = open(file, mode="r")   左邊只列出最常用的2個參數
'''
file: 用字串列出欲開啟檔案，若不指名則開啟目前工作資料夾
mode: 開啟檔案的模式
"r": 預設，開啟檔案供讀取(read)
"w": 開啟檔案供寫入，如果原先有內容則將被覆蓋
"a': 開啟檔案供寫入，如果原先有內容，新寫入資料將附加在後面
"x": 開啟一個新檔案供寫入，若所開啟檔案已經存在會產生錯誤
下列是第二個字母的意義，代表檔案類型
"b": 開啟二進位檔案模式
"t": 預設，開啟文字檔案模式
file_Obj: 這是檔案物件，可自行給予名稱
'''
# fstream1 = open("C:/Users/jim/Desktop/Python/file/out1.txt", mode="w")
# print("Testing for output", file=fstream1)
# fstream1.close()
# fstream2 = open("C:/Users/jim/Desktop/Python/file/out2.txt", mode="a")
# print("Testing for output", file=fstream2)
# fstream2.close()
# print("=====================")

# 資料輸入 input()
# value = input("prompt: ")
# 不知道錯誤原因???
# names = input("Input your name:")
# enghs = input("Input your score:")
# print("name的資料型態是", type(names))
# print("engh的資料型態是", type(enghs))

# print("Welcome to input your score")
# names = input("Input your name:")
# enghs = input("Input your English score:")
# math = input("Input your MAth score:")
# total = int(enghs) + int(math)
# print("%s Total score %d" % (names, total))

# clastname = input("Input your Chinese lastname:")
# cfirstname = input("Input your Chinese firstname:")
# cfullname = clastname + cfirstname
# print("%s Welcome the system" % cfullname)
# lastname = input("Input your English lastname:")
# firstname = input("Input your English firstname:")
# fullname = firstname + " " + lastname
# print("%s Welcome to SSE system" % fullname)
# print("=====================")

# 處理字串的數學運算 eval()
numberStr = input("請輸入數值公式")
number = eval(numberStr)
print("計算結果 : %5.2f" % number)  
# 列出所有內建函數 dir()
print("=====================")

# 溫度轉換
# 攝氏(Celsius) = (華氏 -32) * 5 / 9
# 華氏(Fahrenheit) = 攝氏 * (9 / 5) + 32
f = input("Input Fahrenheit:")
c = (int(f) - 32) * 5 / 9
print("Fahrenheit %s = Celsius %4.1f" % (f, c))
# 房貸問題
loan = eval(input("輸入貸款金額:"))
year = eval(input("輸入年限:"))
rate = eval(input("輸入年利率:"))
monthrate = rate / (12*100)

molecules = loan * monthrate
denominator = 1 - (1 / (1 + monthrate) ** (year * 12))
monthlyPay = molecules / denominator    # 每月還款金額
totalPay = monthlyPay * year * 12       # 總共還款金額
print("每月還款金額 %d" % int(monthlyPay))
print("總共還款金額 %d" % int(totalPay))

# 正五角形面積
s = eval(input("請輸入正五角形邊長:"))
area = (5 * s ** 2) / (4 * math.tan(math.pi / 5))
print("arae = ", area)

# 計算經緯度距離
r = 6371
x1, y1 = 22.2838, 114.1731
x2, y2 = 25.0452, 121.5168
d = 6371*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                   math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                   math.cos(math.radians(y1-y2)))
print("distance = ", d)









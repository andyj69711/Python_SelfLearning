print("hello world")


# 1.基本資料型態&變數
    #字串: "純文字"or'純文字', 想在字串裡面打雙引號前面要加/ 告訴程式這不是字串的結尾
print("hello world")
    #數字(正負都可、小數點後可有數字)
    #布林值(True or False)
    #變數命名規則
#清除指令: cls
    #字串函式
    # .lower() : 把字串變小寫回傳
    # .isupper()/.islower() : 檢查是否式大小寫，回傳true/false
phrase = "HELLO Mr.World Kk"     
print(phrase.lower())
print(phrase.isupper())
print(phrase[2])
print(phrase.index("k"))
print(phrase.replace())
print(phrase.replace("H","h"))
    #數字
    #函數
print(8/5)
print(8//5) #整數除法
print(8%5)


#2.列表
    #Python中的數字是從0開始計算
scores = [90,70,80,60,50]
print(scores[-1])        #取得scores中第幾位,負號代表倒數
print(scores[0:2])       #從第0未開始取，取道第2位，不包含第2位
print(scores[1:])        #從第1位開始取，取道列表結束
scores.extend([0,1,2])
scores.append()          #在列表後面加入一個值
scores.insert(2,30)      #在列表第2個位置插入30的值
scores.clear()           #把列表全部清空
scores.pop()             #移除列表的最後一位
scores.sort()            #把列表由小到大做排列
scores.reverse()         #把列表順序做反轉
scores.index(60)


#3.元組 tuple-----一旦創立就不能新增、修改或刪除，防止資料被意外修改
scores2 = (90,80,60,70,50)
print(len(scores2))      #也可用於取得列表長度


#4.函式 function
def hello():
    print("hello")
def add(num1,num2):
    return num1+num2      #return是用來把處理完的值回傳，若沒有回傳東西default會是none
    print("s你好")        #函式遇到return會直接結束，不會再繼續運行下去
print (add(2,3))


#5.If 判斷句
hungry = True
if hungry:                #如果hungry是 true 進入下面的程式碼
    print("去吃一蘭")
else:
    print("要餓死啦")

score = 100                #=是把右邊的值指派給左邊的variable
if score == 100:           #==是看左右兩邊的值是否相等，並回傳布林值
    print("A")
elif score >= 80:
    print("B")
elif score>=60:
    print("C")
else: 
    print("Fail")


#6. 字典 Dictionary
    # key value
    #  鍵    值
dic = {"蘋果":"apple", "橡膠":"Gum"}
print(dic["橡膠"])

#7. while 迴圈
i = 1 
while i<=5:
    print(1)
    i += 1

    print("迴圈結束")
 
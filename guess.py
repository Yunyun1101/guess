# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 “終於猜對了！”
# 猜錯的話 要告訴他 比答案大/小

import random

answer = random.randint(1, 100)

while True :
	guess = input ('請輸入1至100中的隨機整數:')
	guess = int(guess)

	if guess > answer :
		print('比答案大')
	elif guess < answer :
		print('比答案小')
	else :
		print('終於猜對了！')
		break



import random
checkcode="" #把验证码变成5位，就循环5次
for i in range(4):
	current = random.randrange(0,4)
	#i=0
	#字母
	if current ==i:
		tmp=chr(random.randint(65,90))
	#数字
	else:
		tmp=random.randint(0,9)
	#current=random.randint(1,9)
	checkcode+=str(tmp)
print(checkcode)

_author_="hejiacai"
product_list=[
   ('Iphone',5800),
   ('Mac Pro',9800),
   ('Wacth',16000),
   ('Alex Python',210)
]
shopping_list=[]
salary = input("Input your salary:")
if salary.isdigit():
	salary = int(salary)
	while True:
		for index,item in enumerate(product_list):
			print(index,item)
		#for item in product_list:
			#print(product_list.index(item),item)
		user_choice = input("选择要买嘛?>>>:")
		if user_choice.isdigit(): 
			user_choice=int(user_choice)
			if user_choice<len(product_list) and user_choice>=0:
				p_item = product_list[user_choice]
				if p_item[1] <=salary:#买得起
				    shopping_list.append(p_item)
				    salary-=p_item[1]#31 41红色  32 42绿色
				    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
		        #else:
		        	#print("\033[41;1m你的余额只剩[%s]啦,买不起\033[0m" % salary)
		elif user_choice == "q":
			print("-----shopping list-----")
			for p in shopping_list:
				print(p)
			print("Your current balance:",salary)
			exit()	
		else:
		     print("invalid option")		
		break
			

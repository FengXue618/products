
products = []
while True: # 当不知道要循环几次是，通常都选 while loop
	name = input('名称：')
	if name == 'q':  
		break
	price = input('价格：')
	#p = []
	#p.append(name)
	#p.append(price)

	# p = [name, price]   # 12, 可以取代8,9,10这三行
	# products.append(p)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的价格是：', p[1])
	

# 运行结果：







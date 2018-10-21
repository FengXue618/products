
products = []
while True: # 当不知道要循环几次是，通常都选 while loop
	name = input('请输入商品名称：')
	if name == 'q':  
		break
	price = input('请输入商品价格：')
	#p = []
	#p.append(name)
	#p.append(price)

	# p = [name, price]   # 12, 可以取代8,9,10这三行
	# products.append(p)
	products.append([name, price])
print(products)

# 请输入商品名称：coffe
# 请输入商品价格：£3   
# 请输入商品名称：ramen
# 请输入商品价格：£1.60
# 请输入商品名称：q
# [['coffe', '£3'], ['ramen', '£1.60']]






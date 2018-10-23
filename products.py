
products = []
while True: # 当不知道要循环几次是，通常都选 while loop
	name = input('名称：')
	if name == 'q':  
		break
	price = input('价格：')
	price = int(price)    # 型别转换提点  
	data = input('日期📅：')
	products.append([name, price, data])
print(products)

for p in products:
	print(p[0], '的价格是：', p[1], '日期📅：', p[2])


	
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,价格,日期\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + ',' + p[2] + '\n')








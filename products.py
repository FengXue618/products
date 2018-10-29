# 读取档案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品, 价格, 日期' in line:
			continue
		s = line.strip().split(',')
		products.append(s)
print(products)

# 写入采购数据
while True:
	name = input('名称：')
	if name == 'q':
		break
	price = input('价格：')
	data = input('日期')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price] 
	#products.append(product)
	products.append([name, price, data]) # 11,12 == 13
print(products)
# 印出购买记录
for p in products:
	print(p[0], '的价格：', p[1], ',', '日期/:', p[2])
# 写入 档案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 价格, 日期\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n')










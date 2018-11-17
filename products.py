
import os # operating system (操作系统)
# 读取档案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品, 价格, 日期' in line:
				continue
		name, price, riqi = line.strip().split(',')
		products.append([name, price, riqi])
	return products
# 用户写入采购数据
def user_input(products):
	while True:
		name = input('名称：')
		if name == 'q':
			break
		price = input('价格：')
		riqi = input('日期')
		products.append([name, price, riqi]) 
	print(products)
	return products
# 印出所有购买记录
def print_products(products):
	for p in products:
		print(p[0], '的价格是：', p[1], ',', '采购日期:', p[2])
# 写入 档案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品, 价格, 日期\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + ',' + p[2] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):  # 检查档案在不在
		print('yeah! 找到档案了')
		products = read_file(filename)	 
	else:
		print('找不到档案...')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()
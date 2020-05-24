# Преобразование числа в список
def listFromNum(num):
	num_list = []
	while num != 0:
		num_list.append(num % 10)
		num //= 10
	num_list.reverse()
	return num_list


# Преобразование списка в число
def numFromList(num_list):
	num = 0
	while num_list != [] :
		num = num * 10 + num_list[0]
		num_list.pop(0)
	return num

# Проверка, является ли данное число Капрекаровым
def kaprekar(num, base):
	num1 = listFromNum(num)
	num1.sort(reverse=True)
	num2 = []
	num2.extend(num1)
	num2.reverse()
	check = []
	i = len(num2) - 1
	while i >= 0 :
		if (num1[i] < num2[i]) :
			check.append(num1[i] + base - num2[i])
			num1[i - 1] -= 1
		else :
			check.append(num1[i] - num2[i])
		i -= 1
	check.reverse()
	result = numFromList(check)
	if result == num :
		return 1
	else :
		return 0

# Перевод числа из десятичной системы счисления в произвольную
def dec2base(dec, base):
	if base == 10:
		return dec
	list = []
	while dec > 0:
		list.append(dec % base)
		dec //= base
	list.reverse()
	num = numFromList(list)
	return num


def Lab_1():
	base_list = list(range(2, 11))
	output_list = []
	for base in base_list:
		print('Система счисления:', base)
		num = 1
		prev_len = 1
		flag = 0
		while True:
			tmp_num = dec2base(num, base)
			num_list = listFromNum(tmp_num)
			tmp_len = len(num_list)
			if tmp_len != prev_len and output_list != []:
				print('   Количество цифр:', prev_len)
				j = 0
				while j <= len(output_list) - 1:
					print('    ', output_list[j])
					j += 1
				output_list = []
			if tmp_len > 6:
				if flag == 0:
					print('     Числа Капрекара отсутствуют')
				break
			if kaprekar(tmp_num, base) == 1:
				if prev_len == tmp_len:
					output_list.append(tmp_num)
					flag = 1
			num += 1
			prev_len = tmp_len
Lab_1()

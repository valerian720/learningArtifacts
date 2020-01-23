def nextLine():
	return inp.readline()[:-1]
	
def amplif(cur_w_type):
	return (1000 if cur_w_type == "kg" else 1) * (1000 if cur_w_type == "l" else 1) * (10 if cur_w_type == "tens" else 1)
#####
money_sum = 0
ingridient_list = {}
dish_list = {}
#
with open("input.txt") as inp:
	# обработка
	dish_count = int(nextLine())
	for i in range(dish_count):
		cur_dish = nextLine().split()
		cur_dish_name = cur_dish[0]
		cu_dish_count = int(cur_dish[1])
		dish_list[cur_dish_name]={"count":int(cur_dish[1])}
		ingr_mass = []
		
		for j in range(int(cur_dish[2])):
			# обработка ингридиентов по каждому блюду
			cur_ingridient = nextLine().split()
			cur_w_type = cur_ingridient[2]
			cur_name = cur_ingridient[0]
			cur_ingr_amount = int(cur_ingridient[1]) * amplif(cur_w_type)
			ingr_mass.append([cur_name, cur_ingr_amount])
			ingridient_list[cur_name] = {"amount":(ingridient_list[cur_name]["amount"] if cur_name in ingridient_list else 0) + cur_ingr_amount * cu_dish_count, 
			"amount_per": (ingridient_list[cur_name]["amount_per"] if cur_name in ingridient_list else 0)+cur_ingr_amount}
			#print(">>>",cur_name,cur_ingr_amount)
		dish_list[cur_dish_name]["ingr"] = ingr_mass
	# получение суммы которую надо заплатить
	check_ingr_count = int(nextLine())
	for i in range (check_ingr_count):
		cur_line = nextLine().split()
		cur_w_type = cur_line[3]
		amount_per_pac = int(cur_line[2]) * amplif(cur_w_type)
		if (cur_line[0] in ingridient_list):
			dig = ingridient_list[cur_line[0]]["amount"] / amount_per_pac
			pac_count = dig // 1 + (1 if dig % 1 >0 else 0)
			ingridient_list[cur_line[0]]["pac_count"] = int(pac_count)
			money_sum += pac_count * int(cur_line[1]) 
		else:
			ingridient_list[cur_line[0]] = {"pac_count":0}
	# подгрузка пищевой ценности 
	check_ingr_count = int(nextLine())
	for i in range (check_ingr_count):
		cur_line = nextLine().split()
		if (cur_line[0] in ingridient_list):
			cur_name = cur_line[0]
			cur_w_type = cur_line[2]
			amount_per_pac = int(cur_line[1]) * amplif(cur_w_type)
			# a b c d
			#print(cur_name,amount_per_pac,ingridient_list[cur_name]["amount_per"], float(cur_line[3]))
			ingridient_list[cur_name]["a"] = float(cur_line[3]) / amount_per_pac
			ingridient_list[cur_name]["b"] = float(cur_line[4]) / amount_per_pac
			ingridient_list[cur_name]["c"] = float(cur_line[5]) / amount_per_pac
			ingridient_list[cur_name]["d"] = float(cur_line[6]) / amount_per_pac
	# сохранение пищевой ценности для каждого блюда
	for dish in dish_list:
		sum_a = 0
		sum_b = 0
		sum_c = 0
		sum_d = 0
		for ingr in dish_list[dish]["ingr"]:
			#print(dish,ingridient_list[ingr[0]]["a"])
			sum_a += ingridient_list[ingr[0]]["a"]*ingr[1]
			sum_b += ingridient_list[ingr[0]]["b"]*ingr[1]
			sum_c += ingridient_list[ingr[0]]["c"]*ingr[1]
			sum_d += ingridient_list[ingr[0]]["d"]*ingr[1]
		dish_list[dish]["a"] = round(sum_a, 3)
		dish_list[dish]["b"] = round(sum_b, 3)
		dish_list[dish]["c"] = round(sum_c, 3)
		dish_list[dish]["d"] = round(sum_d, 3)
	#print(dish_list, "\n")
	#print(ingridient_list)
	#print(money_sum)
	# вывод
	with open("output.txt", "w") as outp:
		outp.write(str(int(money_sum)))
		outp.write("\n")
		for ingr in ingridient_list:
			outp.write(ingr+" "+str(ingridient_list[ingr]["pac_count"])+"\n")
		for dish in dish_list:
			outp.write(dish+" "+str(dish_list[dish]["a"])+" "+str(dish_list[dish]["b"])+" "+str(dish_list[dish]["c"])+" "+str(dish_list[dish]["d"])+"\n" )
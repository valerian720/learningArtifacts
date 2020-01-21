# на вход:
# количество измерений
# для каждого измерения:
# - название измерения
# - количество значений

# затем заполнить все ячейки значений
######
def loadHyper(layerNum, message):
    if (layerNum>-1):
        subCube = []
        header = headers.get(layerNum)
        for i in range(header["amount"]):
            subCube.append(loadHyper(layerNum-1, message + " " + header["name"]+":"+ header["subCateg"][i]))
        return subCube
    else:
        return [int(input("введите значение по адресу "+message+" > "))]
#
def print2dSlise(slise2d, colNames, rowNames):
    print("\t"+"\t".join(colNames))
    for i in range(len(colNames)):
        print(rowNames[i]+"\t"+"\t".join([str(x[0]) for x in slise2d[i]]))

######

hypercube = []
headers = {} # num:{name, amount, subCateg:["зима","лето"]
print()
# заполнение списка заголовков
headerAmount = int(input("введите размерность> "))
if headerAmount>0:
    for i in range(headerAmount):
        name = input("введите название измерения "+str(i+1)+" порядка> ")
        amount = int(input("введите количество значений> "))
        subCategories = [input("введите название категории "+str(j+1)+" для измерения "+name+"> ") for j in range(amount)]
        headers.update({i: {'name': name, 'amount': amount, "subCateg": subCategories}})
    print (headers)

    # заполнение гиперкуба через рекурсию
    hypercube = loadHyper(headerAmount-1,"")
    print(hypercube)
else:
    headers = {0: {'name': 'suba', 'amount': 2, 'subCateg': ['shuba1', 'shuba255']}, 1: {'name': 'sezon', 'amount': 2, 'subCateg': ['zima', 'leto']}} # TODO
    hypercube = [[[1], [255]], [[2], [256]]] # TODO
# вывод значений
print2dSlise(hypercube, headers[0]["subCateg"], headers[1]["subCateg"],) # TODO
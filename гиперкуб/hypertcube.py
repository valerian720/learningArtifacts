# на вход:
# количество измерений
# для каждого измерения:
# - название измерения
# - количество значений
# - названия категорий

# затем заполнить все ячейки значений
# затем вывести срез по 2м измерениям
######
def loadHyper(layerNum, message):
    if (layerNum>-1):
        subCube = []
        header = headers.get(layerNum)
        for i in range(header["amount"]):
            subCube.append(loadHyper(layerNum-1, message + " " + header["name"] + ":" + header["subCateg"][i]))
        return subCube
    else:
        return [int(input("введите значение по адресу "+message+" > "))]
#
def print2dSlise(slise2d, colNames, rowNames):
    print("\t"+"\t".join(colNames))
    for i in range(len(colNames)):
        print(rowNames[i]+"\t"+"\t".join([str(x[0]) for x in slise2d[i]]))

def convertHyperTo2d(hypercube, curLayer, neededLayers, myPosCol, myPosRow, outMAtrix): # TODO
    if curLayer > -1:
        isInCol = (curLayer == neededLayers[0])
        isInRow = (curLayer == neededLayers[1])

        posCol = 0
        posRow = 0

        for layer in hypercube:
            # разворачивание гиперкуба до одиночного слоя, с отслеживанием его позиции в выходной матрице
            if not isInCol and not isInRow:  # дальше идёт по входным координатам
                convertHyperTo2d(layer, curLayer - 1, neededLayers, myPosCol, myPosRow, outMAtrix)
            if isInCol and not isInRow:  # дальше идёт по 0-n и myPosRow
                convertHyperTo2d(layer, curLayer - 1, neededLayers, posCol, myPosRow, outMAtrix)
                posCol += 1
            if not isInCol and isInRow:  # дальше идёт по myPosCol и 0-n
                convertHyperTo2d(layer, curLayer - 1, neededLayers, myPosCol, posRow, outMAtrix)
                posRow += 1
            if isInCol and isInRow:  # дальше идёт по myPosCol и myPosRow
                convertHyperTo2d(layer, curLayer - 1, neededLayers, posCol, posRow, outMAtrix)
                posCol += 1
                posRow += 1

    else:
        # коннактация размеченных данных в выходную матрицу
        outMAtrix[myPosCol][myPosRow] += hypercube
        # print("ячейка: ", hypercube, " ", myPosCol, " ", myPosRow)



######

hypercube = []
headers = {} # num:{name, amount, subCateg:["зима","лето"]
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
    headers = {0: {'name': 'Город', 'amount': 3, 'subCateg': ['Москва', 'Саратов', 'Кубинка']},
               1: {'name': 'время года', 'amount': 3, 'subCateg': ['зима', 'весна', 'лето']},
               2: {'name': 'одежда', 'amount': 3, 'subCateg': ['пальто', 'куртка', 'майка']}} # TODO
    hypercube = [[[[13], [15], [12]],
                  [[14], [15], [13]],
                  [[15], [16], [13]]],
                 [[[11], [16], [17]],
                  [[14], [13], [16]],
                  [[13], [15], [16]]],
                 [[[17], [14], [16]],
                  [[14], [13], [16]],
                  [[17], [15], [13]]]] # TODO

# получение двумерного среза из гиперкуба
message = "введите 2 кода измерений через пробел из списка: " + " ".join([str(x)+":"+headers[x]["name"] for x in headers]) + " > "
outIndexes = [int(x) for x in input(message).split()]
new2Dmatr = [[[] for y in range(headers[outIndexes[1]]["amount"])] for x in range(headers[outIndexes[0]]["amount"])]

convertHyperTo2d(hypercube, len(headers)-1, outIndexes, 0, 0, new2Dmatr)
# вывод значений
print2dSlise(new2Dmatr, headers[outIndexes[0]]["subCateg"], headers[outIndexes[1]]["subCateg"],) # TODO
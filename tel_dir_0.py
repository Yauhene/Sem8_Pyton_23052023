
currPos = 0
#getOut = False
# === функция чтения файла ===========================================
def readFile(fName):
    print()
    with open(fName, 'r', encoding='utf-8') as file:
        print()
        fileContent = list()
        for line in file.readlines():
            fileContent.append((list(line.split('\n')[0].split(';'))))
        # for el in fileContent:
        #     for i in range(0,len(el)):
        #         print(el[i], ' ', end = '')
            print()
        #print('Поиграемся!')
        # for i in range(0,len(fileContent)):
        #     for j in range(0,len(fileContent[i])):
        #         print(fileContent[i][j], " ", end='')
        #     print()
        #print(fileContent)
        #prAbonents(fileContent)
    file.close()
    #input()
    return fileContent

# === функция сохранения файла ===========================================
def saveFile(fName):
    print()
    # пока пусто

# === функция поиска абонента ===========================================
def findAbonent(findArg):
    #print(findArg)
    getOut = False
    found = list()
    while getOut != True:
        print('Выберите категорию поиска:')
        print('1. По номеру записи')
        print('2. По фамилии')
        print('3. По имени')
        choice = int(input('Ваш выбор: '))
        if 1 <= choice <= 4: 
            getOut = True
        
        arg = input('Введите образец поиска: ')
        arg = arg.lower()
        for ab in findArg:
            if (ab[int(choice)-1]).lower().find(arg) != -1:
                found.append(ab)
        if len(found) > 0:
            print()
            print('====== А вот чего нашлось: ==========================')
            for x in found:
                for i in x:
                    #print(f'x = {x}')
                    print(i, ' ', end='')
                print()
            print('=====================================================')        
            
        else:
            print('=====================================================')
            print(f'По образцу "', arg,'" ничего не найдено')
            print()
   

#=== функция вывода содержимого файла (fileContent)
def prAbonents(abList, currPos=0):
    outStr = ''
    for i in range(0,len(abList)):
        for j in range(0, len(abList[i])):
            outStr += abList[i][j] + ' '
        if i != currPos:
            outStr = '    ' + outStr
        else:
            outStr = '==> ' + outStr
        print(outStr)
        outStr = ''

                
# === функция поиска абонента ===========================================
def mainMenu():
    getOut=False
    while getOut != True:
        print()
        print('=========================================================')
        print('Выберите пункт меню, нажав соответствующую цифру и Enter.')
        print('1. Найти абонента')
        print('S/s Сохранить файл')
        print('Q/q. Выйти из программы')
        print()
        choice = input('Ваш выбор: ')
        if choice == '1':
            findAbonent(fileContent)
        
        if choice == '4':
            print('======================================================')
            fCont = readFile('telephone_direct.txt')
            print('======================================================')
            #input()
            
        if choice == 'Q' or choice == 'q' or choice == 'й': 
            getOut=True
            print()
            print('Дело хозяйское... До новых встреч!')
            print()

# def main():
#     mainMenu()

#main() # старт программы -------------------------------------------------------------------
fileContent = readFile('phones.txt')
prAbonents(fileContent)
mainMenu()

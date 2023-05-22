
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
def findAbon(findArg):
    print()
    # пока пусто

#=== функция вывода содержимого файла (fileContent)
def prAbonents(abList, currPos=0):
    outStr = ''
    for i in range(0,len(abList)):
        
        #print(f'Едем по i = {i}')
        for j in range(0, len(abList[i])):
            #print(f'abList[i][j] = {abList[i][j]}')
            outStr += abList[i][j] + ' '
            #print(f'outStr = {outStr}')
        
        if i != currPos:
            outStr = '    ' + outStr
            #print(outStr)
        else:
            outStr = '==> ' + outStr
            #print('out: ', outStr)
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
        print('2. Удалить абонента')
        print('3. Добавить абонента')
        print('4. Редактировать запись')
        print('Q/q. выйти из программы')
        print()
        choice = input('Ваш выбор: ')
        #print(f'choice = {choice}')
        if choice == '1':
            readFile('telephone_direct.txt')
        
        if choice == '4':
            print('======================================================')
            fCont = readFile('telephone_direct.txt')
            print('======================================================')
            #input()
            
        if choice == 'Q' or choice == 'q': 
            getOut=True
            print()
            print('Дело хозяйское... До новых встреч!')
            print()

def main():
    mainMenu()

#main() # старт программы -------------------------------------------------------------------
fileContent = readFile('telephone_direct.txt')
prAbonents(fileContent)
mainMenu()

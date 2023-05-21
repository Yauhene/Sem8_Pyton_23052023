

#getOut = False
# === функция чтения файла ===========================================
def readFile(fName):
    print()
    with open(fName, 'r', encoding='utf-8') as file:
        print()
        fileContent = list()
        for line in file.readlines():
            fileContent.append((tuple(line.split('\n')[0].split(';'))))
        for el in fileContent:
            for i in range(0,len(el)):
                print(el[i], ' ', end = '')
            print()
        #print('Поиграемся!')
        # for i in range(0,len(fileContent)):
        #     for j in range(0,len(fileContent[i])):
        #         print(fileContent[i][j], " ", end='')
        #     print()
        #print(fileContent)

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

# === функция поиска абонента ===========================================
def mainMenu():
    getOut=False
    

    while getOut != True:
        print()
        print('=========================================================')
        print('Выберите пункт меню, нажав соответствующую цифру и Enter.')
        print('1. Открыть файл')
        print('2. Добавить абонента')
        print('3. Удалить абонента')
        print('4. Найти абонента')
        print('5. Редактировать запись')
        print('Q/q. выйти из программы')
        print()
        choice = input('Ваш выбор: ')
        #print(f'choice = {choice}')
        if choice == '1':
            readFile('telephone_direct.txt')
            
        if choice == 'Q' or choice == 'q': 
            getOut=True
            print()
            print('Дело хозяйское... До новых встреч!')
            print()

def main():
    mainMenu()

#main() # старт программы -------------------------------------------------------------------
mainMenu()
Model = []
Color = []
Fara = []
Dveri = []
Wheels = []
Cost = []
#что-то пишем что-то пишем
def AddCv(cost = 0, model = '', color = '', fara = 'OFF', dveri = ['None']*4, wheels = ['None']*4):
    Model.append(model)
    Color.append(color)
    Fara.append(fara)
    Dveri.append(dveri)
    Wheels.append(wheels)
    Cost.append(cost)

def Delete(i):
    del Model[i]
    del Color[i]
    del Fara[i]
    del Dveri[i]
    del Wheels[i]
    del Cost[i]
    
def Interface():
    while True:
            print('1. Добавить машину')
            print('2. Редактировать машину')
            print('3. Посмотреть состояние машины')
            print('4. Список машин')
            print('5. Удаление машин')
            a = input()
            
            if a == '1':
                print('Введите модель')
                AddCv(model = input())   
            elif a == '2':
                for i in range(len(Model)):
                    print(i+1,') ',Model[i], sep = '')
                i = int(input())-1
                print('1. Поменять модель')
                print('2. Поменять цвет')
                print('3. Добавить/удалить колёса')
                print('4. Открыть/закрыть двери')
                print('5. Включить/выключить фары')
                print('6. Изменить стоимость')
                print('0. Назад')
                b = input()

                if b == '1':
                    print('Введите модель')
                    Model[i] = input()

                if b == '2':
                    print('Введите цвет')
                    Color[i] = input()

                if b == '3':
                    c = ''
                    while c != '0':
                        print(Wheels[i])
                        print('1. Добавить колесо')
                        print('2. Удалить колесо')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            print('Введите номер колеса')
                            Wheels[i][int(input())-1] = 'True'
                        if c == '2':
                            print('Введите номер колеса')
                            Wheels[i][int(input())-1] = 'None'
        
                if b == '4':
                    c = ''
                    while c != '0':
                        print(Dveri[i])
                        print('1. Открыть двери')
                        print('2. Закрыть двери')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            print('Введите номер двери')
                            Dveri[i][int(input())-1] = 'True'
                        if c == '2':
                            print('Введите номер двери')
                            Dveri[i][int(input())-1] = 'None'


                if b == '5':
                    c = ''
                    while c != '0':
                        print('1. Включить')
                        print('2. Выключить')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            Fara[i] = 'ON'
                        if c == '2':
                            print('Введите номер колеса')
                            Fara[i] = 'OFF'

                if b == '6':
                    print('Введите стоимость')
                    Cost[i] = int(input())

                if b == '0':
                    Interface()
                    



            elif a == '3':
                if len(Model) == 0:
                    print('Нету доступных машин')
                    input()
                else:
                    print('0. Выход')
                    for i in range(len(Model)):
                        print(i+1,') ',Model[i], sep = '')
                    i = int(input())-1
                    if i == -1:
                        a = Interface()
                    if Model[i] != '':
                        print('Модель-', Model[i])
                    if Color[i] != '':
                        print('Цвет-', Color[i])
                    print ('Фары = ',Fara[i])
                    print('Колёса-', Wheels[i])
                    print('Двери -', Dveri[i])
                    if Cost[i] != 0:
                        print('Стоимость-', Cost[i])
                       

            elif a == '4':
                if len(Model) == 0:
                    print('Машин нету')
                else:
                    for i in range(len(Model)):
                        print(i+1,') ',Model[i], sep = '')
                input()
    

            elif a == '5':
                if len(Model) == 0:
                    print('Нет машин для удаления')
                else:
                    for i in range(len(Model)):
                        print(i+1,') ',Model[i], sep = '')
                    c = int(input())
                    Delete(i) 
Interface()

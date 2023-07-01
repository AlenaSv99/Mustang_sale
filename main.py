#задача про продажу тачки на авито

class Car:
    '''описание свойств тачки'''
    def __init__(self, mark, driving_gear, speed, rule, model, color, year, volume, condition, modification, mileage, start_price, finish_price):
        self.mark = mark #марка тачки
        self.driving_gear = driving_gear #привод
        self.speed = speed #максимальная скорость
        self.rule = rule #расположение руля

        self.model = model #модель тачки - Mustang VI Рестайлинг
        self.color = color #цвет тачки
        self.year = year #год выпуска
        self.volume = volume #объём двигателя

        self.condition = condition #состояние тачки - 'Не битый, не крашеный'
        self.modification = modification #мощность двигателя - 760 л. с.
        self.mileage = mileage #пробег

        self.start_price = start_price #начальная цена на данный момент
        self.finish_price = finish_price #конечная цена

    def Sale_plus(self):
        '''расчёт цены тачки со всеми плюсами по цене (без проблемных моментов)'''
        print('Марка вашей машины: ' + self.mark + '. Это значит, что к цене добавляется 1 000 000 ₽.')
        self.finish_price += 1000000

        if 'Рестайлинг' in self.model:
            print('Надбавка за рестайлинг 65 000 ₽.')
            self.finish_price += 65000
            self.model = self.model.replace('Рестайлинг', '')

        if self.model[-3:] == 'I':
            allowance = 450000
        elif self.model[-3:] == 'II':
            allowance = 200000
        elif self.model[-3:] == 'III':
            allowance = 300000
        elif self.model[-3:] == 'IV':
            allowance = 400000
        elif self.model[-3:] == 'V':
            allowance = 500000
        else:
            allowance = 850000

        print('Поколение вашей машины: ' + self.model[-3:] + ', тогда надбавка к стоимости составит: ' + str(allowance) + ' ₽.')
        self.finish_price += allowance
        return self.finish_price

    def Sale_grabezh(self):
        '''расчёт цены тачки с учётом всех минусов по цене (с проблемными моментами)'''
        if 220 <= self.modification < 300:
            reduction = 10000
        elif 300 <= self.modification < 450:
            reduction = 45000
        elif 450 <= self.modification < 600:
            reduction = 67500
        elif 600 <= self.modification < 900:
            reduction = 127500
        else:
            reduction = 130000

        print('Мощность вашего автомобиля: ' + str(self.modification) + ', тогда от цены отнимется годовой налог в размере ' + str(reduction) + ' ₽.')
        self.finish_price -= reduction

        if self.mileage < 20000:
            print('Ваш пробег составляет: ' + str(self.mileage) + 'КМ. В таком случае к цене прибавляется 35000 ₽.')
            self.finish_price += 35000
        elif 20000 <= self.mileage < 80000:
            print('Ваш пробег составляет: ' + str(self.mileage) + 'КМ. В таком случае цена никак не изменится')
        else:
            print('Ваш пробег составляет: ' + str(self.mileage) + 'КМ. В таком случае от цены отнимается ' + str(17000 + 6000 * ((self.mileage / 10000) - 8)) + ' ₽.')
            self.finish_price -= 17000 + 6000 * ((self.mileage / 10000) - 8)

        self.finish_price -= minus_price
        return self.finish_price

    def Info_of_Price(self):
        print('В среднем похожие на ваш автомобиль автомобили стоят ' + str(self.start_price) + ' ₽. Цена вашей машины: ' + str(self.finish_price) + ' ₽')
        otv = input('Согласны ли вы с такой ценой? >> ').lower()
        if otv == 'да':
            print('Супер!')
        else:
            print('Ты че чучело')

    def get_Price(self):
        price = self.finish_price
        return price

mark = 'Ford'
driving_gear = 'RWD'
speed = '270 км/ч'
rule = 'левый'
kpp = 'АКПП'

start_price = 3000000 #средняя рыночная цена
finish_price = 0

model = input('Введите модель вашей машины марки Ford: ')
color = input('Введите цвет машины: ')
year = int(input('Введите год выпуска вашей машины: '))
modification = int(input('Введите мощность вашего автомобиля в Л.С.: '))
volume = float(input('Введите объём вашей машины: '))
mileage = int(input('Введите пробег в КМ: '))

condition = input('Опишите словами состояние вашей машины: ').lower()
condition_1 = int(input('Оцените степень повреждений вашей машины от 0 до 10, где 0 - нет повреждений, 10 - машина полность разбита (только цифра): '))
if 0 <= condition_1 <= 2:
    print('В таком случае цена никак не изменится')
    minus_price = 0
elif 3 <= condition_1 <= 5:
    print('В таком случае от цены отнимается 130 000 рублей')
    minus_price = 130000
elif 6 <= condition_1 <= 8:
    print('В таком случае от цены отнимается 200 000 рублей')
    minus_price = 200000
else:
    print('В таком случае от цены отнимается 500 000 рублей')
    minus_price = 500000

city = input('Укажите, в каком городе продаёте машину: ')

mustang = Car(mark, driving_gear, speed, rule, model, color, year, volume, condition, modification, mileage, start_price, finish_price)
mustang.Sale_plus()
mustang.Sale_grabezh()
mustang.Info_of_Price()
ford = mustang.get_Price()
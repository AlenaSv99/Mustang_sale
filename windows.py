from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import main as m

answer = input('Выберите, с телефона (1) или с компьютера (2) хотите посмотреть превью объявления >> ').lower()
if answer == '1' or answer == 'с телефона':
    W1 = Tk()
    W1.geometry('460x750+600+10')  #окно размером 460x750, смещённое вправо на 600 п и вниз на 10 п
    W1.resizable(False, False)  #размеры окна нельзя изменить
    W1.title('Не бойся, когда ты один, бойся, когда ты два')
    W1.iconphoto(False, PhotoImage(file='window_icon.png')) #иконка окна

    '''создание и размещение заголовка объявления'''
    title_mob = ttk.Label(text='Продажа Ford Mustang, ' + str(m.year) + ' год ' + m.city, font="Arial 18 bold roman")
    title_mob.pack(anchor='nw', padx=20, pady=10)

    '''загрузка телефонных версий картинок'''
    picture1 = PhotoImage(file='Car_Mobila/p.png')
    picture1_mini = PhotoImage(file='Car_Mobila/p_mini.png')

    picture2 = PhotoImage(file='Car_Mobila/p1.png')
    picture2_mini = PhotoImage(file='Car_Mobila/p1_mini.png')

    picture3 = PhotoImage(file='Car_Mobila/p2.png')
    picture3_mini = PhotoImage(file='Car_Mobila/p2_mini.png')

    picture4 = PhotoImage(file='Car_Mobila/p3.png')
    picture4_mini = PhotoImage(file='Car_Mobila/p3_mini.png')

    picture5 = PhotoImage(file='Car_Mobila/p4.png')
    picture5_mini = PhotoImage(file='Car_Mobila/p4_mini.png')

    picture6 = PhotoImage(file='Car_Mobila/p5.png')
    picture6_mini = PhotoImage(file='Car_Mobila/p5_mini.png')

    '''создание фрейма, в котором находятся основная картинка и миниатюры остальных'''
    mob_frame = Frame(W1)
    main_pic = ttk.Button(image=picture1)
    main_pic.pack()

    def change_main_pic(image):
        main_pic['image'] = image

    pic1 = ttk.Button(mob_frame, image=picture1_mini, command=lambda f=picture1: change_main_pic(f))
    pic2 = ttk.Button(mob_frame, image=picture2_mini, command=lambda f=picture2: change_main_pic(f))
    pic3 = ttk.Button(mob_frame, image=picture3_mini, command=lambda f=picture3: change_main_pic(f))
    pic4 = ttk.Button(mob_frame, image=picture4_mini, command=lambda f=picture4: change_main_pic(f))
    pic5 = ttk.Button(mob_frame, image=picture5_mini, command=lambda f=picture5: change_main_pic(f))
    pic6 = ttk.Button(mob_frame, image=picture6_mini, command=lambda f=picture6: change_main_pic(f))
    mob_frame.pack()
    pic1.pack(side=LEFT)
    pic2.pack(side=LEFT)
    pic3.pack(side=LEFT)
    pic4.pack(side=LEFT)
    pic5.pack(side=LEFT)
    pic6.pack(side=LEFT)

    '''размещение надписи с ценой машины и цветной метки с характеристикой цены'''
    price = ttk.Label(text=str(m.ford) + ' ₽', font="Arial 20 bold roman")
    price.pack(anchor='nw', padx=20, pady=6)

    if m.start_price - m.ford >= 1500000:
        info_price = ttk.Label(text='отличная цена', background='#009933', foreground='white')
        info_price.pack(anchor="nw", padx=20, pady=6)
    elif 500000 <= m.start_price - m.ford < 1500000:
        info_price = ttk.Label(text='хорошая цена', background='#91e39c', foreground='#27573e')
        info_price.pack(anchor="nw", padx=20, pady=6)
    elif 200000 <= m.start_price - m.ford <= 500000:
        info_price = ttk.Label(text='нормальная цена', background='#b4f0c5', foreground='#57ad80')
        info_price.pack(anchor="nw", padx=20, pady=6)
    elif 0 <= m.start_price - m.ford < 200000 or m.ford > m.start_price:
        info_price = ttk.Label(text='высокая цена', background='#b8b8b8', foreground='#545252')
        info_price.pack(anchor="nw", padx=20, pady=6)

    main_frame = ttk.Frame(W1, borderwidth=1, relief=SOLID)
    main_frame.pack(anchor='nw', padx=15)
    frame_left = ttk.Frame(main_frame, borderwidth=1, relief=SOLID)
    frame_right = ttk.Frame(main_frame, borderwidth=1, relief=SOLID)
    frame_left.pack(anchor='nw', side=LEFT)
    frame_right.pack(anchor='nw', side=LEFT)

    har_1 = ttk.Label(frame_left, text='Двигатель', foreground='grey', font="Arial 12 roman")
    har_2 = ttk.Label(frame_left, text='Мощность', foreground='grey', font="Arial 12 roman")
    har_3 = ttk.Label(frame_left, text='Коробка передач', foreground='grey', font="Arial 12 roman")
    har_4 = ttk.Label(frame_left, text='Привод', foreground='grey', font="Arial 12 roman")
    har_5 = ttk.Label(frame_left, text='Цвет', foreground='grey', font="Arial 12 roman")
    har_6 = ttk.Label(frame_left, text='Пробег, км', foreground='grey', font="Arial 12 roman")
    har_7 = ttk.Label(frame_left, text='Руль', foreground='grey', font="Arial 12 roman")
    har_8 = ttk.Label(frame_left, text='Поколение', foreground='grey', font="Arial 12 roman")

    har_9 = ttk.Label(frame_right, text='бензин, ' + str(m.volume) + ' л', foreground='black', font="Arial 12 roman")
    har_10 = ttk.Label(frame_right, text=str(m.modification) + ' л.с.', foreground='black', font="Arial 12 roman")
    har_11 = ttk.Label(frame_right, text=m.kpp, foreground='black', font="Arial 12 roman")
    har_12 = ttk.Label(frame_right, text=m.driving_gear, foreground='black', font="Arial 12 roman")
    har_13 = ttk.Label(frame_right, text=m.color, foreground='black', font="Arial 12 roman")
    har_14 = ttk.Label(frame_right, text=str(m.mileage), foreground='black', font="Arial 12 roman")
    har_15 = ttk.Label(frame_right, text=m.rule, foreground='black', font="Arial 12 roman")
    dop1 = m.model.replace(' Рестайлинг', '')
    har_16 = ttk.Label(frame_right, text=dop1[-3:], foreground='black', font="Arial 12 roman")

    har_1.pack(anchor="nw", padx=20, pady=2)
    har_2.pack(anchor="nw", padx=20, pady=2)
    har_3.pack(anchor="nw", padx=20, pady=2)
    har_4.pack(anchor="nw", padx=20, pady=2)
    har_5.pack(anchor="nw", padx=20, pady=2)
    har_6.pack(anchor="nw", padx=20, pady=2)
    har_7.pack(anchor="nw", padx=20, pady=2)
    har_8.pack(anchor="nw", padx=20, pady=2)

    har_9.pack(anchor="nw", padx=20, pady=2)
    har_10.pack(anchor="nw", padx=20, pady=2)
    har_11.pack(anchor="nw", padx=20, pady=2)
    har_12.pack(anchor="nw", padx=20, pady=2)
    har_13.pack(anchor="nw", padx=20, pady=2)
    har_14.pack(anchor="nw", padx=20, pady=2)
    har_15.pack(anchor="nw", padx=20, pady=2)
    har_16.pack(anchor="nw", padx=20, pady=2)

    title_text = ttk.Label(text='Введите описание машины:', font="Arial 13 roman")
    title_text.pack(anchor='nw', padx=20, pady=10)
    comment = ScrolledText(width=50, height=10, wrap='word')
    comment.pack(fill=BOTH, expand=True)

    W1.mainloop()

elif answer == '2' or answer == 'с компьютера':
    W2 = Tk()
    W2.title('Окно для пекаря')
    w = W2.winfo_screenwidth()  # ширина экрана
    h = W2.winfo_screenheight()  # высота экрана
    W2.geometry(f'{w}x{h}')
    W2.iconphoto(False, PhotoImage(file='window_icon.png')) # иконка окна

    '''создание и размещение заголовка объявления'''
    title_comp = ttk.Label(text='Продажа Ford Mustang, ' + str(m.year) + ' год ' + m.city, font="Arial 26 bold roman")
    title_comp.pack(anchor='nw', padx=60, pady=25)

    '''загрузка компьютерных версий картинок'''
    picture = PhotoImage(file='Car_Pk/comp_pic.png')
    picture_mini = PhotoImage(file='Car_Pk/comp_pic_mini.png')

    picture1 = PhotoImage(file='Car_Pk/comp_pic1.png')
    picture1_mini = PhotoImage(file='Car_Pk/comp_pic1_mini.png')

    picture2 = PhotoImage(file='Car_Pk/comp_pic2.png')
    picture2_mini = PhotoImage(file='Car_Pk/comp_pic2_mini.png')

    picture3 = PhotoImage(file='Car_Pk/comp_pic3.png')
    picture3_mini = PhotoImage(file='Car_Pk/comp_pic3_mini.png')

    picture4 = PhotoImage(file='Car_Pk/comp_pic4.png')
    picture4_mini = PhotoImage(file='Car_Pk/comp_pic4_mini.png')

    picture5 = PhotoImage(file='Car_Pk/comp_pic5.png')
    picture5_mini = PhotoImage(file='Car_Pk/comp_pic5_mini.png')

    '''создание самого главного фрейма, в котором находятся два менее главных'''
    batya_frame = ttk.Frame(W2, borderwidth=1, relief=SOLID)
    batya_frame.pack(anchor='nw')

    '''создание первого основного фрейма, с верхним фреймом (картинки и инфо о тачке) и нижним фреймом (текстовое поле для ввода)'''
    main_frame1 = ttk.Frame(batya_frame, borderwidth=1, relief=SOLID)
    main_frame1.pack(side=LEFT)

    frame_top = ttk.Frame(main_frame1, borderwidth=1, relief=SOLID)
    frame_top.pack()
    frame_left = ttk.Frame(frame_top, borderwidth=1, relief=SOLID) # создание левого фрейма, прикреплённого к основному
    frame_left.pack(side=LEFT, anchor='nw', padx=60, pady=10)

    main_pic = ttk.Button(frame_left, image=picture)
    main_pic.pack()

    def change_gl_pic(image):
        main_pic['image'] = image

    car_pic1_pk = ttk.Button(frame_left, image=picture_mini, command=lambda x=picture: change_main_pic(x))
    car_pic2_pk = ttk.Button(frame_left, image=picture1_mini, command=lambda x=picture1: change_main_pic(x))
    car_pic3_pk = ttk.Button(frame_left, image=picture2_mini, command=lambda x=picture2: change_main_pic(x))
    car_pic4_pk = ttk.Button(frame_left, image=picture3_mini, command=lambda x=picture3: change_main_pic(x))
    car_pic5_pk = ttk.Button(frame_left, image=picture4_mini, command=lambda x=picture4: change_main_pic(x))
    car_pic6_pk = ttk.Button(frame_left, image=picture5_mini, command=lambda x=picture5: change_main_pic(x))

    car_pic1_pk.pack(side=LEFT)
    car_pic2_pk.pack(side=LEFT)
    car_pic3_pk.pack(side=LEFT)
    car_pic4_pk.pack(side=LEFT)
    car_pic5_pk.pack(side=LEFT)
    car_pic6_pk.pack(side=LEFT)

    frame_right = ttk.Frame(frame_top, borderwidth=1, relief=SOLID) # создание правого фрейма, прикреплённого к основному
    frame_right.pack(side=RIGHT, anchor='nw', padx=60, pady=10)

    '''размещение надписи с ценой машины и цветной метки с характеристикой цены'''
    car_price = str(m.ford) + ' ₽'
    price = ttk.Label(frame_right, text=car_price, font="Arial 24 bold roman")
    price.pack(anchor='nw', pady=10)

    if m.start_price - m.ford >= 1500000:
        info_price = ttk.Label(frame_right, text='отличная цена', background='#009933', foreground='white')
        info_price.pack(anchor="nw", padx=3, pady=6)
    elif 500000 <= m.start_price - m.ford < 1500000:
        info_price = ttk.Label(frame_right, text='хорошая цена', background='#91e39c', foreground='#27573e')
        info_price.pack(anchor="nw", padx=3, pady=6)
    elif 200000 <= m.start_price - m.ford <= 500000:
        info_price = ttk.Label(frame_right, text='нормальная цена', background='#b4f0c5', foreground='#57ad80')
        info_price.pack(anchor="nw", padx=3, pady=6)
    elif 0 <= m.start_price - m.ford < 200000 or m.ford > m.start_price:
        info_price = ttk.Label(frame_right, text='высокая цена', background='#b8b8b8', foreground='#545252')
        info_price.pack(anchor="nw", padx=3, pady=6)

    frame_right1 = ttk.Frame(frame_right, borderwidth=1, relief=SOLID)
    frame_right2 = ttk.Frame(frame_right, borderwidth=1, relief=SOLID)
    frame_right1.pack(anchor='nw', side=LEFT)
    frame_right2.pack(anchor='nw', side=LEFT)

    har_1 = ttk.Label(frame_right1, text='Двигатель', foreground='grey', font="Arial 12 roman")
    har_2 = ttk.Label(frame_right1, text='Мощность', foreground='grey', font="Arial 12 roman")
    har_3 = ttk.Label(frame_right1, text='Коробка передач', foreground='grey', font="Arial 12 roman")
    har_4 = ttk.Label(frame_right1, text='Привод', foreground='grey', font="Arial 12 roman")
    har_5 = ttk.Label(frame_right1, text='Цвет', foreground='grey', font="Arial 12 roman")
    har_6 = ttk.Label(frame_right1, text='Пробег, км', foreground='grey', font="Arial 12 roman")
    har_7 = ttk.Label(frame_right1, text='Руль', foreground='grey', font="Arial 12 roman")
    har_8 = ttk.Label(frame_right1, text='Поколение', foreground='grey', font="Arial 12 roman")

    har_9 = ttk.Label(frame_right2, text='бензин, ' + str(m.volume) + ' л', foreground='black', font="Arial 12 roman")
    har_10 = ttk.Label(frame_right2, text=str(m.modification) + ' л.с.', foreground='black', font="Arial 12 roman")
    har_11 = ttk.Label(frame_right2, text=m.kpp, foreground='black', font="Arial 12 roman")
    har_12 = ttk.Label(frame_right2, text=m.driving_gear, foreground='black', font="Arial 12 roman")
    har_13 = ttk.Label(frame_right2, text=m.color, foreground='black', font="Arial 12 roman")
    har_14 = ttk.Label(frame_right2, text=str(m.mileage), foreground='black', font="Arial 12 roman")
    har_15 = ttk.Label(frame_right2, text=m.rule, foreground='black', font="Arial 12 roman")
    dop1 = m.model.replace(' Рестайлинг', '')
    har_16 = ttk.Label(frame_right2, text=dop1[-3:], foreground='black', font="Arial 12 roman")

    har_1.pack(anchor="nw", pady=5)
    har_2.pack(anchor="nw", pady=5)
    har_3.pack(anchor="nw", pady=5)
    har_4.pack(anchor="nw", pady=5)
    har_5.pack(anchor="nw", pady=5)
    har_6.pack(anchor="nw", pady=5)
    har_7.pack(anchor="nw", pady=5)
    har_8.pack(anchor="nw", pady=5)

    har_9.pack(anchor="nw", padx=5, pady=5)
    har_10.pack(anchor="nw", padx=5, pady=5)
    har_11.pack(anchor="nw", padx=5, pady=5)
    har_12.pack(anchor="nw", padx=5, pady=5)
    har_13.pack(anchor="nw", padx=5, pady=5)
    har_14.pack(anchor="nw", padx=5, pady=5)
    har_15.pack(anchor="nw", padx=5, pady=5)
    har_16.pack(anchor="nw", padx=5, pady=5)

    frame_bottom = ttk.Frame(main_frame1, borderwidth=1, relief=SOLID)
    frame_bottom.pack()
    title_text = ttk.Label(frame_bottom, text='Введите описание машины:', font="Arial 13 roman")
    title_text.pack(anchor='sw', padx=40, pady=10)
    comment = ScrolledText(frame_bottom, width=127, height=10, wrap='word')
    comment.pack(expand=True, padx=40)

    main_frame2 = ttk.Frame(batya_frame, borderwidth=1, relief=SOLID)
    main_frame2.pack(side=LEFT, anchor='ne')
    i = PhotoImage(file="Car_Pk/reklama.png")
    advertisement = ttk.Label(main_frame2, image=i)
    advertisement.pack()

    W2.mainloop()
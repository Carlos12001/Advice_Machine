from tkinter import *
import random, time
from threading import Thread

# Colores

dark_green = "#718C85"
brown = "#CBBAA6"
dark_yellow = "#E8B623"
purple = "#A4ACC3"
white = "#FFFFFF"
gray = "#AEAEAE"
black = "#000000"
red_light = '#c26d06'
# fonts

font1 = ("fixedsys", 25)
font2 = ("fixedsys", 50)
font3 = ("arial", 18)
font4 = ("fixedsys", 20)
font5 = ("fixedsys", 18)


# -------------------------- Bases de datos ----------------------------- #

def load_base(idioma):
    if idioma == "español":
        rute = "Data/base_espa.txt"
    elif idioma == "ingles":
        rute = "Data/base_ing.txt"
    file = open(rute, "r")
    conse_base = []  # varibale qu alamcena los consejos
    dicho_base = []  # variable que almacena los dichos
    chiste_base = []  # variable que almacena los chistes
    cont = 0
    for line in file:
        if 0 <= cont <= 16:
            conse_base.append(line)
            cont +=1
        elif 16 < cont <= 33:
            dicho_base.append(line)
            cont += 1
        elif 33 < cont <= 50:
            chiste_base.append(line)
            cont += 1
    file.close()
    print(conse_base)
   0#print(dicho_base)
    #print(chiste_base)

# -------------------------- Setea el idioma ---------------------------- #
def set_idi(idioma):
    global glo_idioma, reset_var, off_var, return_var, ex_var
    global conse_var, dicho_var, chiste_var, coins_var, sms, rest_var
    global titulo_ventana_ms

    glo_idioma = idioma
    if idioma == "español":
        # Texto machine
        conse_var = "Consejos"
        dicho_var = "Dichos"
        chiste_var = "Chistes"
        coins_var = "Su dinero"
        sms = "Su selección es:"
        titulo_ventana_ms = 'Paper'
        rest_var = "Monto a pagar: "
        # Texto admin
        reset_var = "Restaurar"
        off_var = "Apagar"
        return_var = "Volver"
        ex_var = "Generar Excel"
        load_base(idioma)
    elif idioma == "ingles":
        # Texto machine
        conse_var = "Advice"
        dicho_var = "Sayings"
        chiste_var = "Jokes"
        coins_var = "Your cash"
        sms = "Your selection is:"
        titulo_ventana_ms = 'Papel'
        rest_var = "Amount to be paid: "
        # Texto admin
        reset_var = "Reset"
        off_var = "Turn off"
        return_var = "Return"
        ex_var = "Generate Excel"

        # ----logica para cargar archivo en englicsj---


# ---------------------------  Abrir Ventanas  ---------------------------- #

def openAdmin(window, idioma):
    window.destroy()
    set_idi(idioma)
    admin()


def openMachine(window, idioma):
    window.destroy()
    set_idi(idioma)
    machine()


# ---------------------------  tienda  ---------------------------- #

def set_shop(tipo):
    global sms, conse_var, dicho_var, chiste_var, screen_sms, active_shop, price_str, rest_var, price
    # tipo consejo
    if tipo == 1 and active_shop:
        screen_sms.set(sms + "\n" + conse_var)
        active_shop = False
        price = 250
        price_str.set(rest_var + str(price))  # agregar variable que cambie
    # tipo dicho
    elif tipo == 2 and active_shop:
        screen_sms.set(sms + "\n" + dicho_var)
        active_shop = False
        price = 500
        price_str.set(rest_var + str(price))
    # tipo chiste
    elif tipo == 3 and active_shop:
        screen_sms.set(sms + "\n" + chiste_var)
        active_shop = False
        price = 700
        price_str.set(rest_var + str(price))


def shop(pay):
    global price_str, price
    if (price - pay) >= 0:
        price -= pay
        price_str.set(rest_var + str(price))
    elif (price - pay) == 0:
        # logica de print
        pass
    else:
        price = -1 * (price - pay)
        money.set(price)
        # logica vuelto
        pass


def coins_rest(type1, window):
    global price, money_tmp, price_str, money
    if price > 0:
        if type1 == 25:
            price -= 25
            money_tmp -= 25
            price_str.set(rest_var + str(price))
            money.set(money_tmp)
            return paying(window)
        elif type1 == 50:
            price -= 50
            money_tmp -= 50
            price_str.set(rest_var + str(price))
            money.set(money_tmp)
            return paying(window)
        elif type1 == 100:
            price -= 100
            money_tmp -= 100
            price_str.set(rest_var + str(price))
            money.set(money_tmp)
            return paying(window)
        elif type1 == 500:
            price -= 500
            money_tmp -= 500
            price_str.set(rest_var + str(price))
            money.set(money_tmp)
            return paying(window)


# --------------------------- Animacion ---------------------------- #

def paying(window):
    global price, rest_var, money, price_str, money_tmp
    if price > 0:
        pass
    elif price == 0:
        return paying_aux(window)
    elif price < 0:
        price = -1 * price
        money_tmp += price
        money.set(money_tmp)
        price_str.set("Su vuelto es: " + str(price))
        return paying_aux(window)


def paying_aux(window):
    t = Thread(name='Ani_Paper', target=paying_aux_2, args=(window,))
    t.daemon = True
    t.start()


def paying_aux_2(window):
    global image_paper, all_canvas
    anchor = 20
    all_canvas = []
    image_paper = Canvas(window, width=300, height=anchor)
    all_canvas += [image_paper]
    while anchor < 300:
        anchor += 20
        time.sleep(0.5)
        image_paper = Canvas(window, width=300, height=anchor)
        image_paper.place(x=110, y=310)
        all_canvas += [image_paper]

    image_paper.bind("<Button-1>", paying_aux_3)


def paying_aux_3(s):
    global all_canvas, titulo_ventana_ms
    for i in all_canvas:
        i.place(x=-1000)
    window = Tk()
    window.resizable(width=False, height=False)
    window.geometry('500x500+350+250')
    window.title(titulo_ventana_ms)

    window.mainloop()


# --------------------------- Ventanas ---------------------------- #

def idioma_screen():
    # Ventana principal, aqui se encuentra la animacion

    idi_screen = Tk()  # se crea una ventana de inicio
    idi_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    idi_screen.geometry("1200x800+100+100")
    idi_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvas_idio = Canvas(idi_screen, width=1200, height=800, bg=purple, highlightbackground=dark_green)
    canvas_idio.pack()

    # Botones

    button_español = Button(idi_screen, text="Español", font=font1, bg=dark_yellow,
                            activebackground=purple, activeforeground=dark_yellow,
                            command=lambda x=idi_screen, y="español": openMachine(x, y))
    button_español.place(x=200, y=400, width=300, height=100)

    button_ingles = Button(idi_screen, text="English", font=font1, bg=dark_yellow,
                           activebackground=purple, activeforeground=dark_yellow,
                           command=lambda x=idi_screen, y="ingles": openMachine(x, y))
    button_ingles.place(x=700, y=400, width=300, height=100)

    # Texto
    canvas_idio.create_text(600, 100, text="Idioma / Language", font=font2)

    mainloop()


def machine():
    set_idi("español")
    global conse_var, dicho_var, chiste_var, coins_var, money, screen_sms, price_str, money_tmp
    global active_shop, im_printing

    # Variables de la ventana
    active_shop = True
    money = 1000

    # Ventana principal, aqui se encuentra la animacion

    machine_screen = Tk()  # se crea una ventana de inicio
    machine_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    machine_screen.geometry("1200x800+100+100")
    machine_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(machine_screen, width=1200, height=800, bg=dark_green, highlightbackground=dark_green)
    canvasP.pack()

    # Botones

    button_Conse = Button(machine_screen, text=conse_var, font=font3, bg=dark_yellow,
                          activebackground=purple, activeforeground=dark_yellow, relief=SUNKEN,
                          command=lambda x=1: set_shop(x))
    button_Conse.place(x=850, y=300, width=100, height=50)

    button_Dicho = Button(machine_screen, text=dicho_var, font=font3, bg=dark_yellow,
                          activebackground=purple, activeforeground=dark_yellow, relief=SUNKEN,
                          command=lambda x=2: set_shop(x))
    button_Dicho.place(x=850, y=370, width=100, height=50)

    button_chiste = Button(machine_screen, text=chiste_var, font=font3, bg=dark_yellow,
                           activebackground=purple, activeforeground=dark_yellow, relief=SUNKEN,
                           command=lambda x=3: set_shop(x))
    button_chiste.place(x=850, y=440, width=100, height=50)

    button_admin = Button(machine_screen, text="ADMIN", font=font3, bg=gray,
                          activebackground=purple, activeforeground=dark_yellow, relief=SUNKEN,
                          command=lambda x=machine_screen, y=glo_idioma: openAdmin(x, y))
    button_admin.place(x=850, y=700, width=100, height=50)

    button_pay = Button(
        machine_screen, text='PUSH ME ( ͡° ͜ʖ ͡°)', font=font3, bg=red_light,
        command=lambda x=machine_screen: paying(x))
    button_pay.place(x=750, y=560)

    # Boton monedas
    button_coin25 = Button(machine_screen, text=25, font=font3, bg=brown, relief=FLAT,
                           command=lambda x=25, y=machine_screen: coins_rest(x, y))
    button_coin25.place(x=1050, y=150, width=100, height=100)

    button_coin50 = Button(machine_screen, text=50, font=font3, bg=brown, relief=FLAT,
                           command=lambda x=50, y=machine_screen: coins_rest(x, y))
    button_coin50.place(x=1050, y=300, width=100, height=100)

    button_coin100 = Button(machine_screen, text=100, font=font3, bg=brown, relief=FLAT,
                            command=lambda x=100, y=machine_screen: coins_rest(x, y))
    button_coin100.place(x=1050, y=450, width=100, height=100)

    button_coin500 = Button(machine_screen, text=500, font=font3, bg=brown, relief=FLAT,
                            command=lambda x=500, y=machine_screen: coins_rest(x, y))
    button_coin500.place(x=1050, y=600, width=100, height=100)

    # Etiquetas
    screen_sms = StringVar()
    consola = Label(machine_screen, textvariable=screen_sms, font=font5, bg=purple)
    consola.place(x=685, y=70, width=290, height=100)

    money = StringVar()
    money_tmp = random.randrange(100, 2000, 25)
    money.set(money_tmp)

    monedas = Label(machine_screen, textvariable=money, font=font4, bg=white)
    monedas.place(x=1020, y=90, width=160, height=50)

    price_str = StringVar()
    precio_consol = Label(machine_screen, textvariable=price_str, font=font4, bg=purple)
    precio_consol.place(x=685, y=200, width=290, height=50)

    # Dibujos en pantalla
    canvasP.create_rectangle(1000, 0, 1200, 800, fill=brown, outline=brown)
    canvasP.create_rectangle(680, 20, 980, 280, fill=purple, outline=purple)
    canvasP.create_rectangle(50, 200, 650, 400, width=15, outline='#959593')
    image_printa = PhotoImage(file='resource/printa.png')
    canvasP.create_image(350, 300, image=image_printa)

    canvasP.create_rectangle(1020, 90, 1180, 140, fill=white, outline=black)

    # texto
    canvasP.create_text(350, 50, text="ADVICE MACHINE", font=font2, fill=dark_yellow)
    canvasP.create_text(1100, 45, text=coins_var, font=font4, fill=dark_green)
    canvasP.create_text(1100, 115, text=str(money), font=font4, fill=black)

    mainloop()


def admin():
    global glo_idioma, reset_var, off_var, return_var, ex_var

    # Ventana principal, aqui se encuentra la animacion

    admin_screen = Tk()  # se crea una ventana de inicio
    admin_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    admin_screen.geometry("1200x800+100+100")
    admin_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(admin_screen, width=1200, height=800, bg=gray, highlightbackground=gray)
    canvasP.pack()

    # Botones   HACER EL TEXTO VARIABLE
    # Volver a la maquina
    button_return = Button(admin_screen, text=return_var, font=font4, bg=gray,
                           activebackground=purple, activeforeground=dark_yellow,
                           command=lambda x=admin_screen, y=glo_idioma: openMachine(x, y))
    button_return.place(x=20, y=700, width=350, height=50)
    # Resetear la maquina
    button_reset = Button(admin_screen, text=reset_var, font=font4, bg=gray,
                          activebackground=purple, activeforeground=dark_yellow)
    button_reset.place(x=20, y=400, width=350, height=50)
    # Apagar la maquina
    button_off = Button(admin_screen, text=off_var, font=font4, bg=gray,
                        activebackground=purple, activeforeground=dark_yellow)
    button_off.place(x=20, y=500, width=350, height=50)
    # Excel
    button_ex = Button(admin_screen, text=ex_var, font=font4, bg=gray,
                       activebackground=purple, activeforeground=dark_yellow)
    button_ex.place(x=20, y=600, width=350, height=50)

    # Dibujos
    canvasP.create_rectangle(400, 20, 1180, 780, fill=white)

    mainloop()


if __name__ == "__main__":
    idioma_screen()

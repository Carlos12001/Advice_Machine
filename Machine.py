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
red_light='#c26d06'
# fonts

font1 = ("fixedsys", 25)
font2 = ("fixedsys", 50)
font3 = ("arial", 18)
font4 = ("fixedsys", 20)
font5 = ("fixedsys", 18)


# Cargar idioma


def set_idi (idioma):
    global glo_idioma, reset_var, off_var, return_var, ex_var
    global conse_var, dicho_var, chiste_var, coins_var, sms
    global cost_sms, titulo_ventana_ms
    glo_idioma = idioma
    if idioma == "español":
        # Texto machine
        conse_var = "Consejos"
        dicho_var = "Dichos"
        chiste_var = "Chistes"
        coins_var = "Su dinero"
        sms = "Su selección es:"
        cost_sms = 'Tienes que pagar:'
        titulo_ventana_ms = 'Paper'
        # Texto admin
        reset_var = "Restaurar"
        off_var = "Apagar"
        return_var = "Volver"
        ex_var = "Generar Excel"
    elif idioma == "ingles":
        # Texto machine
        conse_var = "Advice"
        dicho_var = "Sayings"
        chiste_var = "Jokes"
        coins_var = "Your cash"
        sms = "Your selection is:"
        cost_sms  = 'You need to pay:'
        titulo_ventana_ms = 'Papel'
        # Texto admin
        reset_var = "Reset"
        off_var = "Turn off"
        return_var = "Return"
        ex_var = "Generate Excel"

        # ----logica para cargar archivo en englicsj---

# ---------------------------  Abriri Ventanas  ---------------------------- #


def openAdmin(window, idioma):
    window.destroy()
    set_idi(idioma)
    admin()


def openMachine(window, idioma):
    global money
    money = random.randrange(100, 2000, 25)
    window.destroy()
    set_idi(idioma)
    machine()

# ---------------------------  tienda  ---------------------------- #

def shop (tipo):
    global sms, conse_var, dicho_var, chiste_var, screen_sms, active_shop
    # tipo consejo
    if tipo == 1 and active_shop:
        screen_sms.set(sms + "\n" + conse_var)
        active_shop = False

    # tipo dicho
    elif tipo == 2 and active_shop:
        screen_sms.set(sms + "\n" + dicho_var)
        active_shop = False
    # tipo chiste
    elif tipo == 3 and active_shop:
        screen_sms.set(sms + "\n" + chiste_var)
        active_shop = False


# --------------------------- Animacion ---------------------------- #

def paying(window):
    if 0<18:
        return paying_aux(window)
    else:
        pass

def paying_aux(window):
    t = Thread( name = 'Ani_Paper', target = paying_aux_2, args = (window,))
    t.daemon = True
    t.start()

def paying_aux_2(window):
    global image_paper,all_canvas
    anchor = 20
    all_canvas= []
    image_paper = Canvas(window, width=300, height=anchor)
    all_canvas+= [image_paper]
    while anchor<300:
        anchor += 20
        time.sleep(0.5)
        image_paper = Canvas(window, width=300, height=anchor)
        image_paper.place(x=110,y=310)
        all_canvas += [image_paper]

    image_paper.bind("<Button-1>",paying_aux_3)
    
def paying_aux_3(s):
    global  all_canvas, titulo_ventana_ms
    for i in all_canvas:
        i.place(x=-1000)
    window = Tk()
    window.resizable(width = False, height = False)
    window.geometry('500x500+350+250')
    window.title(titulo_ventana_ms )
    
    window.mainloop()

# --------------------------- Ventanas ---------------------------- #

def idioma_screen ():


    # Ventana principal, aqui se encuentra la animacion

    idi_screen = Tk() # se crea una ventana de inicio
    idi_screen.title ("Advice Machine") # Cambiar el nombre a la ventana
    idi_screen.geometry ("1200x800+100+100")
    idi_screen.resizable (0,0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvas_idio = Canvas(idi_screen, width = 1200, height = 800, bg = purple, highlightbackground = dark_green)
    canvas_idio.pack()

    # Botones

    button_español = Button (idi_screen, text = "Español", font = font1, bg = dark_yellow,
                             activebackground = purple, activeforeground = dark_yellow,
                             command = lambda x = idi_screen, y = "español": openMachine(x, y))
    button_español.place (x = 200, y = 400, width = 300, height = 100)

    button_ingles = Button(idi_screen, text = "English", font = font1, bg = dark_yellow,
                           activebackground = purple, activeforeground = dark_yellow,
                             command = lambda x = idi_screen, y = "ingles": openMachine(x, y))
    button_ingles.place(x = 700, y = 400, width = 300, height = 100)

    # Texto
    canvas_idio.create_text(600, 100, text = "Idioma / Language", font = font2)

    mainloop()


def machine ():
    set_idi("español")
    global conse_var, dicho_var, chiste_var, coins_var, money, screen_sms, active_shop , im_printing

    #Variables de la ventana
    active_shop = True
    money = 1000

    # Ventana principal, aqui se encuentra la animacion

    machine_screen = Tk() # se crea una ventana de inicio
    machine_screen.title ("Advice Machine") # Cambiar el nombre a la ventana
    machine_screen.geometry ("1200x800+100+100")
    machine_screen.resizable (0,0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(machine_screen, width = 1200, height = 800, bg = dark_green, highlightbackground = dark_green)
    canvasP.pack()

    #Botones

    button_Conse = Button (machine_screen, text = conse_var, font = font3, bg = dark_yellow,
                             activebackground = purple, activeforeground = dark_yellow, relief = SUNKEN,
                           command = lambda x = 1: shop(x))
    button_Conse.place (x = 850, y = 300, width = 100, height = 50)

    button_Dicho = Button(machine_screen, text= dicho_var, font=font3, bg=dark_yellow,
                    activebackground=purple, activeforeground=dark_yellow, relief = SUNKEN,
                          command = lambda x = 2: shop(x))
    button_Dicho.place(x=850, y=370, width=100, height=50)

    button_chiste = Button(machine_screen, text=chiste_var, font=font3, bg=dark_yellow,
                    activebackground=purple, activeforeground=dark_yellow, relief = SUNKEN,
                           command = lambda x = 3: shop(x))
    button_chiste.place(x=850, y=440, width=100, height=50)

    button_admin = Button(machine_screen, text = "ADMIN", font=font3, bg=gray,
                    activebackground=purple, activeforeground=dark_yellow, relief = SUNKEN,
                          command = lambda x = machine_screen, y = glo_idioma : openAdmin(x, y))
    button_admin.place(x=850, y=700, width=100, height=50)

    button_pay = Button(
        machine_screen, text='PUSH ME ( ͡° ͜ʖ ͡°)', font=font3, bg=red_light,
        command = lambda x = machine_screen: paying(x))
    button_pay.place(x=750, y=560)

        # Boton monedas
    button_coin25 = Button(machine_screen, text=25, font=font3, bg=brown, relief = FLAT)
    button_coin25.place(x=1050, y=150, width=100, height=100)

    button_coin50 = Button(machine_screen, text=50, font=font3, bg=brown, relief=FLAT)
    button_coin50.place(x=1050, y=300, width=100, height=100)

    button_coin100 = Button(machine_screen, text=100, font=font3, bg=brown, relief=FLAT)
    button_coin100.place(x=1050, y=450, width=100, height=100)

    button_coin500 = Button(machine_screen, text=500, font=font3, bg=brown, relief=FLAT)
    button_coin500.place(x=1050, y=600, width=100, height=100)

    # Etiquetas
    screen_sms = StringVar()
    consola = Label(machine_screen,textvariable = screen_sms, font = font5, bg = purple)
    consola.place(x = 685, y = 70, width = 290, height = 100)

    # Dibujos en pantalla
    canvasP.create_rectangle(1000, 0, 1200, 800, fill = brown, outline = brown)
    canvasP.create_rectangle(680, 20, 980, 280, fill = purple, outline = purple)
    canvasP.create_rectangle(50, 200, 650, 400, width=15, outline = '#959593')
    image_printa = PhotoImage(file='resource/printa.png')
    canvasP.create_image(350,300,image = image_printa)

    canvasP.create_rectangle(1020, 90, 1180, 140, fill = white, outline = black)
 

    # texto
    canvasP.create_text(350, 50, text = "ADVICE MACHINE", font = font2, fill = dark_yellow)
    canvasP.create_text(1100, 45, text=coins_var, font = font4, fill = dark_green)
    canvasP.create_text(1100, 115, text =str (money), font = font4, fill = black)


    mainloop()


def admin():
    global glo_idioma, reset_var, off_var, return_var, ex_var

    
    # Ventana principal, aqui se encuentra la animacion

    admin_screen = Tk() # se crea una ventana de inicio
    admin_screen.title ("Advice Machine") # Cambiar el nombre a la ventana
    admin_screen.geometry ("1200x800+100+100")
    admin_screen.resizable (0,0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(admin_screen, width = 1200, height = 800, bg = gray, highlightbackground = gray)
    canvasP.pack()

    #Botones   HACER EL TEXTO VARIABLE
        # Volver a la maquina
    button_return = Button (admin_screen, text = return_var, font = font4, bg = gray,
                             activebackground = purple, activeforeground = dark_yellow,
                     command = lambda x = admin_screen, y = glo_idioma : openMachine(x, y))
    button_return.place (x = 20, y = 700, width = 350, height = 50)
        # Resetear la maquina
    button_reset = Button(admin_screen, text= reset_var, font=font4, bg=gray,
                           activebackground=purple, activeforeground=dark_yellow)
    button_reset.place(x=20, y=400, width=350, height=50)
        # Apagar la maquina
    button_off = Button(admin_screen, text= off_var, font=font4, bg=gray,
                           activebackground=purple, activeforeground=dark_yellow)
    button_off.place(x=20, y=500, width=350, height=50)
        # Excel
    button_ex = Button(admin_screen, text= ex_var, font=font4, bg=gray,
                           activebackground=purple, activeforeground=dark_yellow)
    button_ex.place(x=20, y=600, width=350, height=50)

    # Dibujos
    canvasP.create_rectangle(400, 20, 1180, 780, fill = white)

    mainloop()
    
if __name__ == "__main__" :
    machine()



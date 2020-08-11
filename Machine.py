from tkinter import *
import random, time, pygame, pickle
from threading import Thread

"""
Se crea un documento con serilizacion 

data = open("Data/Ao3", "wb")
pickle.dump("admin", data)

files = open("Data/Ao3", "rb")
contraseña = pickle.load(files)
print(contraseña)

Se elimina por seguridad de la maquina en caso de que revisen el codigo y asi obtengan la contraseña
"""


# Colores

dark_green = "#718C85"
brown = "#CBBAA6"
dark_yellow = "#E8B623"
purple = "#A4ACC3"
white = "#FFFFFF"
gray = "#8a8a8a"
black = "#000000"
red_light = '#c26d06'
red = "#FF6666"
light_yellow = '#e6d3a1'
# fonts

font1 = ("fixedsys", 25)
font2 = ("fixedsys", 50)
font3 = ("arial", 18)
font4 = ("fixedsys", 20)
font5 = ("fixedsys", 18)
font6 = ('MS Mincho', 16)

# inicio de variable total
global co_message_list, di_message_list, ch_message_list, select_message, vuelto_total
co_message_list = []
di_message_list = []
ch_message_list = []
select_message = None
total_money = 0
vuelto_total = 0


# -------------------------- Bases de datos ----------------------------- #

class Message(object):
    def __init__(self, text, idioma):

        # Logica para cargar todos los datos del texto
        data = text.split('@')
        data = data[1: len(data) - 1]
        i_coun = 0
        real_data = []
        self.spaces = []
        for element in data:
            if i_coun % 2 == 0:
                real_data.append(element)
            else:
                self.spaces.append(element)
            i_coun += 1

        

        # Atrbutos de la clase
        self.idioma = idioma

        self.type = int(real_data[0])

        self.message_id = int(real_data[1])

        self.message_text = real_data[2].split('\\')

        self.cost = int(real_data[3])

        self.solds = int(real_data[4])

        self.rute_image = real_data[5]

    def get_idioma(self):
        return self.idioma

    def get_type(self):
        return self.type

    def get_message_id(self):
        return self.message_id

    def get_message_text(self):
        return self.message_text

    def get_cost(self):
        return self.cost

    def get_solds(self):
        return self.solds

    def get_rute(self):
        return self.rute_image

    def increse_solds(self, delete=False, num=0):

        # Logica si borra el sold o lo incremento
        if delete:
            value = num
        else:
            value = self.solds + 1

        # Ruta del archivo que depende del idioma
        if self.idioma == "español":
            rute = "Data/base_espa.txt"
        elif self.idioma == "ingles":
            rute = "Data/base_ing.txt"

        # Carga el archivo
        file = open(rute, "r+")

        # Obtiene los datos
        data_archivo = file.readlines()

        # Cierra el archivo
        file.close()

        # Lista con strings del archivo
        all_data = [data_archivo[0]]
        for text in data_archivo[1:]:
            text = text.split('@')
            # Revisa cual mesaje es y si lo es cambia el dato
            if int(text[1]) == self.type and int(text[3]) == self.message_id:
                text[9] = f'{value}'

            # Reacomoda la linea de texto para quede con el formato anterior
            i = 0
            line_text = ""
            for line in text:
                if i % 2 != 0:
                    line_text += '@' + line + '@'
                else:
                    line_text += line
                i += 1
            all_data.append(line_text)



        # Carga el archivo
        file = open(rute, "w")

        # logica para guardar los datos modificados en el archivo
        i_counter = 0
        for data_line in all_data:
            file.write(data_line)
            
        # Cierra el archivo
        file.close()

        #Acutiliza el valor en la clase
        self.solds = value

def load_base_message(idioma):
    global co_message_list, di_message_list, ch_message_list

    # Ruta del archivo que depende del idioma
    if idioma == "español":
        rute = "Data/base_espa.txt"
    elif idioma == "ingles":
        rute = "Data/base_ing.txt"
    # Carga el archivo
    file = open(rute, "r")
    # Obtiene los datos
    data_archivo = file.readlines()

    # Cierra el archivo
    file.close()


    # Crea la variavles del
    for text in data_archivo[1:]:
        message = Message(text, idioma)
        if message.get_type() == 1:
            co_message_list.append(message)
        elif message.get_type() == 2:
            di_message_list.append(message)
        elif message.get_type() == 3:
            ch_message_list.append(message)
        else:
            pass

def data_text_funcion():
    #Variables de idioma
    global base_ventas_titulo_1, base_ventas_titulo_2, buttom_text_change_uno ,  buttom_text_change_dos
    #Variables para setiar el idioma
    global data_text, num_data_text, titulo_base_datos, button_text_change
    if num_data_text>0:
        #Setea la el modo del resumen
        button_text_change.set(buttom_text_change_uno)
        titulo_base_datos.set(base_ventas_titulo_1)
        data_text.set(data_text_funcion_aux_1())
        num_data_text *= -1
    else:
        #Setea el modo extenso
        button_text_change.set(buttom_text_change_dos)
        titulo_base_datos.set(base_ventas_titulo_2)
        data_text.set(data_text_funcion_aux_2())
        num_data_text *= -1

def data_text_funcion_aux_1():
    global co_message_list, di_message_list, ch_message_list

    texto_imprimir = ''

    for consejos in co_message_list:
        mensaje_imprimir = ''
        for mensaje in consejos.get_message_text():
            done = False
            for i in mensaje:
                mensaje_imprimir += i

                if len( mensaje_imprimir ) >=25:
                    done =True
                    mensaje_imprimir += "..."
                    break
            if done:
                break
        if len(mensaje_imprimir)//10==0:
            mensaje_imprimir += '\t\t\t\t'
        elif  len(mensaje_imprimir)//10==1:
            mensaje_imprimir += '\t\t\t'
        elif len(mensaje_imprimir)//10>=2:
            mensaje_imprimir += '\t\t'

        texto_imprimir += f"{consejos.get_type()}"+"\t"+f"{consejos.get_message_id()}"+"\t"+f"{mensaje_imprimir}"+\
                          f"{consejos.get_solds()}"+"\t"+f"{consejos.get_solds()*consejos.get_cost()}"+"\n"

    for dichos in di_message_list:
        mensaje_imprimir = ''
        for mensaje in dichos.get_message_text():
            done = False
            for i in mensaje:
                mensaje_imprimir += i

                if len(mensaje_imprimir) >= 25:
                    done = True
                    mensaje_imprimir += "..."
                    break
            if done:
                break
        if len(mensaje_imprimir) // 10 == 0:
            mensaje_imprimir += '\t\t\t\t'
        elif len(mensaje_imprimir) // 10 == 1:
            mensaje_imprimir += '\t\t\t'
        elif len(mensaje_imprimir) // 10 >= 2:
            mensaje_imprimir += '\t\t'

        texto_imprimir += f"{dichos.get_type()}"+"\t"+f"{dichos.get_message_id()}"+"\t"+f"{mensaje_imprimir}"+\
                          f"{dichos.get_solds()}"+"\t"+f"{dichos.get_solds()*dichos.get_cost()}"+"\n"

    for chistes in ch_message_list:
        mensaje_imprimir = ''
        for mensaje in chistes.get_message_text():
            done = False
            for i in mensaje:
                mensaje_imprimir += i

                if len(mensaje_imprimir) >= 25:
                    done = True
                    mensaje_imprimir += "..."
                    break
            if done:
                break
        if len(mensaje_imprimir) // 10 == 0:
            mensaje_imprimir += '\t\t\t\t'
        elif len(mensaje_imprimir) // 10 == 1:
            mensaje_imprimir += '\t\t\t'
        elif len(mensaje_imprimir) // 10 >= 2:
            mensaje_imprimir += '\t\t'

        texto_imprimir += f"{chistes.get_type()}"+"\t"+f"{chistes.get_message_id()}"+"\t"+f"{mensaje_imprimir}"+\
                          f"{chistes.get_solds()}"+"\t"+f"{chistes.get_solds()*chistes.get_cost()}"+"\n"


    return texto_imprimir

def data_text_funcion_aux_2():
    rute = "Data/base_ventas.txt"
    file = open(rute, "r")
    file_total = file.readlines()[5:]
    file.close()

    texto_imprimir = ''

    for line in file_total:
        j = 0
        for word in line.split("@")[1:len(line.split("@"))-1]:
            if j%2==0:
                texto_imprimir += word
            else:
                texto_imprimir += word
        texto_imprimir +='\t\n'

    return texto_imprimir

# -------------------------- Base de ventas ----------------------------- #

def ventas_read():
    global N_transa
    rute = "Data/base_ventas.txt"
    file = open(rute, "r")
    file_total = file.readlines()[- 1]
    file.close()
    ult_line = file_total.split("@")
    if len(ult_line) > 2:
        N_transa = int(ult_line[1])
    else:
        N_transa = 1

def ventas_load():
    global N_transa, total_money, vuelto_temp
    global select_message
    N_transa += 1  # Se incrementa el numero de transaccion
    date = time.strftime("%d/%m/%y")  # Se encarga de colocar la fecha
    hour = time.strftime("%X")  # Se encarga de colocar la hora de la compra
    type_sms = select_message.get_type()  # obtener estos valores de la clase
    code_sms = select_message.get_message_id()  # obtener estos valores de la clase
    price_sms = 250  # obtener de la clase
    rute = "Data/base_ventas.txt"
    file = open(rute, "a")
    file.write("\n" + "@" + str(N_transa) + "@" + "\t" + "@" + date + "@" + "\t" + "@" + hour + "@" + "\t" + "@   " + str(
        type_sms) + "@" + "\t" + "@" + str(code_sms) + "@" +"\t" + "@" + str(price_sms) + "@" + "\t" + "@" + str(total_money) + "@" + "\t" + "@" + str(vuelto_temp) + "@" )
    file.close()


# -------------------- Funciones administracion -------------------- #

def login_validation(entry_box, window1, window2, canvas):
    global invalid
    file = open("Data/Ao3", "rb")
    valid = pickle.load(file)
    entry = entry_box.get()
    if entry == valid:
        window1.destroy()
        window2.destroy()
        admin()
    else:
        canvas.create_text(250, 60, text=invalid, font=font5, fill=red)

def reset():

    #Logica para reset individuales
    global co_message_list, di_message_list, ch_message_list

    for message_co in co_message_list:
        message_co.increse_solds(delete = True)

    for message_di in di_message_list:
        message_di.increse_solds(delete = True)

    for message_ch in ch_message_list:
        message_ch.increse_solds(delete = True)

    #Vuelve a cargar los datos en pantalla
    global num_data_text
    num_data_text *= -1
    data_text_funcion()

    rute = "Data/base_ventas.txt"
    file = open(rute, "r")
    total_ventas = file.readlines()[:4]
    file.close()
    file = open(rute, "w")
    for linea in total_ventas:
        file.write(linea)
    file.close()

def turn_off():
    global on_sms, off_sms, turn_off_title, glo_idioma
    # Ventana de apagado

    off_screen = Tk()  # se crea una ventana de inicio
    off_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    off_screen.geometry("1200x800+100+100")
    off_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvas_idio = Canvas(off_screen, width=1200, height=800, bg=purple, highlightbackground=dark_green)
    canvas_idio.pack()

    # Botones

    button_on = Button(off_screen, text=on_sms, font=font1, bg=dark_yellow,
                            activebackground=purple, activeforeground=dark_yellow, command = lambda x = off_screen, y = glo_idioma: openMachine(x, y))
    button_on.place(x=200, y=400, width=300, height=100)

    button_off = Button(off_screen, text=off_sms, font=font1, bg=dark_yellow,
                           activebackground=purple, activeforeground=dark_yellow, command = lambda x = off_screen: destroy(x))
    button_off.place(x=700, y=400, width=300, height=100)

    # Texto
    canvas_idio.create_text(600, 100, text=turn_off_title, font=font2)

    mainloop()

def excel():
    pass

# -------------------------- Contraseñas -------------------------------- #

def new_password():
    pass

def password_validation(entry_box):
    entry = entry_box.get()
    for letter in entry:
        pass

# -------------------------- Setea el idioma ---------------------------- #


def set_idi(idioma):
    global glo_idioma, reset_var, off_var, return_var, ex_var, on_sms, off_sms, turn_off_title
    global conse_var, dicho_var, chiste_var, coins_var, sms, rest_var, vuelto_sms, contra_sms
    global titulo_ventana_ms, invalid
    global base_ventas_titulo_1, base_ventas_titulo_2, buttom_text_change_uno ,  buttom_text_change_dos

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
        vuelto_sms = "Su vuelto es: "
        # Texto admin
        reset_var = "Restaurar"
        off_var = "Apagar"
        return_var = "Volver"
        ex_var = "Generar Excel"
        on_sms = "Cancelar"
        off_sms = "Apagar"
        turn_off_title = "¿Quiere apagar la máquina?"
        contra_sms = "Contraseña"
        invalid = "Contraseña incorrecta"
        base_ventas_titulo_1 = "Tipo"+"\t"+"Código"+"\t"+"Mensaje" \
                               +"\t\t\t\t"+"Vendidos"+"\t"+"Monto"
        base_ventas_titulo_2 = "Código"+"\t"+"Fecha"+"\t"+"Hora"\
                                +"\t"+"  Tipo"+"\t"+"ID"+"\t"+" Monto "\
                               +"\t"+"Pago"+"\t"+"Vuelto"
        buttom_text_change_uno = "Extenso"
        buttom_text_change_dos = "Resumen"
    elif idioma == "ingles":
        # Texto machine
        conse_var = "Advice"
        dicho_var = "Sayings"
        chiste_var = "Jokes"
        coins_var = "Your cash"
        sms = "Your selection is:"
        titulo_ventana_ms = 'Papel'
        rest_var = "Amount \nto be paid: "
        vuelto_sms = "Your change \nis: "
        # Texto admin
        reset_var = "Reset"
        off_var = "Turn off"
        return_var = "Return"
        ex_var = "Generate Excel"
        on_sms = "Cancel"
        off_sms = "Turn off"
        turn_off_title = "Do you want to turn off the machine?"
        contra_sms = "Password"
        invalid = "Incorrect password"

        base_ventas_titulo_1 = "Type" + "\t" + "Code" + "\t" + "Menssage" \
                               + "\t\t\t" + "Sold" + "\t" + "Amount"
        base_ventas_titulo_2 = "Code"+"\t"+"Date"+"\t"+"Time"\
                                +"\t"+"  Type"+"\t"+"ID"+"\t"+"Amount"+\
                               "\t"+"Payout"+"\t"+"Change"
        buttom_text_change_uno = "Extensive"
        buttom_text_change_dos = "Summary"

        # ----logica para cargar archivo en englicsj---


# ---------------------------  Abrir Ventanas  ---------------------------- #

def openAdmin(window, idioma):
    window.destroy()
    set_idi(idioma)
    admin()

def openMachine(window, idioma):
    window.destroy()
    set_idi(idioma)
    ventas_read()
    load_base_message(idioma)
    machine()

def openOff(window):
    window.destroy()
    turn_off()

def openLogin(window):
    login(window)

def destroy(window):
    window.destroy()

# ---------------------------  tienda  ---------------------------- #

def set_shop(tipo):
    global sms, conse_var, dicho_var, chiste_var, screen_sms, active_shop, price_str, rest_var, price, co_message_list,\
        di_message_list,ch_message_list , select_message
    # tipo consejo
    if tipo == 1 and active_shop:
        screen_sms.set(sms + "\n" + conse_var)
        active_shop = False

        #Escoge mensage de la lista consejos
        select_message = random.choice(co_message_list)
        price = select_message.get_cost()


        price_str.set(rest_var + str(price))  # agregar variable que cambie
    # tipo dicho
    elif tipo == 2 and active_shop:
        screen_sms.set(sms + "\n" + dicho_var)
        active_shop = False


        #Escoge mensage de la lista de dichos
        select_message = random.choice(di_message_list)
        price = select_message.get_cost()


        price_str.set(rest_var + str(price))
    # tipo chiste
    elif tipo == 3 and active_shop:
        screen_sms.set(sms + "\n" + chiste_var)
        active_shop = False


        #Escoge mensage de la lista de chistes
        select_message = random.choice(ch_message_list)
        price = select_message.get_cost()


        price_str.set(rest_var + str(price))

def coins_rest(type1, window, canvas):
    global price, money_tmp, price_str, money, total_money, active_shop
    if not active_shop:
        if price > 0:
            if type1 == 25 and money_tmp >= 25:
                price -= 25
                money_tmp -= 25
                total_money += 25
                price_str.set(rest_var + str(price))
                money.set(money_tmp)
                return paying(window, canvas)
            elif type1 == 50 and money_tmp >= 50:
                price -= 50
                money_tmp -= 50
                total_money += 50
                price_str.set(rest_var + str(price))
                money.set(money_tmp)
                return paying(window, canvas)
            elif type1 == 100 and money_tmp >= 100:
                price -= 100
                money_tmp -= 100
                total_money += 100
                price_str.set(rest_var + str(price))
                money.set(money_tmp)
                return paying(window, canvas)
            elif type1 == 500 and money_tmp >= 500:
                price -= 500
                money_tmp -= 500
                total_money += 500
                price_str.set(rest_var + str(price))
                money.set(money_tmp)
                return paying(window, canvas)

def vuelto_return_aux(canvas):
    #El suma las variables de monet tmperoral y seta cantidad de monedas
    global vuelto_total,  money_tmp, money
    money_tmp += vuelto_total
    vuelto_total = 0
    money.set(money_tmp)
    return vuelto_volar(canvas)

def vuelto_volar(canvas):
    #Mueve las del vuelto a volar
    global active_vuelto, imagen_monedas_canvas
    if active_vuelto:
        canvas.move(imagen_monedas_canvas, -1000, -1000)
        active_vuelto = False
        
def vuelto_move(canvas):
    #Mueve el vuelto a la interfaz
    global  imagen_monedas
    canvas.move(imagen_monedas_canvas,1000,1000)


# --------------------------- Animacion ---------------------------- #

def paying(window, canvas):
    global price, rest_var, money, price_str, money_tmp, vuelto_temp, total_money, vuelto_sms, vuelto_total, active_vuelto
    if price > 0:
        pass
    elif price == 0:
        vuelto_temp = 0
        ventas_load()
        total_money = 0
        return paying_aux(window)
    elif price < 0:
        vuelto_temp = -1 * price
        #Revisa si ya esta vuelto
        if vuelto_total==0:
            active_vuelto = True
            vuelto_move(canvas)

        vuelto_total += vuelto_temp

        money.set(money_tmp)
        price_str.set(vuelto_sms + str(abs(price)))

        #Se llaman para guardar a ventas
        ventas_load()

        #Se quita el vuelto en ese momento y la cantidad de monedas con las que pago
        total_money = 0
        vuelto_temp = 0
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
    global all_canvas, titulo_ventana_ms, active_shop, select_message


    for i in all_canvas:
        i.place(x=-1000)
    active_shop = True
    select_message.increse_solds()

    #Ventana en pygame
    pygame.init()
    pygame.font.init()

    #Configuraciones de esta
    pygame.display.set_caption(titulo_ventana_ms)
    screen = pygame.display.set_mode((500,650))
    screen.fill((255,255,255))
    #Fuente
    font_1_pyg = pygame.font.SysFont("Times New Roman", 20)

    #Imagen
    image_message = pygame.image.load(select_message.get_rute())
    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        try:
            # Dibujo imagen
            screen.blit(image_message, (0, 0))

            x_text = 250
            y_text = 520

            for element_text in select_message.get_message_text():
                text_pygame(element_text, font_1_pyg, (0,0,0), screen, x_text, y_text)
                y_text += 20

            pygame.display.flip()
        except:
            pass

def text_pygame (text, font, color, surface, x , y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)


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

    # Mini canvas del vuelto
    global imagen_monedas_canvas, active_vuelto

    canvas_vuelto = Canvas(machine_screen, width=200, height=125,  bg=dark_green, highlightbackground=dark_green)
    canvas_vuelto.place(x=500, y=600)
    imagen_de_monedero = PhotoImage(file='resource/monedero.png')
    canvas_vuelto.create_image(2 , 2, image=imagen_de_monedero, anchor='nw')

    imagen_monedas = PhotoImage(file='resource/monedas.png')
    imagen_monedas_canvas = canvas_vuelto.create_image(-990, -970, image=imagen_monedas, anchor='nw')

    active_vuelto = False
    canvas_vuelto.bind("<Button-1>", lambda event, x=canvas_vuelto: vuelto_return_aux(x))

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
                          command=lambda x= machine_screen: openLogin(x))
    button_admin.place(x=850, y=700, width=100, height=50)


    # Boton monedas
    img_25 = PhotoImage(file='resource/25.gif')
    coin25_img = img_25.subsample(4, 4)
    button_coin25 = Button(machine_screen, image = coin25_img, font=font3, bg=brown, relief=FLAT,
                           command=lambda x=25, y=machine_screen, z =canvas_vuelto: coins_rest(x, y, z))
    button_coin25.place(x=1050, y=150, width=100, height=100)

    img_50 = PhotoImage(file='resource/50.gif')
    coin50_img = img_50.subsample(4, 4)
    button_coin50 = Button(machine_screen,image = coin50_img, font=font3, bg=brown, relief=FLAT,
                           command=lambda x=50, y=machine_screen, z =canvas_vuelto: coins_rest(x, y, z))
    button_coin50.place(x=1050, y=300, width=100, height=100)

    img_100 = PhotoImage(file='resource/100.gif')
    coin100_img = img_100.subsample(4, 4)
    button_coin100 = Button(machine_screen,image = coin100_img, font=font3, bg=brown, relief=FLAT,
                            command=lambda x=100, y=machine_screen, z =canvas_vuelto: coins_rest(x, y, z))
    button_coin100.place(x=1050, y=450, width=100, height=100)

    img_500 = PhotoImage(file='resource/500.gif')
    coin500_img = img_500.subsample(7, 7)
    button_coin500 = Button(machine_screen, image = coin500_img, font=font3, bg=brown, relief=FLAT,
                            command=lambda x=500, y=machine_screen, z =canvas_vuelto: coins_rest(x, y, z))
    button_coin500.place(x=1050, y=600, width=100, height=100)

    # Etiquetas

    #Imprime el mensaje en pantalla de la maquina
    screen_sms = StringVar()
    consola = Label(machine_screen, textvariable=screen_sms, font=font5, bg=purple)
    consola.place(x=685, y=70, width=290, height=100)

    #Variables para el dinero  de usaurio es aleatorio al iniciar
    money = StringVar()
    money_tmp = random.randrange(100, 2000, 25) #Cantidad de monedas del usario
    money.set(money_tmp)

    #Label que impreme en pantalla el dinero del usario
    monedas = Label(machine_screen, textvariable=money, font=font4, bg=white)
    monedas.place(x=1020, y=90, width=160, height=50)

    #Variable del precio por mensaje y label que imprime dicho precio
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



    mainloop()


def login(window1):
    global contra_sms

    # Ventana principal, aqui se encuentra la animacion

    login_screen = Tk()  # se crea una ventana de inicio
    login_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    login_screen.geometry("500x250+450+400")
    login_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvas_log = Canvas(login_screen, width=500, height=250, bg=gray, highlightbackground=gray)
    canvas_log.pack()

    entry_passw = Entry(login_screen, font=font5, bg=white, bd=3, show="*")
    entry_passw.place(x=50, y=100, width=400, heigh=50)

    # Botones

    button_valid = Button(login_screen, text= "ok", font=font5, bg=gray,
                            activeforeground=dark_yellow, command= lambda x=entry_passw, y=window1,
                            z= login_screen, w = canvas_log : login_validation(x, y, z, w))
    button_valid.place(x=100, y=180, width=300, height=50)




    # Texto
    canvas_log.create_text(250, 20, text=contra_sms, font=font5)

    mainloop()


def admin():


    # Ventana principal, aqui se encuentra la animacion

    admin_screen = Tk()  # se crea una ventana de inicio
    admin_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    admin_screen.geometry("1200x800+100+100")
    admin_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # Crea la variable del texto
    global glo_idioma, reset_var, off_var, return_var, ex_var
    global base_ventas_titulo_2
    global data_text, num_data_text, titulo_base_datos, button_text_change

    titulo_base_datos = StringVar()
    data_text = StringVar()
    button_text_change = StringVar()
    num_data_text = 1

    # se crea un canvas para dibujar

    canvasP = Canvas(admin_screen, width=1200, height=800, bg=gray, highlightbackground=gray)
    canvasP.place(x=0,y=0)


    #Logica para scroll bar de la ventana
    cereal_bar = Scrollbar(admin_screen)

    canvas_print = Canvas(admin_screen, background=white, width=765,
                          height=600, yscrollcommand=cereal_bar.set)

    cereal_bar.config(command=canvas_print.yview)

    cereal_bar.pack(fill=Y, side='right')

    elframe = Frame(canvas_print)

    canvas_print.place(x=400, y=100)
    canvas_print.create_window(0, 0, window=elframe, anchor='nw')



    #Asigna el
    data_text_funcion()

    #Labels
    texto_label = Label(elframe, wraplength=780,textvariable=data_text, bg=white, font=font6,justify=LEFT)
    texto_label.pack()

    admin_screen.update()
    canvas_print.config(scrollregion=canvas_print.bbox("all"))

    label_name = Label(admin_screen, textvariable=titulo_base_datos, font=font6, bg=gray)
    label_name.place(x=400, y=20)

     #Botones

    #Boton de imprimir pantalla cual base de datos
    button_text_funcion =  Button(admin_screen, textvariable=button_text_change, font=font4, bg=gray,
                           activebackground=purple, activeforeground=dark_yellow,
                           command=data_text_funcion)
    button_text_funcion.place(x=20, y=300, width=350, height=50)

    # Volver a la maquina
    button_return = Button(admin_screen, text=return_var, font=font4, bg=gray,
                           activebackground=purple, activeforeground=dark_yellow,
                           command=lambda x=admin_screen, y=glo_idioma: openMachine(x, y))
    button_return.place(x=20, y=700, width=350, height=50)
    # Resetear la maquina
    button_reset = Button(admin_screen, text=reset_var, font=font4, bg=gray,
                          activebackground=purple, activeforeground=dark_yellow, command=reset)
    button_reset.place(x=20, y=400, width=350, height=50)
    # Apagar la maquina
    button_off = Button(admin_screen, text=off_var, font=font4, bg=gray,
                        activebackground=purple, activeforeground=dark_yellow,
                        command=lambda x=admin_screen: openOff(x))
    button_off.place(x=20, y=500, width=350, height=50)
    # Excel
    button_ex = Button(admin_screen, text=ex_var, font=font4, bg=gray,
                       activebackground=purple, activeforeground=dark_yellow)
    button_ex.place(x=20, y=600, width=350, height=50)


    mainloop()


if __name__ == "__main__":
    idioma_screen()

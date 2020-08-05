from tkinter import *

# Colores

dark_green = "#718C85"
brown = "#CBBAA6"
dark_yellow = "#E8B623"
purple = "#A4ACC3"
white = "#FFFFFF"

# fonts

font1 = ("fixedsys", 25)
font2 = ("fixedsys", 50)
font3 = ("arial", 18)

# --------------------------- Ventanas ---------------------------- #

def idioma_screen ():
    global idi_screen, machine_screen

    try:
        machine_screen.destroy()
    except:
        pass

    # Ventana principal, aqui se encuentra la animacion

    idi_screen = Tk() # se crea una ventana de inicio
    idi_screen.title ("Advice Machine") # Cambiar el nombre a la ventana
    idi_screen.geometry ("1200x800+400+100")
    idi_screen.resizable (0,0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvas_idio = Canvas(idi_screen, width = 1200, height = 800, bg = purple, highlightbackground = dark_green)
    canvas_idio.pack()

    # Botones

    button_español = Button (idi_screen, text = "Español", font = font1, bg = dark_yellow,
                             activebackground = purple, activeforeground = dark_yellow, command = machine)
    button_español.place (x = 200, y = 400, width = 300, height = 100)

    button_ingles = Button(idi_screen, text = "English", font = font1, bg = dark_yellow,
                           activebackground = purple, activeforeground = dark_yellow)
    button_ingles.place(x = 700, y = 400, width = 300, height = 100)

    # Texto
    canvas_idio.create_text(600, 100, text = "Idioma / Language", font = font2)

    mainloop()


def machine ():
    global idioma_screen, machine_screen

    try:
        idi_screen.destroy()
    except:
        pass

    try:
        admin_screen.destroy()
    except:
        pass

    # Ventana principal, aqui se encuentra la animacion

    machine_screen = Tk() # se crea una ventana de inicio
    machine_screen.title ("Advice Machine") # Cambiar el nombre a la ventana
    machine_screen.geometry ("1200x800+400+100")
    machine_screen.resizable (0,0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(machine_screen, width = 1200, height = 800, bg = dark_green, highlightbackground = dark_green)
    canvasP.pack()

    #Botones

    button_Conse = Button (machine_screen, text = "Consejo", font = font3, bg = dark_yellow,
                             activebackground = purple, activeforeground = dark_yellow)
    button_Conse.place (x = 850, y = 300, width = 100, height = 50)

    button_Dicho = Button(machine_screen, text="Dichos", font=font3, bg=dark_yellow,
                    activebackground=purple, activeforeground=dark_yellow)
    button_Dicho.place(x=850, y=370, width=100, height=50)

    button_chiste = Button(machine_screen, text="Chistes", font=font3, bg=dark_yellow,
                    activebackground=purple, activeforeground=dark_yellow)
    button_chiste.place(x=850, y=440, width=100, height=50)

    # Dibujos en pantalla
    canvasP.create_rectangle(1000, 0, 1200, 800, fill = brown, outline = brown)

    mainloop()


def admin():
    global machine_screen,admin_screen
    try:
        machine_screen.destroy()
    except:
        pass

    
    # Ventana principal, aqui se encuentra la animacion

    admin_screen = Tk() # se crea una ventana de inicio
    admin_screen.title ("Advice Machine") # Cambiar el nombre a la ventana
    admin_screen.geometry ("1200x800+400+100")
    admin_screen.resizable (0,0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(admin_screen, width = 1200, height = 800, bg = dark_yellow, highlightbackground = dark_green)
    canvasP.pack()

    #Botones
    button = Button (admin_screen, text = "prueba2", font = font1, bg = dark_yellow,
                             activebackground = purple, activeforeground = dark_yellow, command = machine)
    button.place (x = 200, y = 400, width = 300, height = 100)
    mainloop()


    
if __name__ == "__main__" :
    idioma_screen()



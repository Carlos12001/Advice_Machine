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


#--------------------------- Cierre de Ventanas ---------------------------- #

def openadministrador(window):
    window.destroy()
    admin()


def openmachine(window):
    window.destroy()
    machine()


# --------------------------- Ventanas ---------------------------- #

def idioma_screen():

    # Ventana principal, aqui se encuentra la animacion

    idi_screen = Tk()  # se crea una ventana de inicio
    idi_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    idi_screen.geometry("1200x800+400+100")
    idi_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvas_idio = Canvas(idi_screen, width=1200, height=800, bg=purple, highlightbackground=dark_green)
    canvas_idio.pack()

    # Botones

    button_español = Button(idi_screen, text="Español", font=font1, bg=dark_yellow,
                            activebackground=purple, activeforeground=dark_yellow,
                            command = lambda x = idi_screen : openmachine(x))
    button_español.place(x=200, y=400, width=300, height=100)

    button_ingles = Button(idi_screen, text="English", font=font1, bg=dark_yellow,
                           activebackground=purple, activeforeground=dark_yellow)
    button_ingles.place(x=700, y=400, width=300, height=100)

    # Texto
    canvas_idio.create_text(600, 100, text="Idioma / Language", font=font2)

    idi_screen.mainloop()


def machine():


    # Ventana principal, aqui se encuentra la animacion

    machine_screen = Tk()  # se crea una ventana de inicio
    machine_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    machine_screen.geometry("1200x800+400+100")
    machine_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(machine_screen, width=1200, height=800, bg=dark_green, highlightbackground=dark_green)
    canvasP.pack()

    # Botones
    button = Button(machine_screen, text="prueba", font=font1, bg=dark_yellow,
                    activebackground=purple, activeforeground=dark_yellow,
                    command=lambda x = machine_screen: openadministrador(x))
    button.place(x=200, y=400, width=300, height=100)

    # Dibujos en pantalla 
    machine_screen.mainloop()
    exit()


def admin():



    # Ventana principal, aqui se encuentra la animacion

    admin_screen = Tk()  # se crea una ventana de inicio
    admin_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    admin_screen.geometry("1200x800+400+100")
    admin_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(admin_screen, width=1200, height=800, bg=dark_yellow, highlightbackground=dark_green)
    canvasP.pack()

    # Botones
    button = Button(admin_screen, text="prueba2", font=font1, bg=dark_yellow,
                    activebackground=purple, activeforeground=dark_yellow,
                    command = lambda x = admin_screen: openmachine(x))
    button.place(x=200, y=400, width=300, height=100)
    mainloop()

    # Ventana principal

    machine_screen = Tk()  # se crea una ventana de inicio
    machine_screen.title("Advice Machine")  # Cambiar el nombre a la ventana
    machine_screen.geometry("1200x800+400+100")
    machine_screen.resizable(0, 0)  # No hay cambio de tamaño de la ventana

    # se crea un canvas para dibujar

    canvasP = Canvas(machine_screen, width=1200, height=800,
                     bg=dark_green, highlightbackground=white)
    canvasP.pack()

    # Botones
    button = Button(machine_screen, text="prueba", font=font1, bg=dark_yellow,
                    activebackground=purple, activeforeground=dark_yellow, command=idioma_screen)
    button.place(x=200, y=400, width=300, height=100)

    admin_screen.mainloop()
    exit()

if __name__ == "__main__":
    idioma_screen()

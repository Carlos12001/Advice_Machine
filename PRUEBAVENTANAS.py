from tkinter import *
import time
import threading
matriz = [1,2,3,4]



def openadministrador(window):
    window.destroy()
    administrador()

def openRegistro(window):
    window.destroy()
    registro()

def openMenu(window):
    window.destroy()
    menu()

def registro():

    window = Tk()
    window.title("REGISTRO")
    window.geometry("700x600+400+70")
    window.minsize(700, 600)
    window.resizable(width="NO", height="NO")
    window.config(bg="black")


    lblTitle = Label(text="REGISTRO", bg="black", fg="white")
    lblTitle.place(x=300, y=150)
    print("REGISTRO", matriz)
    # playImage = PhotoImage(file = "resources/start.png")
    btnPlay = Button(window, width=10, text="FUNCION", height=2, bg="white", fg="black", activebackground="blue",
                     )  # , image = playImage)
    btnPlay.place(x=300, y=280)

    btnMenu = Button(window, width=10, text="MENU", height=2, bg="white", fg="black", activebackground="blue",
                     command = lambda x = window : openMenu(x))  # , image = playImage)
    btnMenu.place(x=450, y=280)



    window.mainloop()



def administrador():
    window = Tk()
    window.title("ADINISTRADOR")
    window.geometry("700x600+400+70")
    window.minsize(700, 600)
    window.resizable(width="NO", height="NO")
    window.config(bg="black")
    print("ADMINISTRADOR",matriz)

    lblTitle = Label(text="ADMINISTRADOR", bg="black", fg="white")
    lblTitle.place(x=300, y=150)

    # playImage = PhotoImage(file = "resources/start.png")
    btnPlay = Button(window, width=10, text="REGISTRO", height=2, bg="white", fg="black", activebackground="blue",
                     command = lambda x = window: openRegistro(x))  # , image = playImage)
    btnPlay.place(x=300, y=280)



    window.mainloop()




def menu():
    window = Tk()
    window.title("MENU")
    window.geometry("700x600+400+70")
    window.minsize(700, 600)
    window.resizable(width="NO", height="NO")
    window.config(bg="black")

    #frame = Frame(window, width=100, height=100)
    #window.config(bg = "white")
    window.bind("<Button-1>", callback)

    #frame.place(x = 50,y = 400)

    canvas = Canvas(window,width= 200 ,height=200 ,bg= "white" )

    canvas.place(x = 400 , y = 400)

    rectangulo = canvas.create_rectangle(0,0,10,10,fill = "red")

    window.bind("<w>", lambda event,a=canvas, b = rectangulo : mover(event,a,b))



    lblTitle = Label(text="MENU", bg="black", fg="white")
    lblTitle.place(x=300, y=150)

    print("MENU", matriz)

    # playImage = PhotoImage(file = "resources/start.png")
    btnPlay = Button(window, width=10, text="ADMINISTRADOR", height=2, bg="white", fg="black", activebackground="blue",
                     command = lambda x = window: openadministrador(x))  # , image = playImage)
    btnPlay.place(x=300, y=280)



    window.mainloop()


## FUNCIONES DE MENU
def callback(event):
    print("clicked at", event.x//50, event.y//50)

def mover(event,canvas,rectangulo):
    print(event.char)

    t  = threading.Thread(target=tmove,args=(canvas,rectangulo))
    t.start()

    #canvas.move(rectangulo,10,0)


def tmove(canvas,rectangulo):
    for i in range(100):
        canvas.move(rectangulo,2,1)
        time.sleep(0.1)
if __name__=='__main__':

    menu()

from tkinter import *

root = Tk()
Frutas = {"MANZANA": 0.52, "KIWI": 0.51, "GRANADA": 0.65, "ARROZ BLANCO": 3.54, "ARANDANOS": 0.41,"CAQUI": 0.64,"CEREZA":0.47,"CHIRIMOYA":0.78,"CIRUELA":0.44 ,"CIRUELA SECA": 0.44,"COCO":.646,"DAMASCO":0.44,"DATIL":2.79,"DATIL SECO": 3.06,"DURAZNO": 0.52,"FRAMBUESA":0.40,"FRESAS":0.36,"GROSELLA":0.37,"HIGOS":80,
          "HIGOS SECOS": 2.75,"LIMON":0.39,"MANDARINA":0.40,"MANGO":0.57,"MELON":0.31,"MORA":0.37,"NARANJA":0.44,"NECTARINA":0.44,"NISPEROS":0.97,"PALTA":1.67,"PAPAYA":0.45,"PERA":6.1,"PIÑA":0.51,
        "PLATANO":0.90,"POMELO":0.30,"SANDIA":0.30,"UVA":0.81,"PASAS":3.24,"ZUMO DE NARANJA":0.42,"ALMENDRAS":6.20,"AVELLANAS":6.75,"CASTAÑAS":1.99,"MANI":5.60,"NUECES":6.60,}
Verduras={"TOMATE":2.34, "CALABAZA": 0.24, "BROCOLI":0.30, "APIO":0.20, "COLIFLOR":0.30, "LECHUGA":0.18, "ESPARRAGOS":0.26, "COL":0.28, "ARVERJAS":0.78, "ACEITUNAS NEGRAS":3.49, "ACEITUNAS VERDES":1.32, "BERROS":2.40}
alimentos = {}

frame = Frame(root)
frame.pack()

ali_var = StringVar(root)
ali_var.set(next(iter(Frutas.keys())))
am_var= StringVar(root)
am_var.set(next(iter(Verduras.keys())))


entry_alimento = OptionMenu(frame, ali_var, *Frutas.keys())
entry_cantidad = Entry(frame)
entry_alimento2 = OptionMenu(frame, am_var, *Verduras.keys())
entry_cantidad2 = Entry(frame)
tr = Entry(frame)
texto = Text(root)
ans = 0


def update():
    texto.delete("1.0", END)
    print(alimentos)
    for i in alimentos.keys():
        cant = alimentos[i]
        al = i
        print(i)

        cal = Frutas[i.upper()] if i.upper() in Frutas.keys() else Verduras[i.upper()]
        tot = cal*cant
        texto.insert(INSERT, str(cant) + " de " + i + "( " + str(cal) + " )" + ": " + str(tot) + "\n")
    texto.insert(INSERT, "Total: " + str(ans))

def exec_evento(elem,verd):
    print("evento",elem)
    texto.delete("1.0", END)
    alimentos[elem] = int(entry_cantidad.get())
    alimentos[verd] = int(entry_cantidad2.get())
    update()
    texto.pack()

def event_frutas(event):
    global ans
    print("b")
    ans += Frutas[ali_var.get().upper()]*int(entry_cantidad.get())


    ans += Verduras[am_var.get().upper()]*int(entry_cantidad2.get())
    exec_evento(ali_var.get(),am_var.get())


def resultados():
    print(ans)
root.title("Contador de Calorias")
root.minsize(width=400, height=200)
f = Label(frame, text="Frutas")
f.grid(row=0, column=0, sticky=E)






c=Label(frame , text = "Cantidad")
c.grid(row=1, column=0, sticky=E)


entry_alimento.grid(row=0, column=1)
entry_cantidad.grid(row=1, column=1)
entry_alimento2.grid(row=0, column=2)
entry_cantidad2.grid(row=0, column=3)

entry_cantidad.bind("<Return>", event_frutas)

root.mainloop()

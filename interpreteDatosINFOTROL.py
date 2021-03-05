import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib


window = tk.Tk()
window.title("Interprete de Datos INFOTROL")
window.geometry('1000x750')

##################################################################
#________PARTE INTERFAZ GRAFICA___________________________________

#________INTRODUCIR LOGO AL INICIO________________________________

canvas = tk.Canvas(window, width = 1000, height = 100, bg = 'white')
canvas.grid(row = 0, column = 0, columnspan = 2, sticky = 'NSWE')

logo = tk.PhotoImage(file = "/Users/lomil/Documents/Python/code_linux/imagenes/logoINFOTROL.png")

def on_expand(event):   #funcion para mover el logo al expandir la ventana
    canvas.delete("all")
    #canvas.update()    #solo es necesario al inicializar
    canvas.create_image(canvas.winfo_width()/2, 
        canvas.winfo_height()/2, image = logo)

canvas.update() #actualizar los valores de .winfo_width/height, si no, son 1
canvas.create_image(canvas.winfo_width()/2,
    canvas.winfo_height()/2, image = logo)
canvas.bind('<Configure>', on_expand)

#________PARTIR VENTANA FRAMES PARA ORGANIZAR WIDGETS________________
left_frame = tk.Frame(window, width = 500, height = 95, bg = 'grey')
left_frame.grid(column = 0, row = 1, sticky = 'NWE', padx=5, pady = 5)

left_frame_plotSelect = tk.Frame(left_frame, width = 500, height = 195, bg = 'grey')
left_frame_plotSelect.grid(column = 0, row = 1, columnspan = 10, sticky = 'WE', padx=5, pady = 5)

right_frame = tk.Frame(window, width = 500, height = 500, bg='grey')
right_frame.grid(column = 1, row = 1, sticky = 'NEWS', padx=5, pady = 5)

#_______CARGAR CSV________________________________________________
#funciones para cuando se clica dentro o fuera de la entrada de texto
def on_entry_click(event):
    if txt_CSVName.get() == 'Nombre del archivo .csv ...':
        txt_CSVName.delete(0,  'end')
        txt_CSVName.configure(fg = 'black')
def on_focus_out(event):
    if txt_CSVName.get() == '':
        txt_CSVName.insert(0, 'Nombre del archivo .csv ...')
        txt_CSVName.configure(fg = 'grey')
#crear entrada de texto
txt_CSVName = tk.Entry(left_frame, width = 50, fg = 'grey')
txt_CSVName.insert(0, 'Nombre del archivo .csv ...' )
txt_CSVName.grid(column = 0, row = 0, columnspan=2, sticky = 'EW', pady=20)
txt_CSVName.bind('<FocusIn>', on_entry_click)
txt_CSVName.bind('<FocusOut>', on_focus_out)

#boton para buscar archivo en sistema
def btn_browseCSV_clicked():
    filename = filedialog.askopenfilename(initialdir = '/Users/lomil/Documents/Python/code_linux',
        title = "Seleccione archivo .csv",
         filetypes = (("CSV Files", "*.csv*"),))
    txt_CSVName.delete(0, 'end')
    txt_CSVName.insert(0, filename)
    txt_CSVName.config(fg = 'black')#.subsample(5,5)
btn_browseCSV = tk.Button(left_frame, text = '...', 
    bg = 'orange', fg = 'black',
     command = btn_browseCSV_clicked)
btn_browseCSV.grid(column = 2, row = 0, sticky = 'N', pady=20)

#boton para abrir archivo seleccionado
def btn_openCSV_clicked():
    try:
        print(txt_CSVName.get())
        csv_data = pd.read_csv(str(txt_CSVName.get()), header=4)
        file_read = True
    except:
        tk.messagebox.showwarning('Ha ocurrido un error',
         'Introduzca un nombre de archivo o compruebe que el nombre es el correcto. Debe ser un archivo .csv. El nombre debe incluir la ruta absoluta del archivo.')
btn_openCSV = tk.Button(left_frame, text='Arir',
 bg='orange', command =btn_openCSV_clicked)
btn_openCSV.grid(row=0, column = 3, pady=20)

#_________Seleccionar Estilo de Grafico__________________________
lbl_selectPlot = tk.Label(left_frame_plotSelect, text='Seleccione un estilo de grafica', bg='gray')
lbl_selectPlot.grid(row=0, column=0, columnspan=2, sticky = 'W')
#select bar plot
def btn_selectScatterPlot_clicked():
    btn_selectScatterPlot.configure(image = scatterPlot)
    btn_selectBarPlot.configure(image = barPlot_gray)
    btn_selectSurfPlot.configure(image = surfPlot_gray)

scatterPlot = tk.PhotoImage(file = "/Users/lomil/Documents/Python/code_linux/imagenes/scatterPlot.png")
scatterPlot_gray = tk.PhotoImage(file = "/Users/lomil/Documents/Python/code_linux/imagenes/scatterPlot_gray.png")
btn_selectScatterPlot = tk.Button(left_frame_plotSelect, text='Barras',
 image=scatterPlot_gray, command = btn_selectScatterPlot_clicked)
btn_selectScatterPlot.grid(row=1, column=0, padx=30, pady = 20)
def btn_selectBarPlot_clicked():
    btn_selectBarPlot.configure(image = barPlot)
    btn_selectScatterPlot.configure(image = scatterPlot_gray)
    btn_selectSurfPlot.configure(image = surfPlot_gray)

barPlot = tk.PhotoImage(file = "/Users/lomil/Documents/Python/code_linux/imagenes/barPlot.png")
barPlot_gray = tk.PhotoImage(file = "/Users/lomil/Documents/Python/code_linux/imagenes/barPlot_gray.png")
btn_selectBarPlot = tk.Button(left_frame_plotSelect, text='Barras',
 image=barPlot_gray, command = btn_selectBarPlot_clicked)
btn_selectBarPlot.grid(row=1, column=1, padx=30, pady = 20)

#select surf plot
def btn_selectSurfPlot_clicked():
    btn_selectSurfPlot.configure(image = surfPlot)
    btn_selectBarPlot.configure(image = barPlot_gray)
    btn_selectScatterPlot.configure(image = scatterPlot_gray)
surfPlot = tk.PhotoImage(file = "/Users/lomil/Documents/Python/code_linux/imagenes/surfPlot.png")
surfPlot_gray = tk.PhotoImage(file="/Users/lomil/Documents/Python/code_linux/imagenes/surfPlot_gray.png")
btn_selectSurfPlot = tk.Button(left_frame_plotSelect, image = surfPlot_gray, command= btn_selectSurfPlot_clicked)
btn_selectSurfPlot.grid(row=1, column = 2, padx=30, pady = 20)

#________Seleccionar Tiempo_____________________________________
spinboxValues = []
for i in range(24):
    for j in range(60):
        for k in range(60):
            time = str(i) + ':' + str(j) + ':' + str(k)
            spinboxValues.append(time)

spin_fromTime = tk.Spinbox(left_frame, values = (spinboxValues))
spin_fromTime.grid(column = 0, row = 4)
spin_toTime = tk.Spinbox(left_frame, values = (spinboxValues))
spin_toTime.grid(column = 0, row = 5)

#_________Introducir titulo de grafica__________________________
txt_titulo = tk.Entry(left_frame, width = 30, fg = 'gray')
txt_titulo.insert(0, 'Introduzca el titulo de la grafica...')
txt_titulo.grid(row = 3, column = 0, pady=5)
#_________Seleccionar Columnas___________________________________


#________Generar grafica(s)______________________________________
def btn_plotClicked():
    #introducir todos los gets de las variables
    #necesarias para el plot
    pass

btn_plot = tk.Button(left_frame, text='Generar',
 bg='Orange', command=btn_plotClicked())
btn_plot.grid(row=7, column=0)

#__________Definir comportamiento al expandir la ventana_________
#definir como se expanden los widjets al expandir la ventana
window.rowconfigure(1, weight = 1)
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 2)

canvas.columnconfigure(0, weight = 1)
canvas.columnconfigure(1, weight = 1)

left_frame.columnconfigure(0, weight = 1)

left_frame_plotSelect.columnconfigure(0, weight = 1)
left_frame_plotSelect.columnconfigure(1, weight = 1)
left_frame_plotSelect.columnconfigure(2, weight = 1)
#################################################################
window.mainloop()
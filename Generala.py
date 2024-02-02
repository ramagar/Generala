from tkinter import *
from tkinter import ttk
from typing import Type
from PIL import Image, ImageTk


class Juego:
    '''Clase contenedora de la logica del juego'''
    def __init__(self):
        self.__cantidad_jugadores:int = int()
        self.__la_apuesta:str = str()
        self.__jugadores:list[str] = []
        self.__puntos_jugador:dict = {}
        self.__ronda:int = 0

    def set_cantidad_jugadores(self, cantidad):
        '''Metodo que setea la cantidad de jugadores'''
        self.__cantidad_jugadores = cantidad

    def get_cantidad_jugadores(self) -> int:
        '''Metodo que devuelve la cantidad de jugadores'''
        return self.__cantidad_jugadores
    
    def set_la_apuesta(self, apuesta:str) -> None:
        '''Metodo que setea la apuesta'''
        self.__la_apuesta = apuesta
        
    def get_la_apuesta(self):
        '''Metodo para obtener que es lo que se apuesta'''
        return self.__la_apuesta

    def set_jugadores(self, jugadores:list[str]) -> None:
        '''Metodo para setear los nombres de los jugadores y tambien sus puntos'''
        self.__jugadores = jugadores
        self.__puntos_jugador = (dict(zip(jugadores, [0 for _ in jugadores])))

    def get_jugadores(self) -> list[str]:
        '''Metodo para obtener los nombres de los jugadores'''
        return self.__jugadores
    
    def set_puntos_jugador(self, nombre:str, puntos:int = 0) -> None:
        self.__puntos_jugador[nombre:puntos]
        
    def get_puntos_jugador(self, nombre:str) -> int:
        return self.__puntos_jugador[nombre]
    
    def set_ronda(self) -> None:
        self.__ronda = self.__ronda + 1
        
    def get_ronda(self) -> int:
        return self.__ronda

class JuegoApp:
    '''Clase contenedora de la Interfaz Grafica del juego'''
    def __init__(self, root: Tk, juego: Juego) -> None:
        #Root
        self.root = root
        '''Ventana principal de la aplicacion grafica'''
        
        #Juego
        self.juego = juego
        '''Clase que contiene la logica del juego'''
        
        #MainFrame
        self.mainframe = Frame(root, background='#032339')
        '''Contenedor principal de widgets'''
        self.mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

        #Boton de cierre
        self.boton_cierre = Button(root, text='❌', font=('Arial', 8, 'bold'), foreground='red', background='#032339', pady=4, width=3, command=self.cerrar_programa)
        self.boton_cierre.place(relx=1, rely=0, anchor='ne')
        self.boton_cierre.bind('<Enter>', lambda event: self.boton_cierre.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton_cierre.bind('<Leave>', lambda event: self.boton_cierre.config(background='#18435F'))
        self.root.bind('<KeyPress-Escape>', lambda event: self.cerrar_programa())

        #Estilo de titulos
        self.estilo_titulo = {'font':'impact 55', 'foreground':'#FF8C00', 'background':'#032339'}

    def cerrar_programa(self) -> None:
        '''Metodo que permite cerrar el programa destruyendo el root'''
        root.destroy()
       
    def desvincular_teclas(self) -> None:  
        '''Metodo para desvincular teclas menos la tecla de escape'''
        for i in range (10):
            self.root.unbind(f'<KeyPress-{i}>')
            self.root.unbind(f'<KeyRelease-{i}>')
        self.root.unbind('<KeyPress-Return>')
        self.root.unbind('<KeyRelease-Return>')
       
    def eliminar_widgets(self) -> None:
        '''Metodo que destruye los widgets que contiene el mainframe'''  
        for widget in self.mainframe.winfo_children():
            widget.destroy()
            
    def cambiar_pantalla(self, nueva_pantalla:Type) -> None:
        '''Metodo que permite cambiar la pantalla de la interfaz'''
        self.desvincular_teclas()
        self.eliminar_widgets()
        nueva_pantalla(self.root, self.juego)
        
    def jugar(self) -> None:
        '''Metodo para mantener activo el juego'''
        pass
        #while True:

class PantallaInicial(JuegoApp):
    '''Pantalla inicial donde comienza la aplicacion'''
    def __init__(self, root: Tk, juego: Juego):
        super().__init__(root, juego)
        #Imagen para la presentacion
        imagen = ImageTk.PhotoImage(Image.open('logo.png'))
        label = Label(self.mainframe, image=imagen, background='#032339')
        label.pack()
        self.imagen_referencia = imagen

        #Estilo Barra de Progreso
        self.estilo_barra_progreso = ttk.Style()
        self.estilo_barra_progreso.theme_use("classic")
        self.estilo_barra_progreso.configure("TProgressbar", troughcolor='#1C5B83', thickness=20, background='#FF8C00')
        
        #Defino la barra de Progreso
        self.barra_progreso = ttk.Progressbar(self.mainframe, orient='horizontal', length=500, mode='determinate', style="Horizontal.TProgressbar")
        self.barra_progreso.pack(pady=20)
        
        #Inicio la barra de progreso
        self.iniciar_progreso()

    def iniciar_progreso(self):
        '''Metodo que activa la barra de progreso al iniciar el programa'''
        valor_actual = self.barra_progreso['value']
        if valor_actual < 100:
            self.barra_progreso['value'] += 100
            self.root.after(100, self.iniciar_progreso)
        else:
            self.cambiar_pantalla(Pantalla1)

class Pantalla1(JuegoApp):
    '''Pantalla inicial donde comienza la aplicacion'''
    def __init__(self, root: Tk, juego: Juego) -> None:
        super().__init__(root, juego)
        
        #Titulo
        self.titulo:Label = Label(self.mainframe, text='Cantidad de Jugadores', **self.estilo_titulo)
        self.titulo.pack(ipady=70)
        
        #Contenedores de botones
        self.button_container1:Frame = Frame(self.mainframe, background='#032339')
        self.button_container1.pack(pady=20)

        self.button_container2:Frame = Frame(self.mainframe, background='#032339')
        self.button_container2.pack(pady=20)

        #Estilo botones
        self.estilo_botones:dict = {'font':'impact 30', 'foreground':'#FF8C00', 'width':8, 'background':'#18435F'}
        
        #Defino los botones del 2 al 7
        for numero in range(2, 8):
            self.boton = Button(self.button_container1, text=str(numero), command=lambda num=numero: self.set_cantidad_jugadores(num), **self.estilo_botones)
            self.boton.grid(row=(0 if numero <= 4 else 1), column=(numero - 2 if numero <= 4 else numero - 5), padx=50, pady=30)
            self.boton.bind('<Enter>', lambda event, b=self.boton: b.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
            self.boton.bind('<Leave>', lambda event, b=self.boton: b.config(background='#18435F'))
            self.root.bind(f'<KeyPress-{numero}>', lambda event, b=self.boton, n=numero: self.set_cantidad_jugadores(n) or b.config(background='#1C5B83', foreground='#D84500'))
            self.root.bind(f'<KeyRelease-{numero}>', lambda event, b=self.boton: b.config(background='#18435F', foreground='#FF8C00'))
        
        #Boton Continuar
        self.boton_continuar = Button(self.button_container2, text='Continuar', command=lambda:self.cambiar_pantalla(Pantalla2), font='impact 30', foreground='#FF8C00', background='#18435F', width=10, state='disabled')
        self.root.bind('<KeyPress-Return>', lambda event: self.cambiar_pantalla(Pantalla2) if self.boton_continuar['state'] == 'normal' else None)
        self.boton_continuar.grid(row=0, column=0, padx=30, pady=20)

    def set_cantidad_jugadores(self, cantidad):
        '''Funcion que setea la cantidad de jugadores en funcion al boton que se oprimio, habilita el boton Continuar'''
        self.juego.set_cantidad_jugadores(cantidad)
        self.titulo.config(text=f'La Cantidad de Jugadores es de {cantidad}')
        self.boton_continuar.configure(state='normal')
        self.boton_continuar.bind('<Enter>', lambda event: self.boton_continuar.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton_continuar.bind('<Leave>', lambda event: self.boton_continuar.config(background='#18435F'))

class Pantalla2(JuegoApp):
    '''Segunda pantalla de la aplicacion grafica'''
    def __init__(self, root: Tk, juego: Juego) -> None:
        super().__init__(root, juego)
        
        #Defino el titulo
        self.titulo:Label = Label(self.mainframe, text='Escribir la Apuesta', **self.estilo_titulo)
        self.titulo.pack(ipady=70)
        
        #Estilo de cajas de texto
        self.estilo_caja_texto:dict = {'font':'impact 30', 'foreground':'#FF8C00', 'background':'#18435F', 'width':50, 'border':5, 'insertbackground':'#FF8C00', 'justify':'center'}
        
        #Estilo botones
        self.estilo_botones:dict = {'font':'impact 30', 'foreground':'#FF8C00', 'width':8, 'background':'#18435F'}
        
        #Defino la caja de texto
        self.texto_entrada:StringVar = StringVar()
        self.text_area:Entry = Entry(self.mainframe, textvariable=self.texto_entrada, **self.estilo_caja_texto)
        self.text_area.pack(pady=50, ipady=5)
        self.text_area.bind('<Enter>', lambda event: self.text_area.config(background='#1C5B83'))
        self.text_area.bind('<Leave>', lambda event: self.text_area.config(background='#18435F'))
        self.text_area.bind('<Return>', self.obtener_texto)
        
        self.boton_continuar:Button = Button(self.mainframe, text='Continuar', command=lambda: self.cambiar_pantalla(Pantalla3), **self.estilo_botones, state='disabled')
        self.boton_continuar.bind('<Enter>', lambda event: self.boton_continuar.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton_continuar.bind('<Leave>', lambda event: self.boton_continuar.config(background='#18435F'))
        self.boton_continuar.pack(pady=10)
    
    def validar_apuesta(self, apuesta:str) -> bool:
        '''Metodo que valida lo ingresado en la apuesta, si la apuesta es valida de vuelve True, de lo contrario False'''
        if apuesta.isspace() or not apuesta.isprintable or apuesta == '':
            return False
        else:
            self.boton_continuar.configure(state='normal')
            return True        

    def obtener_texto(self, event):
        '''Metodo que obtiene lo escrito en la caja de texto'''
        texto_ingresado:str = self.texto_entrada.get()
        if self.validar_apuesta(texto_ingresado):
            juego.set_la_apuesta(texto_ingresado)
            self.text_area.unbind('<Return>')
            self.boton_continuar.bind('<KeyPress-Return>', lambda event: self.cambiar_pantalla(Pantalla3))
            self.text_area.bind('<Return>', lambda event: self.cambiar_pantalla(Pantalla3))
            self.text_area.configure(state='disabled', disabledbackground='#1C5B83')
        else:
            self.texto_entrada.set("")
            if hasattr(self, 'problema'):
                self.problema.config(text='La apuesta ingresada no es valida, escribir otra por favor')
            else:
                self.problema:Label = Label(self.mainframe, text='La apuesta ingresada no es valida, escribir otra por favor', font='impact 22', foreground='#FF8C00', background='#032339')
                self.problema.pack()
        
class Pantalla3(JuegoApp):
    '''Segunda pantalla de la aplicacion grafica'''
    def __init__(self, root: Tk, juego: Juego) -> None:
        super().__init__(root, juego)
        
        #Crear titulo        
        self.titulo:Label = Label(self.mainframe, text='Escribir los nombres de los jugadores', **self.estilo_titulo)
        self.titulo.pack(ipady=70)
        
        self.contenedor:Frame = Frame(self.mainframe, background='#032339')
        self.contenedor.pack()

        # Estilo de label
        self.estilo_labels:dict = {'font':'impact 22', 'foreground':'#FF8C00', 'background':'#032339'}
        
        # Estilo de cajas de texto
        self.estilo_caja_texto:dict = {'font':'impact 22', 'foreground':'#FF8C00', 'background':'#18435F', 'width':20, 'border':5, 'insertbackground':'#FF8C00', 'justify':'center'}

        # Lista entradas
        self.nombres_entradas: list[StringVar] = []
        
        # Lista nombres jugadores
        self.nombres_jugadores: list[str] = []
        
        #Lista Casillas de verificacion
        self.lista_casillas_verificacion:list[Label] = []
        
        # Defino labels y entradas de texto
        for jugador in range(self.juego.get_cantidad_jugadores()):
            # Labels
            self.nombre_label:str = f'self.label{jugador + 1}'
            self.nombre_label:Label = Label(self.contenedor, text=f'Nombre del Jugador/a  {jugador + 1}', **self.estilo_labels)
            self.nombre_label.grid(column=0, row=jugador, ipady=3, pady=5, padx=(100,15))        
            
            # Entradas de texto
            nombre_entrada_texto:StringVar = StringVar()
            self.nombres_entradas.append(nombre_entrada_texto)
            nombre_caja_texto:str = f'self.caja_texto{jugador + 1}'
            nombre_caja_texto:Entry = Entry(self.contenedor, textvariable=nombre_entrada_texto, **self.estilo_caja_texto)
            nombre_caja_texto.grid(column=1, row=jugador, ipady=3, pady=5, padx=15)

            #Casillas de verificacion
            self.nombre_casilla_verificacion:str = f'self.casilla_verificacion{jugador +1}'
            self.nombre_casilla_verificacion:Label = Label(self.contenedor, text='❎', font='impact 22', foreground='red', background='#032339')
            self.nombre_casilla_verificacion.grid(column=2, row=jugador, ipady=3, pady=5, padx=15)
            self.lista_casillas_verificacion.append(self.nombre_casilla_verificacion)  

        # Defino boton de continuar
        self.boton_continuar:Button = Button(self.contenedor, text='Continuar', command=lambda: self.cambiar_pantalla(Pantalla4), font='impact 30', foreground='#FF8C00', background='#18435F', width=10, state='disabled')
        self.boton_continuar.bind('<Enter>', lambda event: self.boton_continuar.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton_continuar.bind('<Leave>', lambda event: self.boton_continuar.config(background='#18435F'))
        self.boton_continuar.grid(row=2, column=3, padx=(90, 150))

        #Defino boton de verificacion
        self.boton_verificar:Button = Button(self.contenedor, text='Verificar', command=lambda: self.obtener_texto(self.nombres_entradas), font='impact 15', foreground='#FF8C00', background='#18435F', width=10)
        self.boton_verificar.bind('<Enter>', lambda event: self.boton_verificar.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton_verificar.bind('<Leave>', lambda event: self.boton_verificar.config(background='#18435F'))
        self.boton_verificar.grid(row=3, column=3, padx=(90, 150), pady=(20,0))
                
        #Defino label de verificacion
        self.label_verificacion:Label = Label(self.contenedor, text='Pulsa ENTER para verificar\nLos nombres no pueden estar repetidos o contener numeros', foreground='#FF8C00', background='#032339', font='impact 12')
        self.label_verificacion.grid(row=4, column=3, padx=(90, 150))

        self.root.bind('<Return>', lambda event, entry=self.nombres_entradas: self.obtener_texto(entry))
    
    def obtener_texto(self, entries: list[StringVar]):
        '''Metodo que obtiene los nombres escritos en las cajas de texto'''
        self.nombres_jugadores:list[str] = [entry.get().upper() for entry in entries]
        self.validar_nombres(self.nombres_jugadores)
        
    def validar_nombres(self, nombres: list[str]) -> None:
        '''Metodo que valida los nombres ingresados en las cajas de texto'''
        for pos, nombre_jugador in enumerate(nombres):
            if not nombre_jugador.isalpha() or nombres.count(nombre_jugador) > 1:
                self.nombres_jugadores.clear()
                self.lista_casillas_verificacion[pos].config(text='❎', foreground='red')
                return None
            else:
                self.lista_casillas_verificacion[pos].config(text='✅', foreground='green')
        self.juego.set_jugadores(nombres)
        self.boton_continuar.configure(state='normal')
        self.boton_verificar.configure(state='disabled')
        self.label_verificacion.config(text=f'{' '*35}Pulsa ENTER para Continuar{' '*35}\n')
        self.root.bind('<Return>', lambda event: self.cambiar_pantalla(Pantalla4))

class Pantalla4(JuegoApp):
    '''Segunda pantalla de la aplicacion grafica'''
    def __init__(self, root: Tk, juego: Juego) -> None:
        super().__init__(root, juego)
        
        # Estilo para el titulo
        self.estilo_titulo: dict = {'font': 'impact 35', 'foreground': '#FF8C00', 'background': '#032339'}
        
        # Crear el titulo
        self.titulo: Label = Label(self.mainframe, text='Le toca jugar a Jugador', **self.estilo_titulo)
        self.titulo.pack(pady=0, ipady=0, padx=(270,0))
        
        # Crear el marco principal
        self.contenedor_tablero: Frame = Frame(self.mainframe, background='#032339')
        self.contenedor_tablero.pack(expand=True, fill='both', pady=0, ipady=0)

        # Configuración para que el Frame se expanda
        self.contenedor_tablero.columnconfigure(0, weight=1)
        self.contenedor_tablero.rowconfigure(0, weight=1)

        # Crear un Canvas para el tablero
        self.canvas: Canvas = Canvas(self.contenedor_tablero, background='#032339', highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew', pady=0)

        # Calcula el tamaño de la cuadrícula
        num_filas: int = 13
        num_columnas: int = self.juego.get_cantidad_jugadores() + 2

        # Dibujar líneas horizontales y verticales
        margen = 50
        ancho_celda = (810 - 2 * margen) / num_columnas * 1.8
        alto_celda = (550 - 2 * margen) / num_filas * 1.4

        # Dibujar líneas horizontales y verticales después de los casilleros
        for i in range(num_filas + 1):
            y = i * alto_celda + margen
            self.canvas.create_line((margen + ancho_celda), y, 700 - margen, y, fill='#FF8C00')  # Líneas horizontales

        for i in range(1, num_columnas + 1):  # Comenzar desde la columna 1
            x = i * ancho_celda + margen
            self.canvas.create_line(x, margen, x, 550 - margen, fill='#FF8C00')  # Líneas verticales

        # Crear los casilleros con texto o botón
        for row in range(num_filas):
            for col in range(num_columnas):
                x1 = col * ancho_celda + margen
                y1 = row * alto_celda + margen
                x2 = (col + 1) * ancho_celda + margen
                y2 = (row + 1) * alto_celda + margen
                
                # Determinar el color de fondo según la fila
                if row == 0: 
                    background_color = '#663D7A' 
                elif row <= 6:
                    background_color = f'#1C{7-row}B83' 
                elif row > 6 and row <= 11:
                    background_color = f'#1C5B{11-row}3'
                else:
                    background_color = '#BB2020'
                
                # Agrega el texto o botón
                if row == 0 and col > 1:
                    texto = self.juego.get_jugadores()[col-2]
                elif col == 0 and row > 0 and row < 7:
                    #Modificar para agregar botones segun fila
                    btn_width = (x2 - x1) / 6  # Ancho para cinco botones
                    for i in range(5):
                        btn = Button(self.canvas, text=f'x{i+1}', font='impact 12', background='#18435F', foreground='#FF8C00')
                        btn.place(x=x1 + (i + 0.5) * btn_width, y=(y1 + y2) / 2, anchor='center')
                    continue
                elif col == 0 and row >= 7 and row != 12:
                    btn_width = (x2 - x1) / 3
                    btn = Button(self.canvas, text=f'Servida', font='impact 12', background='#18435F', foreground='#FF8C00')
                    btn.place(x=x1 + (0 + 0.5) * btn_width, y=(y1 + y2) / 2, anchor='center')
                    btn2 = Button(self.canvas, text=f'Normal', font='impact 12', background='#18435F', foreground='#FF8C00')
                    btn2.place(x=x1 + (1 + 1) * btn_width, y=(y1 + y2) / 2, anchor='center')
                elif col == 0 and row == 12:
                    btn = Button(self.canvas, text=f'Mostrar', font='impact 12', background='#18435F', foreground='#FF8C00')
                    btn.place(x=(x1 + x2) / 2.25, y=(y1 + y2) / 2, anchor='center')
                    continue
                elif col == 1 and row == 0 or col == 0 and row > 11 or col == 0 and row == 0:
                    texto = ''
                elif col == 1 and row >= 1:
                    if row < 7:
                        texto = f'{row}'
                    elif row == 7:
                        texto = 'Escalera'
                    elif row == 8:
                        texto = 'Full'
                    elif row == 9:
                        texto = 'Poker'
                    elif row == 10:
                        texto = 'Generala'
                    elif row == 11:
                        texto = 'Doble Generala'
                    else:
                        texto = 'Puntos Totales'
                elif row == 12 and col != 0:
                    texto = '***'
                else:
                    texto = '*'
                
                x_texto = (x1 + x2) / 2
                y_texto = (y1 + y2) / 2

                if col != 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=background_color)
                    self.canvas.create_text(x_texto, y_texto, text=texto, font='impact 15', fill='#FF8C00')

        self.jugar()

if __name__ == "__main__":
    #Defino el root
    root = Tk()     
    root.title('Generala')
    root.attributes('-fullscreen', True)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    juego = Juego()
    app = PantallaInicial(root, juego)
    root.mainloop()
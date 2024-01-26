from tkinter import *
from tkinter import Tk
from typing import Type

class Juego:
    '''Clase contenedora de la logica del juego'''
    def __init__(self):
        self.__cantidad_jugadores = int()
        self.__la_apuesta = str()
        self.nombres_jugadores = []

    def set_cantidad_jugadores(self, cantidad):
        self.__cantidad_jugadores = cantidad

    def get_cantidad_jugadores(self):
        return self.__cantidad_jugadores
    
    def set_la_apuesta(self, apuesta):
        self.__la_apuesta = apuesta
        
    def get_la_apuesta(self):
        return self.__la_apuesta

    def set_nombre_jugador(self, nombre):
        self.nombres_jugadores.append(nombre)

    def get_nombres_jugadores(self):
        return self.nombres_jugadores
    

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
        self.boton_cierre = Button(root, text='X', font=('Arial', 10, 'bold'), foreground='red', background='#032339', width=3, command=self.cerrar_programa)
        '''Boton que cierra el programa'''
        self.boton_cierre.place(relx=1, rely=0, anchor='ne')
        self.boton_cierre.bind('<Enter>', lambda event: self.boton_cierre.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton_cierre.bind('<Leave>', lambda event: self.boton_cierre.config(background='#18435F'))
        self.root.bind('<KeyPress-Escape>', lambda event: self.cerrar_programa())

        #Estilo de titulos
        self.estilo_titulo = {'font':'impact 55', 'foreground':'#FF8C00', 'background':'#032339'}
        '''Estilo para los titulos'''
        
        #Estilo de cajas de texto
        self.estilo_caja_texto = {'font':'impact 30', 'foreground':'#FF8C00', 'background':'#205067', 'width':40}

    def cerrar_programa(self):
        '''Metodo que permite cerrar el programa destruyendo el root'''
        root.destroy()
       
    def cambiar_pantalla(self, nueva_pantalla:Type):
        '''Metodo que permite cambiar la pantalla de la interfaz a una nueva que se quiera producir destruyendo los widgets que contiene el mainframe'''
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        nueva_pantalla(self.root, self.juego)
    

            
class PantallaInicial(JuegoApp):
    '''Pantalla inicial donde comienza la aplicacion'''
    def __init__(self, root: Tk, juego: Juego):
        super().__init__(root, juego)
        
        #Titulo
        self.titulo = Label(self.mainframe, text='Cantidad de Jugadores', **self.estilo_titulo)
        '''Label del titulo'''
        self.titulo.pack(ipady=70)
        
        #Contenedores de botones
        self.button_container1 = Frame(self.mainframe, background='#032339')
        '''Contenedor de botones 1'''
        self.button_container1.pack(pady=20)

        self.button_container2 = Frame(self.mainframe, background='#032339')
        '''Contenedor de botones 2'''
        self.button_container2.pack(pady=20)

        #Estilo botones
        self.estilo_botones = {'font':'impact 30', 'foreground':'#FF8C00', 'width':8, 'background':'#18435F'}
        '''Estilo de botones'''
        

        # Definir los botones
        #Boton 1
        self.boton1 = Button(self.button_container1, text='2', command=lambda: self.set_cantidad_jugadores(2), **self.estilo_botones)
        self.boton1.grid(row=0, column=0, padx=50, pady=30)
        self.boton1.bind('<Enter>', lambda event: self.boton1.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton1.bind('<Leave>', lambda event: self.boton1.config(background='#18435F'))
        self.root.bind('<KeyPress-2>', lambda event: self.set_cantidad_jugadores(2) or self.boton1.config(background='#1C5B83', foreground='#D84500'))
        self.root.bind('<KeyRelease-2>', lambda event: self.boton1.config(background='#18435F', foreground='#FF8C00'))
        
        #Boton 2
        self.boton2 = Button(self.button_container1, text='3', command=lambda: self.set_cantidad_jugadores(3), **self.estilo_botones)
        self.boton2.grid(row=0, column=1, padx=50, pady=30)
        self.boton2.bind('<Enter>', lambda event: self.boton2.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton2.bind('<Leave>', lambda event: self.boton2.config(background='#18435F'))
        self.root.bind('<KeyPress-3>', lambda event: self.set_cantidad_jugadores(3) or self.boton2.config(background='#1C5B83', foreground='#D84500'))
        self.root.bind('<KeyRelease-3>', lambda event: self.boton2.config(background='#18435F', foreground='#FF8C00'))
        
        #Boton 3
        self.boton3 = Button(self.button_container1, text='4', command=lambda: self.set_cantidad_jugadores(4), **self.estilo_botones)
        self.boton3.grid(row=0, column=2, padx=50, pady=30)
        self.boton3.bind('<Enter>', lambda event: self.boton3.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton3.bind('<Leave>', lambda event: self.boton3.config(background='#18435F'))
        self.root.bind('<KeyPress-4>', lambda event: self.set_cantidad_jugadores(4) or self.boton3.config(background='#1C5B83', foreground='#D84500'))
        self.root.bind('<KeyRelease-4>', lambda event: self.boton3.config(background='#18435F', foreground='#FF8C00'))
        
        #Boton 4
        self.boton4 = Button(self.button_container1, text='5', command=lambda: self.set_cantidad_jugadores(5), **self.estilo_botones)
        self.boton4.grid(row=1, column=0, padx=50, pady=30)
        self.boton4.bind('<Enter>', lambda event: self.boton4.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton4.bind('<Leave>', lambda event: self.boton4.config(background='#18435F'))
        self.root.bind('<KeyPress-5>', lambda event: self.set_cantidad_jugadores(5) or self.boton4.config(background='#1C5B83', foreground='#D84500'))
        self.root.bind('<KeyRelease-5>', lambda event: self.boton4.config(background='#18435F', foreground='#FF8C00'))
        
        #Boton 5
        self.boton5 = Button(self.button_container1, text='6', command=lambda: self.set_cantidad_jugadores(6), **self.estilo_botones)
        self.boton5.grid(row=1, column=1, padx=50, pady=30)
        self.boton5.bind('<Enter>', lambda event: self.boton5.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton5.bind('<Leave>', lambda event: self.boton5.config(background='#18435F'))
        self.root.bind('<KeyPress-6>', lambda event: self.set_cantidad_jugadores(6) or self.boton5.config(background='#1C5B83', foreground='#D84500'))
        self.root.bind('<KeyRelease-6>', lambda event: self.boton5.config(background='#18435F', foreground='#FF8C00'))
        
        #Boton 6
        self.boton6 = Button(self.button_container1, text='7', command=lambda: self.set_cantidad_jugadores(7), **self.estilo_botones)
        self.boton6.grid(row=1, column=2, padx=50, pady=30)
        self.boton6.bind('<Enter>', lambda event: self.boton6.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton6.bind('<Leave>', lambda event: self.boton6.config(background='#18435F'))
        self.root.bind('<KeyPress-7>', lambda event: self.set_cantidad_jugadores(7) or self.boton6.config(background='#1C5B83', foreground='#D84500'))
        self.root.bind('<KeyRelease-7>', lambda event: self.boton6.config(background='#18435F', foreground='#FF8C00'))
        
        #Boton 7
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
    def __init__(self, root: Tk, juego: Juego):
        super().__init__(root, juego)
        
        #Defino el titulo
        self.titulo = Label(self.mainframe, text='Que se Apuesta', **self.estilo_titulo)
        '''Label del titulo'''
        self.titulo.pack(ipady=70)
        
        #Defino la caja de texto
        self.texto_entrada = StringVar()
        '''Entrada del texto'''
        self.text_area = Text(self.mainframe, wrap="word", height=2, **self.estilo_caja_texto)
        self.text_area.pack(pady=100)

        
        
                
        
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

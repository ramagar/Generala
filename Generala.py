from tkinter import *
from tkinter import Tk
from typing import Type

class Juego:
    '''Clase contenedora de la logica del juego'''
    def __init__(self):
        self.__cantidad_jugadores:int = int()
        self.__la_apuesta:str = str()
        self.__jugadores:list[str] = []

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
        '''Metodo para setear los nombres de los jugadores'''
        self.__jugadores = jugadores

    def get_jugadores(self) -> list[str]:
        '''Metodo para obtener los nombres de los jugadores'''
        return self.__jugadores
    

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
        '''Boton que cierra el programa'''
        self.boton_cierre.place(relx=1, rely=0, anchor='ne')
        self.boton_cierre.bind('<Enter>', lambda event: self.boton_cierre.config(background='#1C5B83', activeforeground='#D84500', activebackground='#205067'))
        self.boton_cierre.bind('<Leave>', lambda event: self.boton_cierre.config(background='#18435F'))
        self.root.bind('<KeyPress-Escape>', lambda event: self.cerrar_programa())

        #Estilo de titulos
        self.estilo_titulo = {'font':'impact 55', 'foreground':'#FF8C00', 'background':'#032339'}
        '''Estilo para los titulos'''

    def cerrar_programa(self) -> None:
        '''Metodo que permite cerrar el programa destruyendo el root'''
        root.destroy()
       
    def desvincular_teclas(self) -> None:  
        '''Metodo para desvincular teclas menos la tecla de escape'''
        for i in range (10):
            self.root.unbind(f'<KeyPress-{i}>')
            self.root.unbind(f'<KeyRelease-{i}>')
        self.root.unbind(f'<KeyPress-Return>')
        self.root.unbind(f'<KeyRelease-Return>')
        self.root.unbind(f'<KeyPress-f>')
        self.root.unbind(f'<KeyRelease-f>')
        self.root.unbind(f'<KeyPress-e>')
        self.root.unbind(f'<KeyRelease-e>')
        self.root.unbind(f'<KeyPress-p>')
        self.root.unbind(f'<KeyRelease-p>')
        self.root.unbind(f'<KeyPress-g>')
        self.root.unbind(f'<KeyRelease-g>')
        self.root.unbind(f'<KeyPress-d>')
        self.root.unbind(f'<KeyRelease-d>')
        
        
       
    def eliminar_widgets(self) -> None:
        '''Metodo que destruye los widgets que contiene el mainframe'''  
        for widget in self.mainframe.winfo_children():
            widget.destroy()
            
    def cambiar_pantalla(self, nueva_pantalla:Type) -> None:
        '''Metodo que permite cambiar la pantalla de la interfaz'''
        self.desvincular_teclas()
        self.eliminar_widgets()
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
        
        #Estilo de cajas de texto
        self.estilo_caja_texto = {'font':'impact 30', 'foreground':'#FF8C00', 'background':'#18435F', 'width':50, 'border':5, 'insertbackground':'#FF8C00', 'justify':'center'}
        
        #Defino la caja de texto
        self.texto_entrada = StringVar()
        '''Entrada del texto'''
        self.text_area = Entry(self.mainframe, textvariable=self.texto_entrada, **self.estilo_caja_texto)
        self.text_area.pack(pady=100, ipady=5)
        self.text_area.bind('<Enter>', lambda event: self.text_area.config(background='#1C5B83'))
        self.text_area.bind('<Leave>', lambda event: self.text_area.config(background='#18435F'))
        self.text_area.bind('<Return>', self.obtener_texto)
    
    def validar_apuesta(self, apuesta:str) -> bool:
        '''Metodo que valida lo ingresado en la apuesta, si la apuesta es valida de vuelve True, de lo contrario False'''
        if apuesta.isspace() or not apuesta.isprintable or apuesta == '':
            return False
        else:
            return True        

    def obtener_texto(self, event):
        texto_ingresado = self.texto_entrada.get()
        self.texto_entrada.set("")
        if self.validar_apuesta(texto_ingresado):
            juego.set_la_apuesta(texto_ingresado)
            self.cambiar_pantalla(Pantalla3)
        else:
            if hasattr(self, 'problema'):
                self.problema.config(text='La apuesta ingresada no es valida, escribir otra por favor')
            else:
                self.problema = Label(self.mainframe, text='La apuesta ingresada no es valida, escribir otra por favor', font='impact 22', foreground='#FF8C00', background='#032339')
                self.problema.pack()
        
        
class Pantalla3(JuegoApp):
    '''Segunda pantalla de la aplicacion grafica'''
    def __init__(self, root: Tk, juego: Juego):
        super().__init__(root, juego)
                
        self.titulo = Label(self.mainframe, text='Escribir los nombres de los jugadores', **self.estilo_titulo)
        '''Label del titulo'''
        self.titulo.pack(ipady=70)
        
        self.contenedor = Frame(self.mainframe, background='#032339')
        '''Contenedor de botones 1'''
        self.contenedor.pack()

        # Estilo de label
        self.estilo_labels = {'font':'impact 22', 'foreground':'#FF8C00', 'background':'#032339'}
        
        # Estilo de cajas de texto
        self.estilo_caja_texto = {'font':'impact 22', 'foreground':'#FF8C00', 'background':'#18435F', 'width':20, 'border':5, 'insertbackground':'#FF8C00', 'justify':'center'}

        # Lista entradas
        self.nombres_entradas: list[StringVar] = []
        
        # Lista nombres jugadores
        self.nombres_jugadores: list[str] = []
        
        #Lista Casillas de verificacion
        self.lista_casillas_verificacion:list[Label] = []
        
        # Defino labels y entradas de texto
        for jugador in range(self.juego.get_cantidad_jugadores()):
            # Labels
            self.nombre_label = f'self.label{jugador + 1}'
            self.nombre_label = Label(self.contenedor, text=f'Nombre del Jugador/a  {jugador + 1}', **self.estilo_labels)
            self.nombre_label.grid(column=0, row=jugador, ipady=3, pady=5, padx=(100,15))        
            
            # Entradas de texto
            nombre_entrada_texto = StringVar()
            self.nombres_entradas.append(nombre_entrada_texto)
            nombre_caja_texto = f'self.caja_texto{jugador + 1}'
            nombre_caja_texto = Entry(self.contenedor, textvariable=nombre_entrada_texto, **self.estilo_caja_texto)
            nombre_caja_texto.grid(column=1, row=jugador, ipady=3, pady=5, padx=15)

            #Casillas de verificacion
            self.nombre_casilla_verificacion = f'self.casilla_verificacion{jugador +1}'
            self.nombre_casilla_verificacion = Label(self.contenedor, text='', **self.estilo_labels)
            self.nombre_casilla_verificacion.grid(column=2, row=jugador, ipady=3, pady=5, padx=15)
            self.lista_casillas_verificacion.append(self.nombre_casilla_verificacion)  

        # Defino boton de continuar
        self.boton_continuar = Button(self.contenedor, text='Continuar', command=lambda: self.cambiar_pantalla(Pantalla4), font='impact 30', foreground='#FF8C00', background='#18435F', width=10, state='disabled')
        self.boton_continuar.grid(row=int((self.juego.get_cantidad_jugadores()-1)/2), column=3, padx=(130, 150))
        
        #Defino label de verificacion
        self.label_verificacion = Label(self.contenedor, text='\nPulsa ENTER para verificar\n\nLos nombres no pueden estar repetidos o contener numeros', foreground='#FF8C00', background='#032339', font='impact 12')
        self.label_verificacion.grid(row=int((self.juego.get_cantidad_jugadores()-1)/2)+1, column=3, padx=(130, 150))

        self.root.bind('<Return>', lambda event, entry=self.nombres_entradas: self.obtener_texto(entry))
    
    def obtener_texto(self, entries: list[StringVar]):
        '''Metodo que obtiene los nombres escritos en las cajas de texto'''
        self.nombres_jugadores = [entry.get().upper() for entry in entries]
        self.validar_nombres(self.nombres_jugadores)
        
    def validar_nombres(self, nombres: list[str]) -> None:
        '''Metodo que valida los nombres ingresados en las cajas de texto'''
        for pos, nombre_jugador in enumerate(nombres):
            if not nombre_jugador.isalpha() or nombres.count(nombre_jugador) > 1:
                self.nombres_jugadores.clear()
                self.lista_casillas_verificacion[pos].config(text='❎')
                return None
            else:
                self.lista_casillas_verificacion[pos].config(text='✅')
        self.juego.set_jugadores(nombres)
        self.boton_continuar.configure(state='normal')
        self.root.bind('<Return>', lambda event: self.cambiar_pantalla(Pantalla4))

        
class Pantalla4(JuegoApp):
    '''Segunda pantalla de la aplicacion grafica'''
    def __init__(self, root: Tk, juego: Juego):
        super().__init__(root, juego)
        print('Los jugadores son:', self.juego.get_jugadores())
        print('Se apuesta: ', self.juego.get_la_apuesta())

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

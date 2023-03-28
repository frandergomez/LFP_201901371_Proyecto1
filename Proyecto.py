import tkinter as tk
import webbrowser
from tkinter import filedialog
import json
import graphviz

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Lenguajes formales A")
        self.pack()
        self.create_widgets()
        #self.mostrar_errores = ""

    def create_widgets(self):
        # Crear la barra de menú
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # Crear el menú "Archivo"
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        file_menu.add_command(label = "Guardar Como", command=self.guardar_como)
        file_menu.add_command(label="Analizar", command=self.analizar_texto)
        file_menu.add_command(label="Errores", command=self.mostrar_errores)
        file_menu.add_command(label="Grafica", command=self.mostrar_grafica)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.master.quit)
        menubar.add_cascade(label="Archivo", menu=file_menu)

        # Crear el menú "Herramientas"
        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Manual de Usuario", command=self.manual_usuario)
        tools_menu.add_command(label="Manuan Técnico", command=self.manual_tecnico)
        tools_menu.add_command(label="Temas de Ayuda", command=self.temas_ayuda)
        menubar.add_cascade(label="Herramientas", menu=tools_menu)

        # Agregar un cuadro de texto para editar el archivo
        self.textbox = tk.Text(self)
        self.textbox.pack(fill="both", expand=True)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                self.textbox.delete("1.0", tk.END)
                self.textbox.insert(tk.END, f.read())

    def guardar_archivo(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.textbox.get("1.0", tk.END))

    def guardar_como(self):
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
        file_path = filedialog.asksaveasfilename(filetypes=filetypes)
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.textbox.get("1.0", tk.END))

    def analizar_texto(self):
        # Obtener el texto del cuadro de texto
        texto = self.textbox.get("1.0", tk.END)

        # Intentar cargar el texto como un objeto JSON
        try:
            datos = json.loads(texto)
        except json.JSONDecodeError as e:
            # Mostrar un mensaje de error si el texto no es un JSON válido
            tk.messagebox.showerror("Error", "El texto no es un JSON válido: {}".format(str(e)))
            return

        # Mostrar los elementos reconocidos en una nueva ventana
        lista_elementos = list(datos.keys())
        elementos_window = tk.Toplevel(self.master)
        elementos_window.title("Elementos reconocidos")
        elementos_label = tk.Label(elementos_window, text="\n".join(lista_elementos))
        elementos_label.pack()
        pass

    def mostrar_errores(self):
        # Obtener el texto del cuadro de texto
        texto = self.textbox.get("1.0", tk.END)

        # Intentar cargar el texto como un objeto JSON
        try:
            datos = json.loads(texto)
        except json.JSONDecodeError as e:
            # Mostrar un mensaje de error si el texto no es un JSON válido
            tk.messagebox.showerror("Error", "El texto no es un JSON válido: {}".format(str(e)))
            return

        # Analizar el texto para buscar errores
        errores = []
        for elemento, valor in datos.items():
            if not isinstance(valor, str):
                errores.append("El valor para el elemento {} no es una cadena: {}".format(elemento, valor))

        # Mostrar los errores en una nueva ventana
        if errores:
            errores_window = tk.Toplevel(self.master)
            errores_window.title("Errores encontrados")
            errores_label = tk.Label(errores_window, text="\n".join(errores))
            errores_label.pack()
        else:
            tk.messagebox.showinfo("Errores", "No se encontraron errores.")
        pass

        #Mostrar la grafica con nodos
    def mostrar_grafica(self):
        # Definir los nodos y aristas
        nodos = ["A", "B", "C", "D", "E"]
        aristas = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "A")]

        # Crear el objeto Graph
        g = graphviz.Graph()

        # Agregar los nodos al objeto Graph
        for nodo in nodos:
            g.node(nodo)

        # Agregar las aristas al objeto Graph
        for arista in aristas:
            g.edge(arista[0], arista[1])

        # Guardar el diagrama en un archivo PDF
        g.render(filename='diagrama_con_nodos', format='pdf')
        pass

    def manual_usuario(self):
        #cambiar la direccion del archivo para que se abra la documentacion de este proyecto
        pathTecnico = "file:///C:/Users/DELL/Desktop/Proyecto1%20lenguajes%20formales/Manual_Usuario.pdf" 
        webbrowser.open_new(pathTecnico)
        pass

    def manual_tecnico(self):
        #cambiar la direccion del archivo para que se abra la documentacion de este proyecto
        pathTecnico = "file:///C:/Users/DELL/Desktop/Proyecto1%20lenguajes%20formales/Manual_Tecnico.pdf" 
        webbrowser.open_new(pathTecnico)
        pass

    def temas_ayuda(self):
        # Crear la ventana emergente
        ayuda_window = tk.Toplevel(self.master)
        ayuda_window.title("Temas de Ayuda")

        # Agregar un Label con el texto de ayuda
        ayuda_texto = "Graphviz es una herramienta de visualizacion de graficos que permite crear diagramas de manera facil y rapida. 1. Descarga e instala Grapviz: es un sistema libre que se puede descargar de la pagina: (https://graphviz.org/download/). 2. Crea un archivo de texto plano: Crea un archivo de texto plano con la extensión dot. Este archivo debe contener el código que describe el grafo que deseas visualizar. 3. Escribe el código para el grafo: Utiliza el lenguaje de descripción de grafo de Graphviz para escribir el código que describe el grafo que deseas visualizar. Este código incluirá la estructura del grafo, los nodos y las aristas. 4. Compila el archivo .dot: Utiliza el comando dot de Graphviz para compilar el archivo .dot. Por ejemplo, si tu archivo se llama grafo.dot, escribe en la terminal dot -Tpdf grafo.dot -o grafo.pdf para compilarlo en formato PDF. 5. Visualiza el grafo: Abre el archivo PDF en un visor de PDF para visualizar el grafo. También puedes compilar el archivo en otros formatos como PNG, SVG o JPG."
        ayuda_label = tk.Label(ayuda_window, text=ayuda_texto)
        ayuda_label.pack()
        pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()
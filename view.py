from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model import Agenda,Data



class App:
    ##### armado de menu y operadores de entry/tabla
    def __init__(self, master):
        self.frame = master
        self.frame.title("Iniciar Sesion")
        self.frame.config(background="LightCyan3")
        self.frame.geometry("390x250")
        self.draw_label_login()
        self.draw_entry_login()
        self.draw_button_login()

    def draw_button_login(self):
        self.btn_confirm = Button(
            self.frame,
            foreground="white",
            text="Ingresar",
            borderwidth=2,
            relief="flat",
            cursor="hand1",
            overrelief="raise",
            background="black",
            command=lambda: self.login(),
        ).place(x=180, y=138, width=70)
        self.btn_registro = Button(
            self.frame,
            foreground="white",
            text="Registrarme",
            borderwidth=2,
            relief="flat",
            cursor="hand1",
            overrelief="raise",
            background="black",
            command=lambda: self.registro(),
        ).place(x=180, y=175, width=70)

    def draw_entry_login(self):
        # variables

        self.inicio = StringVar()
        self.contraseña = StringVar()
        self.lb_sesion = Entry(
            self.frame,
            font=("Arial", 12),
            relief="flat",
            background="linen",
            textvariable=self.inicio,
        ).place(x=130, y=55)
        self.lb_contraseña = Entry(
            self.frame,
            font=("Arial", 12),
            relief="flat",
            background="linen",
            textvariable=self.contraseña,
            show="*",
        ).place(x=130, y=100)

    def draw_label_login(self):
        self.lbl_titulo = Label(
            self.frame,
            foreground="black",
            background="LightCyan3",
            font=("Arial", 15, "bold italic"),
            text="INICIAR SESION",
        ).place(x=120, y=15)
        self.lbl_inicio = Label(
            self.frame, foreground="black", background="LightCyan3", text="Usuario:"
        ).place(x=60, y=55)
        self.lbl_password = Label(
            self.frame,
            foreground="black",
            textvariable="*",
            background="LightCyan3",
            text="Contraseña:",
        ).place(x=60, y=100)

    def login(self):
        if (self.inicio.get() != "" and self.contraseña.get() != ""):
            arr = [self.inicio.get(), self.contraseña.get()]
            print("usuario ingresado:{} contraseña: {}".format(arr[0],arr[1]))
            d = Data()
            if d.verification_login(arr) is True:
                # inicio de programa
                # self.frame.quit()
                self.draw_window()
                self.draw_entry()
                self.draw_buttons()
                self.draw_label()
                self.draw_list()
            else:
                messagebox.showinfo(title="Error", message="Error usuario no registrado")
            
        else:
            messagebox.showinfo(title="Error", message="Error campos vacios")

    def registro(self):

        ##definimos variables
        self.usuario = StringVar()
        self.password = StringVar()
        self.mail = StringVar()

        self.pop = Toplevel(self.frame, background="LightCyan3")
        self.pop.geometry("350x280")
        ##labels
        self.lbl_user = Label(
            self.pop,
            font=("Arial", 10, "bold"),
            fg="black",
            bg="LightCyan3",
            text="Usuario:",
        ).place(x=50, y=30)
        self.lbl_password = Label(
            self.pop,
            font=("Arial", 10, "bold"),
            fg="black",
            bg="LightCyan3",
            text="Contraseña:",
        ).place(x=50, y=80)
        self.lbl_mail = Label(
            self.pop,
            font=("Arial", 10, "bold"),
            fg="black",
            bg="LightCyan3",
            text="e-mail:",
        ).place(x=50, y=130)
        ##entry
        self.txt_usuario = Entry(
            self.pop,
            font=("Arial", 12),
            relief="flat",
            background="white",
            textvariable=self.usuario,
        ).place(x=140, y=30)
        self.txt_password = Entry(
            self.pop,
            font=("Arial", 12),
            relief="flat",
            background="white",
            textvariable=self.password,
        ).place(x=140, y=80)
        self.txt_email = Entry(
            self.pop,
            font=("Arial", 12),
            relief="flat",
            background="white",
            textvariable=self.mail,
        ).place(x=140, y=130)
        ##button
        self.btn_registro = Button(
            self.pop,
            text="Aceptar",
            fg="black",
            background="SeaGreen3",
            command=lambda: self.confirm_registro(),
        ).place(x=160, y=170)

    def confirm_registro(self):
        if (
            self.usuario.get() != ""
            and self.password.get() != ""
            and self.mail.get() != ""
        ):
            d = Data()
            arr = [self.usuario.get(), self.password.get(), self.mail.get()]
            d.insert_user(arr)
            messagebox.showinfo(title="Exito", message="Usuario Guardado Existosamente")
            self.pop.destroy()
        else:
            messagebox.showinfo(
                title="Error", message="No se pudo registrar con exito", parent=self.pop
            )

    def draw_window(self):
        self.frame.withdraw()  # cierra ventana inicio sesion
        self.t = Toplevel()
        self.t.config(background="slate gray")
        self.t.config(cursor="circle")
        self.t.geometry("1180x400")
        self.t.config(relief="sunken")
        self.t.config(bd=15)
        self.t.resizable(1, 1)

    def salir(self):
        self.t.quit()
        self.t.destroy()


    def draw_label(self):
        # los label donde almacenamos los textos
        self.lbl_nombre = Label(
            self.t,
            foreground="white",
            font=(8),
            background="slate gray",
            text="Nombre",
        ).place(x=60, y=110)
        self.lbl_apellido = Label(
            self.t,
            foreground="white",
            font=(8),
            background="slate gray",
            text="Apellido",
        ).place(x=60, y=160)
        self.lbl_celular = Label(
            self.t,
            foreground="white",
            font=(8),
            background="slate gray",
            text="Celular",
        ).place(x=60, y=210)
        self.lbl_mail = Label(
            self.t,
            foreground="white",
            font=(8),
            background="slate gray",
            text="Mail",
        ).place(x=60, y=260)

    def draw_entry(self):
        # caja de texto que permiten manejar las variables
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.celular = StringVar()
        self.mail = StringVar()
        # se cran las cajas de texto para las variables. Menu principal
        self.txt_name = Entry(
            self.t,
            font=("Arial", 12),
            relief="flat",
            background="linen",
            textvariable=self.nombre,
        ).place(x=140, y=110, height=25, width=150)
        self.txt_apellido = Entry(
            self.t,
            font=("Arial", 12),
            relief="flat",
            background="linen",
            textvariable=self.apellido,
        ).place(x=140, y=160, height=25, width=150)
        self.txt_celular = Entry(
            self.t,
            font=("Arial", 12),
            relief="flat",
            background="linen",
            textvariable=self.celular,
        ).place(x=140, y=210, height=25, width=150)
        self.txt_mail = Entry(
            self.t,
            font=("Arial", 12),
            relief="flat",
            background="linen",
            textvariable=self.mail,
        ).place(x=140, y=260, height=25, width=150)

        # los titulos que vemos en patalla
        lbl_n12 = Label(
            self.t,
            font=("Arial", 22, "bold"),
            fg="gold",
            background="slate gray",
            text="Agenda en Python II",
        ).place(x=500, y=20, width=300)
        lbl_n13 = Label(
            self.t,
            font=("Arial", 7, "bold"),
            fg="gold",
            background="slate gray",
            text="Creado por Lourdes Duarte / Carlos Héctor Matons Cesco / Alejandro Silva ",
        ).place(x=800, y=357, width=350)
        lbl_n14 = Label(
            self.t,
            font=("Arial", 18, "bold"),
            fg="gold",
            background="slate gray",
            text="Agregar Contacto: ",
        ).place(x=70, y=65, width=220)

    def draw_buttons(self):
        self.btn_confirm = Button(
            self.t,
            foreground="white",
            text="Guardar",
            borderwidth=2,
            relief="flat",
            cursor="hand1",
            overrelief="raise",
            background="green4",
            command=lambda: self.confirm_process(),
        ).place(x=100, y=300, width=70)
        self.btn_cancel = Button(
            self.t,
            text="Limpiar datos",
            foreground="white",
            borderwidth=2,
            relief="flat",
            cursor="hand1",
            overrelief="raise",
            background="blue",
            command=lambda: self.cancel_process(),
        ).place(x=200, y=300, width=90)
        self.btn_cerrar = Button(
            self.t,
            text="Cerrar Sesion",
            foreground="white",
            borderwidth=5,
            relief="flat",
            cursor="hand1",
            overrelief="raise",
            background="red2",
            width=50,
            command=lambda: self.salir(),
        ).place(x=950, y=25, width=90)
        self.btn_cerrar = Button(
            self.t,
            text="Prender servidor",
            foreground="black",
            borderwidth=5,
            relief="flat",
            cursor="hand1",
            overrelief="raise",
            background="spring green",
            width=50,
            command=self.server,
        ).place(x=150, y=25, width=90)
    

    def load_image(self):
        self.lbl_image = Label(
            self.frame, text="imagen", background="slate gray", foreground="white"
        ).place(x=430, y=25)
        canvas = Canvas(self.frame)
        canvas.place(x=350, y=50, width=200, height=160)

    def draw_list(self):
        # creamos la lista que mostramos en pantall importada de ODBC
        self.list_elemts = ttk.Treeview(
            self.t, columns=(1, 2, 3, 4), show="headings", height="9"
        )  # identifico las columnas

        # --- STYLE ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview.Heading", background="black", relief="flat", foreground="red"
        )
        style.map(
            "Treeview",
            background=[("selected", "deep sky blue")],
            foreground=[("selected", "black")],
        )

        # --- Evento---
        self.list_elemts.bind("<Double 1>", self.get_row)
        # ---- fin ---

        self.list_elemts.heading(1, text="Nombre")
        self.list_elemts.heading(2, text="Apellido")
        self.list_elemts.heading(3, text="Celular")
        self.list_elemts.heading(4, text="Mail")
        self.list_elemts.column(1, anchor=CENTER)
        self.list_elemts.column(2, anchor=CENTER)
        self.list_elemts.column(3, anchor=CENTER)
        self.list_elemts.column(4, anchor=CENTER)

        # -- llenamos la lista--
        records = self.list_elemts.get_children()
        for element in records:
            self.list_elements.delete(element)

        for x in Agenda.select():
            self.list_elemts.insert(
                "",
                0,
                text=x.id,
                values=(
                    x.nombre,
                    x.apellido,
                    x.telefono,
                    x.email,
                ),
            )

        # ----- fin -----

        self.list_elemts.place(x=340, y=100)


    def get_row(self, event):
        id = StringVar()
        na = StringVar()
        ed = StringVar()
        ca = StringVar()
        ma = StringVar()
        # traemos los rados del ROW
        rowName = self.list_elemts.identify_row(event.y)
        item = self.list_elemts.item(self.list_elemts.focus())
        i = item["text"]
        n = item["values"][0]
        e = item["values"][1]
        c = item["values"][2]
        m = item["values"][3]
        id.set(i)
        na.set(n)
        ed.set(e)
        ca.set(c)
        ma.set(m)
        pop = Toplevel(self.t, background="slate gray")
        pop.geometry("350x280")
        # parametrizo el pop up
        lbl_n11 = Label(
            pop,
            font=("Arial", 10, "bold"),
            fg="lemon chiffon",
            bg="slate gray",
            text="Actualizar o Eliminar Contacto",
        ).place(x=70, y=10, width=240)
        lbl_n1 = Label(
            pop,
            text="Nombre",
            font=("Arial", 9, "bold"),
            fg="lemon chiffon",
            bg="slate gray",
        ).place(x=40, y=50)
        lbl_e1 = Label(
            pop,
            text="Apellido",
            font=("Arial", 9, "bold"),
            fg="lemon chiffon",
            bg="slate gray",
        ).place(x=40, y=90)
        lbl_c1 = Label(
            pop,
            text="Celular",
            font=("Arial", 9, "bold"),
            fg="lemon chiffon",
            bg="slate gray",
        ).place(x=40, y=130)
        lbl_m1 = Label(
            pop,
            text="Mail",
            font=("Arial", 9, "bold"),
            fg="lemon chiffon",
            bg="slate gray",
        ).place(x=40, y=170)
        lbl_n = Entry(pop, textvariable=na).place(x=130, y=50, width=200)
        lbl_e = Entry(pop, textvariable=ed).place(x=130, y=90, width=200)
        lbl_c = Entry(pop, textvariable=ca).place(x=130, y=130, width=200)
        lbl_m = Entry(pop, textvariable=ma).place(x=130, y=170, width=200)
        btn_change = Button(
            pop,
            text="Actualizar",
            relief="flat",
            background="blue",
            foreground="white",
            command=lambda: [
                self.editar(id.get(),na.get(), ed.get(), ca.get(), ma.get()),
                pop.destroy(),
            ],
        ).place(x=70, y=220, width=70)
        btn_delete = Button(
            pop,
            text="Eliminar",
            relief="flat",
            background="red",
            foreground="white",
            command=lambda: [
                self.eliminar(id.get()),
                pop.destroy(),
            ]
        ).place(x=200, y=220, width=70)

    def editar(self, id, na, ed, ca, ma):
        arr = [id, na, ed, ca, ma]
        d = Data()
        # d.UpdateItem(arr, n)
        try:
            d = Data()
            d.update_item(arr) 
            messagebox.showinfo(
                title="Actualizacion",
                message="Se han actualizado los datos correctamente",
            )
            self.clear_list()
            self.draw_list()
            self.clear_entry()
            print(id)    
        except:
            messagebox.showinfo(
                title="Actualizacion", message="Error al actualizar datos"
            )

    def eliminar(self, n):
        d = Data()
        d.delete(n)
        messagebox.showinfo(
            title="Actualizacion", message="Se han actualizado los datos correctamente"
        )
        self.clear_list()
        self.draw_list()
        self.clear_entry()
    
    def server(self):
        d = Data()
        if d.server_on() is True:
            messagebox.showinfo(
                title="Mensaje del servidor", message="Conexion con servidor exitosa!"
            )
        else:
             messagebox.showinfo(
                title="Mensaje del servidor", message="El servidor ya se encuentra encendido!"
            )

    def clear_list(self):
        self.list_elemts.delete(*self.list_elemts.get_children())

    def cancel_process(self):
        self.clear_entry()

    def clear_entry(self):
        self.nombre.set("")
        self.apellido.set("")
        self.celular.set("")
        self.mail.set("")


    def confirm_process(self):
        # proceso de confirmacion
        if (
            self.nombre.get() != ""
            and self.apellido.get() != ""
            and self.celular.get() != ""
            and self.mail.get() != ""
        ):
            d = Data()
            arr = [
                self.nombre.get(),
                self.apellido.get(),
                self.celular.get(),
                self.mail.get(),
            ]
            try: 
                d.insert_items(arr) 
                messagebox.showinfo(title="Alerta", message="Se inserto correctamente!")
                self.clear_list()
                self.draw_list()
                self.clear_entry()
            except:
                messagebox.showinfo(
                    title="Error", message="Error al cargar el registro!"
                )
        else:
            messagebox.showinfo(
                title="Error", message="Los campos no deben estar vacios!"
            )

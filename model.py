from re import sub
from tkinter.constants import TRUE
from peewee import *
import subprocess
from subprocess import *
import sys
from server.client import cliente
from pathlib import Path
import os
import smtplib
import time
import datetime



#mensaje para el usuario - Info Eventos bienvenida
print("------------------------------------------------------------------------")
print("               Bienvenidos al sistema de Agenda en Python               ")
print("------------------------------------------------------------------------")
print("Creado por Lourdes Duarte / Carlos Héctor Matons Cesco / Alejandro Silva")
print("------------------------------------------------------------------------")
print("---------------Seguimiento de Eventos Generados----------(Version 5.3.1)")


try:
      
    db = SqliteDatabase("nivel_avanzado.db")

    class BaseModel(Model):
        class Meta:
            database = db

    class Login(BaseModel):
    
        username = CharField()
        password = CharField()
        email = CharField()



    class Agenda(BaseModel):
        nombre = CharField()
        apellido = CharField()
        telefono = CharField()
        email = CharField()

    db.connect()
    db.create_tables([Login])
    db.create_tables([Agenda])

except:
    print("la base de datos ya ha sido creada")

ahora = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()) ### variable que determina la fecha DD/MM/AA %d-%m-%Y %H:%M:%S
 
class Data:

    def __init__(self):
        pass
    
    
    """esta funcion decoradora nos brinda informacion de como viene los procesos, cuando inician y cuando terminan"""
    def funcion_decoradora(f):
        #acciones que decoran/agregan
        def inner(*args, **kwargs):
            print(f">>>>Inicia Ejecucion" +"  "+ ahora)
            print ("Se ejecuto %s" % f.__name__)
            resultado = f(*args, **kwargs)
            print(">>>>Finalizo la Ejecucion >>>>>")
            a = (f">>>>Inicia Ejecucion >>>>>" +"  "+ ahora)
            b = ("Se ejecuto %s" % f.__name__)
            c = (">>>>Finalizo la Ejecucion >>>>>")
            nombre = open("log_app.log", "a")
            nombre.write(
                f"Inicia el Log \n" + 
                a +"\n"+  
                b +"\n" +  
                c +"\n")
            nombre.close()
            return resultado
        return inner 

    @funcion_decoradora 
    def verification_login(self, element):
        """El usuario carga sus credenciales y se validan contra la base datos. funciona con respuesta TRUE/FALSE
        si es True le permite acceder a la View de la agenda y interactuar con ella"""
        if (
            element[0] != " " and 
            element[1] != " "):
            if Login.select().where(
                Login.username == element[0], 
                Login.password == element[1]):
                print("usuario encontrado")


                #se declara la variable del msg a enviar via mail
                m = (f"""Estimados, se ha ejecutado la aplicacion  

                Usuario : {element[0]}
                Password : {element[1]}
                horario : {ahora}



                Atte 
                Dpto de Sistemas""")
                message = str(m)

                ######determino en esta condicion que MAIL A usar y parametros ####
                args = sys.argv[1:]

                ######determino destinatarios de mail con TO ####
                destino = [
                    'alejandrofabian2013@gmail.com',
                    'lourdes123duarte@gmail.com',
                    'cmatons@gmail.com',
                    'alejandrofabian20@hotmail.com'
                    ]

                ##############################Declaracion de informacion asunto y cuerpo mail##################3
                SUBJECT = "Se accedio a la APP Diplomatura"  #### declaro el nombre del asunto
                TEXT = message  ##### declaro el cuerpo del mail

                #### sta variable toma a TExt Y SUBJET y los parametriza para ser enviados.
                text = "Subject: {}\n\n{}".format(SUBJECT, TEXT)

                # Nos conectamos al servidor SMTP

                smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo()
                smtpserver.login('mail.diplomatura@gmail.com','piucomltoimebgdw')

                # Enviamos el mensaje
                smtpserver.sendmail('mail.diplomatura@gmail.com', destino, text)
                # Cerramos la conexion
                smtpserver.close()
                print(f"mail  enviados con exito")  

                return True 
            else:
                print("usuario no encontrado")
                return False
        else:
            print("campos vacios")

    @funcion_decoradora 
    def insert_items(self, element):
        """NUESTROS ELementos contiene nombre,apellido,celular,mail, en pocicion 0, 1, 2, 3.
        Los mismo se insertan en la tabla agenda."""
      
        try:
            agenda = Agenda()
            agenda.nombre = element[0]
            agenda.apellido = element[1]
            agenda.telefono = element [2]
            agenda.email = element[3]
            agenda.save()
            if self.on[0] == 1:            
                c = cliente()
                c.message(0x00003EF8)
            else:
                pass
            print("guardado")
            return True
        except:
            print("no guardado")
            return False

    @funcion_decoradora 
    def insert_user(self, element):
        """Cuando se registra un usuario nuevo, los datos se graban en la tabla login, la misma la componene 3 campos
        usuario/password/email."""
        try:
            login = Login()
            login.username = element[0]
            login.password = element[1]
            login.email = element[2]
            login.save()
            print("guardado con exito")
            return True
        except:
            print("No se grabo el registro")
            return False

    @funcion_decoradora 
    def delete(self, ref):
        """ Deleteamos el registro que indica REF, el mismo es seleccionado por el usuario. Rastrea el dato
        y lo elimina de la tabla"""
        try:
            borrar = Agenda.get(Agenda.id == ref[0])
            borrar.delete_instance()
            if self.on[0] == 1:
                c = cliente()
                c.message(0x00003EF3)
            else:
                pass
            print("registro eliminado")
        except:
            print("error")

    @funcion_decoradora 
    def update_item(self, element):
        # elemento que queremos cambiar incluido el id, el cual solo es enviado. El mismo no puede ser editado por el usuario ya que se encuentra 
        #oculto
        try:
            actualizar = Agenda.update(
                nombre=element[1], 
                apellido=element[2],
                telefono=element[3],
                email=element[4]).where(
            Agenda.id == element[0]
            )
            actualizar.execute()
            if self.on[0] == 1:
                c = cliente()
                c.message(0x00003EF5)
            else:
                pass
            print("actualizado")
            return True
        except:
            print("no actualizado")
            return False

    on = [0]
    
    @funcion_decoradora 
    def server_on(self):   
        raiz = Path(__file__).resolve().parent
        ruta_server = os.path.join(
            raiz, 
            'server\server.py')
        the_path =  ruta_server
        print(the_path)
        #se inicia subproceso en una nueva consola
        if self.on[0] == 0:
            if subprocess.Popen([
                sys.executable, 
                the_path], 
                creationflags = subprocess.CREATE_NEW_CONSOLE):
                print("conexion con servidor establecida con exito")
                self.on[0] = 1
                print ("estado del server: {}".format(self.on[0]))
                return True
        else:
            print("el servidor ya se encuentra encendido")
            return False
            
 
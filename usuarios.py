class Usuario:
    # crear una funcion para el CONSTRUCTROR
    def __init__(self, id_usuario, documento, nombre, apellido, correo, telefono, direccion):
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        
lista_usuarios = []
        
def saludar(self):
            print(f"Hola, soy {self.nombre} {self.apellido}")
            
            #Metodos base CRUD
            #Create
def crear_usuario(self):
        lista_usuarios.append(self)
        print(f"👌 Exito: El usuario {self.nombre} ha sido creado exitosamente.")
        
        #READ
        def ver_usuario(self):
            print(f"ID: {self.id_usuario} Nombre: {self.nombre} {self.apellido}")
         
        
        #UPDATE
        def actualizar_usuario(self, nuevo_nombre=None, nuevo_apellido=None):
            self.nombre = nuevo_nombre
            self.apellido = nuevo_apellido
           
            print(f"👌 Exito: El usuario {self.nombre} ha sido actualizado exitosamente.")
            
        #DELETE
        def eliminar_usuario(self):
            if self in lista_usuarios:
                lista_usuarios.remove(self)
                print(f"👌 Exito: El usuario {self.nombre} ha sido eliminado exitosamente.")
            else:
                print(f"❌ Error: El usuario {self.nombre} no se encuentra en la lista.")

 #creando una instancia de la clase Usuario
usuario1 = Usuario(1, "1055312061", "Juan", "Perez", "juan.perez@example.com", "3001234567", "Calle 123 #45-67")

usuario2 = Usuario(2, "1055312062", "James", "Rodriguez", "maria.gomez@example.com", "3001234568", "Carrera 456 #78-90")

print(usuario1.nombre)  # Imprime: Juan
print(usuario2.nombre)  # Imprime: James

usuario1.saludar()  # Imprime: Hola, soy Juan Perez
usuario2.saludar()  # Imprime: Hola, soy James Rodriguez

# llame a los metodos de la clase Usuario
usuario1.saludar()
usuario2.saludar()
#Metodos crear usuario
print(f"Lista de usuarios: {lista_usuarios}")  # lista vacia
usuario1.crear_usuario()
usuario2.crear_usuario()

print(f"Lista de usuarios: {lista_usuarios[0].nombre}")
print(f"Lista de usuarios: {lista_usuarios[1].nombre}")
usuario1. ver_usuario()
usuario2. ver_usuario()


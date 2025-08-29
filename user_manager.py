import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)

if __name__ == "__main__":
    user_manager = UserManager()
#RF1: Agregar usuario:
    #for i in range(500): 
        #user_manager.add_user(i,f"Soy el número: {i}")
    #print("end")

#RF2: Buscar usuario:   
    #for i in range(500): 
        #user_manager.find_user(i)
    #print("end")

#RF3: Eliminar usuario
    #for i in range(500): 
        #user_manager.delete_user(i)
    #print("end")
     
#RF4: Obtener todos los usuarios.
    #all=user_manager.get_all_names()
    #print(all)

#RF5: Promediar usuarios.
    #all=user_manager.average_user_id()
    #print(all)

#RNF1: Manejar 1000 usuarios.
    #for i in range(1000): 
        #user_manager.add_user(i,f"Soy el número: {i}")
    #assert len(user_manager.users) == 1000 #Verifica el código.
    #print("end")

#RNF2: Tiempo de busqueda #time.time para calcular el tiempo.
    #start = time.time()
    #user = user_manager.find_user(1000)
    #timekeeper = time.time() - start
    #if timekeeper < 0.01:
        #print(f"Tiempo de busqueda por ID menor a 0.01s")
    #else:
        #print(f"Tiempo de busqueda por ID mayor a 0.01s")

#RNF3: Eliminar IDs duplicados.
    '''user_manager.add_user(50, "Duplicado")
    nBefore = len(user_manager.users)
    user_manager.delete_user(50)
    nAfter = len(user_manager.users)
    if nAfter == nBefore - 1:
        print(f"Se borro el ID duplicado")
    else:
        print("error")'''

#Rendimiento: Agrega 1000 usuarios y mide el tiempo de búsqueda del usuario 500.
    '''for i in range(1000): 
        user_manager.add_user(i, f"Soy el número: {i}")
        start = time.time()
        user = user_manager.find_user(i)  
        timekeeper = time.time() - start
        if user and user["id"] == 499:  
            print(f"Hola, soy el número: {i+1}, tardaste {timekeeper:.6f}s en encontrarme")
            print("end")'''
#Robustez: Prueba eliminar un usuario que no existe.
    '''for i in range(500): 
        user_manager.add_user(i, f"Soy el número: {i}")
        print("end")
    user_manager.delete_user(501)
    print("end")'''
#Robustez: Calcula average_user_id en lista vacía.
    all=user_manager.average_user_id()
    print(all)

    print("end")
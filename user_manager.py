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
    #time.time para calcular el tiempo.

#RF5: Promediar usuarios.
    #all=user_manager.average_user_id()
    #print(all)

#RNF1: Manejar 1000 usuarios.
    for i in range(1000): 
        user_manager.add_user(i,f"Soy el número: {i}")
    assert len(user_manager.users) == 1000 #Verifica el código.
    print("end")

    print("end")
import requests

URL = "http://127.0.0.1:5000"




def registrar():
    usuario = input("Usuario: ")
    contrasena = input("Contrasena: ")
    r = requests.post(
        f"{URL}/registro",
        json={"usuario": usuario, "contraseña": contrasena}
    )
    print(r.status_code, r.text)




def iniciar_sesion():
    usuario = input("Usuario: ")
    contrasena = input("Contrasena: ")
    r = requests.post(
        f"{URL}/login",
        json={"usuario": usuario, "contraseña": contrasena}
    )
    print(r.status_code, r.text)
    if r.status_code == 200:
        ver_tareas()





def ver_tareas():
    r = requests.get(f"{URL}/tareas")
    print(r.status_code, r.text)





def menu():
    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesion")
        print("3. Ver tareas")
        print("4. Salir")
        opcion = input("Opcion: ")
        try:
            if opcion == "1":
                registrar()
            elif opcion == "2":
                iniciar_sesion()
            elif opcion == "3":
                ver_tareas()
            elif opcion == "4":
                break
        except requests.RequestException as e:
            print("Error de conexion:", e)





if __name__ == "__main__":
    menu()
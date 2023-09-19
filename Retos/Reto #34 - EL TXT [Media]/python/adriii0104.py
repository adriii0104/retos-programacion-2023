import os
class Fichero():
    def __init__(self):
        self.fichero = "texto.txt"
        self.escribir_data()

    def check_exist(self):
        return os.path.exists(self.fichero)

    def escribir_data_exist(self, response, mode):
        with open(self.fichero, mode) as file:
            file.write(response + "\n")

    def escribir_data(self):
        while True:
            try:
                if not self.check_exist():
                    response = input(
                        "Escribe un texto que desees guardar en el fichero, para detener el programa escriba 'break':\n")
                    if response == "break":
                        break
                    mode = "w"
                else:
                    response = input(
                        "Si desea escribir en el fichero, simplemente escriba; de lo contrario, escriba 'break'.\n")
                    if response == "break":
                        break
                    elif response == "new":
                        mode = "w"
                    else:
                        mode = "a"
                self.escribir_data_exist(response, mode)
            except Exception as e:
                print(f"Ha ocurrido un error desconocido {e}")

if __name__ == "__main__":
    Fichero()
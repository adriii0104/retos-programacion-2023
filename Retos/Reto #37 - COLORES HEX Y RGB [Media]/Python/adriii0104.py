# Reto #37: Colores HEX y RGB
# Dificultad: Media | Publicación: 18/09/23 | Corrección: 25/09/23

# Enunciado

# ```
# /*
# * Crea las funciones capaces de transformar colores HEX
# * a RGB y viceversa.
# * Ejemplos:
# * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
# * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
# */
# ```
# Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.
#
# Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.
#
# > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
class Converter():
    def __init__(self):
        response = int(
            input("Para convertir de RGB a HEX introduce 1, si es viceversa pulsa 2: "))

        if response == 1:
            self.rgb_to_hex()
        elif response == 2:
            self.hex_to_rgb()
        else:
            print("Opción no válida. Debes introducir 1 o 2.")

    def rgb_to_hex(self):
        r = int(input("Introduce el valor de R (0-255): "))
        g = int(input("Introduce el valor de G (0-255): "))
        b = int(input("Introduce el valor de B (0-255): "))

        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            hex_value = "#{:02X}{:02X}{:02X}".format(r, g, b)
            print(f"El valor HEX correspondiente es: {hex_value}")
        else:
            print("Los valores RGB deben estar en el rango de 0 a 255.")

    def hex_to_rgb(self):
        hex_value = input("Introduce el valor HEX (por ejemplo, #FF0000): ")

        if len(hex_value) == 7 and hex_value[0] == "#" and all(c in "0123456789ABCDEF" for c in hex_value[1:]):
            r = int(hex_value[1:3], 16)
            g = int(hex_value[3:5], 16)
            b = int(hex_value[5:7], 16)
            print(f"Los valores RGB correspondientes son: R={r}, G={g}, B={b}")
        else:
            print("El valor HEX debe tener el formato correcto, por ejemplo, #FF0000.")


if __name__ == "__main__":
    Converter()

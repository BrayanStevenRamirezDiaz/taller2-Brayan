import time
import os

def clear_screen():
    # Esto limpia la pantalla, funciona en Windows y Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def print_smiley(position):
    # Imprime la carita feliz en una posición específica
    spaces = ' ' * position
    print(f"{spaces}:-)\n")

def main():
    # Tamaño de la pantalla
    width = 40

    try:
        while True:
            for position in range(width):
                clear_screen()
                print_smiley(position)
                time.sleep(0.1)  # Ajusta el tiempo de espera para controlar la velocidad

            for position in range(width - 1, -1, -1):
                clear_screen()
                print_smiley(position)
                time.sleep(0.1)  # Ajusta el tiempo de espera para controlar la velocidad

    except KeyboardInterrupt:
        # Permite detener el programa con Ctrl+C
        clear_screen()
        print("¡Hasta luego!")

if __name__ == "__main__":
    main()

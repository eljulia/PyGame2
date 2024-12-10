import pygame
import sys

# Importar la lógica del juego y controles
import Nuevo_Juego
import Controles  # Importar el módulo de controles

# Inicialización de Pygame
pygame.init()

# Pantalla - Ventana
W, H = 900, 600
Pantalla = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dutty - Menú Principal")

# Colores y fuente
BLANCO = (248, 244, 243)
AMARILLO = (255, 223, 0)
CYAN = (0, 255, 255)
TRANSLUCIDO_NEGRO = (0, 0, 0, 128)  # Fondo translúcido
FUENTE_TITULO = pygame.font.Font(None, 70)
FUENTE_OPCIONES = pygame.font.Font(None, 40)

# Fondo del menú
fondo = pygame.image.load("Imagenes/Pared.png").convert()

# Audio
audio_fondo = pygame.mixer.Sound("Audios/Nave1.wav")

# Configuración del menú
opciones = ["Nuevo Juego", "Controles", "Salir"]  # Opciones del menú principal
opcion_seleccionada = 0

# Reproducir audio de fondo en bucle
audio_fondo.play(-1)  # Reproducción continua


def dibujar_menu():
    # Dibujar el fondo
    Pantalla.blit(fondo, (0, 0))

    # Dibujar el título
    titulo = FUENTE_TITULO.render("MENÚ PRINCIPAL", True, AMARILLO)
    Pantalla.blit(titulo, ((W - titulo.get_width()) // 2, 150))

    # Dibujar las opciones del menú
    y_inicial = 220
    for i, opcion in enumerate(opciones):
        color = CYAN if i == opcion_seleccionada else BLANCO
        texto = FUENTE_OPCIONES.render(opcion, True, color)
        x = (W - texto.get_width()) // 2
        y = y_inicial + i * 50
        Pantalla.blit(texto, (x, y))


# Bucle principal
def iniciar_menu():
    global opcion_seleccionada

    reloj = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Navegación del menú
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif event.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if opciones[opcion_seleccionada] == "Nuevo Juego":
                        audio_fondo.stop()
                        Nuevo_Juego.iniciar()  # Cambiar al nuevo juego
                    elif opciones[opcion_seleccionada] == "Controles":
                        Controles.ejecutar()  # Abrir pantalla de controles
                    elif opciones[opcion_seleccionada] == "Salir":
                        pygame.quit()
                        sys.exit()

        # Dibujar menú
        Pantalla.fill((0, 0, 0))
        dibujar_menu()
        pygame.display.flip()
        reloj.tick(60)


# Iniciar el menú
if __name__ == "__main__":
    iniciar_menu()

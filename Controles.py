import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Pantalla - Ventana
W, H = 900, 600
Pantalla = pygame.display.set_mode((W, H))
pygame.display.set_caption("Controles de Juego")

# Colores
BLANCO = (248, 244, 243)
AMARILLO = (255, 223, 0)
CYAN = (0, 255, 255)
NEGRO = (0, 0, 0)

# Fuentes
FUENTE_TITULO = pygame.font.Font(None, 70)
FUENTE_TEXTO = pygame.font.Font(None, 40)

# Fondo del menú
fondo = pygame.image.load("Imagenes/Pared.png").convert()

# Audio
audio_fondo = pygame.mixer.Sound("Audios/Nave1.wav")
audio_fondo.play(-1)  # Reproducción continua

# Opciones del menú
opciones = ["Regresar"]
opcion_seleccionada = 0


def dibujar_controles():
    # Dibujar el fondo
    Pantalla.blit(fondo, (0, 0))

    # Título
    titulo = FUENTE_TITULO.render("Controles de Juego", True, AMARILLO)
    Pantalla.blit(titulo, ((W - titulo.get_width()) // 2, 150))

    # Controles
    controles = [
        ("Desplázate:", "<   -   >"),
        ("Dispara:", "Espacio"),
    ]

    y_inicial = 250  # Posición inicial para dibujar el texto
    for texto, detalle in controles:
        texto_render = FUENTE_TEXTO.render(texto, True, BLANCO)
        detalle_render = FUENTE_TEXTO.render(detalle, True, CYAN)
        Pantalla.blit(texto_render, (W // 4, y_inicial))
        Pantalla.blit(detalle_render, (W // 2, y_inicial))
        y_inicial += 50  # Espaciado entre líneas

    # Dibujar opción "Regresar"
    regresar_y = y_inicial + 20  # Espacio reducido
    regresar_texto = FUENTE_TEXTO.render("Regresar", True, BLANCO if opcion_seleccionada == 0 else CYAN)
    regresar_rect = regresar_texto.get_rect(center=(W // 2, regresar_y))
    Pantalla.blit(regresar_texto, regresar_rect)

    return regresar_rect


def ejecutar():
    global opcion_seleccionada

    reloj = pygame.time.Clock()
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Navegación del menú con teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if opciones[opcion_seleccionada] == "Regresar":
                        return  # Regresa al menú principal

            # Navegación del menú con mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Click izquierdo
                    mouse_click = True

        # Dibujar la pantalla
        Pantalla.fill(NEGRO)
        regresar_rect = dibujar_controles()

        # Comprobar si el mouse está sobre la opción "Regresar"
        if regresar_rect.collidepoint(mouse_pos):
            opcion_seleccionada = 0
            if mouse_click:
                return  # Regresa al menú principal

        pygame.display.flip()
        reloj.tick(60)

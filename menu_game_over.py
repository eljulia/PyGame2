import pygame
import sys

# Función para el menú de Game Over
def menu_game_over(pantalla, puntaje):
    # Inicializar Pygame
    pygame.init()
    pygame.font.init()

    # Cargar el fondo
    fondo = pygame.image.load("Imagenes/Pared.png").convert()

    # Colores
    COLOR_TITULO = (255, 215, 0)  # Oro
    COLOR_OPCION = (0, 255, 255)  # Cian
    COLOR_OPCION_SELECCIONADA_BASE = (255, 215, 0)  # Oro (para animación)
    COLOR_RESPLANDOR = (255, 255, 100)  # Color para el resplandor

    # Fuentes
    fuente_titulo = pygame.font.Font(None, 80)
    fuente_opciones = pygame.font.Font(None, 50)

    # Opciones del menú
    opciones = ["Reiniciar", "Salir"]
    seleccion_actual = 0  # Índice de la opción seleccionada

    # Dimensiones de la pantalla
    W, H = pantalla.get_size()

    # Reloj para controlar FPS
    reloj = pygame.time.Clock()

    # Variables para animación de resplandor
    resplandor_alpha = 0
    alpha_direccion = 1  # 1 para incrementar, -1 para decrementar

    # Bucle del menú
    while True:
        pantalla.blit(fondo, (0, 0))  # Dibujar fondo

        # Título del menú
        texto_titulo = fuente_titulo.render("GAME OVER", True, COLOR_TITULO)
        pantalla.blit(texto_titulo, ((W - texto_titulo.get_width()) // 2, 180))

        # Mostrar puntaje
        texto_puntaje = fuente_opciones.render(f"Puntaje: {puntaje}", True, COLOR_OPCION)
        pantalla.blit(texto_puntaje, ((W - texto_puntaje.get_width()) // 2, 250))

        # Dibujar opciones del menú
        for i, opcion in enumerate(opciones):
            if i == seleccion_actual:
                # Efecto de resplandor
                texto_opcion = fuente_opciones.render(opcion, True, COLOR_RESPLANDOR)
                texto_opcion.set_alpha(resplandor_alpha)  # Ajustar opacidad del resplandor
                resplandor_rect = texto_opcion.get_rect(center=(W // 2, 300 + i * 60))
                pantalla.blit(texto_opcion, resplandor_rect)

                # Texto base seleccionado
                texto_opcion = fuente_opciones.render(opcion, True, COLOR_OPCION_SELECCIONADA_BASE)
            else:
                # Opciones no seleccionadas
                texto_opcion = fuente_opciones.render(opcion, True, COLOR_OPCION)

            pantalla.blit(texto_opcion, ((W - texto_opcion.get_width()) // 2, 300 + i * 60))

        # Actualizar animación de resplandor
        resplandor_alpha += alpha_direccion * 5
        if resplandor_alpha >= 255 or resplandor_alpha <= 50:  # Limitar el rango
            alpha_direccion *= -1

        # Actualizar la pantalla
        pygame.display.flip()

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    seleccion_actual = (seleccion_actual - 1) % len(opciones)  # Navegar hacia arriba
                if event.key == pygame.K_DOWN:
                    seleccion_actual = (seleccion_actual + 1) % len(opciones)  # Navegar hacia abajo
                if event.key == pygame.K_RETURN:  # Enter para seleccionar
                    if seleccion_actual == 0:  # Reiniciar
                        return True
                    if seleccion_actual == 1:  # Salir
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.MOUSEMOTION:  # Sensibilidad con el mouse
                mouse_x, mouse_y = event.pos
                for i, opcion in enumerate(opciones):
                    texto_opcion = fuente_opciones.render(opcion, True, COLOR_OPCION)
                    opcion_rect = texto_opcion.get_rect(center=(W // 2, 300 + i * 60))
                    if opcion_rect.collidepoint(mouse_x, mouse_y):
                        seleccion_actual = i
            if event.type == pygame.MOUSEBUTTONDOWN:  # Seleccionar con clic del mouse
                if event.button == 1:  # Botón izquierdo
                    if seleccion_actual == 0:  # Reiniciar
                        return True
                    if seleccion_actual == 1:  # Salir
                        pygame.quit()
                        sys.exit()

        # Controlar la velocidad del bucle
        reloj.tick(60)

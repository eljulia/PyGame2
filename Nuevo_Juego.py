import pygame
import sys
import random
from menu_game_over import menu_game_over

# Función para generar partículas de explosión
def generar_explosion(x, y, num_particulas=30):
    explosion = []
    for _ in range(num_particulas):
        particula = {
            "x": x,
            "y": y,
            "vx": random.uniform(-3, 3),
            "vy": random.uniform(-3, 3),
            "vida": random.randint(20, 50),
            "color": random.choice([(255, 69, 0), (255, 215, 0), (255, 0, 0)])
        }
        explosion.append(particula)
    return explosion

# Función para generar obstáculos como círculos fosforescentes
def generar_obstaculo():
    radio = random.randint(20, 40)
    x = random.randint(radio, 900 - radio)
    y = random.randint(-300, -50)
    velocidad = random.randint(2, 5)
    color = random.choice([(57, 255, 20),(6, 74, 137),(211, 204, 217), (0, 255, 255),(234, 183, 0), (255, 105, 180)])
    return {"x": x, "y": y, "radio": radio, "velocidad": velocidad, "color": color}

# Función principal del juego
def iniciar():
    pygame.init()
    W, H = 900, 600
    Pantalla = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Nuevo Juego")

    fondo = pygame.image.load("Imagenes/Fondo1.jpg").convert()
    nave = pygame.image.load("Imagenes/Nave5.png").convert_alpha()
    nave_rect = nave.get_rect(midbottom=(W // 2, H - 50))
    vida_nave = 100

    proyectil_img = pygame.Surface((10, 20), pygame.SRCALPHA)
    pygame.draw.rect(proyectil_img, (255, 255, 0), (0, 0, 10, 20))

    proyectiles = []
    particulas = []
    enemigos = [generar_obstaculo() for _ in range(5)]

    puntaje = 0
    fuente_puntaje = pygame.font.Font(None, 30)
    velocidad_nave = 5
    velocidad_proyectil = 7

    pygame.mixer.init()
    pygame.mixer.music.load("Audios/FondoSonido.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    sonido_disparo = pygame.mixer.Sound("Audios/Explo.wav")
    sonido_disparo.set_volume(0.7)

    reloj = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                nuevo_proyectil = proyectil_img.get_rect(midbottom=nave_rect.midtop)
                proyectiles.append(nuevo_proyectil)
                sonido_disparo.play()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            nave_rect.x -= velocidad_nave
        if teclas[pygame.K_RIGHT]:
            nave_rect.x += velocidad_nave

        if nave_rect.left < 0:
            nave_rect.left = 0
        if nave_rect.right > W:
            nave_rect.right = W

        for proyectil in proyectiles[:]:
            proyectil.y -= velocidad_proyectil
            if proyectil.bottom < 0:
                proyectiles.remove(proyectil)

        for particula in particulas[:]:
            particula["x"] += particula["vx"]
            particula["y"] += particula["vy"]
            particula["vida"] -= 1
            if particula["vida"] <= 0:
                particulas.remove(particula)

        for enemigo in enemigos[:]:
            enemigo["y"] += enemigo["velocidad"]
            if enemigo["y"] - enemigo["radio"] > H:
                enemigos.remove(enemigo)
                enemigos.append(generar_obstaculo())

            distancia_nave = ((nave_rect.centerx - enemigo["x"]) ** 2 + (nave_rect.centery - enemigo["y"]) ** 2) ** 0.5
            if distancia_nave <= enemigo["radio"]:
                vida_nave -= 10
                particulas.extend(generar_explosion(nave_rect.centerx, nave_rect.centery, 50))
                enemigos.remove(enemigo)
                enemigos.append(generar_obstaculo())
                if vida_nave <= 0:
                    pygame.mixer.music.stop()
                    if menu_game_over(Pantalla, puntaje):
                        return  # Volver a `iniciar` tras el retorno
                    else:
                        pygame.quit()
                        sys.exit()

        for proyectil in proyectiles[:]:
            for enemigo in enemigos[:]:
                distancia = ((proyectil.centerx - enemigo["x"]) ** 2 + (proyectil.centery - enemigo["y"]) ** 2) ** 0.5
                if distancia <= enemigo["radio"]:
                    proyectiles.remove(proyectil)
                    particulas.extend(generar_explosion(enemigo["x"], enemigo["y"]))
                    enemigos.remove(enemigo)
                    enemigos.append(generar_obstaculo())
                    puntaje += 10
                    break

        Pantalla.blit(fondo, (0, 0))
        Pantalla.blit(nave, nave_rect)

        for proyectil in proyectiles:
            Pantalla.blit(proyectil_img, proyectil)

        for particula in particulas:
            pygame.draw.circle(Pantalla, particula["color"], (int(particula["x"]), int(particula["y"])), 3)

        for enemigo in enemigos:
            pygame.draw.circle(Pantalla, enemigo["color"], (int(enemigo["x"]), int(enemigo["y"])), enemigo["radio"])

        texto_puntaje = fuente_puntaje.render(f"Puntaje: {puntaje}", True, (0, 255, 255))
        Pantalla.blit(texto_puntaje, (W - 150, 10))

        barra_ancho = 100
        barra_alto = 10
        barra_roja = max(0, int((vida_nave / 100) * barra_ancho))
        pygame.draw.rect(Pantalla, (255, 255, 255), (20, 20, barra_ancho, barra_alto))
        pygame.draw.rect(Pantalla, (255, 0, 0), (20, 20, barra_roja, barra_alto))

        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    while True:
        iniciar()

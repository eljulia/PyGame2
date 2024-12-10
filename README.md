# Dutty

**Dutty** es un videojuego desarrollado en Python utilizando la librería Pygame. Este proyecto incluye un menú principal interactivo, una sección de controles y un emocionante juego donde el jugador controla una nave espacial para esquivar obstáculos y eliminar enemigos.

## Características principales

- **Menú principal**: Permite navegar entre las opciones de "Nuevo Juego", "Controles" y "Salir".
- **Juego interactivo**: Controla una nave espacial, dispara proyectiles, evita obstáculos y gana puntos eliminando enemigos.
- **Efectos visuales y sonoros**: Incluye partículas de explosión, obstáculos fosforescentes y música de fondo.
- **Pantalla de controles**: Instrucciones detalladas sobre cómo jugar.
- **Pantalla de Game Over**: Permite reiniciar el juego o salir.

## Archivos principales

1. **`Menu.py`**
   - Implementa el menú principal del juego.
   - Navegación entre las opciones del menú.
   - Integración con los módulos `Nuevo_Juego` y `Controles`.

2. **`Nuevo_Juego.py`**
   - Lógica principal del juego.
   - Manejo de la nave espacial, enemigos, proyectiles y partículas de explosión.
   - Cálculo del puntaje y barra de vida.
   - Finalización del juego y acceso al menú de Game Over.

3. **`Controles.py`**
   - Muestra una pantalla con las instrucciones para jugar.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/dutty.git
   cd dutty
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install pygame
   ```

3. Asegúrate de tener las siguientes carpetas y archivos en el directorio del proyecto:
   - Carpeta `Imagenes`: Contiene las imágenes necesarias para el juego.
     - `Pared.png`: Fondo del menú principal.
     - `Fondo1.jpg`: Fondo del juego.
     - `Nave5.png`: Sprite de la nave espacial.
   - Carpeta `Audios`: Contiene los sonidos y música de fondo.
     - `Nave1.wav`: Música del menú principal.
     - `FondoSonido.wav`: Música del juego.
     - `Explo.wav`: Sonido de disparos.

## Cómo jugar

1. Ejecuta el archivo principal:
   ```bash
   python Menu.py
   ```

2. Navega por el menú principal usando las teclas:
   - **Flecha arriba/abajo**: Mover entre opciones del menú.
   - **Enter**: Seleccionar una opción.

3. Durante el juego:
   - **Flecha izquierda/derecha**: Mover la nave.
   - **Espacio**: Disparar proyectiles.

4. Evita los obstáculos, elimina enemigos y acumula puntos.

## Créditos

Proyecto desarrollado por Julian Arcos

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto, no dudes en abrir un *issue* o enviar un *pull request*.



import pygame
import cv2
import numpy as np

class Ship:
    def __init__(self, x_max: int, y_max: int, mode : str, size=120, smooth_factor=0.2):
        """
        Representa un barco en el tablero con detección de movimiento facial.
        """
        self.last_frame =  None  # Inicializar el frame
        self.lives = 3
        self.mode = mode
        if mode == "video":
            self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            self.cap = cv2.VideoCapture(0)

        self.x_max = x_max
        self.y_max = y_max
        self.size = size
        self.smooth_factor = smooth_factor  # Factor para suavizar el movimiento

        # Posición inicial en el centro
        self.rect = pygame.Rect(x_max // 2, y_max - size * 2, size, size)

        # Cargar imagen y escalarla
        try:
            self.image = pygame.image.load("./assets/Ship.png")
            self.image = pygame.transform.scale(self.image, (size, size))
        except pygame.error:
            print("🚨 Error: No se pudo cargar la imagen. Verifica la ruta.")

        # Última posición de la cabeza detectada (para suavizado)
        self.target_x = self.rect.x

    def ship_face_movement(self):
        """
        Captura la cámara y mueve la nave suavemente según la detección facial.
        """
        ret, frame = self.cap.read()
        if not ret:
            return

        # Espejar la imagen (flip horizontal para que coincida con el movimiento)
        frame = cv2.flip(frame, 1)

        # Convertir a escala de grises y detectar rostros
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            x, y, w, h = faces[0]  # Tomar el primer rostro detectado

            # Normalizar la posición en la pantalla correctamente
            screen_x = int(((x + w // 2) / frame.shape[1]) * self.x_max)  # Usar el centro del rostro

            # Actualizar la posición objetivo
            self.target_x = screen_x

        # Aplicar suavizado con interpolación lineal (lerp)
        self.rect.x += (self.target_x - self.rect.x) * self.smooth_factor
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Verde con grosor 2
            break  # solo marcamos la primera cara detectada


        # Asegurar que no salga de los límites de la pantalla
        self.rect.x = max(0, min(self.x_max - self.size, self.rect.x))

        # Mostrar la cámara (para depuración)
        # cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            self.cap.release()
            cv2.destroyAllWindows()

        self.last_frame = frame  

    def draw(self, screen):
        """
        Dibuja la nave en la pantalla y el video en la esquina.
        """
        if self.mode == "video":
            self.ship_face_movement()

        if hasattr(self, 'last_frame') and self.last_frame is not None:
            # Redimensionar el frame a algo más chico para que no moleste
            small_frame = cv2.resize(self.last_frame, (280, 200))  # Tamaño chico
            small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # Convertir a RGB

            # Crear superficie de pygame
            frame_surface = pygame.surfarray.make_surface(np.rot90(small_frame))  # Rotar porque cv2 y pygame usan orden diferente

            # Mostrar en la esquina superior izquierda
            screen.blit(frame_surface, (20,20))

        screen.blit(self.image, self.rect.topleft)  
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Borde para debug


    def move(self, dx, dy):
        """
        Mueve la nave en la pantalla sin salir de los límites.
        """
        self.rect.x = max(0, min(self.x_max - self.size, self.rect.x + dx))

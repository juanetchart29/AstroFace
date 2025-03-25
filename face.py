import pygame
import cv2
import numpy as np

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Face Controlled Ship")

# Cargar la nave
ship = pygame.image.load("./assets/Ship.png")
ship = pygame.transform.scale(ship, (50, 50))
ship_rect = ship.get_rect(center=(400, 500))

# Iniciar la cámara con OpenCV
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

running = True
while running:
    screen.fill((0, 0, 0))  # Limpiar pantalla
    
    # Capturar imagen de la cámara
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostros
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Si detecta un rostro, mueve la nave
    for (x, y, w, h) in faces:
        # Convertir coordenadas de OpenCV a Pygame
        ship_rect.x = int(x * 800 / frame.shape[1])

        # Dibujar rectángulo en el rostro (para depuración)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        break  # Solo usar la primera cara detectada

    # Mostrar la nave en la pantalla de Pygame
    screen.blit(ship, ship_rect)

    # Procesar eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Actualizar pantalla
    
    # Mostrar la cámara en una ventana OpenCV (para depuración)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
pygame.quit()

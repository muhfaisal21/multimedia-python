import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('games.jpeg')

# Memuat suara
sound = pygame.mixer.Sound('result.wav')

# Memutar suara
sound.play()

# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = -image.get_width()  # Mengatur x ke posisi kiri luar layar saat melewati batas kanan

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))  # Mengisi layar dengan warna hitam sebelum menggambar gambar
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

    # Menambahkan jeda untuk mengatur kecepatan gerakan
    pygame.time.delay(30)

pygame.quit()
import pygame

pygame.init()
pygame.mixer.init()

def play_a_different_song():
    global currently_playing_song, songs, current_song_index
    next_song_index = (current_song_index + 1) % len(songs)
    currently_playing_song = songs[next_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = next_song_index

def play_previous_song():
    global currently_playing_song, songs, current_song_index
    previous_song_index = (current_song_index - 1) % len(songs)
    currently_playing_song = songs[previous_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = previous_song_index

def stop_music():
    pygame.mixer.music.stop()

def play_pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
songs = ['Yeat Never Quit.mp4', 'Yeat Keep Pushin.mp4', 'Yeat Psychocaine.mp4']
current_song_index = 0
currently_playing_song = songs[current_song_index]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause_music()
            elif event.key == pygame.K_n:
                play_a_different_song()
            elif event.key == pygame.K_p:
                play_previous_song()
            elif event.key == pygame.K_s:
                stop_music()
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
import PySimpleGUI as sg
import os
from pygame import mixer

mixer.init()

def get_files_inside_directory_not_recursive(directory):
    directories = []
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            directories.append(root + os.sep + file)
    return directories

def play_sound(sound_path):
    mixer.music.load(sound_path)
    mixer.music.play()

def stop_sounds():
    mixer.music.stop()

def pause_sounds():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def is_sound_playing():
    if mixer.music.get_busy() == True:
        return True
    return False

def set_volume(vol):
    mixer.music.set_volume(vol)
def update_song_display():
    janela['song_name'].update(os.path.basename(get_files_inside_directory_not_recursive(directory)[Index]))

def update_pause():
    janela['play'].update(filename='pause.png')

def update_play():
    janela['play'].update(filename='iconspy2.png')


sg.theme('DarkTeal11')

main = [
    [ sg.Canvas( size=(500,25))],

    [sg.Canvas( size=(50,250)),
     sg.Image( size=(250,300), filename='musica.png'),
     sg.Canvas( size=(50,250))],

    [sg.Text(text='Press play..', justification='center', background_color='black',
             text_color='white', size=(200, 0), font='Tahoma', key='song_name')],

    [sg.Canvas(size=(110,150)),
     sg.Image(filename='iconprev.png', size=(35,35), enable_events=True, key='previous'),
     sg.Image(filename='iconspy2.png', size=(50,50), enable_events=True, key='play'),
     sg.Image(filename='iconspy.png', size=(35,35), enable_events=True, key='next'),
     sg.Canvas(size=(110,150))]
]

janela = sg.Window('vplayer', layout = main, size=(400,600))
Index = 0
isPaused = 0

while True:
    events, valores = janela.read()
    if events == sg.WIN_CLOSED:
        break
    if events == 'play':
        if is_sound_playing()==True:

            pause_sounds()

            update_play()

            isPaused = True
        elif isPaused == True:

            unpause()

            update_pause()

            isPaused = False
        else:
            directory = sg.popup_get_folder('music directory')

            sizeIndex = len(get_files_inside_directory_not_recursive(directory))

            play_sound(get_files_inside_directory_not_recursive(directory)[Index])

            update_song_display()

            update_pause()

    if events == 'next':
        Index += 1

        if Index == sizeIndex:
            Index = 0

        play_sound(get_files_inside_directory_not_recursive(directory)[Index])

        update_song_display()

        if isPaused==True:
            pause_sounds()

    if events == 'previous':
        Index -= 1
        if Index == -sizeIndex:
            Index = 0

        play_sound(get_files_inside_directory_not_recursive(directory)[Index])

        update_song_display()

        if isPaused==True:
            pause_sounds()

#from gpiozero import Button
import vlc
import time

#play = Button(4,pull_up=False)
#VolumeUp = Button(27,pull_up=False)
#VolumeDown = Button(17,pull_up=False)
audioFile = '/Users/cory/SynologyDrive/Project/sleep.mp3'
is_playing = False
defaultVolume = 50
debounceTime = .07


def play_audio(sound):
    print("Play Audio")
    sound.audio_set_volume(defaultVolume)
    sound.play()
    time.sleep(1)

def change_volume(button,sound):
    global volume
    if(button==VolumeUp):
        volume=volume+1
    else:
        volume=volume-1
    sound.audio_set_volume(volume)

def debounce(button):
    global debounceTime
    time.sleep(debounceTime)
    if(button.is_pressed):
        return True
    else:
        return False


print("ready")
while True:
    if(!is_playing):
        if(play.is_pressed):
            if(debounce(play)):
                sound=vlc.MediaPlayer(audioFile)
                play_audio(sound)
                is_playing=True

    else:
        if(play.is_pressed):
            if(debounce(play)):
                print("Stop Audio")
                sound.stop()
                time.sleep(2)
                is_playing=False
        while(VolumeUp.is_pressed):
            if(debounce(VolumeUp)):
                print("Volume Up")
                change_volume(VolumeUp,sound)
        while(VolumeDown.is_pressed):
            if(debounce(VolumeDown)):
                print("Volume Down")
                change_volume(VolumeDown,sound)

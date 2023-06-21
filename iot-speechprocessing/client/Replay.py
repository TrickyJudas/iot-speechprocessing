import sounddevice as sound
import numpy


def replay_recording(data, sample_rate, output_device):
    """Tries to play sound from a numpy-array with a given samplerate over the given output_device ('sysdefault' works
        fine).
        Allows the user to stop the replay in the terminal by pressing ctrl+c"""
    try:
        # set the given output_device to the one used for replaying the sound
        sound.default.device = output_device
        # play sound from  the array
        sound.play(data, sample_rate)
        # else tell the user there is no data and return false
    # let the user interrupt the replay by pressing ctrl+c on the keyboard
    except KeyboardInterrupt:
        print('Stopping the replay...')
        sound.stop()
        print('Replay stopped')
        # return false since the function was interrupted
        return False

    # Jump here if the data contains any not playable elements
    except ValueError:
        print('The given data is not playable!')
        return False

    except OSError:
        print("No existing record could be found!")
        return False
    # wait for the replay to finish, then continue with the program
    # sound.wait also returns true if an underflow/overflow error has occurred, inform the user after
    # the console-spam
    try:
        if sound.wait():
            print("Could not replay!")
            print("Check output-device ('sysdefault' should work fine) or change the samplerate!")
            # return true since everything worked
            return True
    except KeyboardInterrupt:
        print('Stopping the replay...')
        sound.stop()
        print('Replay stopped')
        # return false since the function was interrupted
        return False


#debugging for testing purposes
if __name__ == "__main__":
    #record 5 seconds of sound
    myrecording = sound.rec(5 * 44100, 44100, channels = 2)
    sound.wait()

    #print the array
    print(myrecording)

    #replay it
    replay_recording(myrecording, 44100, 'sysdefault')

import numpy as np
import sounddevice as sd
import os

os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop/PythonPrograms/Guitar'))

# Sampling rate
sample_rate = 44100

def karplus_strong(frequency, duration=1.0, damping=0.996):
    """ Simulate a plucked guitar string using Karplus-Strong algorithm """
    n_samples = int(sample_rate * duration)
    buffer_size = int(sample_rate / frequency)

    # Initial noise burst (random excitation of the string)
    buffer = np.random.uniform(-1, 1, buffer_size)
    output = np.zeros(n_samples)

    for i in range(n_samples):
        buffer[0] = damping * 0.5 * (buffer[0] + buffer[1])  # Simulates energy loss
        output[i] = buffer[0]
        buffer = np.roll(buffer, -1)  # Shift buffer left

    return output

# Frequencies for "Do Re Mi Fa So La Ti Do"
notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

def front():
    # Duration settings
    duration = 1.0  
    overlap = 0.75  # Start next note at 75% of previous note
    n_samples = int(sample_rate * duration)

    # Initialize an empty waveform buffer
    final_output = np.zeros(n_samples + int(n_samples * (len(notes) - 1) * overlap))

    # Mix overlapping notes into the same buffer
    for i, freq in enumerate(notes):
        start_sample = int(i * overlap * n_samples)  # Compute start position in buffer
        sound_wave = karplus_strong(freq, duration)

        # Add the new note to the final output buffer (mixing)
        final_output[start_sample:start_sample + len(sound_wave)] += sound_wave

    # Normalize to avoid clipping
    final_output /= np.max(np.abs(final_output))
    return final_output

def back():
    # Duration settings
    duration = 1.0  
    overlap = 0.75  # Start next note at 75% of previous note
    n_samples = int(sample_rate * duration)

    # Initialize an empty waveform buffer
    final_output = np.zeros(n_samples + int(n_samples * (len(notes) - 1) * overlap))

    for i, freq in enumerate(notes[::-1]):
        start_sample = int(i * overlap * n_samples)  # Compute start position in buffer
        sound_wave = karplus_strong(freq, duration)

        # Add the new note to the final output buffer (mixing)
        final_output[start_sample:start_sample + len(sound_wave)] += sound_wave

    # Normalize to avoid clipping
    final_output /= np.max(np.abs(final_output))
    return final_output

if 'front.npy' in os.listdir():
    front_output = np.load('front.npy')
    print(front_output)
else:
    front_output = front()
    np.save('front', front_output)

if 'back.npy' in os.listdir():
    back_output = np.load('back.npy')
    print(back_output)
else:
    back_output = back()    
    np.save('back', back_output)

final = np.concatenate((front_output, back_output))
# Play the mixed sound
sd.play(final, samplerate=sample_rate)
sd.wait()

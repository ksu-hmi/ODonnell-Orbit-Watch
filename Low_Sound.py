import numpy as np
import wave
import struct

def generate_super_low_tone(filename, frequency=110, duration=2, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Soft sine wave for low tone
    signal = np.sin(2 * np.pi * frequency * t)

    # Apply fade-in and fade-out
    fade_in = np.linspace(0, 1, int(sample_rate * 0.5))  # 0.5s fade in
    fade_out = np.linspace(1, 0, int(sample_rate * 0.5)) # 0.5s fade out
    middle = np.ones(len(signal) - len(fade_in) - len(fade_out))
    envelope = np.concatenate((fade_in, middle, fade_out))

    signal *= envelope
    signal = np.int16(signal / np.max(np.abs(signal)) * 32767)

    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        for s in signal:
            wav_file.writeframes(struct.pack('h', s))

# 🌌 Make the super low gentle tone
generate_super_low_tone("super_low_tone.wav", frequency=330, duration=3)


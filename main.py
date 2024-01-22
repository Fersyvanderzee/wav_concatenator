from pydub import AudioSegment
import os
import random


def concatenate_wav_files(input_files, output_file):
    # Initialize an empty AudioSegment object
    concatenated_audio = AudioSegment.silent(duration=0)

    # Iterate through the input files and append them to the concatenated_audio
    for input_file in input_files:
        audio_segment = AudioSegment.from_wav(input_file)
        concatenated_audio += audio_segment

    # Export the concatenated audio to the output file
    concatenated_audio.export(output_file, format="wav")


path = 'C:/game_ambience_vids'

inputs = []

for file in os.listdir(path):
    inputs.append(path + "/" + file)


for i in range(10):
    random.shuffle(inputs)
    concatenate_wav_files(input_files=inputs, output_file=f'mc_chill_{i}.wav')

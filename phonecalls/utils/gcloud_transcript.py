import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


class GCloudTranscript:

    def __init__(self):
        self.client = speech.SpeechClient()

    def transcribe_file(self, file_name):
        # Instantiates a client
        client = self.client

        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=8000,
            language_code='en-US')

        # Detects speech in the audio file
        response = client.recognize(config, audio)

        transcripts = []
        for result in response.results:
            if (result.alternatives[0].transcript):
                transcripts.append(result.alternatives[0].transcript)

        return transcripts
import record
import storing
import speechToText

record.record()
storing.upload_blob("hangman-audio-files", "letters.wav", "letters.wav")
print(speechToText.sample_recognize('gs://hangman-audio-files/letters.wav'))





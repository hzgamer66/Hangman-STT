import record
import storing
import speechToText


def get_letter():
    record.record()
    storing.upload_blob("hangman-audio-files", "letters.wav", "letters.wav")
    return speechToText.sample_recognize('gs://hangman-audio-files/letters.wav')



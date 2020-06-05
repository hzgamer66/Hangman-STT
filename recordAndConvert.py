import record
import storing
import speechToText


def get_letter():
    record.record()
    storing.upload_blob("hangman-audio-files", "letters.wav", "letters.wav")
    speech = speechToText.sample_recognize('gs://hangman-audio-files/letters.wav')
    if 'letter' in speech:
        speech = list(speech)
        for i in range(7):
            del speech[0]
        if ' ' in speech:
            speech.remove(' ')
        speech = ''.join(speech)

    return speech




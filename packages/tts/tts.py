from google_speech import Speech


class TextToSpeech:
    """
    Convert texts to speech
    """

    def __init__(
        self,
        text: str = "Please Type Something to Speak",
        language: str = "en",
        volume: int = 100,
        speed: int = 100,
    ):
        """
        __init__ is the constructor of the class.

        :param text: Text to be converted to speech, default is "Please Type Something to Speak".
        :type text: str, optional

        :param language: Language of the text, default is "en".
        :type language: str, optional

        :param volume: Volume of the speech, default is 100.
        :type volume: int, optional

        :param speed: Speed of the speech, default is 100.
        :type speed: int, optional
        """
        self.text = text
        self.language = language
        self.volume = volume / 100
        self.speed = speed / 100

        self.speech = Speech(self.text, self.language)
        self.sox_effects = ("speed", f"{self.speed}", "vol", f"{self.volume}")

    def say(self) -> bool:
        """
        say is the method that converts the text to speech.

        :return: True if the text was converted to speech, False if not.
        :rtype: bool
        """
        try:
            self.speech.play(self.sox_effects)
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    def save_to_mp3(self, file_name: str) -> bool:
        """
        save_to_mp3 is the method that converts the text to speech and saves it to a mp3 file.

        :param file_name: Name of the mp3 file.
        :type file_name: str

        :return: True if the text was converted to speech and saved to a mp3 file, False if not.
        :rtype: bool
        """
        try:
            self.speech.save(f"{file_name}")
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    @staticmethod
    def stop() -> None:
        """
        stop will stop the speach.
        """
        exit(1)

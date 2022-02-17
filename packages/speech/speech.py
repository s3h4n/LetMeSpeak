from ..command import Command


class Speech:
    @staticmethod
    def say(
        ampitude: int = 50,
        pitch: int = 50,
        speed: int = 50,
        words: str = "Nothing to Speak",
    ) -> bool:

        command = Command

        return command.run(
            "espeak-ng -a {} -p {} -s {} -v mb-en1 -k 10 '{}' > /dev/null 2>&1 &".format(
                ampitude * 2, pitch, speed * 3, words
            )
        )

    def stop(self) -> bool:
        command = Command

        return command.run("killall espeak-ng")

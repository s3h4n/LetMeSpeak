from subprocess import run


class Command:
    @staticmethod
    def run(command: str) -> bool:
        try:
            return (
                run(
                    command,
                    shell=True,
                    text=True,
                    capture_output=True,
                ).returncode
                == 0
            )

        except Exception as e:
            print(f"Error: {e}")
            return False

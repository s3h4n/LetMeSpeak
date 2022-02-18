from os import mkdir


class FileHelper:
    """
    This class handles the file operations.

    :raises e: If any error occurs raises an exception.
    """

    @staticmethod
    def create_dir(path: str) -> None:
        """
        create_dir creates a directory.

        :param path: The path of the directory.
        :type path: str

        :raises e: If any error occurs raises an exception.
        """
        try:
            mkdir(path)
        except FileExistsError:
            pass
        except Exception as e:
            raise e

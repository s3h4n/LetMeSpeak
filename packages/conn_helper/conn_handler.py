import requests


class ConnectionHelper:
    """
     This class handles the network related operations.

    :raises e: Raise an exception if there is any network error.
    """

    @staticmethod
    def is_active() -> bool:
        """
        is_active will check if the internet connection is active or not.

        :raises e: Raise an exception if there is any network error.
        :return: True if network is active. False otherwise.
        :rtype: bool
        """
        timeout = 1

        try:
            requests.head("https://www.google.com", timeout=timeout)
            return True
        except requests.ConnectionError:
            return False
        except Exception as e:
            raise e

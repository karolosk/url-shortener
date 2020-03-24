class ShortedUrlNotFoundException(Exception):

    def get_message(self):
        return("Could not found requested shorted url")


class NotValidUrlException(Exception):
    pass

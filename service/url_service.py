from models.url_model import UrlModel


class UrlService:
    
    def __init__(self):
        self.model = UrlModel()

    def create(self, url, short_url):
        return self.model.create(url, short_url)
    
    def get_all(self):
        return self.model.retrieve()

    def get_by_url(self, url):
        return self.model.retrieve_by_url(url)

    def get_by_shorted_url(self, shorted_url):
        return self.model.retrieve_by_url_shorted(shorted_url)

    def short_url(self, url):
        return url, url*2
        
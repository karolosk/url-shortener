from models.url_model import Url
from errors.not_valid_url_error import NotValidUrlException
import validators
import uuid
import os


class UrlService:

    # This can be generified if needed
    def get_or_create(self, session, url_to_stump):
        if validators.url(url_to_stump):
            url_to_return = session.query(Url).filter_by(original_url=url_to_stump).first()
            if url_to_return:
                return url_to_return
            else:
                shorted_url = os.getenv("HOST") + self.generate_short_link(session)
                url_to_return = Url(url_to_stump, shorted_url)
                session.add(url_to_return)
                session.commit()
                return url_to_return
        else:
            raise NotValidUrlException

    def generate_short_link(self, session):
        short_url = uuid.uuid4().hex[:6]
        link = session.query(Url).filter_by(shorted_url=short_url).first()

        if link:
            return self.generate_short_link()

        return short_url

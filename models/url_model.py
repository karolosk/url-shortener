import sqlite3
from datetime import datetime


class UrlModel:

    TABLENAME = 'url'

    def __init__(self):
        self.conn = sqlite3.connect('url-stump.db')

    def create(self, original_url, url_shorted):
        query = """
        INSERT INTO {TABLENAME} (original_url, url_shorted, created)
        VALUES ("{original_url}", "{url_shorted}", "{created}")
        """.format(TABLENAME=self.TABLENAME, original_url=original_url, url_shorted=url_shorted, created = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        result = self.conn.execute(query)
        self.conn.commit()

        return result

    def retrieve_by_url(self, original_url):
        where_clause = "AND original_url={original_url}".format(original_url)
        return self.retrieve(where_clause)

    
    def retrieve_by_url_shorted(self, original_url):
        where_clause = "AND url_shorted={url_shorted}".format()
        return self.retrieve(where_clause)

    def retrieve(self, where_clause=""):
        query = f"SELECT id, original_url, url_shorted, created " \
                f"from {self.TABLENAME} " + where_clause + " ORDER BY created DESC LIMIT 10 " 

        result_set = self.conn.execute(query).fetchall()
        return result_set

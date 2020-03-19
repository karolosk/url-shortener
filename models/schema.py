import sqlite3

class Schema:

    def __init__(self):
        self.conn = sqlite3.connect('url-stump.db')
        self.create_url_table()

    def create_url_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "url" (
          id INTEGER PRIMARY KEY,
          original_url TEXT,
          url_shorted TEXT,
          created Date
        );
        """

        self.conn.execute(query)
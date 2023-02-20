import time

from sqlalchemy import create_engine


class Database:
    """Database class, connections and queries"""

    def __init__(self):
        self.engine = create_engine(
            "postgresql://bonpftyd:We1dKSTQdDDUT7fxEocA6OIM0VLP5ghU@dumbo.db.elephantsql.com/bonpftyd")

    def connect(self, connection_count_limit=5):
        """Create connection with database"""
        connection_count = 0
        while connection_count < connection_count_limit:
            try:
                self.engine.connect()
                return self.engine
            except Exception as er:
                print(er)
                time.sleep(2)
                connection_count += 1

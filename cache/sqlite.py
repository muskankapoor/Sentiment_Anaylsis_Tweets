from contextlib import closing
import errno
import os
import sqlite3

from cache import Cache

TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS cache_{namespace} (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , key TEXT NOT NULL
    , value TEXT NOT NULL
    , UNIQUE(key) ON CONFLICT REPLACE
)
;
'''

INDEX_SQL = '''
CREATE INDEX
IF NOT EXISTS cache_{namespace}_key_idx
ON cache_{namespace} (key)
;
'''

GET_SQL = '''
SELECT value FROM cache_{namespace}
WHERE key = ?
'''

PUT_SQL = '''
INSERT INTO cache_{namespace}
(key, value)
VALUES (?, ?)
'''

class SqliteCache(Cache):
    def __init__(self, namespace, path):
        self._table_sql = TABLE_SQL.format(namespace=namespace)
        self._index_sql = INDEX_SQL.format(namespace=namespace)
        self._get_sql = GET_SQL.format(namespace=namespace)
        self._put_sql = PUT_SQL.format(namespace=namespace)

        # Create nested dirs for db if needed
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as e:
            if e.errno !=  errno.EEXIST:
                raise

        self._conn = sqlite3.connect(path)
        self._conn.row_factory = sqlite3.Row

        with closing(self._conn.cursor()) as c:
            c.execute(self._table_sql)
            c.execute(self._index_sql)
        self._conn.commit()

    def get(self, key):
        with closing(self._conn.cursor()) as c:
            c.execute(self._get_sql, (key,))
            row = c.fetchone()

        value = None
        if row is not None:
            value = row['value']
        return value

    def put(self, key, value):
        with closing(self._conn.cursor()) as c:
            c = self._conn.cursor()
            c.execute(self._put_sql, (key, value))
        self._conn.commit()

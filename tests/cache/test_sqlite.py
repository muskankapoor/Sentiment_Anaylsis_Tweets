import os
import unittest

from cache.sqlite import SqliteCache

TEST_DB_PATH = 'db/test.db'

class SqliteCacheTest(unittest.TestCase):
    def setUp(self):
        self.cache = SqliteCache('widgets', TEST_DB_PATH)

    def tearDown(self):
        os.remove(TEST_DB_PATH)

    def test_cache(self):
        # cache miss returns None
        self.assertIsNone(self.cache.get('foo'))

        # cache put populates table
        self.cache.put('foo', 'bar')
        c = self.cache._conn.cursor()
        c.execute('''SELECT COUNT(*) FROM cache_widgets''')
        row = c.fetchone()
        self.assertEqual(1, row[0])

        # cache hit returns value
        self.assertEqual(self.cache.get('foo'), 'bar')

        # cache put on existing key replaces value, no new records
        self.cache.put('foo', 'baz')
        c.execute('''SELECT COUNT(*) FROM cache_widgets''')
        row = c.fetchone()
        self.assertEqual(1, row[0])
        self.assertEqual(self.cache.get('foo'), 'baz')

        c.close()

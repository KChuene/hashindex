CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS Rainbow (
        Id INTEGER PRIMARY KEY,
        Hash TEXT UNIQUE NOT NULL,
        Phrase TEXT UNIQUE NOT NULL
    );
"""

CREATE_INDEX = """
    CREATE UNIQUE INDEX IF NOT EXISTS HashIndex 
    ON Rainbow(Hash);
"""

INSERT = """
    INSERT OR IGNORE INTO Rainbow(Hash, Phrase)
    VALUES (?, ?);
"""

SELECT = """
    SELECT Hash, Phrase FROM Rainbow
    WHERE Hash=?;
"""
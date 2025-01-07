CREATE_TABLE = """
    CREATE TABLE Rainbow (
        Id INTEGER PRIMARY KEY,
        Hash TEXT NOT NULL,
        Phrase TEXT NOT NULL
    );
"""

CREATE_INDEX = """
    CREATE INDEX HashIndex ON Rainbow(Hash);
"""

INSERT = """
    INSERT INTO Rainbow(?, ?);
"""

SELECT = """
    SELECT Phrase FROM Rainbow
    WHERE Hash=?;
"""
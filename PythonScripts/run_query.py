import sqlite3

conn = sqlite3.connect("Database/bluestock_mf.db")

query = """
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;
"""

result = conn.execute(query)

for row in result:
    print(row)

conn.close()

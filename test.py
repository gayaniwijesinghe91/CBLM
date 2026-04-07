import psycopg2

try:
    conn = psycopg2.connect(
        host="193.167.189.153",
        port=5432,
        dbname="cbml",
        user="cbml",
        password="Samiruvidvan@321",
        sslmode="require"
    )
    print("Connected!")
except Exception as e:
    print("Connection failed:", e)

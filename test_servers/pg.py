import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="mlflow_database",
    user="admin_mlflow",
    password="mlflow_postgres_password"
)

q = conn.cursor()
q.execute("SELECT version()")

print(q.fetchone())

conn.close()


# python pg.py
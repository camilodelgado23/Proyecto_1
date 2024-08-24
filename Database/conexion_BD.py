import psycopg2

def create_connection():
    """Crea una conexión a la base de datos PostgreSQL."""
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="root",
            host="localhost",
            port="5432",
            database="proyecto1"
        )
        print("Conexión exitosa a la base de datos PostgreSQL.")
        return connection
    except psycopg2.OperationalError as e:
        print(f"Error al conectar con PostgreSQL: {e}")
        return None

def test_connection():
    """Prueba la conexión y realiza una consulta de prueba."""
    connection = create_connection()
    
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print(f"Conectado a - {record}\n")
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

if __name__ == "__main__":
    test_connection()
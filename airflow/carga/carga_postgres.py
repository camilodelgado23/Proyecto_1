import sys
import os

import psycopg2

# Asegúrate de añadir la ruta correcta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pandas as pd
from Database.conexion_BD import create_connection
from psycopg2 import sql, extras


# Función para crear la tabla en PostgreSQL si no existe
def create_table(conn):
    with conn.cursor() as cur:
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS airplanes_API (
                registration_number VARCHAR(50),
                production_line VARCHAR(50),
                iata_type VARCHAR(50),
                model_name VARCHAR(100),
                model_code VARCHAR(50),
                icao_code_hex VARCHAR(50),
                iata_code_short VARCHAR(50),
                construction_number VARCHAR(50),
                test_registration_number VARCHAR(50),
                rollout_date DATE,
                first_flight_date DATE,
                delivery_date DATE,
                registration_date DATE,
                line_number VARCHAR(50),
                plane_series VARCHAR(50),
                airline_iata_code VARCHAR(50),
                airline_icao_code VARCHAR(50),
                plane_owner VARCHAR(100),
                engines_count INTEGER,
                engines_type VARCHAR(50),
                plane_age INTEGER,
                plane_status VARCHAR(50),
                plane_class JSONB
            );
        """)
        conn.commit()
        print("Tabla creada (si no existía) correctamente.")


# Función para cargar los datos a PostgreSQL desde un CSV
def insert_data_from_csv(csv_file_path, conn):
    try:
        # Cargar datos del CSV en un DataFrame
        df = pd.read_csv(csv_file_path)

        # Filtrar las columnas según la estructura de la tabla
        filtered_df = df[['registration_number', 'production_line', 'iata_type', 'model_name', 
                          'model_code', 'icao_code_hex', 'iata_code_short', 'construction_number', 
                          'test_registration_number', 'rollout_date', 'first_flight_date', 
                          'delivery_date', 'registration_date', 'line_number', 'plane_series', 
                          'airline_iata_code', 'airline_icao_code', 'plane_owner', 'engines_count', 
                          'engines_type', 'plane_age', 'plane_status', 'plane_class']]

        # Convertir las columnas de fecha
        date_columns = ['rollout_date', 'first_flight_date', 'delivery_date', 'registration_date']
        for col in date_columns:
            filtered_df[col] = pd.to_datetime(filtered_df[col], errors='coerce')

        # Verificar datos faltantes
        print("Datos faltantes por columna:", filtered_df.isnull().sum())

        # Convertir el DataFrame a una lista de tuplas
        data_to_insert = filtered_df.values.tolist()
        print("Número de registros a insertar:", len(data_to_insert))

        with conn.cursor() as cursor:
            # Crear consulta de inserción
            insert_query = sql.SQL("""
                INSERT INTO airplanes_API (registration_number, production_line, iata_type, model_name, 
                                            model_code, icao_code_hex, iata_code_short, construction_number, 
                                            test_registration_number, rollout_date, first_flight_date, 
                                            delivery_date, registration_date, line_number, plane_series, 
                                            airline_iata_code, airline_icao_code, plane_owner, engines_count, 
                                            engines_type, plane_age, plane_status, plane_class) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """)

            # Ejecutar la inserción de forma individual para depurar
            for record in data_to_insert:
                try:
                    cursor.execute(insert_query, record)
                except Exception as e:
                    print("Error al insertar el registro:", record)
                    print("Error:", e)

        # Confirmar los cambios
        conn.commit()
        print("Datos insertados exitosamente en la tabla: airplanes_API")

    except Exception as e:
        print("Error al insertar datos:", e)


# Función principal
def main():
    csv_file_path = 'Proyecto_Vuelos_parte1/csv/api_airplanesds.csv'  # Ajusta la ruta según sea necesario
    conn = create_connection()
    if conn:
        create_table(conn)  # Asegúrate de que la tabla esté creada
        insert_data_from_csv(csv_file_path, conn)
        conn.close()  # Cierra la conexión

if __name__ == "__main__":
    main()

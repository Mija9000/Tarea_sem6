import mysql.connector
import csv
import boto3

# Conexión a MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  # si no configuraste contraseña
    database='taller'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM personas")
rows = cursor.fetchall()

# Guardar en CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'nombre', 'apellido', 'edad'])  # encabezado
    writer.writerows(rows)

# Subir a S3
s3 = boto3.client('s3')
s3.upload_file('data.csv', 'mishabuckett', 'Taller_semana6/data.csv')
print("Ingesta completada")

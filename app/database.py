import mysql.connector
from flask import Flask, g, jsonify, request, render_template

# Configuración de la base de datos MySQL
DATABASE = {
    'host': 'localhost',
    'database': 'bdweb',
    'user': 'root',
    'password': '1234'
}

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para el formulario de contacto
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza el formulario HTML

# Función para obtener la conexión a la base de datos
def get_db_connection():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=DATABASE['host'],
            database=DATABASE['database'],
            user=DATABASE['user'],
            password=DATABASE['password']
        )
    return g.db

# Función para cerrar la conexión a la base de datos
@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Función para crear la tabla 'consultas' si no existe
def create_consultas_table():
    with app.app_context():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS consultas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                apellido VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                codigo_area VARCHAR(10) NOT NULL,
                numero_telefono VARCHAR(15) NOT NULL,
                pais_residencia VARCHAR(255) NOT NULL,
                fecha_nacimiento DATE NOT NULL,
                motivo_consulta TEXT,
                destino VARCHAR(255) NOT NULL,
                cantidad_personas INT NOT NULL,
                comentario TEXT,
                suscripcion BOOLEAN NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()

# Asegurar que la tabla 'consultas' esté creada al inicio
with app.app_context():
    create_consultas_table()


# Ruta para procesar el formulario de contacto
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Obtener datos del formulario
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    area_code = request.form['area_code']
    phone_number = request.form['phone_number']
    country = request.form['country']
    birthdate = request.form['birthdate']
    motive_consult = request.form['motive_consult']
    destination = request.form['destination']
    quantity = request.form['quantity']
    comments = request.form['comments']
    subscription = 'subscription' in request.form  # Verifica si el checkbox está marcado

    # Validación básica (puedes mejorarla según tus necesidades)
    if not firstname or not lastname or not email or not area_code or not phone_number or not country or not birthdate or not motive_consult or not destination or not quantity:
        return jsonify({"error": "Missing required fields"}), 400

    # Insertar datos en la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO consultas (nombre, apellido, email, codigo_area, numero_telefono, pais_residencia, fecha_nacimiento, motivo_consulta, destino, cantidad_personas, comentario, suscripcion)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (firstname, lastname, email, area_code, phone_number, country, birthdate, motive_consult, destination, quantity, comments, subscription))
    conn.commit()
    cursor.close()

    return jsonify({"message": "Consulta enviada correctamente"}), 201

if __name__ == "__main__":
    app.run(debug=True)

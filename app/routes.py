from flask import Blueprint, request, jsonify
from .database import get_db_connection

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/destinos', methods=['POST'])
def add_destino():
    try:
        data = request.json
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')
        codigo_area = data.get('codigo_area')
        numero_telefono = data.get('numero_telefono')
        pais_residencia = data.get('pais_residencia')
        fecha_nacimiento = data.get('fecha_nacimiento')
        motivo_consulta = data.get('motivo_consulta')
        destino = data.get('destino')
        cantidad_personas = data.get('cantidad_personas')
        comentario = data.get('comentario')

        if not all([nombre, apellido, email, codigo_area, numero_telefono, pais_residencia, fecha_nacimiento,
                    motivo_consulta, destino, cantidad_personas]):
            return jsonify({'message': 'Todos los campos son obligatorios'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO consultas (nombre, apellido, email, codigo_area, numero_telefono, pais_residencia,
                                   fecha_nacimiento, motivo_consulta, destino, cantidad_personas, comentario)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (nombre, apellido, email, codigo_area, numero_telefono, pais_residencia, fecha_nacimiento,
                        motivo_consulta, destino, cantidad_personas, comentario))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Destino agregado exitosamente'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@routes_bp.route('/destinos/<int:id>', methods=['PUT'])
def update_destino(id):
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    codigo_area = data.get('codigo_area')
    numero_telefono = data.get('numero_telefono')
    pais_residencia = data.get('pais_residencia')
    fecha_nacimiento = data.get('fecha_nacimiento')
    motivo_consulta = data.get('motivo_consulta')
    destino = data.get('destino')
    cantidad_personas = data.get('cantidad_personas')
    comentario = data.get('comentario')

    if not all([nombre, apellido, email, codigo_area, numero_telefono, pais_residencia, fecha_nacimiento,
                motivo_consulta, destino, cantidad_personas]):
        return jsonify({'message': 'Todos los campos son obligatorios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE consultas
        SET nombre = ?, apellido = ?, email = ?, codigo_area = ?, numero_telefono = ?, pais_residencia = ?,
            fecha_nacimiento = ?, motivo_consulta = ?, destino = ?, cantidad_personas = ?, comentario = ?
        WHERE id_destino = ?''',
                   (nombre, apellido, email, codigo_area, numero_telefono, pais_residencia, fecha_nacimiento,
                    motivo_consulta, destino, cantidad_personas, comentario, id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Destino actualizado exitosamente'}), 200

@routes_bp.route('/destinos/<int:id>', methods=['DELETE'])
def delete_destino(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM consultas WHERE id_destino = ?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Destino eliminado exitosamente'}), 200

@routes_bp.route('/destinos', methods=['GET'])
def get_destinos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM consultas')
    destinos = cursor.fetchall()
    cursor.close()
    conn.close()
    destinos_list = [dict(destino) for destino in destinos]
    return jsonify(destinos_list), 200

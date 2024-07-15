from flask import jsonify, request
from app.models import Destino

def add_destino():
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
    suscripcion = data.get('suscripcion', False)  # Assuming suscripcion is a boolean field

    if not all([nombre, apellido, email, codigo_area, numero_telefono, pais_residencia, fecha_nacimiento, motivo_consulta, destino, cantidad_personas]):
        return jsonify({"error": "Missing required fields"}), 400

    new_destino = Destino(
        nombre=nombre,
        apellido=apellido,
        email=email,
        codigo_area=codigo_area,
        numero_telefono=numero_telefono,
        pais_residencia=pais_residencia,
        fecha_nacimiento=fecha_nacimiento,
        motivo_consulta=motivo_consulta,
        destino=destino,
        cantidad_personas=cantidad_personas,
        comentario=comentario,
        suscripcion=suscripcion
    )
    new_destino.save()

    return jsonify({"message": "Destino creado exitosamente"}), 201

def get_all_destinos():
    destinos = Destino.get_all()
    for destino in destinos:
        print(f"ID: {destino.id_destino}, Nombre: {destino.nombre}, Apellido: {destino.apellido}, Email: {destino.email}, Destino: {destino.destino}")
    return jsonify([destino.serialize() for destino in destinos])

def update_destino(id_destino):
    destino = Destino.query.get(id_destino)
    if not destino:
        return jsonify({"error": "Destino no encontrado"}), 404

    data = request.json
    destino.nombre = data.get('nombre', destino.nombre)
    destino.apellido = data.get('apellido', destino.apellido)
    destino.email = data.get('email', destino.email)
    destino.codigo_area = data.get('codigo_area', destino.codigo_area)
    destino.numero_telefono = data.get('numero_telefono', destino.numero_telefono)
    destino.pais_residencia = data.get('pais_residencia', destino.pais_residencia)
    destino.fecha_nacimiento = data.get('fecha_nacimiento', destino.fecha_nacimiento)
    destino.motivo_consulta = data.get('motivo_consulta', destino.motivo_consulta)
    destino.destino = data.get('destino', destino.destino)
    destino.cantidad_personas = data.get('cantidad_personas', destino.cantidad_personas)
    destino.comentario = data.get('comentario', destino.comentario)
    destino.suscripcion = data.get('suscripcion', destino.suscripcion)

    destino.save()  # Guardar los cambios en la base de datos

    return jsonify({"message": "Destino actualizado exitosamente"})

def delete_destino(id_destino):
    destino = Destino.query.get(id_destino)
    if not destino:
        return jsonify({"error": "Destino no encontrado"}), 404

    destino.delete()  # Suponiendo que tengas un método delete() en tu modelo Destino

    return jsonify({"message": "Destino eliminado exitosamente"})

from app.database import get_db_connection

class Destino:
    # Constructor
    def __init__(self, id_destino=None, nombre=None, apellido=None, email=None, codigo_area=None, numero_telefono=None, pais_residencia=None,
                 fecha_nacimiento=None, motivo_consulta=None, destino=None, cantidad_personas=None, comentario=None):
        self.id_destino = id_destino
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.codigo_area = codigo_area
        self.numero_telefono = numero_telefono
        self.pais_residencia = pais_residencia
        self.fecha_nacimiento = fecha_nacimiento
        self.motivo_consulta = motivo_consulta
        self.destino = destino
        self.cantidad_personas = cantidad_personas
        self.comentario = comentario

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM destino")
        rows = cursor.fetchall()
        destinos = []
        for row in rows:
            destino = Destino(
                id_destino=row['id_destino'],
                nombre=row['nombre'],
                apellido=row['apellido'],
                email=row['email'],
                codigo_area=row['codigo_area'],
                numero_telefono=row['numero_telefono'],
                pais_residencia=row['pais_residencia'],
                fecha_nacimiento=row['fecha_nacimiento'],
                motivo_consulta=row['motivo_consulta'],
                destino=row['destino'],
                cantidad_personas=row['cantidad_personas'],
                comentario=row['comentario']
            )
            destinos.append(destino)
        cursor.close()
        return destinos

    def serialize(self):
        return {
            'id_destino': self.id_destino,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'codigo_area': self.codigo_area,
            'numero_telefono': self.numero_telefono,
            'pais_residencia': self.pais_residencia,
            'fecha_nacimiento': self.fecha_nacimiento,
            'motivo_consulta': self.motivo_consulta,
            'destino': self.destino,
            'cantidad_personas': self.cantidad_personas,
            'comentario': self.comentario
        }

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO destino (nombre, apellido, email, codigo_area, numero_telefono, pais_residencia, "
                       "fecha_nacimiento, motivo_consulta, destino, cantidad_personas, comentario) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (self.nombre, self.apellido, self.email, self.codigo_area, self.numero_telefono,
                        self.pais_residencia, self.fecha_nacimiento, self.motivo_consulta, self.destino,
                        self.cantidad_personas, self.comentario))
        conn.commit()
        cursor.close()

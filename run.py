from flask import Flask
from flask_cors import CORS
from app.database import create_consultas_table  # Importar init_db desde app.database
from app.views import get_all_destinos, add_destino, update_destino, delete_destino

app = Flask(__name__)
CORS(app)

# Inicializar la base de datos
create_consultas_table()

# Definir rutas
app.route("/api/destinos", methods=["POST"])(add_destino)
app.route("/api/destinos", methods=["GET"])(get_all_destinos)
app.route("/api/destinos/<int:id_destino>", methods=["PUT"])(update_destino)
app.route("/api/destinos/<int:id_destino>", methods=["DELETE"])(delete_destino)

if __name__ == "__main__":
    app.run(debug=True)

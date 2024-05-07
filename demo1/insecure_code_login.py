from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar_datos():
    nombre_usuario = request.form['username']
    contrasena = request.form['password']
    
    # Código vulnerable: No se valida la contraseña correctamente
    if nombre_usuario == 'admin' and contrasena == 'admin123':
        return 'Bienvenido, admin!'
    else:
        return 'Credenciales incorrectas'

if __name__ == '__main__':
    app.run(debug=True)

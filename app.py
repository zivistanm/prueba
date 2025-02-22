from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('circular-unity-451418-r6-75e41f65ae0c.json', scope)
client = gspread.authorize(creds)

# Abre la hoja de cálculo
sheet = client.open("prueba").sheet1

@app.route('/')
def index():
    # Obtiene todos los registros
    data = sheet.get_all_records()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    nombre = request.form['nombre']
    edad = request.form['edad']
    ciudad = request.form['ciudad']
    lala = request.form['lala']
    
    # Agrega los datos a la hoja
    sheet.append_row([nombre, edad, ciudad, lala])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

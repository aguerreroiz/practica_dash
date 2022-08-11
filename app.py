# Importar los paquetes o librerias requeridas

import dash
import dash_html_components as html

# Crear una instancia de la aplicacion

app = dash.Dash(__name__)

# Crear el diseño de la aplicacion

app.layout = html.Div([

    html.H1("Hello World")

])

# Ejecute la aplicacion,   

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
# Desde la línea de comando, en la misma carpeta donde guardó el archivo de su aplicación, ejecute esto
# nombre archivo.py
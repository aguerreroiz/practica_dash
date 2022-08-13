# Importar los paquetes o librerias requeridas

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# Crear una instancia de la aplicacion

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])

# Crear el diseño de la aplicacion

app.layout = html.Div([

    html.H1("BASE DE DATOS POBREZA Y EQUIDAD"),
    html.H2("Banco Mundial"),
    
    dbc.Tabs([dbc.Tab([html.Ul([
        html.Li("Número de economias: 170"),
        html.Li("Tiempo de Muestra: 1974-2019"),
        html.Li("Frecuencia de actualización: Cutrimestral"),
        html.Li("Ultmima actualización: Marzo 18 2020"),
        html.Li(["Fuente: ", html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',             href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                ]),
    ]),],label="Factores Claves"),dbc.Tab([ html.Ul([
            html.Br(),
            html.Li('Adaptado del libro: Interactive Dashboards and Data Apps with Plotly and Dash'),
            html.Li(['GitHub repo: ',
                     html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                            href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')])
        ])],label="Creditos")]),
        
]) # Div principal
    


# Ejecute la aplicacion,   

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
# Desde la línea de comando, en la misma carpeta donde guardó el archivo de su aplicación, ejecute esto
# nombre archivo.py
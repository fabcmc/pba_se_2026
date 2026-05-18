import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import gspread
import geopandas as gpd
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

# --- CONFIGURAÇÃO DE AMBIENTE ---
os.environ['PROJ_LIB'] = os.path.expanduser("~/anaconda3/envs/pba_env/share/proj")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Carregar Geometrias
path_shp = os.path.join(BASE_DIR, "data_files", "SE_Municipios_2024", "SE_Municipios_2024.shp")
gdf_sergipe = gpd.read_file(path_shp)
if gdf_sergipe.crs != "EPSG:4326":
    gdf_sergipe = gdf_sergipe.to_crs("EPSG:4326")

sergipe_geojson = json.loads(gdf_sergipe.to_json())

# 2. Conexão Google Sheets
path_creds = os.path.join(BASE_DIR, "credentials.json")
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(path_creds, scope)
client = gspread.authorize(creds)

def get_data():
    spreadsheet_id = "1N6hr33h3m1eUKxmYLiHLjIKqvrCEb0KpRmB9mMNn0Qw"
    sheet = client.open_by_key(spreadsheet_id).worksheet("geo_data")
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    
    # Padronização
    df['DRE'] = df['DRE'].astype(str)
    df['Município'] = df['Município'].astype(str)
    df['Classificação'] = df['Classificação'].astype(str)
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
    return df.dropna(subset=['Latitude', 'Longitude'])

# Carregamento inicial para popular os filtros padrão
df_init = get_data()
dre_list = sorted(df_init['DRE'].unique())
mun_list = sorted(df_init['Município'].unique())
class_list = sorted(df_init['Classificação'].unique())

# 3. Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Monitoramento PBA - Sergipe", style={'textAlign': 'center', 'fontFamily': 'Arial'}),
    
    html.Div([
        html.Div([
            html.Label("DRE:"),
            dcc.Dropdown(id='filtro-dre', options=[{'label': i, 'value': i} for i in dre_list], 
                         value=dre_list, multi=True) # Começa com todos
        ], style={'width': '32%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label("Município:"),
            dcc.Dropdown(id='filtro-mun', options=[{'label': i, 'value': i} for i in mun_list], 
                         value=mun_list, multi=True)
        ], style={'width': '32%', 'display': 'inline-block', 'margin': '0 1%'}),
        
        html.Div([
            html.Label("Classificação:"),
            dcc.Dropdown(id='filtro-class', options=[{'label': i, 'value': i} for i in class_list], 
                         value=class_list, multi=True)
        ], style={'width': '32%', 'display': 'inline-block'}),
    ], style={'padding': '20px', 'backgroundColor': '#f9f9f9'}),

    dcc.Graph(id='mapa-sergipe', style={'height': '80vh'}),
    dcc.Interval(id='interval-component', interval=3600*1000, n_intervals=0)
])

@app.callback(
    Output('mapa-sergipe', 'figure'),
    [Input('filtro-dre', 'value'),
     Input('filtro-mun', 'value'),
     Input('filtro-class', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_graph(dre_sel, mun_sel, class_sel, n):
    df = get_data()
    
    # Filtragem dos dados (Pins)
    dff = df.copy()
    if dre_sel: dff = dff[dff['DRE'].isin(dre_sel)]
    if mun_sel: dff = dff[dff['Município'].isin(mun_sel)]
    if class_sel: dff = dff[dff['Classificação'].isin(class_sel)]

    # 4. Lógica de Cores por DRE no Fundo
    # Precisamos associar a DRE de cada município ao GeoDataFrame
    df_mapa = df[['Município', 'DRE']].drop_duplicates()
    gdf_colorido = gdf_sergipe.merge(df_mapa, left_on='NM_MUN', right_on='Município', how='left')
    
    # Filtra polígonos apenas para o que foi selecionado nos filtros superiores
    if mun_sel:
        gdf_colorido = gdf_colorido[gdf_colorido['NM_MUN'].isin(mun_sel)]

    # Mapa Coroplético de Fundo (Cores por DRE)
    fig = px.choropleth_mapbox(
        gdf_colorido,
        geojson=sergipe_geojson,
        locations=gdf_colorido.index,
        color="DRE", # Cores diferentes para cada DRE
        color_discrete_sequence=px.colors.qualitative.Pastel, # Tons clarinhos
        opacity=0.5,
        hover_name="NM_MUN",
        mapbox_style="carto-positron",
        center={"lat": -10.6, "lon": -37.4},
        zoom=7.5
    )

    # Adicionar os Pins por cima
    if not dff.empty:
        pins = px.scatter_mapbox(
            dff, lat="Latitude", lon="Longitude", color="Classificação",
            hover_name="Local", hover_data=["DRE", "Total de Salas"],
            color_discrete_map={"Escolar": "blue", "Não Escolar": "orange"}
        )
        for trace in pins.data:
            fig.add_trace(trace)

    # Adicionar Camada Estática das Linhas de Sergipe (Sempre visível)
    fig.update_layout(
        mapbox_layers=[{
            "sourcetype": "geojson",
            "source": sergipe_geojson,
            "type": "line",
            "color": "gray",
            "line": {"width": 1},
            "opacity": 0.8
        }],
        margin={"r":0,"t":0,"l":0,"b":0}
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
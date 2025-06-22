# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        html.H1("📊 Depot Tracker", className="text-center text-primary my-4", style={
            "fontFamily": "Inter, sans-serif"
        }),

        dcc.Tabs([
            dcc.Tab(label="📄 Depotpositionen", children=[
                html.Div(id="depot-table", className="mt-4")
            ], className="custom-tab", selected_className="custom-tab--selected"),

            dcc.Tab(label="🥧 Asset Allocation", children=[
                html.Div(id="asset-piechart", className="mt-4")
            ], className="custom-tab", selected_className="custom-tab--selected"),

            dcc.Tab(label="📊 Dividenden", children=[
                html.Div(id="dividenden-chart", className="mt-4")
            ], className="custom-tab", selected_className="custom-tab--selected"),
        ], className="mb-4", parent_className="custom-tabs")
    ], fluid=True, className="p-4")

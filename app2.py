# Import Dependencies
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
import pandas as pd
from utils import calculate_amortization, update_dashboard

# Initialize the Dash app
app = Dash()

# Define the app layout 
app.layout = html.Div(children=[
    # Title and Description
    html.H1(children='Loan Analyzer'),

    html.Div(children='''
        A web application to analyze fixed-rate loans.
    '''),
    
    # Container for inputs and loan details side by side
    html.Div(children=[
        # Left column - Input controls
        html.Div(children=[
            html.H3('Loan Parameters'),
            
            # Input for Annual Interest Rate
            html.Div(children=[
                html.Label('Annual Interest Rate (%):'),
                dcc.Input(
                    id='interest-rate-input',
                    type='number',
                    value=5.0,
                    step=0.01,
                    min=0,
                    max=20,
                    style={'marginLeft': '10px'}
                )
            ], style={'marginBottom': '10px'}),

            # Input for Loan Amount
            html.Div(children=[
                html.Label('Loan Amount ($):'),
                dcc.Input(
                    id='loan-amount-input',
                    type='number',
                    value=200000,
                    step=1,
                    min=0,
                    max=1000000,
                    style={'marginLeft': '10px'}
                )
            ], style={'marginBottom': '10px'}),

            # Input for Down Payment
            html.Div(children=[
                html.Label('Down Payment ($):'),
                dcc.Input(
                    id='downpayment-input',
                    type='number',
                    value=40000,
                    step=1,
                    min=0,
                    max=1000000,
                    style={'marginLeft': '10px'}
                )
            ], style={'marginBottom': '10px'}),

            # Input for Loan Term
            html.Div(children=[
                html.Label('Loan Term (years):'),
                dcc.Input(
                    id='loan-term-input',
                    type='number',
                    value=30,
                    step=1,
                    min=1,
                    max=50,
                    style={'marginLeft': '10px'}
                )
            ], style={'marginBottom': '10px'}),

            # Update Button
            html.Button('Update Dashboard', id='update-button', n_clicks=0,
                       style={'padding': '5px 15px', 'cursor': 'pointer'})
        ], style={
            'width': '45%',
            'display': 'inline-block',
            'verticalAlign': 'top',
            'padding': '20px',
            'backgroundColor': '#f0f0f0',
            'borderRadius': '5px',
            'marginRight': '2%'
        }),
        
        # Right column - Loan details display
        html.Div(id='loan-details', style={
            'width': '45%',
            'display': 'inline-block',
            'verticalAlign': 'top',
            'padding': '20px',
            'backgroundColor': '#f0f0f0',
            'borderRadius': '5px'
        })
    ], style={'marginBottom': '30px'}),

    # Charts
    dcc.Graph(id='amortization-graph'),
    dcc.Graph(id='amortization-graph-2')
])  # ADDED: Closing bracket for app.layout

@callback(
    Output('loan-details', 'children'),
    Output('amortization-graph', 'figure'),
    Output('amortization-graph-2', 'figure'),
    Input('update-button', 'n_clicks'),
    State('interest-rate-input', 'value'),
    State('loan-amount-input', 'value'),
    State('downpayment-input', 'value'),
    State('loan-term-input', 'value'),
    prevent_initial_call=False
)
def update_dashboard_callback(n_clicks, annual_int_rate_percent, loan_amount_input, downpayment_input, loan_term_years):
    """Wrapper function that calls the update_dashboard function from utils"""
    return update_dashboard(annual_int_rate_percent, loan_amount_input, downpayment_input, loan_term_years)

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
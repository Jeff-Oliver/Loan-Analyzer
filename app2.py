# Import Dependencies
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from utils import calculate_amortization, update_dashboard

# Initialize the Dash app
app = Dash()

# Define initial loan parameters
loan_amount = 150000
downpayment = 150000 * 0.2
loan_term_years = 30

def calculate_amortization(annual_int_rate, loan_amount, downpayment, loan_term_years):
    return pd.DataFrame(schedule), monthly_payment, total_payment, principal

app.layout = html.Div(children=[
    html.H1(children='Loan Analyzer'),

    html.Div(children='''
        Dash: A web application to analyze loans.
    '''),
    
    html.Div(children=[
        html.Label('Annual Interest Rate (%):'),
        dcc.Input(
            id='interest-rate-input',
            type='number',
            value=6.25,
            step=0.01,
            min=0,
            max=20,
            style={'marginLeft': '10px', 'marginBottom': '20px'}
        )
    ]),
    
    html.Div(id='loan-details'),

    dcc.Graph(id='amortization-graph'),
    dcc.Graph(id='amortization-graph-2')
])

@callback(
    Output('loan-details', 'children'),
    Output('amortization-graph', 'figure'),
    Output('amortization-graph-2', 'figure'),
    Input('interest-rate-input', 'value')
)
# Update dashboard based on interest rate input using the function from utils.py
def update_dashboard_callback(annual_int_rate_percent):
    """Wrapper function that calls the update_dashboard function from utils"""
    return update_dashboard(annual_int_rate_percent, loan_amount, downpayment, loan_term_years)

if __name__ == '__main__':
    app.run(debug=True)
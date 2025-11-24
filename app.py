# Import Dependencies
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash()

# Define loan parameters and variables

annual_int_rate = 0.0625
loan_term_years = 30
loan_amount = 150000
downpayment = 150000 * 0.2
principal = loan_amount - downpayment
monthly_int_rate = annual_int_rate / 12
num_payments = loan_term_years * 12
monthly_payment = principal * (monthly_int_rate * (1 + monthly_int_rate) ** num_payments) / ((1 + monthly_int_rate) ** num_payments - 1)
total_payment = monthly_payment * num_payments

# Create amortization schedule
schedule = []
balance = principal
for payment_num in range(1, num_payments + 1):
    interest_payment = balance * monthly_int_rate
    principal_payment = monthly_payment - interest_payment
    balance -= principal_payment
    schedule.append({
        'Payment Number': payment_num,
        'Principal Payment': principal_payment,
        'Interest Payment': interest_payment,
        'Total Payment': monthly_payment,
        'Remaining Balance': balance if balance > 0 else 0
    })

amortization_df = pd.DataFrame(schedule)

# Create bar chart using Plotly Express
# see https://plotly.com/python/px-arguments/ for more options

# Find the payment where principal and interest are closest to equal
amortization_df['Difference'] = abs(amortization_df['Principal Payment'] - amortization_df['Interest Payment'])
crossover_point = amortization_df.loc[amortization_df['Difference'].idxmin(), 'Payment Number']

# code for a stacked bar chart
fig_1 = px.bar(amortization_df, x='Payment Number', y=['Principal Payment', 'Interest Payment'], 
             title='Amortization Schedule', 
             labels={'value':'Payment Amount ($)', 'Payment Number':'Payment Number'},
             barmode='stack',
             #bargap=0
             )
# Add vertical line at crossover point
fig_1.add_vline(x=crossover_point, line_dash="dash", line_color="red", line_width=3,
              annotation_text=f"Crossover at Payment #{int(crossover_point)}", 
              annotation_position="top right")

# Optional: Add a shape to highlight the bar
fig_1.add_vrect(x0=crossover_point-2, x1=crossover_point+2, 
              fillcolor="yellow", opacity=0.3, line_width=0)

# Format y-axis to show full numbers (no abbreviations)
fig_1.update_yaxes(tickformat=",.0f")

fig_2 = px.line(amortization_df, x='Payment Number', y=['Principal Payment', 'Interest Payment'], 
             title='Amortization Schedule', 
             labels={'value':'Payment Amount ($)', 'Payment Number':'Payment Number'})

# Add vertical line at crossover point
fig_2.add_vline(x=crossover_point, line_dash="dash", line_color="red", line_width=3,
              annotation_text=f"Crossover at Payment #{int(crossover_point)}", 
              annotation_position="top right")

# Optional: Add a shape to highlight the bar
fig_2.add_vrect(x0=crossover_point-2, x1=crossover_point+2, 
              fillcolor="yellow", opacity=0.3, line_width=0)

# Format y-axis to show full numbers (no abbreviations)
fig_2.update_yaxes(tickformat=",.0f")
app.layout = html.Div(children=[
    html.H1(children='Loan Analyzer'),

    html.Div(children='''
        Dash: A web application to analyze loans.
    '''),
    
    html.Div(children=[
        html.H3('Loan Details'),
        html.P(f'Loan Type: Fixed Rate Mortgage'),
        html.P(f'Loan Amount: ${loan_amount:,.2f}'),
        html.P(f'Down Payment: ${downpayment:,.2f}'),
        html.P(f'Principal: ${principal:,.2f}'),
        html.P(f'Monthly Payment: ${monthly_payment:,.2f}'),
        html.P(f'Total Payment: ${total_payment:,.2f}'),
        html.P(f'Interest Rate: {annual_int_rate*100:.2f}%'),
        html.P(f'Loan Term: {loan_term_years} years'),
        html.P(f'Total Interest Paid: ${(total_payment - principal):,.2f}')
    ]),

    dcc.Graph(
        id='amortization-graph',
        figure=fig_1
    ),

    dcc.Graph(
        id='amortization-graph-2',
        figure=fig_2
    )
])

if __name__ == '__main__':
    app.run(debug=True)
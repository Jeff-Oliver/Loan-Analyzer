# Import Dependencies
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

def calculate_amortization(annual_int_rate, loan_amount, downpayment, loan_term_years):
    """Calculate amortization schedule based on input parameters"""
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
    
    return pd.DataFrame(schedule), monthly_payment, total_payment, principal


def update_dashboard(annual_int_rate_percent, loan_amount, downpayment, loan_term_years):
    """Update all outputs when interest rate changes"""
    annual_int_rate = annual_int_rate_percent / 100
    
    amortization_df, monthly_payment, total_payment, principal = calculate_amortization(
        annual_int_rate, loan_amount, downpayment, loan_term_years
    )
    
    # Find crossover point
    amortization_df['Difference'] = abs(amortization_df['Principal Payment'] - amortization_df['Interest Payment'])
    crossover_point = amortization_df.loc[amortization_df['Difference'].idxmin(), 'Payment Number']
    
    # Create loan details section
    loan_details = [
        html.H3('Loan Details'),
        html.P(f'Loan Type: Fixed Rate Mortgage'),
        html.P(f'Loan Amount: ${loan_amount:,.2f}'),
        html.P(f'Down Payment: ${downpayment:,.2f}'),
        html.P(f'Loan Principal: ${principal:,.2f}'),
        html.P(f'Interest Rate: {annual_int_rate*100:.2f}%'),
        html.P(f'Loan Term: {loan_term_years} years'),
        html.P(f'Monthly Payment: ${monthly_payment:,.2f}'),
        html.P(f'Total Cost: ${total_payment:,.2f}'),
        html.P(f'Total Interest Paid: ${(total_payment - principal):,.2f}')
    ]
    
    # Create bar chart
    fig_1 = px.bar(amortization_df, x='Payment Number', y=['Principal Payment', 'Interest Payment'], 
                 title='Amortization Schedule', 
                 labels={'value':'Payment Amount ($)', 'Payment Number':'Payment Number'},
                 barmode='stack')
    fig_1.add_vline(x=crossover_point, line_dash="dash", line_color="red", line_width=3,
                  annotation_text=f"Crossover at Payment #{int(crossover_point)}", 
                  annotation_position="top right")
    fig_1.add_vrect(x0=crossover_point-2, x1=crossover_point+2, 
                  fillcolor="yellow", opacity=0.3, line_width=0)
    fig_1.update_yaxes(tickformat=",.0f")
    
    # Create line chart
    fig_2 = px.line(amortization_df, x='Payment Number', y=['Principal Payment', 'Interest Payment'], 
                 title='Amortization Schedule', 
                 labels={'value':'Payment Amount ($)', 'Payment Number':'Payment Number'})
    fig_2.add_vline(x=crossover_point, line_dash="dash", line_color="red", line_width=3,
                  annotation_text=f"Crossover at Payment #{int(crossover_point)}", 
                  annotation_position="top right")
    fig_2.add_vrect(x0=crossover_point-2, x1=crossover_point+2, 
                  fillcolor="yellow", opacity=0.3, line_width=0)
    fig_2.update_yaxes(tickformat=",.0f")
    
    return loan_details, fig_1, fig_2
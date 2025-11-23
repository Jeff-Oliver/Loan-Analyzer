# Loan Analyzer

### The final cost of an amortized loan is higher than you may think. Many loan recipients are unaware of the final total repayed and the amount of iterest being paid each period.

#### This project will allow users to input loan information and see the breakdown of payments over time.

##### Python 3.10 will be used for this project to allow the inclusion of LLMs if desired. Possibly a web agent that can retrieve current interest rates. That might be a fun addition.

### Loan amortization formula
### This formula calculates the fixed periodic payment needed to pay off a loan over a set period.
- M = Monthly payment
- P = Principal loan amount
- r = Monthly interest rate (annual rate divided by 12) 
- n = Total number of payments (loan term in years multiplied by 12)

#### Steps to calculate a loan amortization payment:
#### Identify the variables: 
- Determine the principal loan amount (P)
the annual interest rate
 and the total number of payments (n).
Convert to monthly rate:
- Divide the annual interest rate by 12 to get the monthly interest rate (r).  
#### Calculate the payment:
- Plug the values into the formula: (M=P\frac{r(1+r)^{n}}{(1+r)^{n}-1})
# Loan Analyzer

<img src="src\cone.png" alt="Under Construction" width="50">

## Under Construction

<img src="src\cone.png" alt="Under Construction" width="50">

### The final cost of an amortized loan is higher than you may think. Many loan recipients are unaware of the final total repaid and the amount of interest being paid each period

#### This project will allow users to input loan information and see the breakdown of payments over time and the final cost of the loan after repayment

#### Inspiration for this project came from the current news (Nov 2025) where lawmakers are considering a 50 year mortgage. I wanted a tool to help visualize the effects of this change. Sure there are tools online, but where's the fun in that!

##### Python 3.10 was used for this project to allow the inclusion of LLMs if desired. Possibly a web agent that can retrieve current interest rates. That might be a fun addition, but likely slower than an api call

## Loan amortization calculation

### For reference, here is the formula used for a fixed rate amortized mortgage

$$M = P \frac{r(1+r)^{n}}{(1+r)^{n}-1}$$

### Variables

    M = Monthly payment
    P = Principal loan amount
    r = Monthly interest rate (annual rate divided by 12) 
    n = Total number of payments (loan term in years multiplied by 12)
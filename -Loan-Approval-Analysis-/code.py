# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
df = pd.read_csv(path)
bank = pd.DataFrame(df)
categorical_var = df.select_dtypes(include = 'object')
print(categorical_var)
print('='*50)
numerical_var = df.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID', axis = 1)
print(banks.isnull().sum())
print('='*50)
bank_mode = banks.mode()
#print(bank_mode)
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
#banks = banks.fillna(banks.mode())
print(banks)
#code ends here


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks, index=['Gender','Married','Self_Employed'],values = 'LoanAmount', aggfunc = np.mean)
print(avg_loan_amount)


# code ends here



# --------------
# code starts here



loan_approved_se = len( banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)
print('='*50)
loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status']=='Y')])
print(loan_approved_nse)
print('='*50)
Loan_Status = 614
percentage_se = loan_approved_se/Loan_Status*100
print(percentage_se)
print('='*50)
percentage_nse = loan_approved_nse/Loan_Status*100
print(percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12 )
print(len(loan_term))
print('='*50)
big_loan_term =len(banks[loan_term >= 25])
print(big_loan_term)



# code ends here


# --------------
# code starts here




loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()
print(loan_groupby)
print('='*50)
print(mean_values)

# code ends here



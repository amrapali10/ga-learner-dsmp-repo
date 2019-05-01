# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()

plt.figure()
plt.title('Loan Status')
plt.xlabel('Count')
plt.ylabel('loan status')
loan_status.plot(kind = 'bar')
plt.show()
#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar', stacked=True, figsize=(10,8))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education']=='Graduate']
#print(graduate)
not_graduate = data[data['Education']=='Not Graduate']
graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density',label='Not Graduate')



#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)
res1 = data.groupby(['ApplicantIncome','LoanAmount'])

res1.plot.scatter(x='ApplicantIncome',y='LoanAmount', ax=ax_1)
ax_1.set_title('Applicant Income ')

res2 = data.groupby(['CoapplicantIncome','LoanAmount'])
res2.plot.scatter(x='CoapplicantIncome',y='LoanAmount', ax=ax_2)
ax_1.set_title('Coapplicant Income')


res2 = res1.fillna(0)
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

res3 =data.groupby(['TotalIncome','LoanAmount'])
res3.plot.scatter(x='TotalIncome',y='LoanAmount', ax=ax_3)
ax_1.set_title('TotalIncome')




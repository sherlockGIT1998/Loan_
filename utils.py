import pickle 
import json 
import numpy as np 
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import config 

class Loan():
    
    def __init__(self,credit_policy,purpose,int_rate,installment,
                 log_annual_inc,dti,fico,days_with_cr_line,revol_bal,
                 revol_util,inq_last_6mths,delinq_2yrs,pub_rec):
        
        self.credit_policy = credit_policy
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico = fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        self.inq_last_6mths =  inq_last_6mths
        self.delinq_2yrs = delinq_2yrs
        self.pub_rec = pub_rec
        
        self.purpose_col = 'purpose_' + purpose
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f :
            self.logistic_model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.save_data = json.load(f)
            
            self.column_names = np.array(self.save_data['column_names'])
            
    def get_predicted_loan(self):
        
        self.load_models()
        
        purpose_col_index = np.where(self.column_names==self.purpose_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.credit_policy
        array[1] = self.int_rate
        array[2] = self.installment
        array[3] = self.log_annual_inc
        array[4] = self.dti
        array[5] = self.fico
        array[6] = self.days_with_cr_line
        array[7] = self.revol_bal
        array[8] = self.revol_util
        array[9] = self.inq_last_6mths
        array[10] = self.delinq_2yrs
        array[11] = self.pub_rec

        array[purpose_col_index] == 1

        print('Array is :',array)
        
        yes_no = self.logistic_model.predict([array])[0]
        
        return yes_no
    
if __name__ == '__main__':
    
    credit_policy = 1.000000
    int_rate = 0.118900
    installment = 829.100000
    log_annual_inc = 11.350407
    dti = 19.480000
    fico = 737.000000
    days_with_cr_line = 5639.958333
    revol_bal = 28854.000000
    revol_util = 52.100000
    inq_last_6mths = 0.000000
    delinq_2yrs = 0.000000
    pub_rec = 0.000000

    purpose = 'credit_card'
    
    loan = Loan(credit_policy,purpose,int_rate,installment,
                 log_annual_inc,dti,fico,days_with_cr_line,revol_bal,
                 revol_util,inq_last_6mths,delinq_2yrs,pub_rec)
    
    yes_no  = loan.get_predicted_loan()
    
    if yes_no == 0 :
        
        print('Loan is Not Fully Paid....')
        
    else :
        
        print('Loan is FUlly Paid...')
        
        
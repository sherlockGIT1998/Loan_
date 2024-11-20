from flask import Flask,render_template,request

from utils import Loan

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Loan Prediction...')
    return render_template('index.html')

@app.route('/predict_loan',methods=['GET','POST'])

def get_loan_info():
    
    if request.method == 'GET':
        
        print('In GET Method...')
        
        data = request.form 
        
        credit_policy = eval(data['credit_policy'])
        purpose = data['purpose']
        int_rate = eval(data['int_rate'])
        installment = eval(data['installment'])
        log_annual_inc = eval(data['log_annual_inc'])
        dti = eval(data['dti'])
        fico = eval(data['fico'])
        days_with_cr_line = eval(data['days_with_cr_line'])
        revol_bal = eval(data['revol_bal'])
        revol_util = eval(data['revol_util'])
        inq_last_6mths = eval(data['inq_last_6mths'])
        delinq_2yrs = eval(data['delinq_2yrs'])
        pub_rec = eval(data['pub_rec'])
        
        loan = Loan(credit_policy,purpose,int_rate,installment,
                 log_annual_inc,dti,fico,days_with_cr_line,revol_bal,
                 revol_util,inq_last_6mths,delinq_2yrs,pub_rec)
        
        yes_no = loan.get_predicted_loan()
        
        return f'Loan is Not Fully Paid'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    app.run()
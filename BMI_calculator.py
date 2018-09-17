#BMI calculator
print('Enter your name')
name1=input()
print('Enter your height in m3')
height=int(input())
print('Enter your weight in kg3')
weight=int(input())
print('')
def calculate(height,weight):
    result=weight/(height**2)
    print('Your BMI=',result)
    if result>25:
        print('You are overweighted')
    else:
        print('You are not overweighted')

(calculate(height,weight))
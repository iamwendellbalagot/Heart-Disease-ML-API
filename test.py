import requests

cols = 'age sex cp trestbps chol fbs restecg thalach exang oldpeak slope ca thal'.split()
inp = {}
tvals = [43,1,0,120,177,0,0,120,1,2.5,1,0,3]

#for col in cols:
#    inp[col] = input('Input a value for ' + str(col) + ' :')

for i,col in enumerate(cols):
    inp[col] = tvals[i]


res = requests.post(url = 'http://127.0.0.1:5000/testapi', json=inp)
output = res.json()

print(inp)

print('='*50)
print('STATUS ' + str(res.status_code))
print('='*50, '\n\n')

print('\nOUTPUT:')
print('='*50, '\n')
print(output)



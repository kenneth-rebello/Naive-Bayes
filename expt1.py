dataset = [
           ['young','high','yes','fair','yes'],
           ['young','medium','yes','fair','no'],
           ['middle','low','no','fair','no'],
           ['senior','high','no','excellent','yes']
          ]

yesCount = {
    'age':{
        'young':0,
        'middle':0,
        'senior':0
    },
    'income':{
        'low':0,
        'high':0,
        'medium':0
    },
    'student':{
        'yes':0,
        'no':0
    },
    'credit':{
        'fair':0,
        'excellent':0
    }
}
yesTotal = 0

noCount = {
    'age':{
        'young':0,
        'middle':0,
        'senior':0
    },
    'income':{
        'low':0,
        'high':0,
        'medium':0
    },
    'student':{
        'yes':0,
        'no':0
    },
    'credit':{
        'fair':0,
        'excellent':0
    }
}
noTotal = 0

eventProb = {
    'age':{
        'young':0,
        'middle':0,
        'senior':0
    },
    'income':{
        'low':0,
        'high':0,
        'medium':0
    },
    'student':{
        'yes':0,
        'no':0
    },
    'credit':{
        'fair':0,
        'excellent':0
    }
}


for tuple in dataset:
    if(tuple[4]=='yes'):
        yesCount['age'][tuple[0]] = yesCount['age'][tuple[0]] + 1
        yesCount['income'][tuple[1]] = yesCount['income'][tuple[1]] + 1
        yesCount['student'][tuple[2]] = yesCount['student'][tuple[2]] + 1
        yesCount['credit'][tuple[3]] = yesCount['credit'][tuple[3]] + 1
        yesTotal = yesTotal + 1
            
    else:
        noCount['age'][tuple[0]] = noCount['age'][tuple[0]] + 1
        noCount['income'][tuple[1]] = noCount['income'][tuple[1]] + 1
        noCount['student'][tuple[2]] = noCount['student'][tuple[2]] + 1
        noCount['credit'][tuple[3]] = noCount['credit'][tuple[3]] + 1
        noTotal = noTotal + 1

for feature in yesCount.keys():
    for value in yesCount[feature].keys():
        eventProb[feature][value] = yesCount[feature][value] + noCount[feature][value]
        yesCount[feature][value] = yesCount[feature][value]/yesTotal

for feature in noCount.keys():
    for value in noCount[feature].keys():
        noCount[feature][value] = noCount[feature][value]/noTotal

print('Enter tuple to test in following lines')
a = input("Enter age").lower()
i = input("Enter income").lower()
s = input("Enter student or not").lower()
c = input("Enter credit score").lower()

probAge = yesCount['age'][a]
probInc = yesCount['income'][i]
probStud = yesCount['student'][s]
probCred = yesCount['credit'][c]

probYes = (probAge * probInc * probStud * probCred)*(yesTotal/(yesTotal+noTotal))

probAge = noCount['age'][a]
probInc = noCount['income'][i]
probStud = noCount['student'][s]
probCred = noCount['credit'][c]

probNo = (probAge * probInc * probStud * probCred)*(noTotal/(yesTotal+noTotal))


if(probYes==0):
    print('No')
else:
    percYes = probYes/(probYes+probNo)
    percNo = probNo/(probYes+probNo)

    print(percYes)
    print(percNo)

    if(percYes > percNo):
        print('Yes')
    else:
        print('No')

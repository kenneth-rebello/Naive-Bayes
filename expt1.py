import csv

dataset = []

yesCount = {}
yesTotal = 0

noCount = {}
noTotal = 0
test = []

print("dataset and dataset2 are the available files for testing")
filename = input("Enter filename, must be a csv\n")

with open(filename+'.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for idx, row in enumerate(csv_reader):
        if idx == 0:
            features = row
            for feature in row:
                yesCount[feature] = {}
                noCount[feature] = {}
        else:
            dataset.append(row)
            for idx, value in enumerate(row):
                yesCount[features[idx]][value] = 0
                noCount[features[idx]][value] = 0


for tuple in dataset:
    if(tuple[4]=='yes'):
        for idx,feature in enumerate(yesCount.keys()):
            yesCount[feature][tuple[idx]] = yesCount[feature][tuple[idx]] + 1
        yesTotal = yesTotal + 1
            
    else:
        for idx,feature in enumerate(yesCount.keys()):
            noCount[feature][tuple[idx]] = noCount[feature][tuple[idx]] + 1
        noTotal = noTotal + 1

for feature in yesCount.keys():
    for value in yesCount[feature].keys():
        yesCount[feature][value] = yesCount[feature][value]/yesTotal

for feature in noCount.keys():
    for value in noCount[feature].keys():
        noCount[feature][value] = noCount[feature][value]/noTotal
        
print('###THIS ALGORITHM IS SPECIFIC TO DATASETS HAVING ONLY ONE CLASS VARAIBLE SPECIFICALLY IN THE LAST COLUMN###')
print('Enter tuple to test in following lines')

features.pop()

totalProbYes = 1
totalProbNo = 1
for idx, f in enumerate(features):
    temp = input("Enter "+f+"\n")
    test.append(temp)
    totalProbYes = totalProbYes * yesCount[features[idx]][temp]
    totalProbNo = totalProbNo * noCount[features[idx]][temp]

print('Tuple to be tested: ')
print(test)

probYes = totalProbYes *(yesTotal/(yesTotal+noTotal))

probNo = totalProbNo *(noTotal/(yesTotal+noTotal))


if(probYes==0):
    print('No')
else:
    percYes = probYes/(probYes+probNo)
    percNo = probNo/(probYes+probNo)

    if(percYes > percNo):
        print('Yes')
    else:
        print('No')

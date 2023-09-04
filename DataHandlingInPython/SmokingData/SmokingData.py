import matplotlib.pyplot as plt
import csv

with open('smoking.csv', newline='') as smoking_data:
    smoke_csv = csv.reader(smoking_data, delimiter=',')
    smokers = []
    non_smokers = []
    marital_status = [0, 0, 0, 0, 0]
    for data in smoke_csv:
        if data[9] == 'Yes':
            smokers.append(data)
        else:
            non_smokers.append(data)
        if data[3] == 'Widowed':
            marital_status[0] += 1
        elif data[3] == 'Married':
            marital_status[1] += 1
        elif data[3] == 'Single':
            marital_status[2] += 1
        elif data[3] == 'Divorced':
            marital_status[3] += 1
        else:
            marital_status[4] += 1

smoke_count = len(smokers)
non_smoke_count = len(non_smokers)
pie_count = [smoke_count, non_smoke_count]
pie_labels = 'Smokers', 'Non-Smokers'
fig, ax = plt.subplots(2,2)
ax[0,0].pie(pie_count, labels=pie_labels)
ax[0,0].title.set_text('No. of Smokers vs Non-Smokers')

total_smoked = []
marital_status_smoke = [0, 0, 0, 0, 0]
status = ['Widowed', 'Married', 'Single', 'Divorced','Separated']
for data in smokers:
    total_smoked.append(int(data[-2]) + int(data[-3]))
    if data[3] == 'Widowed':
        marital_status_smoke[0] += 1
    elif data[3] == 'Married':
        marital_status_smoke[1] += 1
    elif data[3] == 'Single':
        marital_status_smoke[2] += 1
    elif data[3] == 'Divorced':
        marital_status_smoke[3] += 1
    else:
        marital_status_smoke[4] += 1

ax[0,1].hist(total_smoked, bins=20,edgecolor='black')
ax[0,1].title.set_text('Cigarettes smoked per week Histogram')
ax[0,1].set_xlabel('Cigarettes smoked per week')
ax[0,1].set_ylabel('Count')

ax[1,0].bar(status, marital_status_smoke)
ax[1,0].title.set_text('Count of smokers by marital status')
ax[1,0].set_xlabel('Marital Status')
ax[1,0].set_ylabel('Number of smokers')
smoke_ratio_marital = [0, 0, 0, 0, 0]
for x in range(len(marital_status_smoke)):
    smoke_ratio_marital[x] = marital_status_smoke[x] / marital_status[x]

ax[1,1].bar(status, smoke_ratio_marital)
ax[1,1].title.set_text('Proportion of each marital status that smoke')
ax[1,1].set_xlabel('Marital Status')
ax[1,1].set_ylabel('Fraction that smokes')
plt.show()
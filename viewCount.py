import requests
import datetime
import time

database = []

oneday = datetime.timedelta(days=1)
oneday1=datetime.date.today()
yesterday = datetime.date.today() - oneday
x=yesterday.strftime('%Y%m%d').strip()
y=oneday1.strftime('%Y%m%d').strip()

# first get all lines from file
with open('companies.txt', 'r') as w:
    companies = w.readlines()

# remove spaces
companies = [line.replace(' ', '') for line in companies]

# finally, write lines in the file
with open('companies.txt', 'w') as w:
    w.writelines(companies)

f = open("companies.txt","r")
lines = f.readlines()
r=f.read()
for line in lines:
    try:
        z = line.strip()
        url=("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/"+str(z)+"/daily/"+str(x)+"12/"+str(y))

        headers = {
            'User-Agent': 'My User Agent 1.0',
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        viewCount = data['items'][0]['views']
        companyName = f" -> {line}"
        FinalData = ((viewCount,companyName))
        print(FinalData)
        database.append(FinalData)
    except:
        pass

#bubble sort
for mx in range(len(database)-1, -1, -1):
        swapped = False
        for i in range(mx):
            if database[i][0] < database[i+1][0]:
                database[i], database[i+1] = database[i+1], database[i]
                swapped = True
        if not swapped:
            break

with open("DATABASE.txt","w") as file:
    for line in database:
        file.write(str(line[0])+line[1])
    file.close()

print("COMPLETED")

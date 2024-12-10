
import json
import re

# Open and read the JSON file
with open('./db/users.json', 'r') as file:
    users:dict = json.load(file)

# Print the data
users_dict:dict = users 
users:list[dict] = users['users']

# 1. -
print(len(users))

# 2. -
print(users[1]['company'])

# 3. -
print(users[1]['friends'][2]['name'])

# 4. -
print(users[0]['eyeColor'])

# 5. -
for user in users:
    print(user['address'])

# 6. -
user_count = 0
for user in users:
    if user['favoriteFruit'] == 'strawberry':
        user_count += 1

print(user_count)

# 7. -
for user in users:
    if user['name'] == 'Brianna Huffman':
        print(user['greeting'].split(' ')[-3])
        # greeting = user['greeting']
        # unread = re.search('\d', greeting)

# 8.
users_count:int = len(users)

users_male_count = 0
for user in users:
    if user['gender'] == 'male':
        users_male_count += 1

result = (users_male_count / users_count) * 100
print(f'{result:.0f}%')

# 9. -
female_ages = []
for user in users:
    if user['gender'] == 'female':
        female_ages.append(user['age'])
result_1 = round(sum(female_ages) / len(female_ages), 2)
print(result_1)

# 10. -
def sanitize_balance(balance:str) -> float:
    balance = balance[1:].replace(',', '')
    return float(balance)

balances_list = [sanitize_balance(user['balance']) for user in users]
print(sum(balances_list))

# 11. -
for user in users:
    if user['name'] == 'Zelma Sutton':
        print(user['address'].split(', ')[1])


# II.
# 1.
del users[1]

# 2.
users[2]['friends'].append({'id': 3, 'name': 'Toto tata'})

# 3.
users[3]['phone'] = "+1(954) 421-6824"

# 4.
users[0]['company'] = [users[0]['company'], 'SYLENT']

# 5.
for user in users:
    user['first-name'] = user['name'].split(' ')[0]
    user['last-name'] = user['name'].split(' ')[1]

# 6.
last_user_tags:list = users[-1]['tags']
last_user_tags.remove('laborum')

# 7.
for user in users:
    user['age'] += 1

with open('./db/users_updated.json', 'w') as outfile:
    json.dump(users, outfile, indent=4)
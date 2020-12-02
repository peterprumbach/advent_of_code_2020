passwords = []

counter=0

#Open passwords file
with open('2/passwords') as file:
    passwords = list(file.read().splitlines())

#Iterating passwords
for i in passwords:
    split = i.split(': ')
    password = split[1]
    policy = split[0].split('-')
    policy_split = policy[1].split(' ')

    min = int(policy[0])
    max = int(policy_split[0])

    policy_letter = policy_split[1]

    #(First OR last correct) AND (first and last not equal)
    if((password[min-1]==policy_letter or password[max-1]==policy_letter) and (password[min-1]!=password[max-1])):
        counter+=1

print(counter)
    
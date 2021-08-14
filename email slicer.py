email = input('Enter the email address: ')
emailchar = list(email)
username = []
domain = []

if '@' in emailchar:
    for i in range(0, emailchar.index('@')):
        username.append(emailchar[i])
    for i in range(emailchar.index('@'), len(emailchar)):
        domain.append(emailchar[i])
    print('Username: ' + ''.join(username))
    print('Domain: ' + ''.join(domain))  
else:
    if '@' not in emailchar and '.' not in emailchar:
        print('Invalid email address')
    elif '.' not in emailchar and '@' in emailchar:
        print('Invalid email address')
    elif '@' not in emailchar and '.' in emailchar:
        print('Invalid email address')

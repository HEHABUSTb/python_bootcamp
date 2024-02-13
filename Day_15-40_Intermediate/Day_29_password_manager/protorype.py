import csv


def save(website: str, username: str, password: str, mode='a'):
    # Set mode='w' if you want to rewrite file
    header = ['website', 'username', 'password']
    data = [website, username, password]

    with open('secret.csv', mode, newline='') as file:
        writer = csv.writer(file)
        if mode == 'w':
            writer.writerow(header)
        writer.writerow(data)


save('1', '42222', '3')
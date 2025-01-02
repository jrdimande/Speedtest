import json

filename = '/src/resources/Data.json'
filename1 = '/home/vboxuser/PycharmProject/Speed Test/src/resources/relatorio.txt

with open(filename) as f:
    content = json.load(f)

# soma
sum_download = 0
sum_upload = 0
sum_ping = 0

# ultimos 3 elementos da lista
last_three = content[-3:]

# datas
start = last_three[0]["date"]
end = last_three[-1]["date"]

# somando
for down_up in last_three:
    sum_download += down_up["download"]
    sum_upload += down_up["upload"]
    sum_ping += down_up["ping"]

# Calcular as médias
down_avarage = sum_download / len(last_three)
up_avarage = sum_upload / len(last_three)
ping_avarage = sum_ping / len(last_three)

# status
down_status = (down_avarage >= 4 and down_avarage <= 10)
up_status = (up_avarage >= 1 and up_avarage <= 3)
ping_status = (ping_avarage <= 100)

# Criar relatorio
text = (f'\nAvarage Download: {down_avarage: .2f} Mbps  Stable = {down_status}\n'
        f'Avarage Upload: {up_avarage: .2f} Mbps  Stable = {up_status}\n'
        f'Avarage Ping: {ping_avarage: .2f} ms  Stable = {ping_status}\nStart: {start} End: {end}\n')


with open(filename1, 'a') as f:
    f.write(text)

print(f"Report available at the file {filename1}")

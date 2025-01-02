import speedtest
import datetime
import time
import json


filename = '/src/resources/Data.json'

print("Executando o teste...")



st = speedtest.Speedtest()

st.get_best_server()

download = st.download() / 1000000
upload = st.upload() / 1000000
ping = st.results.ping

date = str(datetime.date.today())
current_time = time.localtime()
formatted_time = str(time.strftime("%H:%M:%S", current_time))


speed = {"date" : date, "time" : formatted_time, "download" : download, "upload" : upload, "ping" : ping}

with open(filename) as f:
    content = json.load(f)

content.append(speed)


with open(filename, 'w') as f:
    json.dump(content, f, indent=4)




print(f"Velocidade de Download: {download: .2f} Mbps")
print(f"Velocidade de Upload: {upload: .2f} Mbps")
print(f"Ping: {ping} ms")
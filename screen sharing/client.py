# pip install vidstream

from vidstream import StreamingServer
import threading

reciever = StreamingServer('Reciever_IPv4_address',5000)

t = threading.Thread(target = reciever.start_server)
t.start()

while input("") != "QUIT" :
    continue

reciever.stop_server()

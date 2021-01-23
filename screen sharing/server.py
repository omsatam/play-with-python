# pip install vidstream
from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('sender_IPv4_address',5000)

t = threading.Thread(target = sender.start_stream())
t.start()

while input("") != "QUIT" :
    continue

sender.start_stream()

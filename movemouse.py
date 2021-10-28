import mouse
import keyboard
import socket
from ipparse import parse
import time
import threading

def sendmouse(client):
    revpos = ""
    while True:
        pos1 = mouse.get_position()
        pos1str = str(pos1).strip("()")
        if pos1str == revpos:
            pass
        else:
            print(pos1str)
            revpos = pos1str
            time.sleep(0.2)
            client.send(bytes(pos1str, "utf8"))
        if mouse.is_pressed():
            time.sleep(0.2)
            client.send(bytes("lclick", "utf8"))
        if mouse.is_pressed(button=mouse.RIGHT):
            client.send(bytes("rclick", "utf8"))

def sendkey(client):
    while True:
        time.sleep(0.17)
        a = keyboard.read_event()
        print(a.name)
        client.send(bytes(str(a.name), "utf8"))


if __name__ == "__main__":
    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.bind((parse(), 8080))
    host.listen(1)
    client, addr = host.accept()
    print("connected")
    
    
    sm = threading.Thread(target=sendmouse, args=(client,))
    sk = threading.Thread(target=sendkey, args=(client,))
    
    sm.start()
    sk.start()
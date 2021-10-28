import mouse
import socket
import time
import keyboard

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("HOST_IP", 8080))
special_keys = ["enter", "backspace", "space", "shift", "ctrl", "up", "down", "left", "right"]
print("connected")
while True:
    pos = ""
    pos = client.recv(4096)
    if pos.decode("utf8") == "lclick":
        print("click")
        mouse.click()
    elif pos.decode("utf8") == "rclick":
        print("right click")
        mouse.click(button='right')
    else:
        pos1 = pos.decode("utf8").split(", ")
        if len(pos1) < 2:
            if len(pos1[0]) > 1:
                print(pos1[0])
                keyboard.press(pos1[0])
            else:
                print(pos1)
                keyboard.write(pos1[0]) 
        else:
            print(pos1)
            mouse.move(pos1[0], pos1[1])
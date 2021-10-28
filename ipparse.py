import os

def parse():
    os.system("ipconfig > ipfile")
    with open("ipfile", encoding="utf8") as r:
        reader = r.read()
        l1 = reader.split("IPv4 Address")
        l2 = l1[1].split(":")
        l3 = l2[1].split(" ")
        l4 = l3[1].split("\n")
        print(l4)
        return l4[0]
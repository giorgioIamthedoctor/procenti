import sys
def fuc():
    epsi = float(1)
    while float(1)+float(epsi) != float(1):
        epsi_last = epsi
        epsi = float(epsi) / float(2)
    return epsi_last
print(fuc(),sys.float_info.epsilon)

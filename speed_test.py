import speedtest

s = speedtest.Speedtest()

option = int(input('''What do you want to know : 
                   1) upload speed
                   2) download speed\n'''))

if option == 1:
    up = s.upload()
    upl = int(up)/1048576
    print("upload speed = ", upl, "mbps")

elif option == 2:
    do = s.download()
    down = int(do)/1048576
    print("download speed =", down, "mbps")

else:
    print('Invalid option...')
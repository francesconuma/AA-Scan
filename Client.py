# AAScan: Open source, minimalist, fully automated 3D scanner based on Arduino and Android!

# Server program - To be run on computer (I recommend LINUX)

# Copyright (C) 2020 redditNewUser2017
# Check out my page https://www.reddit.com/user/redditNewUser2017 and my subreddit https://www.reddit.com/r/Simulations/

"""     This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/agpl-3.0.en.html>. """

import serial,time,winsound
import socket

serverAddressList=["192.168.1.21"]    # Put your Phone IP here, multiple IPs are supported now (untested)!
serverPort=2022
bufferSize=12
nPhotos=45
nCicli=4
takephotoCommand="chez"
rotateCommand="go\n"
quitCommand="quit"
changeSound=winsound.MB_OK
serialConnection = serial.Serial('COM3',9600)   # Change this to COMx if you are on Windows, COMx is the port where Arduino serial is connected
print("Serial connection established on {name}".format(name=serialConnection.name))
time.sleep(3)
serialConnection.write((str(nPhotos)+"\n").encode())
time.sleep(1)

socketList=[]
for phone in serverAddressList:
    socketPhoneCommands = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketPhoneCommands.connect((phone,serverPort))
    socketList.append(socketPhoneCommands)
    
for j in range(nCicli):
    for i in range(nPhotos):
        for socketSendCommands in socketList:
            socketSendCommands.send(takephotocommand.encode())
        time.sleep(1.5)
        serialConnection.write(rotateCommand.encode())
        time.sleep(1.5)
        print("{iteration}/{totalIteration} Progress: {count}/{total}".format(iteration=i+1,totalIteration=nCicli,count=i+1,total=nPhotos))
    winsound.MessageBeep(changeSound)
    time.sleep(10)

print("DONE!")
time.sleep(1)
serialConnection.close()
for socketSendCommands in socketList:
    socketSendCommands.send(quitCommand.encode())
    socketSendCommands.close()

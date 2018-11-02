# Adam Pluguez
#10/30/2018
# Program to scan W:\NewDownloads\Feed
# Shows and locations stored in CurrentShows.txt
#Outline:
#0.Load show names into array.
#1.Scan W:\NewDownloads\Feed for matching show names partial strings?
#2.Move each matching file to its storege location in CurrentShows.txt
#3.Remove any remaining files or folders in W:\NewDownloads\Feed.

import shutil, os, send2trash, datetime, time
from pathlib import Path

#Set working directory
os.chdir('W:\\NewDownloads\\Feed\\')

#Read CurrentShows.txt into lines
text_file = open("I:\\CurrentShows.txt", "r")
lines = text_file.read().split(',')
text_file.close()

notice = ' is being moved to '
home = 'W:\\NewDownloads\Feed'

dt = datetime.datetime.now()

executed = False
while True:
    run = False
    while dt.hour != 3:
        time.sleep(3600)
        dt = datetime.datetime.now()
        executed = False
    run = True
    while run and not executed:
        #Walk through files
        for folderName, subfolders, filenames in os.walk('W:\\NewDownloads\Feed'):
                #Mark as executed so code only executes once during designated hour, runs twice a day
                executed = True
                for filename in filenames:
                    if filename.endswith('.mkv') or filename.endswith('.avi') or filename.endswith('.mp4'):
                        # Special Cases
                        if filename.lower().startswith("marvels"):
                            if "spider-man" in filename.lower():
                                    print(filename + notice + lines[160])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[160]+filename)
                                    if my_file.is_file():
                                        os.unlink(lines[160]+filename)
                                    shutil.move(folderName + '\\' + filename, lines[160])
                                    continue
                            elif "agents" in filename.lower():
                                    print(filename + notice + lines[120])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[120] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[120] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[120])
                                    continue
                            elif "cloak" in filename.lower():
                                    print(filename + notice + lines[125])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[125] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[125] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[125])
                                    continue
                            elif "daredevil" in filename.lower():
                                    print(filename + notice + lines[130])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[130] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[130] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[130])
                                    continue
                            elif  "inhumans" in filename.lower():
                                    print(filename + notice + lines[135])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[135] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[135] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[135])
                                    continue
                            elif "Rocket" in filename or "rocket" in filename:
                                    print(filename + notice + lines[150])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[150] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[150] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[150])
                                    continue
                            elif "defenders" in filename.lower():
                                    print(filename + notice + lines[140])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[140] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[140] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[140])
                                    continue
                            elif "runaways" in filename.lower():
                                    print(filename + notice + lines[155])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[155] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[155] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[155])
                                    continue
                            elif "ironfist" in filename.lower():
                                    print(filename + notice + lines[145])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[145] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[145] + filename)
                                    shutil.move(folderName + '\\' + filename, lines[145])
                                    continue
                        elif filename.lower().startswith("star"):
                            if "trek" in filename.lower():
                                print(filename + notice + lines[225])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[225] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[225] + filename)
                                shutil.move(folderName + '\\' + filename, lines[225])
                                continue
                            elif "wars" in filename.lower():
                                print(filename + notice + lines[230])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[230] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[230] + filename)
                                shutil.move(folderName + '\\' + filename, lines[230])
                                continue
                        elif filename.lower().startswith("the"):
                            if "100" in filename.lower():
                                print(filename + notice + lines[244])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[244] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[244] + filename)
                                shutil.move(folderName + '\\' + filename, lines[244])
                                continue
                            elif "big" in filename.lower():
                                print(filename + notice + lines[249])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[249] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[249] + filename)
                                shutil.move(folderName + '\\' + filename, lines[249])
                                continue
                            elif "conners" in filename.lower():
                                print(filename + notice + lines[254])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[254] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[254] + filename)
                                shutil.move(folderName + '\\' + filename, lines[254])
                                break
                            elif "flash" in filename.lower():
                                print(filename + notice + lines[264])
                                print("Copying file please wait patiently....")
                                shutil.move(folderName + '\\' + filename, lines[264])
                                continue
                            elif "crossing" in filename.lower():
                                print(filename + notice + lines[259])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[259] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[259] + filename)
                                shutil.move(folderName + '\\' + filename, lines[259])
                                continue
                            elif "simpsons" in filename.lower():
                                print(filename + notice + lines[269])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[269] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[269] + filename)
                                shutil.move(folderName + '\\' + filename, lines[269])
                                continue
                            elif "venture" in filename.lower():
                                print(filename + notice + lines[274])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[274] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[274] + filename)
                                shutil.move(folderName + '\\' + filename, lines[274])
                                continue
                            elif "walking" in filename.lower():
                                print(filename + notice + lines[279])
                                print("Copying file please wait patiently....")
                                my_file = Path(lines[279] + filename)
                                if my_file.is_file():
                                    os.unlink(lines[279] + filename)
                                shutil.move(folderName + '\\' + filename, lines[279])
                                continue
                        elif filename.lower().startswith("modern"):
                            print(filename + notice + lines[165])
                            print("Copying file please wait patiently....")
                            my_file = Path(lines[165] + filename)
                            if my_file.is_file():
                                os.unlink(lines[165] + filename)
                            shutil.move(folderName + '\\' + filename, lines[165])
                            continue

                        #General Cases
                        else:
                            for i in range(1, 295):
                                if lines[i].lower() in filename.lower():
                                    print(filename + notice + lines[i + 3])
                                    print("Copying file please wait patiently....")
                                    my_file = Path(lines[i + 3] + filename)
                                    if my_file.is_file():
                                        os.unlink(lines[i + 3] + filename)
                                    shutil.move(folderName+'\\'+ filename,lines[i+3])
                                    continue
                        print("All video files have in %s been moved!" % folderName)

        #This section checks for any unmoved video files in folders
        #Counts folders in home location
        flag = []
        count = 0
        for folderName, subfolders, filenames in os.walk('W:\\NewDownloads\Feed'):
            count = count + 1
        count = count

        #Create list and mark folders to be deleted
        for i in range(count):
            flag.append(0)

        #Flag folders with video files or unfinished files
        index = 0
        for folderName, subfolders, filenames in os.walk('W:\\NewDownloads\Feed'):
            for filename in filenames:
                if  filename.endswith('.mkv') or  filename.endswith('.avi') or  filename.endswith('.mp4') or filename.endswith('.part'):
                   flag[index] = 1
            if index < count:
                index = index + 1


        # If no remaining video files delete all folders in home location = W:\\NewDownloads\Feed
        index = 0
        for folderName, subfolders, filenames in os.walk('W:\\NewDownloads\Feed'):
            if "John" in folderName:
                print("Deleting %s ..." % folderName)
                shutil.rmtree(folderName)
            elif folderName != home and flag[index] == 0:
                print("Deleting %s ..." % folderName)
                shutil.rmtree(folderName)
            if index < count-1:
                index = index + 1

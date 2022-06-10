import os

directoryLoc = input("paste the directory with the files you wish to rename\n")
print("Current working directory: {0}\n".format(os.getcwd()))
multipleEpisodes = input("enter 0 for 1 episode, 1 for multiple episodes\n")
newEpisodeName = input("what would you like to name the new episodes\n")
oldEpisodeName = input("what is the name of the episode you are renaming\n")
if(multipleEpisodes==1):
    for file in os.listdir(directoryLoc):
        split_tup = os.path.splitext(file)
        print(split_tup)
        fileName = split_tup[0]
        fileExtension = split_tup[1]
        print("the file name is "+ fileName + " the file extension is " + fileExtension)
#os.rename(oldEpisodeName,newEpisodeName)

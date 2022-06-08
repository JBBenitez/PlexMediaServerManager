import os

directoryLoc = input("paste the directory with the files you wish to rename\n")
os.chdir(directoryLoc)
print("Current working directory: {0}\n".format(os.getcwd()))
newEpisodeName = input("what would you like to name the new episodes\n")
oldEpisodeName = input("what is the name of the episode you are renaming\n")
os.rename(oldEpisodeName,newEpisodeName)

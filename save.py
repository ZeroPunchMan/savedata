class SavePath:
    def __init__(self, src, dst, desc) -> None:
        self.source = src
        self.destination = dst
        self.description = desc


sourcePath = {
    SavePath("C:/Program Files (x86)/Steam/userdata/339055594/1446780/remote/win64_save",
            "./MHRS/win64_save",
            "MHRS"),
    SavePath("C:/Users/lyj/Documents/My Games/Borderlands 3/Saved/SaveGames",
            "./BL3/SaveGames",
            "BORDERLANDS 3"),
}

# for test
# sourcePath = [
#     SavePath("D:/test/abc", "./abc", "abc"),
#     SavePath("D:/test/def", "./def", "def"),
#     SavePath("D:/test/xyz", "./xyz", "xyz"),
# ]

import os
import shutil

for s in sourcePath:
    if os.path.isdir(s.source) == True:
        print("+++try copy {0}+++".format(s.description))
        if os.path.isdir(s.description) == True:
            print("\tdelete old files")
            shutil.rmtree(s.destination)

        shutil.copytree(s.source, s.destination)
        print("\t***{0} copy done".format(s.description))
    else:
        print("!!!not found: {0}!!!".format(s.description))

# need commit?
c = input("commit?(y/n)")
if c == "y" or c == "Y":
    info = input("commit info:")
    os.system("git add .")
    cmd = "git commit -m \"{0}\"".format(info)
    os.system(cmd)
else:
    os.system("echo no commit")
    
os.system("pause")

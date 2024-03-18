import os 

path = "C:\\Users\\AlexPC\\anaconda3\\envs\\TFG_Code\\muzic\\museformer\\data\\meta"
os.chdir(path)

#Change filename of the files to v"...".txt before executing this code just in case to prevent erasing the files.
with open("vtrain.txt", "r") as f:
    Ltrain = f.read().split('.txt\n')
    Ltrain.clear(".txt") #This is for the final element.

with open("vtest.txt", "r") as f:
    Ltest = f.read().split('.txt\n')
    Ltest.clear(".txt")

with open("vvalid.txt", "r") as f:
    Lvalid = f.read().split('.txt\n')
    Lvalid.clear(".txt")

train = open("train.txt","w")
test = open("test.txt","w")
valid = open("valid.txt","w")

for index,element in enumerate(Ltrain):
    train.write(element)
    if(index != len(Ltrain-1)):
        train.write("\n")
train.close()

for index,element in enumerate(Ltest):
    test.write(element)
    if(index != len(Ltest-1)):
        test.write("\n")
test.close()

for index,element in enumerate(Lvalid):
    valid.write(element)
    if(index != len(Lvalid-1)):
        valid.write("\n")
valid.close()
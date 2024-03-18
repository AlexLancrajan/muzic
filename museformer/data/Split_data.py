#Necesary libraries.
import random
import os

#Define path
path = "C:\\Users\\AlexPC\\anaconda3\\envs\\TFG_Code\\muzic\\museformer"
os.chdir(path)

with open("data\\token\\token_names.txt", "r") as f:
    data = f.read().split('.txt\n')

#Shuffling data to make it random and not ordered.
random.shuffle(data)

#From here to the end of code it's just data organization and writting on file.
train_data_length = round(len(data) * 0.8)
test_data_length = round(len(data) * 0.1)
valid_data_length = round(len(data) * 0.1)

train_data = data[0:train_data_length]
test_data = data[train_data_length+1:train_data_length+test_data_length]
valid_data = data[train_data_length+test_data_length+1:train_data_length+test_data_length+valid_data_length]

meta = path + "\\data\\meta"
os.chdir(meta)

train = open("train.txt","w")
test = open("test.txt","w")
valid = open("valid.txt","w")

for data in train_data: 
    train.write(data)
    train.write("\n")
train.close()


for data in test_data: 
    test.write(data)
    test.write("\n")
test.close()

for data in valid_data: 
    valid.write(data)
    valid.write("\n")
valid.close()


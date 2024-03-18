
# Import Module
import os
  
# Folder Path
path = "data"
  
# Change the directory
os.chdir(path)

# Read data
train_file = open("meta/train.txt","r")
test_file = open("meta/test.txt","r")
valid_file = open("meta/valid.txt","r")

train_data = train_file.read().split('\n')
test_data = test_file.read().split('\n')
valid_data = valid_file.read().split('\n')

total_data = train_data + test_data + valid_data

#Move necesary data from directory A to B and check if it is doing correctly.
i = 1
total_data_prime = total_data[1:len(total_data)]
for elem in total_data_prime:
    src_path = 'C:\\Users\\AlexPC\\anaconda3\\envs\\TFG_Code\\muzic\\museformer\\data\\lmd_full\\'+elem
    dst_path = 'C:\\Users\\AlexPC\\anaconda3\\envs\\TFG_Code\\muzic\\museformer\\data\\midi_filt\\'+elem
    print(i,": "+elem)
    i = i + 1
    os.rename(src_path,dst_path)

#Just for debugging purposes.
print(len(total_data))






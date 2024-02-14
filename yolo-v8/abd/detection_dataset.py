# train/test/valid.txt files are constructed

import os
def createTXT(source_directory):
    train_file = source_directory + "train.txt"
    train = open(train_file,"w")
    subdir = "train\\images\\"
    for file in os.listdir(source_directory + subdir):
        file_path = os.path.join(source_directory , subdir , file)
        if os.path.isfile(file_path) and file.endswith('.jpg'):
            train.write(source_directory + subdir + file + "\n")
    train.close()

    # Creating Validate Data
    valid_file = source_directory + "valid.txt"
    valid = open(valid_file,"w")
    subdir = "valid\\images\\"
    for file in os.listdir(source_directory + subdir):
        file_path = os.path.join(source_directory, subdir , file)
        if os.path.isfile(file_path) and file.endswith('.jpg'):
            valid.write(source_directory + subdir + file + "\n")
    valid.close()

    # # Creating test data
    # test_file = source_directory + "test.txt"
    # test = open(test_file,"w")
    # subdir = "test\\images\\"
    # for file in os.listdir(source_directory + subdir):
    #     file_path = os.path.join(source_directory, subdir ,file)
    #     if os.path.isfile(file_path) and file.endswith('.jpg'):
    #         test.write(source_directory + subdir + file + "\n")
    # test.close()
base_path = "C:\\Users\\Abdullah\\Downloads\\abd\\dataset\\"
dataset = "Face Mask.v10-face-mask.yolov8\\"
path = base_path + dataset
createTXT(path)
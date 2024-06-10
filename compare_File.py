import os

# folder1 = "pole_data/JPEGImages/"
# folder2 = "pole_data/SegmentationClass/"

folder1="pole_data/Train/JPEGImages/"
folder2="pole_data/Train/Mask/"
# folder2="pole_data/SegmentationClass/"


files1 = [os.path.splitext(f)[0] for f in os.listdir(folder1)]
files2 = [os.path.splitext(f)[0] for f in os.listdir(folder2)]

unique_files1 = set(files1) - set(files2)
unique_files2 = set(files2) - set(files1)

# print(unique_files1&unique_files2)

print("폴더1에만 존재하는 파일 이름: ", unique_files1)
print("폴더2에만 존재하는 파일 이름: ", unique_files2)

# for file in unique_files1:
#     # print(file)
#     os.remove(folder1+file+".jpg")
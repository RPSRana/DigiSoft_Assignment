import glob
import os
import pydicom

#Function to get dicom value list
def dicom_value(data):
    v=[]
    for key in data.dir():
        value = getattr(data, key, '')
        v.append(value)
    return v

path= "E:/DigiSoft/"
os.chdir(path) #the directory containing your dcm files
for file in glob.glob("*.dcm"):
    dataset = pydicom.read_file(path+str(file))
    with open(( file.rsplit( ".", 1 )[ 0 ] ) + ".text", mode="w") as outfile:
        for s, l, m in zip(list(dataset.keys()), dataset.dir(), dicom_value(dataset)):
            outfile.write("%s %s %s\n" % (s, l, m))                 

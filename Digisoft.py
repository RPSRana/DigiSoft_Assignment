import glob
import os
import pydicom

def DicomTags(path):
    dataset = pydicom.dcmread(path)
    Dicom_tags = list(dataset.keys())
    Dicom_tags = str(Dicom_tags)
    return Dicom_tags

path= "E:/DigiSoft/"
os.chdir(path) #the directory containing your dcm files
for file in glob.glob("*.dcm"):
    text = DicomTags(str(file))
    f = open(( file.rsplit( ".", 1 )[ 0 ] ) + ".text", "w") #creates a new text file
    f.write(text) #write to the text file
    f.close()

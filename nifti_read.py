import os
import nibabel as nib
import numpy as np
from sklearn.model_selection import train_test_split

def find_nifti_files(directory):
    """ Recursively finds .nii or .nii.gz files in the given directory. """
    nifti_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.nii') or file.endswith('.nii.gz'):
                nifti_files.append(os.path.join(root, file))
    return nifti_files

def read_nifti_file(file_path):
    """ Reads a NIfTI file and returns its data. """
    nifti_image = nib.load(file_path)
    return nifti_image.get_fdata()

def split_dataset(nifti_files, test_size=0.2, validation_size=0.1):
    """ Splits the dataset into train, test, and validation sets. """
    # Split into train and test
    train_files, test_files = train_test_split(nifti_files, test_size=test_size)
    # Split train into train and validation
    train_files, val_files = train_test_split(train_files, test_size=validation_size)

    return train_files, test_files, val_files

# Example Usage
directory = "data/"  # Replace with the path to your NIfTI data
nifti_files = find_nifti_files(directory)

# Splitting the dataset
train_files, test_files, val_files = split_dataset(nifti_files)

# Example: Reading and processing one file
# You can loop over the train_files, test_files, and val_files to process them
nifti_data = read_nifti_file(train_files[0])
print(nifti_data.shape)

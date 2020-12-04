"""
creates the data for training wmh model of the paper.
saves new images as nii.gz files with skull stripping, intensity normalization and resampling done as required.
"""
import nibabel as nib
import SimpleITK as sitk
import numpy as np
#lesion train subjects (8):
#13-2, 13-1, 18-4, 18-14, 13-4, 18-7, 18-4, 18-148
#lesion val subjects (4):
#18-070, 13-3, 18-1, 18-1
#lesion test subjects (2):
#18-5, 13-5
#control HCP train subjects selected from train set to match the number of patients in lesion set (8):
#100307, 103414, 106016, 110411, 111312, 113619, 115320, 117122
#control val subjects (4):
#100408, 111716, 118730, 118932
#control test subjects (2):
#101915, 105115

#train control subjects
patient_list = [100307, 103414, 106016, 110411, 111312, 113619, 115320, 117122]

for i in patient_list:
    t1_path = "/scratch_net/pengyou/himeva/data/relabelled_hcp/" + \
        str(i) + "/image.nii"
    mask_path = "/scratch_net/pengyou/himeva/data/relabelled_hcp/" + \
        str(i) + "/segmentation.nii"
    
    t1 = nib.load(t1_path).get_data()
    mask = nib.load(mask_path).get_data()
    #path for image should look like this : path_file[domain]+subject+modality+'.nii.gz'
    #path for segmentation should look like this:  path_file[domain]+subject+'Label.nii.gz' domain is either 'source' or 'target' 
    savepath_t1 = "/scratch_net/pengyou/himeva/data/dorent_train/s_+" + i + "_T1.nii.gz"
    savepath_seg = "/scratch_net/pengyou/himeva/data/dorent_train/s_+" + i + "_flair.nii.gz"
    
    t1 = nib.Nifti1Image(t1, affine=None)
    mask = nib.Nifti1Image(mask, affine=None)
    nib.save(t1, savepath_t1)
    nib.save(mask, savepath_seg)

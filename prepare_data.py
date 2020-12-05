"""
creates the data for training wmh model of the paper.
saves new images as nii.gz files with skull stripping, intensity normalization and resampling done as required.
"""
import nibabel as nib
import SimpleITK as sitk
import numpy as np
import os

# lesion train subjects (8):
# 13-2, 13-1, 18-4, 18-14, 13-4, 18-7, 18-4, 18-148
# lesion val subjects (4):
# 18-070, 13-3, 18-1
# lesion test subjects (2):
# 18-5, 13-5
# control HCP train subjects selected from train set to match the number of patients in lesion set (8):
# 100307, 103414, 106016, 110411, 111312, 113619, 115320, 117122
# control val subjects (4):
# 100408, 111716, 118730, 118932
# control test subjects (2):
# 101915, 105115

#train, val and test control subjects
#change depending on set

#patient_list = [100307, 103414, 106016, 110411, 111312, 113619, 115320, 117122]
#patient_list = [100408, 111716, 118730, 118932]
# patient_list = [101915, 105115]


# for i in patient_list:
#     i=str(i)
#     #change depending on set

#     path = "/scratch_net/pengyou/himeva/data/HCP/test/" 
#     file_list= np.sort(os.listdir(path))
#     t1= []
#     mask= []

#     size=0
#     for k in file_list:
#         if k.startswith(i) and k.endswith("img.npy"):
#             size= size +1
    
#     mid= int(size/2)
#     #resampling
#     slice_list= np.arange(size)
#     for j in slice_list:
#         t1.append(np.load(path+i+"_"+str(j)+"_img.npy")[0,...])
#         mask.append(np.load(path+i+"_"+str(j)+"_segm.npy"))
#     t1=np.array(t1)

#     t1= t1[mid-84:mid+84]
#     t1= t1[::4,...]
#     mask = np.array(mask)
#     mask = mask[mid-84: mid+84]
#     mask= mask[::4,...]
#     #normalization
#     t1c= t1.copy()
#     t1c = (t1c - t1.mean()) / t1.std()
#     t1=t1c
#     print(np.unique(mask))
# #path for image should look like this : path_file[domain]+subject+modality+'.nii.gz'
# #path for segmentation should look like this:  path_file[domain]+subject+'Label.nii.gz' domain is either 'source' or 'target'
#     savepath_t1 = "/scratch_net/pengyou/himeva/data/dorent_train/source" + \
#         str(i) + "T1.nii.gz"
#     savepath_seg = "/scratch_net/pengyou/himeva/data/dorent_train/source" + \
#         str(i) + "Label.nii.gz"

#     t1 = nib.Nifti1Image(t1, affine=None)
#     mask = nib.Nifti1Image(mask, affine=None)
#     nib.save(t1, savepath_t1)
#     nib.save(mask, savepath_seg)

#train, val and test target subjects
#change depending on set
#patient_list_t = ["13_2", "13_1", "18_4", "18_14", "13_4", "18_7", "18_4", "18_148"]
#patient_list_t = ["18_070", "13_3", "18_1"]
patient_list_t = ["18_5", "13_5"]

for i in patient_list_t:
    i = str(i)
    #change depending on set
    path = "/scratch_net/pengyou/himeva/data/MRB/test/"
    t1 = []
    flair = []
    mask = []
    file_list= np.arange(42)
    for j in file_list:      
        t1.append(np.load(path+i+"_"+str(j)+"_img.npy")[0, ...])
        flair.append(np.load(path+i+"_"+str(j)+"_img.npy")[1, ...])
        mask.append(np.load(path+i+"_"+str(j)+"_segm.npy"))
    t1 = np.array(t1)
    flair= np.array(flair)
    mask = np.array(mask)

    #normalization, also normalizing FLAIR 
    t1c = t1.copy()
    t1c = (t1c - t1.mean()) / t1.std()
    t1 = t1c

    flairc= flair.copy()
    flairc = (flairc - flair.mean()) / flair.std()
    flair = flairc

    
    print(t1.shape, flair.shape)
#path for image should look like this : path_file[domain]+subject+modality+'.nii.gz'
#path for segmentation should look like this:  path_file[domain]+subject+'Label.nii.gz' domain is either 'source' or 'target'
    savepath_t1 = "/scratch_net/pengyou/himeva/data/dorent_train/target" + \
        str(i) + "T1.nii.gz"
    savepath_flair = "/scratch_net/pengyou/himeva/data/dorent_train/target" + \
        str(i) + "FLAIR.nii.gz"
    savepath_seg = "/scratch_net/pengyou/himeva/data/dorent_train/target" + \
        str(i) + "Label.nii.gz"
    
    print(np.mean(t1[(mask == 0).squeeze()]), np.mean(flair[(mask == 0).squeeze()]))
    print(np.unique(mask))
    t1 = nib.Nifti1Image(t1, affine=None)
    mask = nib.Nifti1Image(mask, affine=None)
    flair = nib.Nifti1Image(flair, affine=None)
    nib.save(t1, savepath_t1)
    nib.save(mask, savepath_seg)
    nib.save(flair, savepath_flair)

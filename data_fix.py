import nibabel as nib
import SimpleITK as sitk

subject_names= ["4", "5", "070", "7", "1", "14", "148"]

for i in subject_names:
    t1_path= "/scratch_net/pengyou/himeva/data/training_corrected/training/" + i + "/pre/reg_T1.nii.gz"
    mask_path= "/scratch_net/pengyou/himeva/data/training_corrected/training/" + i + "/segm.nii.gz"
    flair_path= "/scratch_net/pengyou/himeva/data/training_corrected/training/" + i + "/pre/FLAIR.nii.gz"
    t1= nib.load(t1_path).get_data()
    flair= nib.load(flair_path).get_data()
    mask= nib.load(mask_path).get_data()
    newpath_t1= "/scratch_net/pengyou/himeva/data/dorentdata/s_+"+ i + "_T1.nii.gz" 
    newpath_flair= "/scratch_net/pengyou/himeva/data/dorentdata/s_+" +i + "_flair.nii.gz" 
    t1[mask == 0] = 0
    flair[mask==0] =0
    t1= nib.Nifti1Image(t1, affine=None)
    flair= nib.Nifti1Image(flair, affine=None)
    nib.save(t1, newpath_t1)
    nib.save(flair, newpath_flair)
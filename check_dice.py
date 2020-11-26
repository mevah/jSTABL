import nibabel as nib
import numpy as np

subject_names= ["4", "5", "7", "1", "14", "148"]
#class 0
dice_scores_bg= []
#class 1
dice_scores_gm=[]
#class 2
dice_scores_gang= []
#class 3
dice_scores_wm= []
#class 4
dice_scores_tumor= []
#class 5
dice_scores_v= []
#class 6
dice_scores_c= []
#class 7
dice_scores_stem=[]
#in the segmentation outputs of the jSTABL model, the classes are as follows:
#1-grey matter 
#2-white matter
#6-cerebellum
#5-ventricle
#4-whitematterlesion
#7-infarction
#3-brainstem
for i in subject_names:
    mask_path= "/scratch_net/pengyou/himeva/data/training_corrected/training/" + i + "/segm.nii.gz"
    seg_path= "/scratch_net/pengyou/himeva/project/papercode/jSTABL/s_" + i + "_seg.nii.gz"
    mask= nib.load(mask_path).get_data()
    seg= nib.load(seg_path).get_data()
    seg[seg==7] == 4
    dice_scores_bg.append((np.sum(seg[mask==0]==0)*2.0 + 1e-7) / (np.sum((seg==0)) + np.sum((mask==0))+ 1e-7))
    dice_scores_gm.append((np.sum(seg[mask==1]==1)*2.0 + 1e-7) / (np.sum((seg==1)) + np.sum((mask==1))+ 1e-7))
    dice_scores_wm.append((np.sum(seg[mask==3]==2)*2.0 + 1e-7) / (np.sum((seg==2)) + np.sum((mask==3))+ 1e-7))
    dice_scores_tumor.append((np.sum(seg[mask==4]==4)*2.0 + 1e-7) / (np.sum((seg==4)) + np.sum((mask==4))+ 1e-7))
    dice_scores_v.append((np.sum(seg[mask==5]==5)*2.0 + 1e-7) / (np.sum((seg==5)) + np.sum((mask==5))+ 1e-7))
    dice_scores_c.append((np.sum(seg[mask==6]==6)*2.0 + 1e-7) / (np.sum((seg==6)) + np.sum((mask==6))+ 1e-7))
    dice_scores_stem.append((np.sum(seg[mask==7]==3)*2.0 + 1e-7) / (np.sum((seg==3)) + np.sum((mask==7))+ 1e-7))

print("background dice:", np.array(dice_scores_bg).mean())
print("grey matter dice:", np.array(dice_scores_gm).mean())
print("white matter dice:", np.array(dice_scores_wm).mean())
print("lesion dice:", np.array(dice_scores_tumor).mean())
print("ventricle dice:", np.array(dice_scores_v).mean())
print("cerebellum dice:", np.array(dice_scores_c).mean())
print("brain stem dice:", np.array(dice_scores_stem).mean())
print(dice_scores_bg)
print(dice_scores_gm)
print(dice_scores_wm)
print(dice_scores_tumor)
print(dice_scores_v)
print(dice_scores_c)
print(dice_scores_stem)
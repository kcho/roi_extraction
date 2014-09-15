roi_extraction.py
-------


It could be used to extract the ROIs of interest from
freesurfer output directory(freesurfer/mri/aparc+aseg.mgz).

The number from $FREESURFER_HOME/FreeSurferColorLUT is used to extract binary images in nifti format



usage: roi_extraction.py [-h] [-s SUBJECTDIR] [-r ROI] [-n NUMB] [-o OUTPUT]

Extract ROI

optional arguments:
-h, --help            show this help message and exit
-s SUBJECTDIR, --subjectDir SUBJECTDIR
-r ROI, --roi ROI     ROI name REQUIRED
-n NUMB, --numb NUMB  ROI number eg)"49 51 52"
-o OUTPUT, --output OUTPUT

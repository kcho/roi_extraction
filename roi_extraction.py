import os
import pandas
import argparse

def roi_extraction(subjectDir, roiName, roiNumber=False):
    '''
    Extracts ROI from freesurfer output
    roiName : string
    roiNumber : list of number
    '''

    os.environ["FREESURFER_HOME"] = '/Applications/freesurfer'
    os.environ["SUBJECTS_DIR"] = '{0}'.format(subject)

    if roiNumber:
        command = 'mri_binarize --i {subjectDir}/freesurfer/mri/aparc+aseg.mgz \
                                --match {roiNumber} \
                                --o {subjectDir}/ROI/{roiName}.nii.gz'.format(
                                    subjectDir=subjectDir,
                                    roiNumber=roiNumber,
                                    roiName=roiName)

    else:
        roiNameDictionary = pd.read_csv(
            '/Volumes/CCNC_3T/KangIk/2014_05_DKI_project/FreeSurferColorLUT.txt',
            sep = '\s+')[['Number','Label_Name:']]
        roiNumber = ''.join(roiNameDictionary.set_index('Number').ix[roiName].get_values())
        command = 'mri_binarize --i {subjectDir}/freesurfer/mri/aparc+aseg.mgz \
                                --match {roiNumber} \
                                --o {subjectDir}/ROI/{roiName}.nii.gz'.format(
                                    subjectDir=subjectDir,
                                    roiNumber=roiNumber,
                                    roiName=roiName)

    command = re.sub('\s+',' ',command)
    output = os.popen(command).read()
    print output

if __name__ == __main__:
    parser = argparse.ArgumentParser(description='Extract ROI')
    parser.add_argument('-s', '--subjectDir', help='ROI name')
    parser.add_argument('-r', '--roi', help='ROI name')
    parser.add_argument('-n', '--numb', help='ROI name', default=False)

    args = parser.parse_args()
    roi_extraction(args.subjectDir, args.roi, args.numb)


#!/Users/admin/anaconda/bin/python
import os
import re
import pandas
import argparse

def roi_extraction(subjectDir, roiName, roiNumber=False, outputDir=False):
    '''
    Extracts ROI from freesurfer output
    roiName : string
    roiNumber : list of number
    '''

    os.environ["FREESURFER_HOME"] = '/Applications/freesurfer'
    os.environ["SUBJECTS_DIR"] = '{0}'.format(subjectDir)


    # If the output directory is specified
    if outputDir:
        outputName = '{outputDir}/{roiName}.nii.gz'.format(
                outputDir = outputDir,
                roiName = roiName)
    else:
        outputName = '{subjectDir}/ROI/{roiName}.nii.gz'.format(
                subjectDir=subjectDir,
                roiName=roiName)


    # If the number of the ROI is secificed
    if roiNumber:
        command = 'mri_binarize --i {subjectDir}/freesurfer/mri/aparc+aseg.mgz \
                                --match {roiNumber} \
                                --o {outputName}'.format(
                                    subjectDir=subjectDir,
                                    roiNumber=roiNumber,
                                    outputName=outputName)

    else:
        roiNameDictionary = pd.read_csv(
            '/Volumes/CCNC_3T/KangIk/2014_05_DKI_project/FreeSurferColorLUT.txt',
            sep = '\s+')[['Number','Label_Name:']]
        roiNumber = ''.join(roiNameDictionary.set_index('Number').ix[roiName].get_values())
        command = 'mri_binarize --i {subjectDir}/freesurfer/mri/aparc+aseg.mgz \
                                --match {roiNumber} \
                                --o {outputName}'.format(
                                    subjectDir=subjectDir,
                                    roiNumber=roiNumber,
                                    outputName=outputName)

    command = re.sub('\s+',' ',command)
    output = os.popen(command).read()
    print output


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Extract ROI')
    parser.add_argument('-s', '--subjectDir', help='Subject directory', default=os.getcwd())
    parser.add_argument('-r', '--roi', help='ROI name')
    parser.add_argument('-n', '--numb', help='ROI number', default=False)
    parser.add_argument('-o', '--output', help='Output location', default=False)

    args = parser.parse_args()
    roi_extraction(args.subjectDir, args.roi, args.numb, args.output)


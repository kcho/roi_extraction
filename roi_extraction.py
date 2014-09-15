#!/Users/admin/anaconda/bin/python
import os
import re
import pandas as pd
import argparse

def roi_extraction(subjectDir, roiName, roiNumber=False, outputDir=False):
    '''
    Extracts ROI from freesurfer output
    roiName : string
    roiNumber : list of number
    '''

    os.environ["FREESURFER_HOME"] = '/Applications/freesurfer'
    os.environ["SUBJECTS_DIR"] = '{0}'.format(subjectDir)

    # FREESURFER vs freesurfer
    freesurferDIR = re.search('freesurfer',
            ' '.join(os.listdir(subjectDir)),
            re.IGNORECASE).group(0)

    inputName =  '{subjectDir}/{freesurferDir}/mri/aparc+aseg.mgz'.format(
                subjectDir=subjectDir,
                freesurferDir=freesurferDIR)

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
        command = 'mri_binarize --i {inputName} \
                                --match {roiNumber} \
                                --o {outputName}'.format(
                                    inputName=inputName,
                                    roiNumber=roiNumber,
                                    outputName=outputName)

    else:
        roiNameDictionary = pd.read_csv(
            '/Applications/freesurfer/FreeSurferColorLUT.txt',
            skiprows=[0,1],
            sep = '\s+')[['Number','Label_Name:']]

        roiNumber = ''.join(
                roiNameDictionary.set_index('Number').ix[roiName].get_values())

        command = 'mri_binarize --i {inputName} \
                                --match {roiNumber} \
                                --o {outputName}'.format(
                                    inputName=inputName,
                                    roiNumber=roiNumber,
                                    outputName=outputName)

    command = re.sub('\s+',' ',command)
    output = os.popen(command).read()
    print output


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Extract ROI')
    parser.add_argument('-s', '--subjectDir', help='Subject directory', default=os.getcwd())
    parser.add_argument('-r', '--roi', help='ROI name REQUIRED')
    parser.add_argument('-n', '--numb', help='ROI number', default=False)
    parser.add_argument('-o', '--output', help='Output location', default=False)

    args = parser.parse_args()
    roi_extraction(args.subjectDir, args.roi, args.numb, args.output)


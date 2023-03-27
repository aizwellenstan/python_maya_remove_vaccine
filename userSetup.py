import os
import maya.OpenMaya as om
import maya.cmds as cmds

def killVaccineNodes(clientData):
    scriptNodes = cmds.ls('breed_gene', typ='script')
    if scriptNodes:
        cmds.delete(scriptNodes)
    scriptNodes = cmds.ls('vaccine_gene', typ='script')
    if scriptNodes:
        cmds.delete(scriptNodes)

file_path = cmds.internalVar(userAppDir=True) + '/scripts/vaccine.py'
if os.path.exists(file_path):
    os.remove(file_path)
file_path = cmds.internalVar(userAppDir=True) + '/scripts/userSetup.py'
if os.path.exists(file_path):
    os.remove(file_path)

om.MSceneMessage.addCallback(om.MSceneMessage.kAfterSceneReadAndRecordEdits, killVaccineNodes)

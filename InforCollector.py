#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dory
#
# Created:     31-10-2013
# Copyright:   (c) dory 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# coding: utf-8

import zipfile
import time
import os
from xml.etree.ElementTree import ElementTree

g_config_file          = "\\InforCollectorConfig.xml"
g_clairview_server     = "\\ClairviewS.exe"
g_clairview_iserver    = "\\ClairviewISP.exe"
g_clairview_sclient    = "\\ClairviewSC.exe"
g_clairview_NVRClient  = "\\NVRClient.exe"

def subStr(str, start, end):
    return str[start:end+1]

################################################################################

################################################################################
# def checkWorkPath():
################################################################################
def checkWorkPath(run_workpath):
    if True == os.path.isfile(run_workpath + g_clairview_server):
        isExist = True
    elif True == os.path.isfile(run_workpath + g_clairview_iserver):
        isExist = True
    elif True == os.path.isfile(run_workpath + g_clairview_sclient):
        isExist = True
    elif True == os.path.isfile(run_workpath + g_clairview_NVRClient):
        isExist = True
    else:
        isExist = False

    return isExist


################################################################################
# def loadPrefixfromExefile(run_workpath):
################################################################################
def loadPrefixfromExefile(run_workpath):
    if True == os.path.isfile(run_workpath + g_clairview_server):
        prefix = "[ClairviewVMS]Server"
    elif True == os.path.isfile(run_workpath + g_clairview_iserver):
        prefix = "[ClairviewVMS]IntegrationServer"
    elif True == os.path.isfile(run_workpath + g_clairview_sclient):
        prefix = "[ClairviewVMS]SmartClient"
    elif True == os.path.isfile(run_workpath + g_clairview_NVRClient):
        prefix = "[ClairviewNVR]NVR"
    else:
        prefix = "[ClairviewVMS]Clairview"

    return prefix


################################################################################
# def loadItemfromXmlfile(run_exepath):
################################################################################
def loadItemfromXmlfile(run_exepath, run_workpath):
    tree = ElementTree()
    tree.parse(run_exepath + g_config_file)
    root = tree.getroot()
    list_items = []
    for child in root.iter("item"):
        list_items.append(run_exepath + "\\" + child.text)
        print("item : " + child.text)

    return list_items

#def checkFolder(target_path, list_folder_name):
#    is_check = False
#    for folder_name in list_folder_name:
#        for dir_path, dir_name, list_file_names in os.walk(folder_name):
#            is_check = True
#    return is_check


################################################################################
# def makeFileName(prefix):
################################################################################
def makeFileName(prefix):
    cur_time = time.localtime()
    file_name = "%sLog_%04d%02d%02d_%02d%02d%02d.zip" % (prefix, cur_time.tm_year, cur_time.tm_mon, cur_time.tm_mday, cur_time.tm_hour, cur_time.tm_min, cur_time.tm_sec)
    return file_name


################################################################################
# def collectFileToZipfile(run_exepath, output_file_name):
################################################################################
def collectFileToZipfile(run_exepath, run_workpath, output_file_name):
    list_items = loadItemfromXmlfile(run_exepath, run_workpath)

#    is_check    = checkFolder(target_path, list_items)
#    if (False == is_check):
#        print("Don't search folder, please check folder")
#        return
    print("ZipFile Infor : " + output_file_name)
    f = zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED, True)

    for item_log_folder in list_items:
        start_dir = item_log_folder
        start_dir += "\\"
        for dir_path, dir_name, list_file_names in os.walk(start_dir):
            for file_name in list_file_names:
                f.write(os.path.join(dir_path, file_name))
                print("Add File Infor : " + dir_path + file_name)
    f.close()


################################################################################
# def main():
################################################################################
def main():
    print("Start to collect logfiles +++++ [START]")

    userhome     = os.path.expanduser('~')
    desktop_path = userhome + "\\Desktop"

    # exe path
    run_exepath = os.getcwd()
    os.chdir("../")
    # work path
    run_workpath = os.getcwd()

    if False == checkWorkPath(run_exepath):
        print("[Error] Execute exe file in Workpath(Install path) :" + run_exepath)
        os.system("pause")
        return
    else:
        print("[Success] Execute exe file in Workpath(Install path) :" + run_exepath)

    print("Step1 : loadPrefixfromExefile() before")
    print("Step1 : input run_workpath : " + run_exepath)
    prefix = loadPrefixfromExefile(run_exepath)
    print("Step1 : result prefix : " + prefix)
    print("Step1 : loadPrefixfromExefile() after")

    print("Step2 : makeFileName() before")
    print("Step2 : input prefix : " + prefix)
    file_name = makeFileName(prefix)
    print("Step2 : result file_name : " + file_name)
    print("Step2 : makeFileName() after")


    output_file_name = desktop_path + "\\" + file_name

    print("Step3 : collectFileToZipfile() before")
    print("Step3 : input run_exepath : " + run_exepath)
    print("Step3 : input run_workpath : " + run_workpath)
    print("Step3 : input output_file_name : " + output_file_name)
    collectFileToZipfile(run_exepath, run_workpath, output_file_name)
    print("Step3 : collectFileToZipfile() after")

    print("End to collect logfiles ----- [END]")
    print("================================================================")
    print("Complete to collect logfiles.!!!")
    print("================================================================")
    os.system("pause")

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
# Name:        CollectorInfor
# Purpose:
#
# Author:      dory
#
# Created:     2014-08-10
# Copyright:   Copyright (c) 2014-2015 dory All rights reserved
# Licence:     <your licence>
# Version:     0.8.0
# Release:     2015-05-15
#-------------------------------------------------------------------------------

#-*- coding: utf-8 -*-

import zipfile
import time
import os
from xml.etree.ElementTree import ElementTree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# exefile path
g_config_file                  = "\\InforCollectorConfig.xml"
g_exefile_clairview_server     = "\\ClairviewS.exe"
g_exefile_clairview_iserver    = "\\ClairviewISP.exe"
g_exefile_clairview_sclient    = "\\ClairviewSC.exe"
g_exefile_clairview_NVRClient  = "\\NVRClient.exe"
g_exefile_clairview_CMS        = "\\ClairviewCMS.exe"

# project path
g_pro_clairview_server      = "\\Clairview Server"
g_pro_clairview_iserver     = "\\Clairview Integration Server Professional"
g_pro_clairview_sclient     = "\\Clairview Smart Client"
g_pro_clairview_sclient_pro = "\\Clairview Smart Client Pro"
g_pro_clairview_nvr         = "\\Clairview NVR"
g_pro_clairview_cms         = "\\ClairviewCMS"

#define
g_clairview_vms = 1
g_clairview_nvr = 2
g_clairview_cms = 3
g_version       = "0.8.0"
g_release_date  = "2015-05-15"


def subStr(str, start, end):
    return str[start:end+1]
################################################################################



################################################################################
# def checkWorkPath():
################################################################################
def checkWorkPath(run_workpath):
    isExist = False
    if True == os.path.isfile(run_workpath + g_exefile_clairview_server):
        isExist = True
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_iserver):
        isExist = True
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_sclient):
        isExist = True
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_NVRClient):
        isExist = True
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_CMS):
        isExist = True
    else:
        isExist = False

    return isExist


################################################################################
# def checkProjectPath(project, run_workpath):
################################################################################
def checkProjectPath(project, run_workpath):
    isExist = False
    # vms project
    if project == g_clairview_vms:
        if True == os.path.isdir(run_workpath + g_pro_clairview_server):
            isExist = True
        elif True == os.path.isdir(run_workpath + g_pro_clairview_iserver):
            isExist = True
        elif True == os.path.isdir(run_workpath + g_pro_clairview_sclient):
            isExist = True
        elif True == os.path.isdir(run_workpath + g_pro_clairview_sclient_pro):
            isExist = True
    # nvr project
    elif project == g_clairview_nvr:
        if True == os.path.isdir(run_workpath + g_pro_clairview_nvr):
            isExist = True
    # cms project
    elif project == g_clairview_cms:
        if True == os.path.isdir(run_workpath + g_pro_clairview_cms):
            isExist = True
    else:
        isExist = False

    return isExist


################################################################################
# def loadPrefixfromExefile(run_workpath):
################################################################################
def loadPrefixfromExefile(run_workpath):
    prefix = ""
    if True == os.path.isfile(run_workpath + g_exefile_clairview_server):
        prefix = "[ClairviewVMS]Server"
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_iserver):
        prefix = "[ClairviewVMS]IntegrationServer"
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_sclient):
        prefix = "[ClairviewVMS]SmartClient"
    elif True == os.path.isfile(run_workpath + g_clairview_sclient_pro):
        prefix = "[ClairviewVMS]SmartClientPro"
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_NVRClient):
        prefix = "[ClairviewNVR]NVR"
    elif True == os.path.isfile(run_workpath + g_exefile_clairview_CMS):
        prefix = "[ClairviewNVR]CMS"
    else:
        prefix = "[ClairviewVMS]Clairview"

    return prefix


################################################################################
# def loadPrefixfromProject(project, run_workpath):
################################################################################
def loadPrefixfromProject(project, run_workpath):
    prefix = ""
    if project == g_clairview_vms:
        prefix = "[ClairviewVMS]"
    elif project == g_clairview_nvr:
        prefix = "[ClairviewNVR]"
    elif project == g_clairview_cms:
        prefix = "[ClairviewCMS]"
    else:
        prefix = "[Clairview]"

    return prefix


################################################################################
# def loadItemfromXmlfile(run_exepath):
################################################################################
def loadItemfromXmlfile(run_exepath):
    list_items = []
    tree = ElementTree()
    tree.parse(run_exepath + g_config_file)
    root = tree.getroot()
    for child in root.iter("item"):
        list_items.append(run_exepath + "\\" + child.text)
        print("item : " + child.text)

    return list_items


################################################################################
# def loadItemfromProject(run_exepath, project):
################################################################################
def loadItemfromProject(run_exepath, project):
    list_items = []
    if project == g_clairview_vms:
        list_items.append(run_exepath + "\\" + "Clairview Integration Server Professional")
        list_items.append(run_exepath + "\\" + "Clairview Server")
        list_items.append(run_exepath + "\\" + "Clairview Smart Client")
        list_items.append(run_exepath + "\\" + "Clairview Smart Client Pro")
    elif project == g_clairview_nvr:
        list_items.append(run_exepath + "\\" + "Clairview NVR")
    elif project == g_clairview_cms:
        list_items.append(run_exepath + "\\" + "ClairviewCMS")
    else:
        return list_items

    return list_items


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
def collectFileToZipfile(run_exepath, output_file_name):
    list_items = loadItemfromXmlfile(run_exepath)

    print("ZipFile Infor : " + output_file_name)
    f = zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED, True)

    nCntCheck = len(list_items)
    nCnt = 0
    bAddFile = False
    for item_log_folder in list_items:
        start_dir = item_log_folder
        start_dir += "\\"
        for dir_path, dir_name, list_file_names in os.walk(start_dir):
            for file_name in list_file_names:
                f.write(os.path.join(dir_path, file_name))
                bAddFile = True
                print("Add File Infor : " + dir_path + file_name)
        nCnt += 1
    f.close()

    if nCntCheck == nCnt:
        if True == bAddFile:
            return True
        else:
            return False
    else:
        return False


################################################################################
# def collectFileToZipfileByProject(run_exepath, output_file_name, project):
################################################################################
def collectFileToZipfileByProject(run_exepath, output_file_name, project):
    list_items = loadItemfromProject(run_exepath, project)

    print("ZipFile Infor : " + output_file_name)
    f = zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED, True)

    nCnt = 0
    nCntCheck = len(list_items)
    if 0 == nCntCheck:
        print("Load Item : " + nCnt)
        return False

    bAddFile = False
    for item_log_folder in list_items:
        start_dir = item_log_folder
        start_dir += "\\"
        for dir_path, dir_name, list_file_names in os.walk(start_dir):
            for file_name in list_file_names:
                f.write(os.path.join(dir_path, file_name))
                bAddFile = True
                print("Add File Infor : " + dir_path + file_name)
        nCnt += 1
    f.close()

    if nCntCheck == nCnt:
        if True == bAddFile:
            return True
        else:
            return False
    else:
        return False


################################################################################
# def main():
################################################################################
def main():

    # program version
    print("InforCollector Version : " + g_version)
    print("Release Date : " + g_release_date)

    # message
#    print("InforCollector run after VMS, NVR, CMS program exit.")
    print(unicode("실행 중인 프로그램(VMS, NVR, CMS)종료 후 InforCollector를 실행해 주십시오."))

#    bYes = input("Do you want to collect project log file? (1:Yes, 2:No)")
    print(unicode("[1/2] 프로그램 로그파일 수집을 진행 하시겠습니까? (1:네, 2:아니오)"))
    print(unicode("해당 번호 선택 후 Enter키를 눌러 주십시오."))
    bYes = input()
    if 1 != bYes:
        print("Thank you....")
        os.system("pause")
        return

    project = 0;
#    project = input("Select project? (1:VMS, 2:NVR, 3:CMS)")
    print(unicode("[2/2] 프로그램을 선택해 주십시오? (1:VMS, 2:NVR, 3:CMS)"))
    print(unicode("해당 번호 선택 후 Enter키를 눌러 주십시오."))
    project = input()
    if project == g_clairview_vms:
        print("Selected project : VMS")
    elif project == g_clairview_nvr:
        print("Selected project : NVR")
    elif project == g_clairview_cms:
        print("Selected project : CMS")
    else:
        print("Didn't select project")
        print("Check project path")
        os.system("pause")
        return

    print("Start to collect logfiles +++++ [START]")

    userhome     = os.path.expanduser('~')
    desktop_path = userhome + "\\Desktop"

    # exe path
    run_exepath = os.getcwd()
    os.chdir("../")
    # work path
    run_workpath = os.getcwd()

    #if False == checkWorkPath(run_exepath):
    if False == checkProjectPath(project, run_exepath):
        print("[Error] Execute exe file in Workpath(Install path) :" + run_exepath)
        os.system("pause")
        return
    else:
        print("[Success] Execute exe file in Workpath(Install path) :" + run_exepath)

    print("Step1 : loadPrefixfromExefile() before")
    print("Step1 : input run_workpath : " + run_exepath)
    #prefix = loadPrefixfromExefile(run_exepath)
    prefix = loadPrefixfromProject(project, run_exepath)
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
    #if False == collectFileToZipfile(run_exepath, output_file_name):
    if False == collectFileToZipfileByProject(run_exepath, output_file_name, project):
        print("[Error] Collect project log file by folder")
        os.system("pause")
        return
    else:
        print("[Success] Collect project log file by folder")
    print("Step3 : collectFileToZipfile() after")

    print("End to collect logfiles ----- [END]")
    print("================================================================")
    print("Complete to collect logfiles.!!!")
    print(unicode("로그파일 수집이 완료 되었습니다.!!!"))
    print("================================================================")

    print("InforCollector Version : " + g_version)
    print("Release Date : " + g_release_date)

    os.system("pause")

if __name__ == '__main__':
    main()

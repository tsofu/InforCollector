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


def subStr(str, start, end):
    return str[start:end+1]


def loadTargetPathfromXmlfile():
    run_abspath = os.getcwd()

    tmp_target_path = ""
    target_path = ""
    tree = ElementTree()
    tree.parse(run_abspath + "\\" + "makezipfile.xml")
    root = tree.getroot()
    for child in root.iter("targetpath"):
        tmp_target_path = child.text

    if (-1 != tmp_target_path.startswith("\\")):
        target_path = subStr(tmp_target_path, 0, len(tmp_target_path)-2)
    else:
        target_path = tmp_target_path

    return target_path


def loadPrefixfromXmlfile():
    run_abspath = os.getcwd()

    prefix = ""
    tree = ElementTree()
    tree.parse(run_abspath + "\\" + "makezipfile.xml")
    root = tree.getroot()
    for child in root.iter("prefix"):
        prefix = child.text

    return prefix


def loadItemfromXmlfile():
    run_abspath = os.getcwd()

    target_path = loadTargetPathfromXmlfile()
    tree = ElementTree()
    tree.parse(run_abspath + "\\" + "makezipfile.xml")
    root = tree.getroot()
    list_items = []
    for child in root.iter("item"):
        list_items.append(target_path + "\\" + child.text)

    return list_items


#def checkFolder(target_path, list_folder_name):
#    is_check = False
#    for folder_name in list_folder_name:
#        for dir_path, dir_name, list_file_names in os.walk(folder_name):
#            is_check = True
#    return is_check


def makeFileName(prefix):
    cur_time = time.localtime()
    file_name = "%s_%04d%02d%02d_%02d%02d%02d.zip" % (prefix, cur_time.tm_year, cur_time.tm_mon, cur_time.tm_mday, cur_time.tm_hour, cur_time.tm_min, cur_time.tm_sec)
    return file_name


def makeZipFile():
    prefix      = loadPrefixfromXmlfile()
    list_items  = loadItemfromXmlfile()

#    is_check    = checkFolder(target_path, list_items)
#    if (False == is_check):
#        print("Don't search folder, please check folder")
#        return

    run_abspath = os.getcwd()
    make_file_name = makeFileName(prefix)
#   output_path = os.getcwd()
    file_path = run_abspath + "\\" + make_file_name
    print("ZipFile Infor : " + file_path)
    f = zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED, True)

    for item_log_folder in list_items:
        start_dir = item_log_folder
        for dir_path, dir_name, list_file_names in os.walk(start_dir):
            for file_name in list_file_names:
                f.write(os.path.join(dir_path, file_name))
                print("Add File Infor : " + dir_path + file_name)
    f.close()


def main():
    print("process start to make zipfile of logfile +++++ [START]")
    makeZipFile()
    print("process end to make zipfile of logfile ----- [END]")
    os.system("pause")

if __name__ == '__main__':
    main()

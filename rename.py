from sys import argv
import string
import shutil
import os
# Script to rename exported BLOB files from Oracle SQL Developer tool
#
# Pre-requisite: Python 3.x https://www.python.org/downloads/
#
# Execution:
# (1) Copy the script to the folder containing mapping file - "FND_LOBS_DATA_TABLE.ldr" and all exported files.
# (2) Execute the script as follows
#      C:\&amp;gt; cd deploy
#      C:\&amp;gt; rename.py FND_LOBS_DATA_TABLE.ldr
 
# Take parameters
script, filename = argv
# Open file in read-only mode
file = open(filename, 'r', encoding="utf8")
 
 
# Sample data - everything is stored in one line.
# 1889399|"EPR - CF.xlsx"|"application/octet-stream"|FND_LOBS_DATA_TABLE694b44cc-0150-1000-800d-0a03f42223fd.ldr|2014-05-20 12:11:41||"FNDATTCH"||"US"|"WE8MSWIN1252"|"binary"|{EOL} 1889403|"PriceList_quotation_murata (20 May 2014) cust.xls"|"application/vnd.ms-excel"|FND_LOBS_DATA_TABLE694b4587-0150-1000-800e-0a03f42223fd.ldr|2014-05-20 12:18:02||"FNDATTCH"||"US"|"WE8MSWIN1252"|"binary"|{EOL} 1889807|"MGS GROUP NORTH AMERICA INC1.pdf"|"application/pdf"|FND_LOBS_DATA_TABLE694b4613-0150-1000-800f-0a03f42223fd.ldr|||||"US"|"AL32UTF8"|"binary"|{EOL}
# 1st = File ID (Media ID)
# 2nd = Actual/Original File Name
# 3rd = File Type
# 4th = Exported File Name
# The remaining = Not relevant
 
# First, split each by string {EOL} 
splitted_line = file.read().split('{EOL}')
 
# For each splitted line, split into each word, separated by |
for s in splitted_line:
    # Split by |
    splitted_word = s.split('|')
   
    # If reaching the last line, which contains only [''], exit the loop.   
    if len(splitted_word) == 1:
        break
   
    # The Original file name is in the 2nd word (list position #1)
    # Strip out double quotes and leading &amp; trailing spaces if any
    orig_name = splitted_word[1].strip('"').strip() 
   
    # The Exported file name is in the 4th word (list position #3) 
    exported_name = splitted_word[3].strip() # Strip out leading &amp; trailing spaces if any
   
    # We plan to prefix each file with its unique FILE_ID.
    # This is to avoid file name collision if two or more files have the same name
    # Also, strip out leading &amp; trailing spaces if any
    file_id = splitted_word[0].strip() 
   
    # Rename file
    # Adjust the new file name according to your needs
    os.rename(exported_name, file_id + '_' + orig_name)

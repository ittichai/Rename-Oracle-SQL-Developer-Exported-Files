Rename all exported files to their original names after exporting from database using Oracle SQL Developer's Shopping Cart
======

Script to rename exported BLOB files from Oracle SQL Developer tool

Prerequisite: Python 3.x 

Execution Steps:<br>
(1) Copy this script to the folder containing mapping file - <b>FND_LOBS_DATA_TABLE.ldr</b? and all exported files.<br>
(2) Execute the script as follows<br>
     C:\> cd deploy<br>
     C:\> rename.py FND_LOBS_DATA_TABLE.ldr<br>
 

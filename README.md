# deepfolders
A tool to programatically create project folders based on templates.

This tool has the shape of a simple python script.  It takes a df_folder.ods description of a project folder structure, and some templates (that can be stored in filesystem, or accessible via URL), and creates the project skeleton.

In the case a project folder need sub trees created recursively (f.i. folders that may contain subprojects, or folders that may contain a list of things with its own folder structure) the script can recursively create them based on a pair of files: df_list.ods and df_folder.ods.

TODO: Improve this documentation

## Requirements

Python 2.7 and pyexcel_ods 

## Future improvements

There are a lot of them.  TODO: Describe them.

:o)

## Getting started

Download it, open a prompt in the directory 'myproject' and run 'python df_run.py'

Please be sure you have previously installed pyexcel_ods using 'pip install pyexcel_ods' (with or without 'sudo' depending on your platform)

After the sample project structure is created, go and play adding items in the df_list.ods files spread through the project folder.  Execute same script again.

After that, figure how to change the templates in the templates folder to tailor this solution to you own needs.

## Please contribute

You know.  Fork it, use it, and if you made any improvement that can be useful for the rest of us, you can choose to sending me a pull request.

Best regards.

Txinto - gatATAC.org 2017

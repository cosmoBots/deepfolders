import easygui as g

df_run_msg = 'Generate'

ret = df_run_msg

while ret == df_run_msg:
    ret = g.buttonbox(msg='Click to Generate or update the folder structure', title='Deepfolders', choices=(['Generate']))
    if ret == df_run_msg:
        execfile("df_run.py")


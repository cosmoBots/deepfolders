from pyexcel_ods import get_data
import json
import os
from shutil import copyfile
import codecs

const_df_folder_name = "df_folder.ods"
const_base_column_number = 17
const_path_column_number = 0
const_obs_column_number = const_path_column_number + 1
const_template_column_number = const_obs_column_number + 2
const_startrow = 1
const_endrow = 101
const_list_file_name = "df_list.ods"
const_item_file_name = "df_item.ods"
const_folder_def_file_name = "df_folder.ods"
const_inner_ident_column_number = 2
const_inner_name_column_number = 0
const_inner_desc_column_number = 1
const_structure_tab = "Structure"
const_list_startrow = 1
const_list_endrow = 101
const_list_startcolumn = 0
const_list_endcolumn = 2
const_list_tab = "List"
const_readme_file_name = "README.txt"

def create_folder(project_path):
    prj_folder_file_path = project_path + "/" + const_df_folder_name

    data = get_data(prj_folder_file_path, start_column=(const_base_column_number + const_path_column_number), column_limit=(const_template_column_number - const_path_column_number+1),
                    start_row=const_startrow, row_limit=(const_endrow - const_startrow))
    print(json.dumps(data))
    datares = data[const_structure_tab]
    print(json.dumps(datares))

    # Rows loop
    cur_step = 0
    end_step = len(datares)

    while (cur_step < end_step):
        datarow = datares[cur_step]

        if len(datarow) > const_path_column_number:
            file_path = project_path + datarow[const_path_column_number]
            print ("* Path being processed: " + file_path)

            if len(datarow) > const_obs_column_number:
                obs_txt = datarow[const_obs_column_number]
                # print ("* Description : " + obs_txt)

            if len(datarow) > const_template_column_number:
                template_path = datarow[const_template_column_number]
                print ("* Template is : " + template_path)
                print ("* File to be created is : " + file_path)
                if not os.path.exists(file_path):
                    copyfile(template_path, file_path)

                # Now we treat the case where there is a pair of "list.ods" and "def_carpeta.ods" files, in order to create
                # recursively the subfolders
                base_name = os.path.basename(file_path)
                print("const_list_file_name: #" + const_list_file_name + "#")
                print("Basename of current file_path: #" + base_name + "#")
                if base_name == const_list_file_name:
                    print("File detected as List file")
                    directory = os.path.dirname(file_path)
                    template_path = directory + "/" + const_folder_def_file_name
                    print ("* Template path for recursive folder must be in the path: " + template_path)
                    if os.path.exists(template_path):
			print("***** Template for recursive folder found")
                        sub_data = get_data(file_path, start_column=const_list_startcolumn,
                                        column_limit=(const_list_endcolumn - const_list_startcolumn + 1),
                                        start_row=const_list_startrow, row_limit=(const_list_endrow - const_list_startrow + 1))
                        sub_data_list = sub_data[const_list_tab]
                        print("********** Sub folders to be created **************")
                        print(json.dumps(sub_data_list))
                        cur_step_inner = 0
                        end_step_inner = len(sub_data_list)
                        inner_base_dir_name = os.path.dirname(file_path)
                        while cur_step_inner < end_step_inner:
                            print("cur_step_inner: " + str(cur_step_inner))
                            print("const_inner_ident_column_number: " + str(const_inner_ident_column_number))
                            if len(sub_data_list[cur_step_inner]) > const_inner_ident_column_number:
                                inner_file_path = inner_base_dir_name + "/" + sub_data_list[cur_step_inner][const_inner_ident_column_number]
                                print("inner_file_path: " + inner_file_path)
                                if not os.path.exists(inner_file_path):
                                    os.makedirs(inner_file_path)

                                readme_path = inner_file_path + "/" + const_readme_file_name
                                if not os.path.exists(readme_path):
                                    file = codecs.open(readme_path,"w","utf-8")
                                    file.write("ident: ") 
                                    file.write((sub_data_list[cur_step_inner][const_inner_ident_column_number]))
                                    file.write("\r\nname: ")
                                    file.write(sub_data_list[cur_step_inner][const_inner_name_column_number])
                                    file.write("\r\ndescription")
                                    file.write("\r\n===========\r\n")
                                    file.write(sub_data_list[cur_step_inner][const_inner_desc_column_number])
                                    file.write("\r\n")
                                    file.close()
                                item_path = inner_file_path + "/" + const_folder_def_file_name
                                if not os.path.exists(item_path):
                                    copyfile(template_path, item_path)

                                create_folder(inner_file_path)

                            cur_step_inner += 1
                else:
                    if base_name == const_item_file_name:
                        print ("* TODO: execute actions corresponding to the file " + const_item_file_name)

            else:
                print ("* As there is no template for this entry, it means it is a folder")
                if not os.path.exists(file_path):
                    os.makedirs(file_path)

                readme_path = file_path + "/" + const_readme_file_name
                if not os.path.exists(readme_path):
                    file = codecs.open(readme_path,"w","utf-8")
                    file.write(obs_txt + "\n")
                    file.close()

        cur_step += 1



create_folder(".")

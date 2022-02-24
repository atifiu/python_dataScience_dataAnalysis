import subprocess
import os
import glob

def upload(v_path = 'datasets', v_file_name = '*.csv') :
    names = [os.path.basename(x) for x in glob.glob(v_path + '/'+ v_file_name)]
    if v_path == 'datasets' :
        directory = os.getcwd() + '\\' + v_path
    else :
        directory = v_path

    print(directory)
    print(names)
    for with_ext in names:
        #os.path.splitext(with_ext)
        file_name = os.path.splitext(with_ext)[0]
        print(file_name)
        #Provide full path of sqlcl
        os.chdir(r"C:\sqlcl\sqlcl-21.4.1.17.1458\sqlcl\bin")

        #test.sql file should be placed in the bin directory of sqlcl or else provide the complete path
        subprocess.run(["sql",
                        "arup/arup@192.168.29.71:1521/testpdb1.localdomain",
                        "@",
                        r"test.sql", ""+file_name+"", ""+directory+"\\"+with_ext+"",
                        ";"])
        print("Table created..."+ file_name)
        os.chdir(directory)
        print("Current directory is "+ os.getcwd())
    return
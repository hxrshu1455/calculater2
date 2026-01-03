import os
import shutil

print("working with path and directories")
c_dir=os.getcwd()
print(f"current directory:{c_dir}")

n_dir=os.path.join(c_dir,"test_dir")
if not os.path.exists(n_dir):
    os.mkdir(n_dir)
    print(f"Directory created:{n_dir}")
    

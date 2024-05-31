import os
import argparse
import re
from datetime import datetime
from glob import iglob

cwd = os.getcwd()
DUMP_TEXT_FILENAME = f"module_list_{datetime.now().strftime('%Y%m%d')}"

argparser = argparse.ArgumentParser(
    description="Lists all the modules from python files in root and subfolders"
)
argparser.add_argument(
    "--dump",
    "-d",
    type=bool,
    default=False,
    help="Create a .txt in the root folder with the output",
)
argparser.add_argument(
    "--ignore-zero",
    "-i",
    type=bool,
    default=False,
    help="Omit python files with 0 modules",
)
args = argparser.parse_args()


py_file_paths = [os.path.join(cwd, f) for f in iglob(f"**/*.py", recursive=True)]


all_modules = {}
for py_file in py_file_paths:
    with open(py_file, "r", encoding="utf-8") as f:
        modules = []
        for line in f:
            if re.match("^(import|from)", line):
                line = line.strip()
                modules.append(line)

        if args.ignore_zero and len(modules) == 0:
            continue

        all_modules[os.path.relpath(py_file)] = sorted(modules)

complete_base_modules_list = []
output_lines = []
for script, modules in all_modules.items():
    output_lines.append(f"\n{script} - {len(modules)} modules")

    printed_modules = []
    for module in modules:
        module_data = module.split()

        base_module = module_data[1]
        sub_modules = []
        if "from" in module_data:
            sub_module = module_data[3:]
            sub_modules.append(sub_module)

        if base_module not in printed_modules:
            output_lines.append(f"\t|__ {base_module}")
            complete_base_modules_list.append(base_module)
        printed_modules.append(base_module)

        for sub_module in sub_modules:
            output_lines.append(f'\t\t|__ {" ".join(sub_module)}')

complete_base_modules_list = set(complete_base_modules_list)
output_lines.append(f"\nAll base modules - {len(complete_base_modules_list)} modules")
for module in sorted(complete_base_modules_list):
    output_lines.append(f"\t|__ {module}")

if args.dump:
    txt_path = os.path.join(cwd, f"{DUMP_TEXT_FILENAME}.txt")
    with open(txt_path, "w") as f:
        for line in output_lines:
            print(line)
            f.writelines(f"{line}\n")
else:
    for line in output_lines:
        print(line)

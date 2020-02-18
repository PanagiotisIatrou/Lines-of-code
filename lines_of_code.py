import os
import sys
import filemapper as fm

scripts_path = sys.argv[1]

allow_print = False
ext_list = []
for x in sys.argv:
	if (x == '-p'):
		allow_print = True
	if (x[0] == '[' and x[-1] == ']'):
		ext_list.append(x[1:-1])

if (not os.path.isdir(scripts_path)):
	sys.exit("Cant find path " + scripts_path)

lines_of_code = 0
file_count = 0
all_files = fm.load(scripts_path)
for root, dirs, files in os.walk(scripts_path):
	for x in files:
		for f in ext_list:
			if (x[(len(x) - len(f)):] == f):
				file = open(root + '\\' + x, 'r')
				script = file.read()
				newLines = script.count('\n')
				lines_of_code += newLines
				file_count += 1
				if (allow_print):
					print("* {} with {} lines".format(x, str(newLines)))

if (file_count != 0 and allow_print):
	print("")
print("- {} lines of code in {} files.".format(lines_of_code, file_count))

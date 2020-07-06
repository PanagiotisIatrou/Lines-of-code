import os
import sys

scripts_path = sys.argv[1]

allow_print = False
allow_print_sorted = False
allow_print_sorted_inverted = False
ext_list = []
for x in sys.argv:
	if (x == '-p'):
		allow_print = True
	if (x == '-ps'):
		allow_print_sorted = True
	if (x == '-psi'):
		allow_print_sorted_inverted = True
	if (x[0] == '[' and x[-1] == ']'):
		ext_list.append(x[1:-1])

if (not os.path.isdir(scripts_path)):
	sys.exit("Cant find path " + scripts_path)

if (allow_print + allow_print_sorted + allow_print_sorted_inverted > 1):
	sys.exit("You can only have one of the -p -ps -psi parameters")

lines_of_code = 0
file_names = []
file_lengths = []
for root, dirs, files in os.walk(scripts_path):
	for x in files:
		for f in ext_list:
			if (x[(len(x) - len(f)):] == f):
				file = open(root + '\\' + x, 'r')
				script = file.read()
				newLines = script.count('\n')
				lines_of_code += newLines
				file_names.append(x)
				file_lengths.append(newLines)

file_count = len(file_names)
if (allow_print or allow_print_sorted or allow_print_sorted_inverted):
	# Sort the lists if -ps or -psi
	if (allow_print_sorted or allow_print_sorted_inverted):
		tuples = zip(*sorted(zip(file_lengths, file_names), reverse=allow_print_sorted_inverted))
		file_lengths, file_names = [ list(tuple) for tuple in tuples]

	# Find longest file name
	longest_file_name_length = len(file_names[0])
	for i in range(1, file_count):
		if (len(file_names[i]) > longest_file_name_length):
			longest_file_name_length = len(file_names[i])

	# Print
	for i in range(file_count):
		print("* {} {} {} lines".format(file_names[i], "." * (longest_file_name_length - len(file_names[i]) + 1), file_lengths[i]))

	if (file_count != 0):
		print("")

print("- {} total lines of code in {} files.".format(lines_of_code, file_count))

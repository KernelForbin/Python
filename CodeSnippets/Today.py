# import os
#
# def copy_files():
#     try:
#         files = os.listdir('Story')
#         with open('master-file', 'x') as master_file:
#             master_file.write('START \n\n')
#             for file in files:
#                 with open('Story/' + file) as other_file:
#                     master_file.write(other_file.read())
#             master_file.write('\n\nEND')
#     except FileExistsError:
#         os.remove('master-file')
#         copy_files()
#     except FileNotFoundError:
#         print('That file does not exist.')
#
# copy_files()
#
# with open('master-file') as master_file:
#     print(master_file.read())





##for file in files:
##    if file.endswith('.py'):
##        continue
##    if file.startswith('.'):
##        continue

##with open('Story1') as f:
##   lines = f.readline()
##   print('%s lines were read' % len(lines))
##   five_letter_words = 0
##   for line in lines:
##   if len(line) == 6

##   chars = len(content)
##   stuff = len(lines)

##   print(chars)
##   print(stuff)

##print(lines)
##print(content)



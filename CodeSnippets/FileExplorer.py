__author__ = 'KernelForbin '

# Open, read and print a file.

while True:
    file_name = input('Input the name of a file: ')
    try:
        f = open(file_name, 'r')
        contents = f.read()
        if len(contents) > 1000:
            raise RuntimeError('That file is too big to print!')
        print(contents + "\n")
        f.close()
    except FileNotFoundError:
        print("That file doesn't exist! \n")
    except RuntimeError as e:
        print("That's an error. Details: %s\n" % e.args)

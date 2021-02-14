import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
for name in glob.glob(pattern):
    print(name)

# TODO: use os.path.getsize to find each file's size
for name in glob.glob(pattern):
    print(name + " is the size " + str(os.path.getsize(name)))

# TODO: Add a test to only display files that are not zero length
file_size = os.path.getsize(name)
if file_size > 0:
    print(name + "is bigger than zero.")

# to be continued .... maybe using a string test

# TODO: Remove the leading directory name(s) from each filename before you print it -
basename = os.path.basename(name)
print(basename)

# to be continued 

# using os.path.basename()

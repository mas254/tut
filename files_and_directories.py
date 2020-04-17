from pathlib import Path

# Absolute path or relative path

# Blank means current direcotry
Path()
path = Path('')
print(Path.exists())

# Make directory

path = Path('test')
print(Path.mkdir())

# Remove directory

path = Path('test')
print(Path.rmdir())

# Find all files and directories in path (useful for automating iteration across entire directory
path = Path()
print(Path.glob('*.*'))
# If adding extension, won't get directories, only files. * means all

path = Path()
for file in path.glob('*'):
    print(file)
import sys

# Read the diff
with open(sys.argv[1], 'r') as f:
    diff = f.read()

print(diff)

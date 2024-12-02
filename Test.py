import sys

# Check if the diff is provided via file or standard input
if len(sys.argv) > 1:
    # Read the diff from the provided file
    with open(sys.argv[1], 'r') as f:
        diff = f.read()
    print("1")
else:
    # Read the diff from standard input
    diff = sys.stdin.read()
    print("2")

# Print the diff (or you could process it further)
print("hi")
print(diff)
print("hi")


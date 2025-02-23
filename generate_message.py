import sys

# Read the diff
with open(sys.argv[1], 'r') as f:
    diff = f.read()

# TODO: Replace this with logic to generate a meaningful commit message
commit_message = "Generated Commit Message:\n\n" + diff[:500]  # Limiting to first 500 chars for brevity

# Write the commit message to a file
with open("commit_message.txt", "w") as f:
    f.write(commit_message)

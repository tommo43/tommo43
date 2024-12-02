import sys
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the model
MODEL_NAME = "Salesforce/codet5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_commit_message(diff):
    # Tokenize the diff
    inputs = tokenizer(
        diff,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )
    # Generate the commit message
    outputs = model.generate(
        inputs["input_ids"],
        max_length=50,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_commit_message.py <diff_file>")
        sys.exit(1)

    diff_file = sys.argv[1]
    with open(diff_file, "r") as f:
        diff = f.read()

    commit_message = generate_commit_message(diff)
    print(commit_message)

if __name__ == "__main__":
    main()

import pickle

# Load the saved answers
with open("answers.pkl", "rb") as f:
    answers = pickle.load(f)

# Print everything
print("Loaded answers:\n")
for k, v in answers.items():
    print(k, ":", v)

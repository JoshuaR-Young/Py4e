def compute_average_spam_confidence(filename):
    total_spam_confidence = 0
    count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    # Extract the floating point number after the colon
                    try:
                        confidence = float(line.strip().split(':')[1])
                        total_spam_confidence += confidence
                        count += 1
                    except ValueError:
                        print("Error converting string to float")

        if count > 0:
            average_spam_confidence = total_spam_confidence / count
            print(f"Average spam confidence: {average_spam_confidence:.12f}")
        else:
            print("No spam confidence lines found")
            
    except FileNotFoundError:
        print(f"File not found: {filename}")

# Example usage
filename = input("Enter the file name: ")
compute_average_spam_confidence(filename)

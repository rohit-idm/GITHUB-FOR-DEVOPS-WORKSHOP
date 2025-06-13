import os

# Path to your folder
input_folder = ""
output_file = os.path.join(input_folder, "combined_output.txt")

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        if os.path.isfile(file_path):  # ✅ Process all file types
            try:
                outfile.write(f"{filename}\n")
                outfile.write("-----\n")
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())
                outfile.write("\n-----\n\n")
                print(f"✔ Processed: {filename}")
            except Exception as e:
                print(f"⚠ Skipped: {filename} (Error: {e})")

print(f"\nDone! Combined file saved as:\n{output_file}")

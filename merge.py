import os

def merge_files():
    folder_path = "mental_health_data"
    output_file = "mental_health_dataset.txt"

    with open(output_file, "w", encoding="utf-8") as outfile:

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # sirf .txt files read karo
            if filename.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as infile:
                    
                    content = infile.read()

                   
                    outfile.write(f"===== {filename} =====\n")
                    outfile.write(content)
                    outfile.write("\n\n")

    print("Master dataset file created successfully!")

if __name__ == "__main__":
    merge_files()

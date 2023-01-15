import os
import shutil

TXT = ".txt"
ANN = ".ann"

def gather(source_folder, output_folder, variation="bokmaal"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        print("Checking metadata against current files...")

    def valid_file(file_name: str) -> bool:
        return TXT in file_name or ANN in file_name

    num_files = 0
    for path, _, filenames in os.walk(source_folder):
        num_files += len(filenames)
        for f in filenames:
            if not valid_file(f):
                continue

            f_path = os.path.join(path, f)
            new_path = os.path.join(output_folder, f"{variation}_{f}")
            shutil.copy2(f_path, new_path)
    print(f"Combined {num_files} .ann and .txt files")

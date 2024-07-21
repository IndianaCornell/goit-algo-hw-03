import os
import shutil
import sys

 
 

def parse_arguments():
    if len(sys.argv) < 3:
        print("Enter: ""python copy_files.py <source_directory> <destination_directory>""")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    return source_dir, dest_dir


def copy_files(source, dest):
    try:        
        for item in os.listdir(source):
            src_path = os.path.join(source, item)
            if os.path.isdir(src_path):
                    copy_files(src_path, dest)
            else:
                file_extension = os.path.splitext(item)[1][1:].lower()
                if file_extension:  
                    target_dir = os.path.join(dest, file_extension)

                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    shutil.copy2(src_path, target_dir)
    except Exception as e:
        print(f"Error: {e}")



def main():
    source_dir, dest_dir = parse_arguments()

    if not os.path.exists(source_dir):
        print(f"The source directory '{source_dir}' does not exist.")
        sys.exit(1)
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copy_files(source_dir, dest_dir)
    print(
        f"Files copied"
    )

if __name__ == "__main__":
    main()

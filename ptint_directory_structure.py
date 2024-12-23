import os

def print_directory_structure(root_dir, indent_level=0):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        print('    ' * indent_level + '|-- ' + item)
        if os.path.isdir(item_path):
            print_directory_structure(item_path, indent_level + 1)

if __name__ == '__main__':
    project_root = '.'  # Change this to the root directory of your project
    print_directory_structure(project_root)

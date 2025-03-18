import os

def create_java_project(project_name):
    

    try:
        # 1. Create the directory
        os.makedirs(project_name, exist_ok=True)
        print(f"Directory '{project_name}' created successfully.")

        # 2. Create the Java file
        java_file_path = os.path.join(project_name, f"{project_name}.java")
        with open(java_file_path, "w") as java_file:
            java_file.write(f"""public class {project_name} {{
    public static void main(String[] args) {{
        
    }}
}}""")
        print(f"Java file '{java_file_path}' created successfully.")

        

    except OSError as e:
        print(f"Error creating directory or file: {e}")


if __name__ == "__main__":
    project_name = input("Enter the project name (which will also be the class name and batch file name): ")
    create_java_project(project_name)
    print("Project creation complete.")

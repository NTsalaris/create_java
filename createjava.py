import os

def create_java_project(project_name):
    """
    Creates a directory with the given name, a Java file 
    (with class name matching the project name), and a batch file 
    to compile and run the Java code.

    Args:
        project_name: The name of the project (directory, Java class, and batch file).
    """

    try:
        # 1. Create the directory
        os.makedirs(project_name, exist_ok=True)
        print(f"Directory '{project_name}' created successfully.")

        # 2. Create the Java file
        java_file_path = os.path.join(project_name, f"{project_name}.java")
        with open(java_file_path, "w") as java_file:
            java_file.write(f"""public class {project_name} {{
    public static void main(String[] args) {{
        System.out.println("Hello from Java!");
    }}
}}""")
        print(f"Java file '{java_file_path}' created successfully.")

        # 3. Create the batch file
        bat_file_path = os.path.join(project_name, f"run_{project_name}.bat")
        with open(bat_file_path, "w") as bat_file:
            bat_file.write(f"""@echo off
echo Compiling {project_name}.java...
javac {project_name}.java
if %errorlevel% neq 0 (
  echo Compilation failed.
  pause
  exit /b %errorlevel%
)

echo Running {project_name}...
java {project_name}
pause""")
        print(f"Batch file '{bat_file_path}' created successfully.")

    except OSError as e:
        print(f"Error creating directory or file: {e}")


if __name__ == "__main__":
    project_name = input("Enter the project name (which will also be the class name and batch file name): ")
    create_java_project(project_name)
    print("Project creation complete.")
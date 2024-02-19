import subprocess

def build():
    print("Building the project...")
    # Replace the command with the actual build command for your project
    subprocess.run(["./build.bat"], check=True)

def test():
    print("Running tests...")
    # Replace the command with the actual test command for your project
    subprocess.run(["./run_tests.bat"], check=True)

def deploy():
    print("Deploying the project...")
    # Replace the command with the actual deployment command for your project
    subprocess.run(["./deploy.bat"], check=True)

def main():
    try:
        build()
        test()
        deploy()
        print("Workflow completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Workflow failed.")

if __name__ == "__main__":
    main()

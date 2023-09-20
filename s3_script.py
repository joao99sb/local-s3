import subprocess
import os

def menu():
    print("\nSelect an option:\n")
    print("1. Install AWSLocal CLI")
    print("2. Start the instance")
    print("3. Create a new bucket")
    print("4. List buckets")
    print("5. Destroy a bucket")
    print("6. Clear all data from a bucket")
    print("7. Stop Instance")
    print("0. Exit")

container_name = 'localstack_main'

def install_aws_local():
    try:
        subprocess.run(["awslocal", "--version"], check=True)
        print("\nawscli-local is already installed.\n")
    except subprocess.CalledProcessError:
        try:
            subprocess.run(["pip", "install", "awscli-local"], check=True)
            print("\nawscli-local installed successfully!\n")
        except subprocess.CalledProcessError as e:
            print(f"\nError installing awscli-local: {e}\n")
        except Exception as e:
            print(f"\nUnexpected error: {e}\n")

def container_exists(container_name):
    try:
        subprocess.run(f'docker inspect {container_name}',
                       shell=True, check=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def start_container(container_name):
    try:
        subprocess.run(
            f'docker start {container_name}', shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"\nError starting container {container_name}\n")

def init_instance():
    current_dir = os.path.dirname(__file__)
    compose_dir = os.path.join(current_dir, "docker-compose.yml")
    if not container_exists(container_name):
        try:
            subprocess.run(
                f'docker-compose -f {compose_dir} up -d', shell=True, check=True)
            print(f"\nContainer {container_name} created and started.\n")
        except subprocess.CalledProcessError:
            print(f"\nError creating and starting container {container_name}.\n")
    else:
        start_container(container_name)
        print(f"\nContainer {container_name} started.\n")

def create_bucket():
    bucket_name = input("Enter the bucket name: ")
    try:
        subprocess.check_call(["awslocal", "s3api", "create-bucket",
                              "--bucket", bucket_name, "--region", "us-east-1"])

    except subprocess.CalledProcessError as e:
        print(f"\nAn error occurred while creating the S3 bucket: {e}\n")
    except FileNotFoundError:
        print("\nThe awslocal command was not found. Please make sure awscli-local is installed.\n")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")

def list_buckets():
    try:
        subprocess.check_call(
            ["awslocal", "s3api", "list-buckets", "--region", "us-east-1"])
        print("\nS3 bucket listing successful.\n")

    except subprocess.CalledProcessError as e:
        print(f"\nAn error occurred while listing S3 buckets: {e}\n")
    except FileNotFoundError:
        print("\nThe awslocal command was not found. Please make sure awscli-local is installed.\n")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")

def destroy_buckets():
    try:
        bucket_name = input("Enter the bucket name: ")
        subprocess.run(
            ["awslocal", "s3", "rb", "s3://"+bucket_name], check=True)
        print("\nBucket 'test' removed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"\nError removing the bucket: {e}\n")
    except Exception as e:
        print(f"\nUnexpected error: {e}\n")

def clear_bucket():
    try:
        bucket_name = input("Enter the bucket name: ")
        subprocess.run(["awslocal", "s3", "rm", "s3://" +
                       bucket_name+"/", "--recursive"], check=True)
        print(f"\nContent of bucket '{bucket_name}' removed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"\nError removing bucket content: {e}\n")
    except Exception as e:
        print(f"\nUnexpected error: {e}\n")

def stop_instance():
    try:
        subprocess.run(f'docker stop {container_name}', shell=True, check=True)
        print(f"\nContainer {container_name} stopped.\n")
    except subprocess.CalledProcessError:
        print(f"\nError stopping container {container_name}.\n")

def main():
    while True:
        menu()
        input_element = input("Enter the desired option number: ")

        if input_element == "1":
            install_aws_local()
        elif input_element == "2":
            init_instance()
        elif input_element == "3":
            create_bucket()
        elif input_element == "4":
            list_buckets()
        elif input_element == "5":
            destroy_buckets()
        elif input_element == "6":
            clear_bucket()
        elif input_element == "7":
            stop_instance()
        elif input_element == "0":
            print("Exiting...")
            break
        else:
            print("\nInvalid option. Please try again.\n")
            main()

if __name__ == '__main__':
    main()

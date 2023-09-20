AWSLocal CLI Script

Overview

This Python script provides a command-line interface (CLI) for interacting with AWS services using the AWSLocal CLI. The AWSLocal CLI allows you to simulate AWS services locally for development and testing purposes. This script is designed to persist S3 bucket data even after the container is stopped.

Features

- Install AWSLocal CLI
- Start and manage a Docker container with AWSLocal services
- Create and manage S3 buckets locally
- List existing S3 buckets
- Remove S3 buckets and their contents
- Stop the Docker container hosting AWSLocal services

Usage

Prerequisites

- Docker installed on your system
- Python 3.x installed
- Pip (Python package manager) installed

Installation

1. Clone the repository or download the script file.
2. Ensure Docker is running on your system.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using Python:

```bash
python s3_script.py
```


Accessing AWSLocal Health Check

To check if the AWSLocal service is running, open a web browser and go to localhost:4566/health.

Menu Options

1. Install AWSLocal CLI: Checks if AWSLocal CLI is installed, and installs it if not.
2. Start the instance: Initializes the Docker container with AWSLocal services.
3. Create a new bucket: Allows you to create a new S3 bucket locally.
4. List buckets: Lists all existing S3 buckets.
5. Destroy a bucket: Removes a specified S3 bucket.
6. Clear all data from a bucket: Removes all contents from a specified S3 bucket.
7. Stop Instance: Stops the Docker container running AWSLocal services.
0. Exit: Quits the script.

Notes

- Make sure Docker is running before starting the instance.
- Some options may prompt for user input (e.g., bucket names).

Troubleshooting

- If you encounter any issues, please refer to the official AWSLocal documentation (https://github.com/localstack/localstack).

Dependencies

- Python 3.x
- Docker
- Pip (for installing AWSLocal CLI)

License

This script is licensed under the MIT License (LICENSE).

Author

João Victor Dias

Acknowledgments

- This script utilizes the AWSLocal CLI and Docker for local development and testing.
- Special thanks to the LocalStack project for providing the AWSLocal CLI.

ref: https://docs.localstack.cloud/getting-started/installation/#docker-compose
ref: https://docs.localstack.cloud/user-guide/aws/s3/
docker-compose file:


version: "3.8"

services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME-localstack_main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
    environment:
      - DEBUG=${DEBUG-}
      - DOCKER_HOST=unix:///var/run/docker.sock
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"


# Install AWSLocal
pip install awscli-local
awslocal s3api list-buckets --region us-east-1

// criar um bucket
awslocal s3api create-bucket --bucket moodar-bucket --region us-east-1

// lisatr os buckets
awslocal s3api list-buckets --region us-east-1
//destruir 
awslocal  s3 rb s3://teste

# to check Services
localhost:4566/heath

# Terraform 
terraform init
terraform fmt
terraform plan
terraform apply
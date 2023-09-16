
import subprocess

def menu():
    print("\nSelecione uma opção:")
    print("1. Instalar AWSLocal CLI")
    print("2. Criar novo bucket")
    print("3. Listar buckets")
    print("4. Destruit um bucket")
    print("5. Limpar todos os dados de um bucket")
    print("0. Sair")

def install_aws_local():
  try:
      subprocess.run(["awslocal", "--version"], check=True)
      print("awscli-local já está instalado.")
  except subprocess.CalledProcessError:
      try:
          subprocess.run(["pip", "install", "awscli-local"], check=True)
          print("awscli-local instalado com sucesso!")
      except subprocess.CalledProcessError as e:
          print(f"Erro ao instalar awscli-local: {e}")
      except Exception as e:
          print(f"Erro inesperado: {e}")

def create_bucket():
    
    bucket_name = input("Digite o nome do bucket: ")
    try:
      # Executa o comando awslocal para criar o bucket
      subprocess.check_call(["awslocal", "s3api", "create-bucket",
                            "--bucket", bucket_name, "--region", "us-east-1"])

    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao criar o bucket S3: {e}")
    except FileNotFoundError:
        print("O comando awslocal não foi encontrado. Verifique se o awscli-local está instalado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def list_buckets():
    try:
        # Executa o comando awslocal para listar os buckets
        subprocess.check_call(
            ["awslocal", "s3api", "list-buckets", "--region", "us-east-1"])
        print("Listagem de buckets S3 bem-sucedida.")

    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao listar os buckets S3: {e}")
    except FileNotFoundError:
        print("O comando awslocal não foi encontrado. Verifique se o awscli-local está instalado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def destroy_buckets():
    try:
        bucket_name = input("Digite o nome do bucket: ")
        subprocess.run(["awslocal", "s3", "rb", "s3://"+bucket_name], check=True)
        print("Bucket 'teste' removido com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao remover o bucket: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")   


def clear_bucket():
    try:
        bucket_name = input("Digite o nome do bucket: ")
        subprocess.run(["awslocal", "s3", "rm", "s3://"+bucket_name+"/", "--recursive"], check=True)
        print(f"Conteúdo do bucket '{bucket_name}' removido com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao remover o conteúdo do bucket: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
  
  menu()
  escolha = input("Digite o número da opção desejada: ")

  if escolha == "1":
      install_aws_local()
  elif escolha == "2":
      create_bucket()
  elif escolha == "3":
      list_buckets()
  elif escolha == "4":
      destroy_buckets()
  elif escolha == "5":
      clear_bucket()
  elif escolha == "0":
      print("Saindo...")
  else:
      print("Opção inválida. Tente novamente.")
      main()


if __name__ == '__main__':
  main()
#API- Quatro principais operações:
"""
CREATE= POST
READ = GET (Buscar informações, "consulta")
UPDATE = PUT
DELETE = DELETE """

#Bibliotecas
pip install request # Para trabalhar com API
pip install virtualenv
pip install chalice

#1 - Instalação Postman no Windows
#2 - Criação da conta gratuita no AWS
# 2.1 -  https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html
# 2.2 - aws --version
# 2.3 - Painel do IAM

#Começando a criação da API:
"""
cd " e o caminho onde está o projeto, exemplo: C:\Users\curai\OneDrive\Área de Trabalho\Projeto API AWS
mkdir consumers
cd consumers
py - m venv consumers_env
consumers_env\scripts\activate
chalice new-project
Enter the project name: consumers
Select your project type: > REST API
cd consumers
code .

"""

#Testes Unitários da API com a Biblioteca PYTEST
#pip install chalice
#pip install pytest
# py.test .\tests\test_app.py -s
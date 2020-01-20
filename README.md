# ecommerce api

Esta em fase de desenvolvimento a api de ecommerce. Para isso está sendo utilizada a linguagem python(framework: Django e django rest framework), e algumas extensões como: django-oauth-toolkit aws-cli e boto3 (apk python aws).

## Arquitetura
A aplicação foi desenvolvida em módulos. Com isso existem algumas regras a serem seguidas, por exemplo: O módulo de produtos, não deverá importar explicitamente outros módulos da aplicação, resultando assim na reutilização desse módulo em outros sistema, sem ter ficar fazendo grandes alterações no código quando essa migração for realizada. 
Porém caso surgir a necessidade de importar outros módulos, dentro da aplicação tem um arquivo chamado categoriesSettings que vai servir como intermediário, auxiliando  na importação de um módulo. 

Alguns módulos estão passando por um processo de refatoração, ficando assim mais claro ao desenvolvedor onde está localizado cada funcionalidade. 
Atualmente os módulos que já passaram por esse processo de refatoração foram: authentication, comments e products. 

Com isso as estrutura de diretórios e arquivos estão sendo construídas da seguinte forma:
serializer, viewSets, apps.py models.py, urls.py

O módulo de produtos está estruturado um pouco diferente dos demais. Dentro existe um diretório Categories que estão todas as categorias dos produtos a serem vendidos no ecommerce. 

## Como rodar a aplicação? 

1. Baixe a imagem docker do ecommerce.
```
docker pull jonasflorencio/ecommerce
```
2. Baixe o código fonte a partir da branch master da api.
```
git clone git@github.com:JonasBarros1998/ecommerce.git
```
3. Configure o docker-compose, adicionando o volume, e também terá que configurar o arquivo .env porque o arquivo docker-compose.yml, vai usar algumas informações que estão localizadas no .env

4. Crie um arquivo .env na raiz do projeto, e cole dentro todo conteúdo que está no envexample.txt. 

5. Agora faça o build com docker-compose
```
docker-compose build
```
6. Inicie o docker
```
docker-compose up
```
7. Rode alguns comando dentro do container.
```
docker exec -it ecommerce python manage.py migrate
docker exec -it ecommerce python manage.py makemigrations
docker exec -it ecommerce python manage.py migrate
```
Ao todo terão que ser criadas 22 tabelas no banco de dados, se verificar que não foram criadas todas as tabelas, verifique o módulo referente aquela tabela e digite o seguinte comando. 

```
docker exec -it ecommerce python manage.py makemigrations user
```

8. Crie um novo usuário. 
```
docker exec -it ecommerce python manage.py createsuperuser
```
Acesse a url localhost://8000/admin, faça o login com nome e senha que você acabou de cadastrar. 

Pronto!! A aplicação já está configurada e pronta para o uso.

## Caso queira usar o pgadmin com docker, para verificação das tabelas faça o seguinte: 

1. Baixe a imagem relacionada ao pgadmin4
```
docker pull dpage/pgadmin4
```
2. Rode o container, essa parte os container ecommerce-db e ecommerce tem que estar rodando. 
```
docker run -it --name pgadmin4 --network=ecommerce_ecommerce-networks -p “15432:80” -e “PGADMIN_DEFAULT_EMAIL=seu_email” 
-e “PGADMIN_DEFAULT_PASSWORD=sua_senha”  dpage/pgadmin4
```
3. Acesse essa url: http://localhost:15432. 

Para conectar um novo servidor, será preciso passar algumas configurações específicas.

- host/name addres: nesse caso é o nome do container rodando pgadmin4. 
- port: 5432.
- username: Nome de usuário que você criou no postgres.
- password: Senha que você criou no postgres.







# projetoBD2

# ATENÇÃO!!
- É necessário criar um banco de dados com o nome "teste_de_mesa" e importar o arquivo teste_de_mesa(1).sql no phpmyadmin. Esse arquivo contém todas as procedures e estruturas utilizadas no projeto.
- O diagrama de casos de uso foi desenvolvido por Fabiano e reutilizado por mim, nessa branch.
## Passos para executar o projeto:
- 1- npm install
- 2- Configurar o arquivo bd_connection.js com os dados da sua instância do mysql
- 3- npm start para iniciar



### Problemas Encontrados
- Durante os testes, percebi algumas falhas que demandariam um pouco mais de tempo para serem tratadas,
uma delas é o fato de que o código fonte não pode ter comentários e as chaves dos blocos de código devem
estar na mesma linha, como no exemplo a seguir:
--- EXEMPLO---
function teste(arr){
    if(arr.length!=0){

    }
}

- Uma outra falha é quando o laço de repetição é muito grande, o motor v8 do node não suporta e estoura a memória
- O projeto ficou devendo um melhor tratamento de exceções e erros
- O projeto também não salva os operadores no banco de dados. Ao adicionar um trecho de código que faria isso, muitos problemas foram disparados ao executar o eval().

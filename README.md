# Clínica Vida+

A Clínica Vida+ é um projeto que comecei em 2025 durante a graduação em Análise e Desenvolvimento de Sistemas.

Na época, a proposta fazia parte de um Projeto Integrado da faculdade e consistia em pensar uma solução para informatizar alguns processos de uma clínica, como cadastro de pacientes e médicos, agendamentos e organização dos atendimentos.

A parte prática em Python que desenvolvi naquele momento era mais simples: um sistema executado pelo terminal para cadastrar e consultar pacientes e gerar algumas estatísticas.

Depois de recuperar o projeto a partir do relatório acadêmico, decidi utilizá-lo como base para praticar novos conteúdos que estou estudando em programação e desenvolvimento back-end.

## De onde o projeto começou

A primeira versão foi desenvolvida como atividade acadêmica em 2025.

O programa utilizava listas e dicionários para armazenar os pacientes durante a execução e possuía funcionalidades como:

- cadastro de pacientes;
- listagem;
- busca por nome;
- cálculo de estatísticas;
- menu pelo terminal.

Como os dados ficavam apenas na memória, eles eram perdidos sempre que o programa era encerrado.

O código dessa etapa está preservado em:

```text
versao-academica-2025/
```

Essa versão foi reconstruída com base no código e nas informações registradas no relatório original do projeto.

## Evolução do projeto

Ao retomar a Clínica Vida+, comecei uma nova implementação para aplicar os conhecimentos adquiridos depois da primeira versão.

Em vez de substituir o trabalho acadêmico original, mantive aquela versão separada para conseguir acompanhar a evolução do projeto.

A nova versão passou a utilizar uma organização com responsabilidades separadas entre modelo, serviço, repositório e banco de dados.

```text
src/
├── database/
│   └── conexao.py
├── models/
│   └── paciente.py
├── repositories/
│   └── paciente_repository.py
├── services/
│   └── paciente_service.py
└── main.py
```

## Funcionalidades atuais

A versão atual permite:

- cadastrar pacientes;
- listar pacientes cadastrados;
- buscar pacientes pelo nome;
- atualizar os dados de um paciente;
- excluir pacientes;
- identificar pacientes por ID;
- manter os dados após o encerramento do programa;
- validar informações básicas antes do cadastro ou atualização.

A exclusão utiliza o ID do paciente e solicita confirmação antes de remover o registro.

Na atualização, é possível manter um dado existente apenas pressionando Enter no campo correspondente.

## Banco de dados

Nesta versão passei a utilizar SQLite para armazenar os pacientes.

A tabela é criada automaticamente caso ainda não exista e possui os seguintes campos:

```text
id
nome
idade
telefone
```

O ID é gerado automaticamente pelo banco.

As operações SQL ficam concentradas no `PacienteRepository`, incluindo:

- `INSERT`;
- `SELECT`;
- `UPDATE`;
- `DELETE`;
- busca utilizando `WHERE` e `LIKE`.

As consultas utilizam parâmetros (`?`) em vez de montar comandos SQL diretamente com os valores informados pelo usuário.

O arquivo local do banco de dados não é enviado para o GitHub e está incluído no `.gitignore`.

## Organização da aplicação

Nesta etapa do projeto, procurei separar as responsabilidades do programa.

### Model

`Paciente` representa os dados utilizados pela aplicação.

### Service

`PacienteService` concentra as regras e validações aplicadas antes das operações com os pacientes.

### Repository

`PacienteRepository` é responsável pelas operações realizadas no SQLite.

### Main

`main.py` contém o menu e a interação com o usuário pelo terminal.

O fluxo principal ficou:

```text
main.py
   ↓
PacienteService
   ↓
PacienteRepository
   ↓
SQLite
```

Essa separação foi uma das principais diferenças em relação à primeira versão do projeto.

## Tecnologias utilizadas

- Python
- SQLite
- SQL
- Git
- GitHub

Não são necessárias bibliotecas externas para executar esta versão.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/gabrielftenorio-droid/clinica-vida-plus.git
```

Entre na pasta:

```bash
cd clinica-vida-plus
```

Execute:

```bash
py src/main.py
```

Dependendo da instalação do Python, também pode ser utilizado:

```bash
python src/main.py
```

Na primeira execução, o banco SQLite será criado automaticamente.

## Menu

Ao iniciar o programa:

```text
Clínica Vida+
1. Cadastrar paciente
2. Listar pacientes
3. Buscar paciente
4. Atualizar paciente
5. Excluir paciente
6. Sair
```

Os registros cadastrados permanecem disponíveis mesmo depois que o programa é encerrado.

## Aprendizados

A retomada deste projeto está servindo principalmente para comparar o que eu conseguia desenvolver no início da graduação com os conhecimentos que fui adquirindo depois.

Durante essa evolução pratiquei conceitos como:

- organização do código em módulos;
- classes e objetos;
- separação de responsabilidades;
- persistência de dados;
- SQLite;
- comandos SQL;
- consultas parametrizadas;
- tratamento de erros;
- validação de dados;
- CRUD;
- Git e versionamento do projeto.

A ideia foi evoluir o projeto por etapas, mantendo a versão acadêmica original separada para registrar esse processo.

## Autor

Gabriel Fernandes Tenório  
Análise e Desenvolvimento de Sistemas
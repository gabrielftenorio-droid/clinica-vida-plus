# Clínica Vida+ — Versão Acadêmica (2025)

Esta pasta preserva a versão acadêmica do projeto **Clínica Vida+**, desenvolvido em 2025 durante o curso de **Análise e Desenvolvimento de Sistemas**.

O trabalho fez parte da disciplina **Projeto Integrado Inovação: Desenvolvimento de uma Plataforma de Saúde** e teve como proposta a aplicação de conceitos de desenvolvimento de sistemas na informatização de processos de uma clínica.

> **Sobre esta versão:** o código desta pasta foi reconstruído com base na implementação registrada no relatório acadêmico original de 2025, preservando a lógica e as funcionalidades documentadas no projeto.

## Contexto acadêmico

A Clínica Vida+ foi utilizada como cenário para propor uma solução tecnológica capaz de reduzir a dependência de processos manuais e melhorar a organização de informações e atendimentos.

O projeto acadêmico abordou um escopo mais amplo, incluindo conceitos relacionados a:

- cadastro de pacientes;
- cadastro de médicos;
- agendamento de consultas e exames;
- regras de negócio;
- organização do fluxo de atendimento;
- lógica booleana;
- algoritmos;
- modelagem por casos de uso;
- planejamento das atividades com Scrum e Trello.

A implementação em Python documentada no relatório representa uma parte desse projeto e concentra-se principalmente no gerenciamento básico de pacientes.

## Programa em Python

A aplicação recuperada utiliza estruturas nativas da linguagem Python para armazenar os dados dos pacientes em memória.

Cada paciente é representado por um dicionário contendo:

- nome;
- idade;
- telefone.

Os pacientes são armazenados em uma lista durante a execução do programa.

A interação acontece por meio de um menu no terminal.

### Funcionalidades implementadas

O programa permite:

1. cadastrar pacientes;
2. visualizar estatísticas;
3. buscar pacientes pelo nome;
4. listar todos os pacientes cadastrados;
5. encerrar o sistema.

As estatísticas apresentam:

- número total de pacientes;
- idade média;
- paciente mais novo;
- paciente mais velho.

A busca aceita correspondências parciais e não diferencia letras maiúsculas de minúsculas.

Também há tratamento para idade digitada em formato inválido e para opções inexistentes no menu.

## Tecnologias e conceitos utilizados

- Python
- listas
- dicionários
- estruturas condicionais
- estruturas de repetição
- tratamento de exceções
- entrada e saída pelo terminal
- manipulação de strings
- cálculo de estatísticas básicas

## Execução

É necessário possuir Python instalado.

No terminal, dentro desta pasta, execute:

```bash
py main.py
```

Dependendo da configuração do ambiente, também pode ser utilizado:

```bash
python main.py
```

## Limitações da versão acadêmica

Esta implementação foi desenvolvida com finalidade acadêmica e representa uma versão inicial e simplificada do sistema.

Entre suas principais limitações estão:

- dados armazenados somente em memória;
- perda dos cadastros ao encerrar o programa;
- ausência de banco de dados;
- ausência de interface gráfica ou web;
- ausência de autenticação;
- cadastro limitado aos dados básicos do paciente;
- ausência, nesta implementação em Python, dos módulos completos de médicos e agendamentos previstos no escopo mais amplo do trabalho;
- código concentrado em um único arquivo.

Essas limitações representam oportunidades de evolução do projeto.

## Evolução do projeto

A Clínica Vida+ está sendo retomada posteriormente como projeto de portfólio, utilizando a ideia acadêmica de 2025 como ponto de partida para uma implementação mais estruturada.

A nova versão será desenvolvida separadamente desta pasta, permitindo comparar a solução acadêmica inicial com sua evolução técnica.

A pasta `versao-academica-2025` será mantida como registro dessa etapa de aprendizado.
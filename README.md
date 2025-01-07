# Gerenciador de Assinaturas e Pagamentos

Este projeto foi desenvolvido como uma solução para gerenciar assinaturas e pagamentos de serviços de streaming ou outros tipos de assinatura. Ele permite adicionar, remover e visualizar assinaturas, realizar pagamentos e gerar relatórios gráficos dos gastos dos últimos 12 meses. O objetivo principal é automatizar o controle financeiro de assinaturas mensais e proporcionar uma visão clara das finanças relacionadas a esses serviços.

## Funcionalidades

- **Adicionar Assinatura**: Registra uma nova assinatura, com informações como empresa, valor e data de assinatura.
- **Remover Assinatura**: Exclui uma assinatura registrada.
- **Valor Total**: Calcula o valor total mensal gasto em assinaturas.
- **Gastos Últimos 12 Meses (Gráfico)**: Gera um gráfico com a comparação entre o valor das assinaturas e os pagamentos realizados nos últimos 12 meses.
- **Realizar Pagamento**: Marca o pagamento de uma assinatura, verificando se já foi pago no mês atual.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada no projeto.
- **SQLModel**: Biblioteca para trabalhar com banco de dados SQL de forma fácil e eficiente.
- **Matplotlib**: Biblioteca para geração de gráficos que visualizam os dados de gastos ao longo do tempo.
- **SQLite**: Banco de dados leve e embutido usado para armazenar as assinaturas e pagamentos.

## Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o projeto, você precisará de:

- **Python 3.8+**: Instale o Python no seu sistema, se ainda não o tiver. Você pode baixá-lo [aqui](https://www.python.org/downloads/).
- **Virtualenv** (opcional, mas recomendado): Uma ferramenta para criar ambientes virtuais isolados para projetos Python.

### Passo 1: Clonar o Repositório

Abra seu terminal e execute o seguinte comando para clonar o repositório:


git clone https://github.com/SEU_USUARIO/GERENCIADOR_ASSINATURAS.git
cd GERENCIADOR_ASSINATURAS

### Passo 2: Criar e Ativar o Ambiente Virtual

python -m venv venv

Para ativar o ambiente virtual, execute:

-Windows:

Copiar código
venv\Scripts\activate

-MacOS/Linux:

Copiar código
source venv/bin/activate

### Passo 3: Instalar as Dependências

pip install -r requirements.txt

### Passo 4: Rodar o Programa

python app.py

### Estrutura do Projeto

/GERENCIADOR_ASSINATURAS
│
├── template/
│   └── app.py                  # Arquivo principal para execução do programa
│
├── models/
│   ├── __init__.py             # Inicializador do pacote 'models'
│   ├── database.py             # Configuração do banco de dados (SQLite)
│   ├── model.py                # Definição das classes Subscription e Payment
│
├── views/
│   ├── __init__.py             # Inicializador do pacote 'views'
│   └── view.py                 # Lógica de operações no banco de dados e interação com o usuário
│
├── requirements.txt            # Lista de dependências do projeto
└── README.md                   # Documentação do projeto (este arquivo)

### Como Funciona
Adicionar Assinatura: O usuário pode adicionar uma nova assinatura, fornecendo o nome da empresa, o valor e a data da assinatura.

Remover Assinatura: O usuário pode excluir uma assinatura fornecendo o ID da assinatura que deseja remover.

Valor Total: O sistema calcula o valor total mensal gasto em todas as assinaturas registradas e exibe o total.

Realizar Pagamento: O usuário pode registrar um pagamento de uma assinatura. O sistema verifica se o pagamento já foi realizado no mês e, caso contrário, solicita confirmação para realizar o pagamento.

Gastos nos Últimos 12 Meses: O sistema gera um gráfico de linha comparando os gastos mensais com as assinaturas e os pagamentos realizados nos últimos 12 meses.

### Contribuição

Se você quiser contribuir com o projeto, fique à vontade para abrir uma issue ou submeter um pull request. Agradecemos contribuições para melhorar o código ou adicionar novas funcionalidades!

### Licença

MIT License

Copyright (c) 2025 Diego Couto

Permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e dos arquivos de documentação associados (o "Software"), para usar, copiar, modificar, fundir, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e para permitir que as pessoas a quem o Software é fornecido o façam, desde que as condições seguintes sejam atendidas:

A cópia do Software deve conter a notificação de copyright acima e esta lista de condições.

O Software é fornecido "no estado em que se encontra", sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando às garantias de comercialização, adequação a um propósito específico e não violação. Em nenhum caso os autores ou detentores do copyright serão responsáveis por qualquer reclamação, dano ou outra responsabilidade, seja em uma ação de contrato, ato ilícito ou de outra forma, decorrente de, fora de ou em conexão com o Software ou o uso ou outras transações no Software.

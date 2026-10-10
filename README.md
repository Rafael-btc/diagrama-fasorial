# ⚡ Diagrama Fasorial

Projeto desenvolvido em Python para plotar e manipular diagramas fasoriais, com foco no auxílio aos estudos de **Circuitos Elétricos em Regime Permanente Senoidal**.

A ideia é oferecer uma ferramenta visual simples para estudantes de Engenharia Elétrica explorarem fasores de tensão e corrente e compreenderem melhor suas defasagens angulares.

O projeto foi desenvolvido por mim, com auxílio de ferramentas de inteligência artificial (IA), e está aberto a sugestões, adaptações e melhorias.

## 🚀 Como utilizar

### Opção 1 — Executável para Windows

Para facilitar o uso, o projeto está disponível em formato executável. Acesse a seção abaixo para baixar o programa:

**[📥 Baixar Diagrama Fasorial para Windows — Releases](https://github.com/Rafael-btc/diagrama-fasorial/releases)**

Após baixar o arquivo `DiagramaFasorial.exe`:

1. Execute o arquivo.
2. Informe a quantidade de fasores de tensão e corrente.
3. Preencha os nomes e os valores das partes real e imaginária.
4. Clique em **Plotar / Atualizar animação** para visualizar o diagrama.

Não é necessário instalar o Python nem as bibliotecas do projeto para utilizar o executável.

> **Aviso:** como o executável não possui assinatura digital, o Windows pode exibir alertas de segurança. Como o projeto ainda está em desenvolvimento, também podem existir erros. Se preferir, você pode analisar o código-fonte e gerar seu próprio executável.

### Opção 2 — Executar o código-fonte

Caso queira estudar, modificar ou executar o projeto pelo Python, siga os passos abaixo.

Instale as dependências:

```bash
pip install numpy matplotlib
```

Execute o arquivo principal:

```bash
python main.py
```

O Tkinter geralmente já está incluído na instalação do Python para Windows.

## 🖥️ Interface inicial

A interface permite definir a quantidade de fasores e informar seus nomes e componentes real e imaginário.

<img width="1135" alt="Tela inicial do Diagrama Fasorial" src="https://github.com/user-attachments/assets/5e54be7e-93bf-4c42-b450-b2b74ab7a4e5" />

## 📊 Diagrama fasorial em execução

O programa apresenta os fasores em um gráfico animado e exibe as defasagens angulares calculadas entre tensões e correntes.

<img width="1917" alt="Diagrama fasorial com animação e defasagens angulares" src="https://github.com/user-attachments/assets/011e509c-a5ce-4a85-811d-f70b4768a056" />

## ⚙️ Funcionalidades

- Plotagem de fasores de tensão e corrente.
- Entrada dos valores pelas partes real e imaginária dos números complexos.
- Animação da rotação dos fasores.
- Cálculo das defasagens angulares entre tensões e correntes.
- Interface gráfica desenvolvida com Tkinter.
- Visualização dos resultados em um diagrama fasorial.

## 🛠️ Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Tkinter** — interface gráfica.
- **NumPy** — operações numéricas e cálculos vetoriais.
- **Matplotlib** — plotagem e animação dos fasores.
- **PyInstaller** — geração do executável para Windows.

## 🎯 Objetivo do projeto

O projeto foi criado como uma ferramenta visual de apoio aos estudantes de Engenharia Elétrica na disciplina de Circuitos Elétricos em Regime Permanente Senoidal.

O código é relativamente simples e ainda pode ser aprimorado. Fiquem à vontade para estudar, adaptar, modificar e contribuir com sugestões de melhorias.

## 📄 Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).

A licença permite utilizar, copiar, modificar e redistribuir o software, inclusive para fins comerciais, respeitando seus termos.

Desenvolvido por mim, com auxílio de ferramentas de inteligência artificial (IA).

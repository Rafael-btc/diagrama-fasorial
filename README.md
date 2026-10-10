# ⚡ Diagrama Fasorial

Projeto desenvolvido em Python para plotar e manipular diagramas fasoriais, com foco no auxílio aos estudos de **Circuitos Elétricos em Regime Permanente Senoidal**.

A ideia é oferecer uma ferramenta visual simples para estudantes de Engenharia Elétrica explorarem fasores de tensão e corrente e compreenderem melhor suas defasagens angulares.

## 🚀 Como utilizar

### Opção 1 — Executável para Windows

Baixe o arquivo `DiagramaFasorial.exe` na seção **Releases** ou nos arquivos disponibilizados neste repositório.

1. Baixe o executável.
2. Execute o arquivo `DiagramaFasorial.exe`.
3. Informe a quantidade de fasores de tensão e corrente.
4. Preencha os nomes e os valores das partes real e imaginária.
5. Clique em **Plotar / Atualizar animação** para visualizar o diagrama.

**Não é necessário instalar o Python nem as bibliotecas do projeto para utilizar o executável.**

> O Windows pode exibir avisos de segurança por se tratar de um executável sem assinatura digital.

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

## 📦 Executável

O executável para Windows pode ser disponibilizado na seção **Releases** do GitHub, facilitando o acesso de quem deseja utilizar o programa sem configurar um ambiente Python.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

Desenvolvido por mim, com auxílio de ferramentas de inteligência artificial (IA).

Sinta-se à vontade para estudar, utilizar, modificar e contribuir com o projeto, respeitando os termos da licença.

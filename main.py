
import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ==================================================
# INTERFACE TKINTER
# ==================================================

root = tk.Tk()
root.title("Analisador de Fasores")
root.geometry("720x650")
root.minsize(600, 500)

entradas_t = []
entradas_c = []
animacao = None


frame_principal = ttk.Frame(root, padding=15)
frame_principal.pack(fill="both", expand=True)

ttk.Label(
    frame_principal,
    text="ANALISADOR DE FASORES",
    font=("Arial", 16, "bold")
).pack(pady=10)


# ==================================================
# QUANTIDADES E LIMITES
# ==================================================

frame_quantidades = ttk.LabelFrame(
    frame_principal,
    text="Quantidade de fasores",
    padding=10
)
frame_quantidades.pack(fill="x", pady=5)

ttk.Label(frame_quantidades, text="Tensões:").grid(
    row=0, column=0, padx=5, pady=5
)

entrada_nt = ttk.Entry(frame_quantidades, width=10)
entrada_nt.insert(0, "2")
entrada_nt.grid(row=0, column=1, padx=5)

ttk.Label(frame_quantidades, text="Correntes:").grid(
    row=0, column=2, padx=5, pady=5
)

entrada_nc = ttk.Entry(frame_quantidades, width=10)
entrada_nc.insert(0, "2")
entrada_nc.grid(row=0, column=3, padx=5)

ttk.Label(
    frame_quantidades,
    text="Acréscimo dos eixos:"
).grid(row=1, column=0, padx=5, pady=5)

entrada_acrescimo = ttk.Entry(frame_quantidades, width=10)
entrada_acrescimo.insert(0, "5")
entrada_acrescimo.grid(row=1, column=1, padx=5)


# ==================================================
# ÁREA ROLÁVEL DOS CAMPOS
# ==================================================

container = ttk.Frame(frame_principal)
container.pack(fill="both", expand=True, pady=10)

canvas_campos = tk.Canvas(
    container,
    highlightthickness=0
)

barra = ttk.Scrollbar(
    container,
    orient="vertical",
    command=canvas_campos.yview
)

frame_campos = ttk.Frame(canvas_campos)

janela_campos = canvas_campos.create_window(
    (0, 0),
    window=frame_campos,
    anchor="nw"
)

canvas_campos.configure(yscrollcommand=barra.set)

canvas_campos.pack(side="left", fill="both", expand=True)
barra.pack(side="right", fill="y")


def atualizar_scroll(event=None):
    canvas_campos.configure(
        scrollregion=canvas_campos.bbox("all")
    )

    canvas_campos.itemconfigure(
        janela_campos,
        width=canvas_campos.winfo_width()
    )


frame_campos.bind("<Configure>", atualizar_scroll)
canvas_campos.bind("<Configure>", atualizar_scroll)


# ==================================================
# CRIAÇÃO DOS CAMPOS DOS FASORES
# ==================================================

def criar_campos():
    global entradas_t, entradas_c

    try:
        nt = int(entrada_nt.get())
        nc = int(entrada_nc.get())

        if nt < 0 or nc < 0 or nt + nc == 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Informe quantidades inteiras válidas. "
            "A soma deve ser maior que zero."
        )
        return

    for widget in frame_campos.winfo_children():
        widget.destroy()

    entradas_t = []
    entradas_c = []

    def criar_secao(titulo, quantidade, destino, prefixo):
        secao = ttk.LabelFrame(
            frame_campos,
            text=titulo,
            padding=8
        )
        secao.pack(fill="x", padx=5, pady=5)

        ttk.Label(
            secao,
            text="Nome",
            width=16
        ).grid(row=0, column=0, padx=3)

        ttk.Label(
            secao,
            text="Parte real (a)",
            width=12
        ).grid(row=0, column=1, padx=3)

        ttk.Label(
            secao,
            text="Parte imaginária (b)",
            width=18
        ).grid(row=0, column=2, padx=3)

        for i in range(quantidade):
            nome = ttk.Entry(secao, width=16)
            real = ttk.Entry(secao, width=12)
            imaginaria = ttk.Entry(secao, width=12)

            nome.insert(0, f"{prefixo}{i + 1}")

            nome.grid(
                row=i + 1, column=0, padx=3, pady=3
            )
            real.grid(
                row=i + 1, column=1, padx=3, pady=3
            )
            imaginaria.grid(
                row=i + 1, column=2, padx=3, pady=3
            )

            destino.append((nome, real, imaginaria))

    criar_secao(
        "TENSÕES (AZUL)",
        nt,
        entradas_t,
        "V"
    )

    criar_secao(
        "CORRENTES (VERMELHO)",
        nc,
        entradas_c,
        "I"
    )

    atualizar_scroll()


# ==================================================
# LEITURA DOS FASORES
# ==================================================

def ler_vetores(entradas):
    nomes = []
    vetores = []

    for nome, real, imaginaria in entradas:
        nome_texto = nome.get().strip()

        if not nome_texto:
            raise ValueError(
                "Todos os fasores precisam de um nome."
            )

        try:
            a = float(real.get())
            b = float(imaginaria.get())

        except ValueError:
            raise ValueError(
                f"Preencha as partes real e imaginária "
                f"corretamente para {nome_texto}."
            )

        nomes.append(nome_texto)
        vetores.append([a, b])

    return nomes, np.array(vetores, dtype=float).reshape(-1, 2)


# ==================================================
# CÁLCULO DOS ÂNGULOS E DEFASAGENS
# ==================================================

def angulo_vetor(v):
    return np.arctan2(v[1], v[0]) % (2 * np.pi)


def defasagem(a, b):
    delta = (a - b + np.pi) % (2 * np.pi) - np.pi
    return abs(np.degrees(delta))


def encontrar_vizinhos(vetores, angulos):
    indices = [
        i for i, v in enumerate(vetores)
        if np.linalg.norm(v) > 1e-12
    ]

    ordenados = sorted(indices, key=lambda i: angulos[i])
    pares = []

    if len(ordenados) < 2:
        return pares

    for j in range(len(ordenados)):
        i1 = ordenados[j]
        i2 = ordenados[(j + 1) % len(ordenados)]

        if any(
            {p[0], p[1]} == {i1, i2}
            for p in pares
        ):
            continue

        pares.append((i1, i2))

    return pares


# ==================================================
# PLOTAGEM E ANIMAÇÃO
# ==================================================

def plotar():
    global animacao

    try:
        nomes_t, tensoes = ler_vetores(entradas_t)
        nomes_c, correntes = ler_vetores(entradas_c)
        acrescimo = float(entrada_acrescimo.get())

        if acrescimo < 0:
            raise ValueError(
                "O acréscimo não pode ser negativo."
            )

    except ValueError as erro:
        messagebox.showerror("Dados inválidos", str(erro))
        return

    ang_t = [angulo_vetor(v) for v in tensoes]
    ang_c = [angulo_vetor(v) for v in correntes]

    pares_t = encontrar_vizinhos(tensoes, ang_t)
    pares_c = encontrar_vizinhos(correntes, ang_c)

    linhas_t = [
        f"{nomes_t[i]} - {nomes_t[j]}: "
        f"{defasagem(ang_t[i], ang_t[j]):.2f}°"
        for i, j in pares_t
    ]

    linhas_c = [
        f"{nomes_c[i]} - {nomes_c[j]}: "
        f"{defasagem(ang_c[i], ang_c[j]):.2f}°"
        for i, j in pares_c
    ]

    linhas_tc = []

    for i in range(len(tensoes)):
        for j in range(len(correntes)):
            if (
                np.linalg.norm(tensoes[i]) < 1e-12
                or np.linalg.norm(correntes[j]) < 1e-12
            ):
                continue

            graus = defasagem(ang_t[i], ang_c[j])

            linhas_tc.append(
                f"{nomes_t[i]} - {nomes_c[j]}: {graus:.2f}°"
            )

    todos = np.vstack((tensoes, correntes))
    limite = max(1, np.max(np.abs(todos))) + acrescimo

    plt.close("all")

    fig = plt.figure(figsize=(14, 8))
    gs = fig.add_gridspec(1, 2, width_ratios=[3, 2])

    ax = fig.add_subplot(gs[0, 0])
    painel = fig.add_subplot(gs[0, 1])
    painel.axis("off")

    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Rotação dos Fasores")
    ax.grid(True)
    ax.set_aspect("equal")

    # Painel estático das defasagens
    painel.set_title(
        "DEFASAGENS ANGULARES",
        fontsize=13,
        pad=15
    )

    y = 0.97

    def adicionar_secao(titulo, linhas, cor):
        nonlocal y

        painel.text(
            0.02,
            y,
            titulo,
            transform=painel.transAxes,
            color=cor,
            fontsize=11,
            fontweight="bold",
            va="top"
        )

        y -= 0.05

        if not linhas:
            linhas = ["Nenhuma combinação disponível"]

        for linha in linhas:
            if y < 0.025:
                painel.text(
                    0.04,
                    y,
                    "... mais resultados omitidos",
                    transform=painel.transAxes,
                    fontsize=8,
                    va="top"
                )
                y -= 0.04
                break

            painel.text(
                0.04,
                y,
                linha,
                transform=painel.transAxes,
                fontsize=9,
                va="top"
            )

            y -= 0.035

        y -= 0.04

    adicionar_secao(
        "TENSÃO × TENSÃO",
        linhas_t,
        "blue"
    )

    adicionar_secao(
        "CORRENTE × CORRENTE",
        linhas_c,
        "red"
    )

    adicionar_secao(
        "TENSÃO × CORRENTE",
        linhas_tc,
        "purple"
    )

    # Criar os fasores
    def criar_vetores(vetores, nomes, cor, legenda):
        setas = []
        textos = []

        for i, v in enumerate(vetores):
            q = ax.quiver(
                0, 0,
                v[0], v[1],
                angles="xy",
                scale_units="xy",
                scale=1,
                color=cor,
                label=legenda if i == 0 else None
            )

            setas.append(q)

            txt = ax.text(
                v[0] + 0.15,
                v[1] + 0.15,
                nomes[i],
                color=cor,
                fontsize=9
            )

            textos.append(txt)

        return setas, textos

    q_t, txt_t = criar_vetores(
        tensoes,
        nomes_t,
        "blue",
        "Tensão"
    )

    q_c, txt_c = criar_vetores(
        correntes,
        nomes_c,
        "red",
        "Corrente"
    )

    if len(tensoes) + len(correntes) > 0:
        ax.legend(loc="upper right")

    velocidade = 0.03

    def atualizar(frame):
        theta = (frame * velocidade) % (2 * np.pi)

        R = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])

        for i, v in enumerate(tensoes):
            rot = R @ v

            q_t[i].set_UVC(rot[0], rot[1])

            txt_t[i].set_position((
                rot[0] + 0.15,
                rot[1] + 0.15
            ))

        for i, v in enumerate(correntes):
            rot = R @ v

            q_c[i].set_UVC(rot[0], rot[1])

            txt_c[i].set_position((
                rot[0] + 0.15,
                rot[1] + 0.15
            ))

        return q_t + q_c + txt_t + txt_c

    animacao = FuncAnimation(
        fig,
        atualizar,
        frames=None,
        interval=30,
        blit=False,
        cache_frame_data=False
    )

    plt.tight_layout()
    plt.show()


# ==================================================
# BOTÕES
# ==================================================

ttk.Button(
    frame_principal,
    text="Gerar campos dos fasores",
    command=criar_campos
).pack(pady=5)

ttk.Button(
    frame_principal,
    text="Plotar / Atualizar animação",
    command=plotar
).pack(pady=5)


# Criar os campos iniciais
criar_campos()

root.mainloop()

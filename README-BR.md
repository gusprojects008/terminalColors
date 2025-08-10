# terminalColors

Utilitário simples para imprimir texto colorido no terminal.

## Instalação

### 1) Criar e ativar um `venv`

```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 2) Instalar diretamente do GitHub (sempre pega o `main`/`default` branch)

```bash
pip install --upgrade pip
pip install git+https://github.com/gusprojects008/terminalColors.git
```

### 3) Instalar uma tag/versão específica ou commit

```bash
pip install git+https://github.com/gusprojects008/terminalColors.git@v0.0.0
```

### 4) Adicionar ao `requirements.txt`

Coloque uma das linhas abaixo no `requirements.txt` do seu projeto:

Pega sempre a última versão do repo

```text
git+https://github.com/gusprojects008/terminalColors.git
```
Ou fixe numa tag específica:

```text
git+https://github.com/gusprojects008/terminalColors.git@v0.0.0
```

Depois, para instalar todas as dependências:

```bash
pip install -r requirements.txt
```
---

## Modo de uso

```python
from terminalColors import Colors
colors = Colors("", "")
print(Colors("blue", "Hello world"))
```

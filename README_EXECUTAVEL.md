# 🏥 Analisador de Bioimpedância - Versão Executável

## 📋 Visão Geral

Esta versão do Analisador de Bioimpedância foi empacotada como um executável para facilitar o uso por usuários finais, eliminando a necessidade de instalar Python e dependências manualmente.

## 🚀 Instalação Rápida

### Opção 1: Instalação Automática (Recomendada)
```bash
# Execute no diretório do projeto
./install.sh
```

### Opção 2: Instalação Manual
```bash
# 1. Instale as dependências do sistema
sudo apt update
sudo apt install python3 python3-pip python3-tk python3-pil

# 2. Instale dependências Python
pip3 install -r requirements.txt

# 3. Crie o executável
python3 build_executable.py

# 4. Execute
./AnalisadorBioimpedancia
```

## 📁 Estrutura de Arquivos

Após a instalação, você terá:

```
graficosBioimpedancia/
├── AnalisadorBioimpedancia          # Executável principal
├── run_analisador.sh                # Script launcher
├── uninstall.sh                     # Script de desinstalação
├── build_executable.py              # Script para criar executável
├── analisador_bioimpedancia.spec    # Configuração PyInstaller
├── install.sh                       # Script de instalação
└── data/                           # Dados do projeto
    ├── raw/                        # Dados brutos
    ├── processed/                  # Dados processados
    └── exports/                    # Gráficos exportados
```

## 🎯 Como Usar

### Executar o Programa
```bash
# Método 1: Executável direto
./AnalisadorBioimpedancia

# Método 2: Script launcher
./run_analisador.sh

# Método 3: Se instalado no sistema
AnalisadorBioimpedancia
```

### Interface do Usuário
1. **Interface Moderna**: Abre automaticamente a interface CustomTkinter
2. **Análise de Dados**: Carregue seus dados CSV de bioimpedância
3. **Visualizações**: Gere gráficos profissionais de composição corporal
4. **Exportação**: Salve gráficos em PNG para relatórios

## 🔧 Configuração

### Dados de Entrada
- Coloque seus dados CSV em `data/raw/dados_bioimpedancia.csv`
- O formato esperado inclui colunas como: data, peso, altura, IMC, etc.

### Personalização
- Modifique `config.py` para ajustar configurações
- Adicione ícones em `assets/` para personalização visual

## 🐛 Solução de Problemas

### Problema: "Executável não encontrado"
```bash
# Verifique se o build foi concluído
ls -la AnalisadorBioimpedancia

# Se não existir, execute o build
python3 build_executable.py
```

### Problema: "Permissão negada"
```bash
# Torne o executável executável
chmod +x AnalisadorBioimpedancia
```

### Problema: "Dependências não encontradas"
```bash
# Reinstale as dependências
pip3 install -r requirements.txt
```

### Problema: "Interface não abre"
```bash
# Execute com debug
python3 main.py

# Ou execute a interface diretamente
python3 src/ui/modern_gui.py
```

## 📦 Desinstalação

```bash
# Execute o script de desinstalação
./uninstall.sh

# Ou remova manualmente
rm -f ~/.local/bin/AnalisadorBioimpedancia
rm -f ~/.local/share/applications/AnalisadorBioimpedancia.desktop
```

## 🔄 Atualizações

Para atualizar o executável:

```bash
# 1. Atualize o código
git pull origin main

# 2. Reconstrua o executável
python3 build_executable.py

# 3. Reinstale se necessário
./install.sh
```

## 📊 Recursos Incluídos

- ✅ Interface gráfica moderna (CustomTkinter)
- ✅ Análise de composição corporal
- ✅ Gráficos profissionais (Matplotlib/Seaborn)
- ✅ Exportação de relatórios
- ✅ Suporte a múltiplos formatos de dados
- ✅ Interface em português
- ✅ Executável standalone

## 🆘 Suporte

Se encontrar problemas:

1. Verifique os logs de erro no terminal
2. Execute `python3 main.py` para debug
3. Verifique se todas as dependências estão instaladas
4. Consulte a documentação em `docs/`

## 📝 Notas Técnicas

- **Tamanho do executável**: ~50-100MB (inclui todas as dependências)
- **Sistema operacional**: Linux (Ubuntu/Debian)
- **Python**: 3.8+ (embutido no executável)
- **Dependências**: Todas incluídas no executável

## 🎉 Benefícios da Versão Executável

1. **Facilidade de uso**: Sem necessidade de instalar Python
2. **Portabilidade**: Funciona em qualquer Linux
3. **Estabilidade**: Dependências fixas e testadas
4. **Distribuição**: Fácil de compartilhar com outros usuários
5. **Manutenção**: Atualizações simples via script

---

**Desenvolvido com ❤️ para profissionais de saúde e fitness**

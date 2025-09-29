# Analisador de Dados de Bioimpedância - Professional Edition

Um projeto Python especializado para analisar dados de balança de bioimpedância e gerar gráficos informativos da evolução da composição corporal.

## Funcionalidades

- **Análise Completa**: Peso, IMC, percentual de gordura, massa muscular e metabolismo
- **Gráficos Especializados**: Visualizações específicas para dados de bioimpedância
- **Dashboard Completo**: Visão geral de todos os indicadores
- **Relatórios Detalhados**: Análise de tendências e mudanças ao longo do tempo
- **Detecção Automática**: Identifica automaticamente as colunas de dados
- **Suporte a CSV**: Fácil importação de dados de balanças de bioimpedância
- **Interface Gráfica Moderna**: Sistema de abas para gerenciamento completo

## Estrutura do Projeto

```
graficosBioimpedancia/
├── main.py                                 # Ponto de entrada principal
├── config.py                              # Configurações do projeto
├── install.sh                             # Script de instalação
├── requirements.txt                       # Dependências do projeto
├── src/                                   # Código fonte organizado
│   ├── core/                              # Módulos principais
│   │   └── bioimpedance_analyzer.py      # Analisador principal
│   ├── ui/                                # Interfaces de usuário
│   │   ├── interface_grafica.py          # Interface gráfica moderna
│   │   └── interface_grafica_backup.py   # Backup da interface
│   ├── utils/                             # Utilitários (futuro)
│   ├── analisar_dados.py                  # Script de linha de comando
│   └── abrir_interface.py                 # Script de conveniência
├── data/                                  # Dados organizados
│   ├── raw/                               # Dados brutos (CSV)
│   │   └── dados_peso_exemplo.csv        # Seus dados de bioimpedância
│   ├── processed/                         # Dados processados (futuro)
│   └── exports/                           # Gráficos e relatórios gerados
├── scripts/                               # Scripts de sistema
│   └── instalar_interface.sh             # Script de instalação antigo
└── docs/                                  # Documentação
    └── README.md                          # Documentação detalhada
```

## Instalação

### Método 1: Script Automático (Recomendado)
```bash
# Execute o script de instalação
./install.sh
```

### Método 2: Instalação Manual
1. **Instale as dependências do sistema**:
   ```bash
   sudo apt install python3-pandas python3-matplotlib python3-seaborn python3-openpyxl python3-tk
   ```

2. **Instale as dependências Python**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Navegue até o diretório do projeto**:
   ```bash
   cd "/home/pedrjunior/Documentos/Projetos Pessoais/graficosBioimpedancia"
   ```

## Como Usar

### 🚀 Início Rápido
```bash
# Execute o programa principal
python3 main.py
```

### 📊 Opções de Uso

1. **Interface Desktop Moderna** (Recomendado)
   - Escolha opção 1 no menu principal
   - Interface moderna com CustomTkinter
   - Seletor de gráficos interativo
   - Visualização em tempo real

2. **Interface Gráfica Clássica** (Tkinter)
   - Escolha opção 2 no menu principal
   - Interface tradicional com abas

3. **Linha de Comando** (Para usuários avançados)
   - Escolha opção 3 no menu principal
   - Análise direta de arquivos CSV

4. **Execução Direta**
   ```bash
   # Interface moderna
   python3 src/ui/modern_gui.py
   
   # Interface clássica
   python3 src/ui/interface_grafica.py
   
   # Análise de dados
   python3 src/analisar_dados.py
   ```

## Formato dos Dados

Seu arquivo CSV deve ter as seguintes colunas:

### Coluna Obrigatória
- **data**: Data da medição (formato: YYYY-MM-DD)

### Colunas de Dados Corporais
- **peso**: Peso em kg
- **imc**: Índice de Massa Corporal
- **Gordura/porcento** ou **Gordura/%**: Percentual de gordura corporal
- **Massa Musucular/porcento** ou **Massa Musucular/%**: Percentual de massa muscular
- **Metabolismo**: Metabolismo basal em kcal/dia
- **Gordura/KG**: Gordura em kg
- **Massa Muscular/KG**: Massa muscular em kg
- **Obesidade/porcento** ou **Obesidade/%**: Percentual de obesidade

### Exemplo de Arquivo CSV
```csv
data,peso,imc,Gordura/porcento,Gordura/KG,Massa Musucular/porcento,Massa Muscular/KG,Metabolismo,Obesidade/porcento
2025-01-24,82.30,28.1,27.5,22.6,36.4,30.0,1727.5,29.2
2025-01-26,79.65,27.2,26.3,21.0,37.0,29.5,1692.7,25.0
```

## Gráficos Gerados

O analisador gera automaticamente os seguintes gráficos na pasta `data/exports/`:

1. **Evolução do Peso** (`evolucao_peso.png`)
2. **Composição Corporal** (`composicao_corporal.png`)
3. **Análise de IMC** (`analise_imc.png`)
4. **Análise de Metabolismo** (`analise_metabolismo.png`)
5. **Dashboard Completo** (`dashboard_completo.png`)

## Estrutura de Diretórios

- **`src/core/`**: Módulos principais de análise
- **`src/ui/`**: Interfaces de usuário
- **`data/raw/`**: Arquivos CSV de dados brutos
- **`data/exports/`**: Gráficos e relatórios gerados
- **`data/processed/`**: Dados processados (futuro)
- **`docs/`**: Documentação do projeto

## Dependências

- **pandas**: Manipulação de dados
- **matplotlib**: Criação de gráficos
- **seaborn**: Estilos visuais aprimorados
- **openpyxl**: Leitura de arquivos Excel (opcional)
- **tkinter**: Interface gráfica (incluído no Python)

## Solução de Problemas

### Erro: "Colunas de composição corporal não encontradas"
- Verifique se as colunas têm nomes como "Gordura/porcento" ou "Massa Musucular/porcento"
- O script detecta automaticamente variações nos nomes

### Erro: "Nenhum dado válido encontrado"
- Verifique se as datas estão no formato YYYY-MM-DD
- Certifique-se de que os valores numéricos estão corretos

### Erro de instalação de dependências
```bash
sudo apt install python3-pandas python3-matplotlib python3-seaborn python3-openpyxl python3-tk
```

## Dicas de Uso

1. **Frequência de Medições**: Meça pelo menos uma vez por semana para ter dados consistentes
2. **Horário Consistente**: Faça as medições sempre no mesmo horário (preferencialmente pela manhã)
3. **Condições Similares**: Use roupas similares e evite medições após exercícios intensos
4. **Backup dos Dados**: Mantenha backup do seu arquivo CSV

## Licença

Este projeto é de uso livre para fins pessoais e educacionais.

## Contribuições

Sinta-se à vontade para sugerir melhorias ou reportar problemas!

---

**Desenvolvido com ❤️ para análise de composição corporal**
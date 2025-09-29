# Analisador de Dados de Bioimpedância

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
├── data/                                    # Pasta para arquivos de dados
│   └── dados_peso_exemplo.csv             # Seus dados de bioimpedância
├── scripts/                                # Scripts Python
│   ├── bioimpedance_analyzer.py           # Analisador principal
│   ├── weight_analyzer_fixed.py           # Analisador básico
│   └── simple_weight_analyzer.py          # Versão sem dependências
├── interface_grafica.py                    # Interface gráfica moderna
├── analisar_dados.py                       # Script de conveniência
├── requirements.txt                        # Dependências do projeto
└── README.md                               # Este arquivo
```

## Instalação

1. **Instale as dependências do sistema**:
   ```bash
   sudo apt install python3-pandas python3-matplotlib python3-seaborn python3-openpyxl
   ```

2. **Navegue até o diretório do projeto**:
   ```bash
   cd "/home/pedrjunior/Documentos/Projetos Pessoais/graficosBioimpedancia"
   ```

## Como Usar - Guia Passo a Passo

### 🎯 **Primeiro, entenda o que este programa faz:**
- **Você tem uma balança de bioimpedância?** (aquela que mostra peso, gordura, músculo, etc.)
- **Quer acompanhar sua evolução?** (ver se está perdendo peso, ganhando músculo, etc.)
- **Quer gráficos bonitos?** (para mostrar para o médico, nutricionista, ou só para você mesmo)

**Se respondeu "sim" para pelo menos uma pergunta, este programa é para você!**

### 🚀 Para Iniciantes (Método Mais Fácil)

**O que você vai fazer:** Usar uma interface visual (como um programa) para adicionar seus dados de peso e ver gráficos bonitos da sua evolução.

#### Passo 1: Preparar o Sistema (Faça apenas uma vez)
1. **Abra o terminal** (pressione Ctrl+Alt+T no Ubuntu)
2. **Digite este comando** para instalar o que precisa:
   ```bash
   ./instalar_interface.sh
   ```
   - Se der erro, digite: `chmod +x instalar_interface.sh` e tente novamente

#### Passo 2: Abrir o Programa
1. **No terminal, digite:**
   ```bash
   python3 interface_grafica.py
   ```
2. **Uma janela vai abrir** com 3 abas no topo

#### Passo 3: Adicionar Seus Dados
1. **Clique na aba "Entrada de Dados"**
2. **Preencha os campos** com seus dados da balança:
   - **Data**: Clique em "Hoje" ou digite a data
   - **Peso**: Seu peso em kg (ex: 70.5)
   - **IMC**: Se a balança mostrar (ex: 24.5)
   - **Gordura %**: Percentual de gordura (ex: 18.5)
   - **Massa Muscular %**: Percentual de músculo (ex: 45.2)
   - **Metabolismo**: Calorias que você queima por dia (ex: 1650)
3. **Clique em "Adicionar Dados"**

#### Passo 4: Ver Seus Gráficos
1. **Clique na aba "Dashboard"** para ver resumos
2. **Clique em "Gerar Gráficos"** para criar os gráficos
3. **Os gráficos aparecerão** na pasta `data/` do projeto

#### Passo 5: Gerenciar Dados Antigos
1. **Clique na aba "Gerenciar Dados"**
2. **Veja todos os seus dados** em uma tabela
3. **Edite ou exclua** dados se necessário

### 💡 **Dicas Importantes para Iniciantes:**

#### ✅ **O que fazer:**
- **Meça sempre no mesmo horário** (de preferência pela manhã, em jejum)
- **Use roupas similares** nas medições
- **Anote os dados logo após pesar** (para não esquecer)
- **Meça pelo menos 1 vez por semana** (para ter dados consistentes)

#### ❌ **O que evitar:**
- **Não meça após exercícios intensos** (o corpo fica desidratado)
- **Não meça após comer muito** (pode alterar os resultados)
- **Não se preocupe com pequenas variações** (o importante é a tendência geral)

#### 🆘 **Se der problema:**
- **Erro ao abrir:** Tente `chmod +x instalar_interface.sh` e execute novamente
- **Dados não aparecem:** Verifique se salvou clicando em "Salvar Dados"
- **Gráficos não geram:** Verifique se tem pelo menos 2 medições diferentes

### 📝 **Exemplo Prático - Primeira Vez:**

**Imagine que você acabou de se pesar e sua balança mostrou:**
- Peso: 75.2 kg
- IMC: 24.8
- Gordura: 18.5%
- Massa Muscular: 42.3%
- Metabolismo: 1680 kcal

**O que fazer:**
1. **Abra o programa:** `python3 interface_grafica.py`
2. **Clique em "Entrada de Dados"**
3. **Preencha os campos:**
   - Data: Clique em "Hoje"
   - Peso: 75.2
   - IMC: 24.8
   - Gordura %: 18.5
   - Massa Muscular %: 42.3
   - Metabolismo: 1680
4. **Clique em "Adicionar Dados"**
5. **Clique em "Salvar Dados"**
6. **Clique em "Gerar Gráficos"**
7. **Pronto!** Seus gráficos estão na pasta `data/`

**Na próxima semana, repita o processo com os novos dados!**

### 📊 Para Usuários Avançados

Se você já tem um arquivo CSV com seus dados:

#### Método 1: Análise Rápida
```bash
python3 analisar_dados.py
```

#### Método 2: Análise de Arquivo Específico
```bash
python3 scripts/bioimpedance_analyzer.py data/seu_arquivo.csv
```

#### Método 3: Detecção Automática
```bash
python3 scripts/bioimpedance_analyzer.py
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

O analisador gera automaticamente os seguintes gráficos:

1. **Evolução do Peso** (`evolucao_peso.png`)
   - Linha temporal do peso corporal
   - Estatísticas de mudança

2. **Composição Corporal** (`composicao_corporal.png`)
   - Evolução do percentual de gordura
   - Evolução do percentual de massa muscular

3. **Análise de IMC** (`analise_imc.png`)
   - Linha temporal do IMC
   - Linhas de referência para classificação
   - Classificação atual

4. **Análise de Metabolismo** (`analise_metabolismo.png`)
   - Evolução do metabolismo basal
   - Mudanças ao longo do tempo

5. **Dashboard Completo** (`dashboard_completo.png`)
   - Visão geral de todos os indicadores
   - Gráficos lado a lado para comparação

## 🖥️ Interface Gráfica - Explicação Detalhada

A interface gráfica é como um programa de computador que você usa clicando com o mouse. É a forma mais fácil de usar o sistema!

### 🎯 O que cada aba faz:

#### 📝 **Aba "Entrada de Dados"** 
- **Para que serve:** Adicionar novos dados da sua balança
- **Como usar:** Preencha os campos e clique em "Adicionar Dados"
- **Dica:** Use o botão "Hoje" para colocar a data atual automaticamente

#### 📊 **Aba "Gerenciar Dados"**
- **Para que serve:** Ver, editar ou apagar dados antigos
- **Como usar:** Clique em uma linha para editar, ou no X para apagar
- **Dica:** Aqui você pode corrigir erros que digitou antes

#### 📈 **Aba "Dashboard"**
- **Para que serve:** Ver resumos rápidos dos seus dados
- **Como usar:** Apenas olhe os números e gráficos que aparecem
- **Dica:** Use o botão "Gerar Gráficos" para criar gráficos bonitos

### ✨ **Recursos Especiais:**
- **Validação Automática**: O programa avisa se você digitou algo errado
- **Data Automática**: Botão "Hoje" coloca a data atual sozinho
- **Gráficos Fáceis**: Um clique cria todos os gráficos
- **Arquivo Escolhido**: Você pode escolher qual arquivo usar

### 🔧 **Como Usar Passo a Passo:**
1. **Abra o programa:** `python3 interface_grafica.py`
2. **Adicione dados:** Use a aba "Entrada de Dados"
3. **Veja seus dados:** Use a aba "Gerenciar Dados" 
4. **Veja resumos:** Use a aba "Dashboard"
5. **Salve tudo:** Clique em "Salvar Dados"
6. **Crie gráficos:** Clique em "Gerar Gráficos"

## Exemplo de Uso

### Interface Gráfica
```bash
# Navegue até o diretório do projeto
cd "/home/pedrjunior/Documentos/Projetos Pessoais/graficosBioimpedancia"

# Abra a interface gráfica
python3 interface_grafica.py
```

### Linha de Comando
```bash
# Execute o analisador
python3 analisar_dados.py
```

## Relatório de Exemplo

```
======================================================================
RELATÓRIO DE COMPOSIÇÃO CORPORAL
======================================================================

Período: 24/01/2025 a 20/09/2025
Total de medições: 4

PESO:
   Inicial: 82.3 kg
   Atual: 82.7 kg
   Mudança: +0.4 kg

IMC:
   Inicial: 28.1
   Atual: 28.3
   Mudança: +0.2

GORDURA:
   Inicial: 27.5%
   Atual: 27.7%
   Mudança: +0.2%

MASSA MUSCULAR:
   Inicial: 36.4%
   Atual: 36.3%
   Mudança: -0.1%

METABOLISMO:
   Inicial: 1728 kcal/dia
   Atual: 1728 kcal/dia
   Mudança: +1 kcal/dia
======================================================================
```

## Personalização

### Adicionando Novos Dados

1. **Use a interface gráfica** para adicionar dados facilmente
2. **Ou edite seu arquivo CSV** na pasta `data/` manualmente
3. **Execute o analisador** para ver os gráficos atualizados

### Exemplo de Nova Entrada
```csv
2025-10-15,81.5,27.8,27.0,22.0,36.8,30.0,1720.0,28.5
```

## Dependências

- **pandas**: Manipulação de dados
- **matplotlib**: Criação de gráficos
- **seaborn**: Estilos visuais aprimorados
- **openpyxl**: Leitura de arquivos Excel (opcional)

## Solução de Problemas

### Erro: "Colunas de composição corporal não encontradas"
- Verifique se as colunas têm nomes como "Gordura/porcento" ou "Massa Musucular/porcento"
- O script detecta automaticamente variações nos nomes

### Erro: "Nenhum dado válido encontrado"
- Verifique se as datas estão no formato YYYY-MM-DD
- Certifique-se de que os valores numéricos estão corretos

### Erro de instalação de dependências
```bash
sudo apt install python3-pandas python3-matplotlib python3-seaborn python3-openpyxl
```

## Dicas de Uso

1. **Frequência de Medições**: Meça pelo menos uma vez por semana para ter dados consistentes
2. **Horário Consistente**: Faça as medições sempre no mesmo horário (preferencialmente pela manhã)
3. **Condições Similares**: Use roupas similares e evite medições após exercícios intensos
4. **Backup dos Dados**: Mantenha backup do seu arquivo CSV

## Metas e Objetivos

O analisador ajuda a acompanhar:
- **Perda de Peso**: Redução gradual e saudável
- **Ganho de Massa Muscular**: Aumento da massa magra
- **Redução de Gordura**: Diminuição do percentual de gordura
- **Melhoria do Metabolismo**: Aumento do metabolismo basal

## Licença

Este projeto é de uso livre para fins pessoais e educacionais.

## Contribuições

Sinta-se à vontade para sugerir melhorias ou reportar problemas!

---

**Desenvolvido com ❤️ para análise de composição corporal**
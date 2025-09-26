# ?? Analisador de Dados de Bioimpedância

Um projeto Python especializado para analisar dados de balança de bioimpedância e gerar gráficos informativos da evolução da composição corporal.

## ?? Funcionalidades

- **Análise Completa**: Peso, IMC, percentual de gordura, massa muscular e metabolismo
- **Gráficos Especializados**: Visualizações específicas para dados de bioimpedância
- **Dashboard Completo**: Visão geral de todos os indicadores
- **Relatórios Detalhados**: Análise de tendências e mudanças ao longo do tempo
- **Detecção Automática**: Identifica automaticamente as colunas de dados
- **Suporte a CSV**: Fácil importação de dados de balanças de bioimpedância

## ?? Estrutura do Projeto

```
Weight/
??? data/                                    # Pasta para arquivos de dados
?   ??? dados_peso_exemplo.csv             # Seus dados de bioimpedância
??? scripts/                                # Scripts Python
?   ??? bioimpedance_analyzer.py           # Analisador principal
?   ??? weight_analyzer_fixed.py           # Analisador básico
?   ??? simple_weight_analyzer.py          # Versão sem dependências
??? analisar_dados.py                       # Script de conveniência
??? requirements.txt                        # Dependências do projeto
??? README.md                               # Este arquivo
```

## ??? Instalação

1. **Instale as dependências do sistema**:
   ```bash
   sudo apt install python3-pandas python3-matplotlib python3-seaborn python3-openpyxl
   ```

2. **Navegue até o diretório do projeto**:
   ```bash
   cd "/home/pedrjunior/Documentos/Projetos Pessoais/Weight"
   ```

## ?? Como Usar

### ??? Interface Gráfica (Recomendado)
```bash
# Instalar dependências (apenas na primeira vez)
./instalar_interface.sh

# Abrir interface gráfica
python3 abrir_interface.py
```

### ?? Linha de Comando

#### Método 1: Script de conveniência
```bash
python3 analisar_dados.py
```

#### Método 2: Analisador direto
```bash
python3 scripts/bioimpedance_analyzer.py data/dados_peso_exemplo.csv
```

#### Método 3: Detecção automática
```bash
python3 scripts/bioimpedance_analyzer.py
```

## ?? Formato dos Dados

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

## ?? Gráficos Gerados

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

## ??? Interface Gráfica

A interface gráfica oferece uma forma fácil e intuitiva de adicionar novos dados:

### Funcionalidades:
- **Entrada de Dados**: Formulário com todos os campos de bioimpedância
- **Validação Automática**: Verifica se os dados estão corretos antes de salvar
- **Data Automática**: Botão "Hoje" para definir a data atual
- **Visualização**: Visualize todos os dados salvos em uma tabela
- **Geração de Gráficos**: Botão para gerar gráficos diretamente da interface
- **Seleção de Arquivo**: Escolha qual arquivo CSV usar

### Como Usar:
1. Execute `python3 abrir_interface.py`
2. Preencha os campos obrigatórios (Data e Peso)
3. Adicione os outros dados conforme disponível
4. Clique em "Salvar Dados"
5. Use "Gerar Gráficos" para visualizar a evolução

## ?? Exemplo de Uso

### Interface Gráfica
```bash
# Navegue até o diretório do projeto
cd "/home/pedrjunior/Documentos/Projetos Pessoais/Weight"

# Abra a interface gráfica
python3 abrir_interface.py
```

### Linha de Comando
```bash
# Execute o analisador
python3 analisar_dados.py
```

## ?? Relatório de Exemplo

```
======================================================================
?? RELATÓRIO DE COMPOSIÇÃO CORPORAL
======================================================================

?? Período: 24/01/2025 a 20/09/2025
?? Total de medições: 4

?? PESO:
   ? Inicial: 82.3 kg
   ? Atual: 82.7 kg
   ? Mudança: +0.4 kg

?? IMC:
   ? Inicial: 28.1
   ? Atual: 28.3
   ? Mudança: +0.2

?? GORDURA:
   ? Inicial: 27.5%
   ? Atual: 27.7%
   ? Mudança: +0.2%

?? MASSA MUSCULAR:
   ? Inicial: 36.4%
   ? Atual: 36.3%
   ? Mudança: -0.1%

?? METABOLISMO:
   ? Inicial: 1728 kcal/dia
   ? Atual: 1728 kcal/dia
   ? Mudança: +1 kcal/dia
======================================================================
```

## ?? Personalização

### Adicionando Novos Dados

1. **Abra seu arquivo CSV** na pasta `data/`
2. **Adicione uma nova linha** com a data e os valores
3. **Execute o analisador** para ver os gráficos atualizados

### Exemplo de Nova Entrada
```csv
2025-10-15,81.5,27.8,27.0,22.0,36.8,30.0,1720.0,28.5
```

## ?? Dependências

- **pandas**: Manipulação de dados
- **matplotlib**: Criação de gráficos
- **seaborn**: Estilos visuais aprimorados
- **openpyxl**: Leitura de arquivos Excel (opcional)

## ?? Solução de Problemas

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

## ?? Dicas de Uso

1. **Frequência de Medições**: Meça pelo menos uma vez por semana para ter dados consistentes
2. **Horário Consistente**: Faça as medições sempre no mesmo horário (preferencialmente pela manhã)
3. **Condições Similares**: Use roupas similares e evite medições após exercícios intensos
4. **Backup dos Dados**: Mantenha backup do seu arquivo CSV

## ?? Metas e Objetivos

O analisador ajuda a acompanhar:
- **Perda de Peso**: Redução gradual e saudável
- **Ganho de Massa Muscular**: Aumento da massa magra
- **Redução de Gordura**: Diminuição do percentual de gordura
- **Melhoria do Metabolismo**: Aumento do metabolismo basal

## ?? Licença

Este projeto é de uso livre para fins pessoais e educacionais.

## ?? Contribuições

Sinta-se à vontade para sugerir melhorias ou reportar problemas!

---

**Desenvolvido com ?? para análise de composição corporal**
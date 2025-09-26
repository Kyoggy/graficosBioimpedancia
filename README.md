# ?? Analisador de Dados de Bioimped�ncia

Um projeto Python especializado para analisar dados de balan�a de bioimped�ncia e gerar gr�ficos informativos da evolu��o da composi��o corporal.

## ?? Funcionalidades

- **An�lise Completa**: Peso, IMC, percentual de gordura, massa muscular e metabolismo
- **Gr�ficos Especializados**: Visualiza��es espec�ficas para dados de bioimped�ncia
- **Dashboard Completo**: Vis�o geral de todos os indicadores
- **Relat�rios Detalhados**: An�lise de tend�ncias e mudan�as ao longo do tempo
- **Detec��o Autom�tica**: Identifica automaticamente as colunas de dados
- **Suporte a CSV**: F�cil importa��o de dados de balan�as de bioimped�ncia

## ?? Estrutura do Projeto

```
Weight/
??? data/                                    # Pasta para arquivos de dados
?   ??? dados_peso_exemplo.csv             # Seus dados de bioimped�ncia
??? scripts/                                # Scripts Python
?   ??? bioimpedance_analyzer.py           # Analisador principal
?   ??? weight_analyzer_fixed.py           # Analisador b�sico
?   ??? simple_weight_analyzer.py          # Vers�o sem depend�ncias
??? analisar_dados.py                       # Script de conveni�ncia
??? requirements.txt                        # Depend�ncias do projeto
??? README.md                               # Este arquivo
```

## ??? Instala��o

1. **Instale as depend�ncias do sistema**:
   ```bash
   sudo apt install python3-pandas python3-matplotlib python3-seaborn python3-openpyxl
   ```

2. **Navegue at� o diret�rio do projeto**:
   ```bash
   cd "/home/pedrjunior/Documentos/Projetos Pessoais/Weight"
   ```

## ?? Como Usar

### ??? Interface Gr�fica (Recomendado)
```bash
# Instalar depend�ncias (apenas na primeira vez)
./instalar_interface.sh

# Abrir interface gr�fica
python3 abrir_interface.py
```

### ?? Linha de Comando

#### M�todo 1: Script de conveni�ncia
```bash
python3 analisar_dados.py
```

#### M�todo 2: Analisador direto
```bash
python3 scripts/bioimpedance_analyzer.py data/dados_peso_exemplo.csv
```

#### M�todo 3: Detec��o autom�tica
```bash
python3 scripts/bioimpedance_analyzer.py
```

## ?? Formato dos Dados

Seu arquivo CSV deve ter as seguintes colunas:

### Coluna Obrigat�ria
- **data**: Data da medi��o (formato: YYYY-MM-DD)

### Colunas de Dados Corporais
- **peso**: Peso em kg
- **imc**: �ndice de Massa Corporal
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

## ?? Gr�ficos Gerados

O analisador gera automaticamente os seguintes gr�ficos:

1. **Evolu��o do Peso** (`evolucao_peso.png`)
   - Linha temporal do peso corporal
   - Estat�sticas de mudan�a

2. **Composi��o Corporal** (`composicao_corporal.png`)
   - Evolu��o do percentual de gordura
   - Evolu��o do percentual de massa muscular

3. **An�lise de IMC** (`analise_imc.png`)
   - Linha temporal do IMC
   - Linhas de refer�ncia para classifica��o
   - Classifica��o atual

4. **An�lise de Metabolismo** (`analise_metabolismo.png`)
   - Evolu��o do metabolismo basal
   - Mudan�as ao longo do tempo

5. **Dashboard Completo** (`dashboard_completo.png`)
   - Vis�o geral de todos os indicadores
   - Gr�ficos lado a lado para compara��o

## ??? Interface Gr�fica

A interface gr�fica oferece uma forma f�cil e intuitiva de adicionar novos dados:

### Funcionalidades:
- **Entrada de Dados**: Formul�rio com todos os campos de bioimped�ncia
- **Valida��o Autom�tica**: Verifica se os dados est�o corretos antes de salvar
- **Data Autom�tica**: Bot�o "Hoje" para definir a data atual
- **Visualiza��o**: Visualize todos os dados salvos em uma tabela
- **Gera��o de Gr�ficos**: Bot�o para gerar gr�ficos diretamente da interface
- **Sele��o de Arquivo**: Escolha qual arquivo CSV usar

### Como Usar:
1. Execute `python3 abrir_interface.py`
2. Preencha os campos obrigat�rios (Data e Peso)
3. Adicione os outros dados conforme dispon�vel
4. Clique em "Salvar Dados"
5. Use "Gerar Gr�ficos" para visualizar a evolu��o

## ?? Exemplo de Uso

### Interface Gr�fica
```bash
# Navegue at� o diret�rio do projeto
cd "/home/pedrjunior/Documentos/Projetos Pessoais/Weight"

# Abra a interface gr�fica
python3 abrir_interface.py
```

### Linha de Comando
```bash
# Execute o analisador
python3 analisar_dados.py
```

## ?? Relat�rio de Exemplo

```
======================================================================
?? RELAT�RIO DE COMPOSI��O CORPORAL
======================================================================

?? Per�odo: 24/01/2025 a 20/09/2025
?? Total de medi��es: 4

?? PESO:
   ? Inicial: 82.3 kg
   ? Atual: 82.7 kg
   ? Mudan�a: +0.4 kg

?? IMC:
   ? Inicial: 28.1
   ? Atual: 28.3
   ? Mudan�a: +0.2

?? GORDURA:
   ? Inicial: 27.5%
   ? Atual: 27.7%
   ? Mudan�a: +0.2%

?? MASSA MUSCULAR:
   ? Inicial: 36.4%
   ? Atual: 36.3%
   ? Mudan�a: -0.1%

?? METABOLISMO:
   ? Inicial: 1728 kcal/dia
   ? Atual: 1728 kcal/dia
   ? Mudan�a: +1 kcal/dia
======================================================================
```

## ?? Personaliza��o

### Adicionando Novos Dados

1. **Abra seu arquivo CSV** na pasta `data/`
2. **Adicione uma nova linha** com a data e os valores
3. **Execute o analisador** para ver os gr�ficos atualizados

### Exemplo de Nova Entrada
```csv
2025-10-15,81.5,27.8,27.0,22.0,36.8,30.0,1720.0,28.5
```

## ?? Depend�ncias

- **pandas**: Manipula��o de dados
- **matplotlib**: Cria��o de gr�ficos
- **seaborn**: Estilos visuais aprimorados
- **openpyxl**: Leitura de arquivos Excel (opcional)

## ?? Solu��o de Problemas

### Erro: "Colunas de composi��o corporal n�o encontradas"
- Verifique se as colunas t�m nomes como "Gordura/porcento" ou "Massa Musucular/porcento"
- O script detecta automaticamente varia��es nos nomes

### Erro: "Nenhum dado v�lido encontrado"
- Verifique se as datas est�o no formato YYYY-MM-DD
- Certifique-se de que os valores num�ricos est�o corretos

### Erro de instala��o de depend�ncias
```bash
sudo apt install python3-pandas python3-matplotlib python3-seaborn python3-openpyxl
```

## ?? Dicas de Uso

1. **Frequ�ncia de Medi��es**: Me�a pelo menos uma vez por semana para ter dados consistentes
2. **Hor�rio Consistente**: Fa�a as medi��es sempre no mesmo hor�rio (preferencialmente pela manh�)
3. **Condi��es Similares**: Use roupas similares e evite medi��es ap�s exerc�cios intensos
4. **Backup dos Dados**: Mantenha backup do seu arquivo CSV

## ?? Metas e Objetivos

O analisador ajuda a acompanhar:
- **Perda de Peso**: Redu��o gradual e saud�vel
- **Ganho de Massa Muscular**: Aumento da massa magra
- **Redu��o de Gordura**: Diminui��o do percentual de gordura
- **Melhoria do Metabolismo**: Aumento do metabolismo basal

## ?? Licen�a

Este projeto � de uso livre para fins pessoais e educacionais.

## ?? Contribui��es

Sinta-se � vontade para sugerir melhorias ou reportar problemas!

---

**Desenvolvido com ?? para an�lise de composi��o corporal**
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import Markdown, display

def eda(df, target=None):
    """
        Realiza un EDA automático visual.
        
        Parámetros:
        - df: DataFrame de pandas.
        - target: (Opcional) Nombre de la columna objetivo para el pairplot.
        - rows: Número de filas a mostrar en head y nulos.
        - max_pairplot_cols: Límite de columnas para evitar cuelgues en pairplot.
    """
    
    # 1. MUESTRA
    print('='*100)
    display(Markdown("### 📋 Muestra"))
    display(df)
    
    # 2. INFO
    print('='*100)
    display(Markdown(f"### 📊 Info → `{df.shape[0]:,}` filas × `{df.shape[1]}` columnas"))
    print(df.info())
    display(Markdown('#### Uniques'))
    print(df.nunique())
    
    # 3. NULOS
    print('='*100)
    display(Markdown("### ⚠️ Null & NaN"))
    print(df.isna().sum())
    display(df[df.isnull().any(axis=1)])
    
    # 4. BOXPLOTS (Solo numéricas)
    print('='*100)
    display(Markdown("### 📦 Describe"))
    display(df.describe().round(3))
    
    cols = df.describe().columns
    n = len(cols)

    # Crear rejilla (ajusta el 3 para más/menos columnas por fila)
    fig, axes = plt.subplots(nrows=(n//3)+1, ncols=3, figsize=(15, 5*((n//3)+1)))
    axes = axes.flatten()

    for i, col in enumerate(cols):
        sns.boxplot(y=df[col], ax=axes[i], showmeans=True)
        axes[i].set_title(col)

    # 4. Limpiar gráficos vacíos sobrantes
    for j in range(i+1, len(axes)):
        axes[j].set_visible(False)
        
    plt.show()
    
    # 5. PAIRPLOT
    print('='*100)
    display(Markdown(f"### 📈 Comparación"))
    
    if target is not None:
        display(Markdown(f"### (target: {target.name})"))
        if target.name not in df[cols]:
            df_plot = df[cols]
            df_plot[target.name] = target
        else:
            df_plot = df[cols]

        sns.pairplot(df_plot, hue=target.name)
        plt.show()
        
    else:
        sns.pairplot(df)
        plt.show()
        
    plt.figure(figsize=(10, 10)) 
    sns.heatmap(df[cols].corr(), annot=True, fmt='.1%',  vmin=-1, vmax=1, cmap="coolwarm")
    plt.show()
    
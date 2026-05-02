import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import Markdown, display

def eda(df, target):
    """
        Realiza un EDA automático visual.
        
        Parámetros:
        - df: DataFrame de pandas.
        - target: (Opcional) Nombre de la columna objetivo para el pairplot.
        - rows: Número de filas a mostrar en head y nulos.
        - max_pairplot_cols: Límite de columnas para evitar cuelgues en pairplot.
    """
    
    print('='*100)
    display(Markdown("### 📋 Muestra"))
    display(df)
    
    print('='*100)
    display(Markdown(f"### 📊 Info → `{df.shape[0]:,}` filas × `{df.shape[1]}` columnas"))
    print(df.info())
    display(Markdown('#### Uniques'))
    print(df.nunique())
    
    print('='*100)
    display(Markdown("### ⚠️ Null & NaN"))
    print(df.isna().sum())
    display(df[df.isnull().any(axis=1)])
    
    print('='*100)
    display(Markdown("### 📦 Describe"))
    display(df.describe().round(3))
    
    cols = df.describe().columns
    n = len(cols)

    # 2. Crear rejilla (ajusta el 3 para más/menos columnas por fila)
    fig, axes = plt.subplots(nrows=(n//3)+1, ncols=3, figsize=(15, 5*((n//3)+1)))
    axes = axes.flatten()

    # 3. Bucle simple
    for i, col in enumerate(cols):
        sns.boxplot(y=df[col], ax=axes[i], showmeans=True)
        axes[i].set_title(col)

    # 4. Limpiar gráficos vacíos sobrantes
    for j in range(i+1, len(axes)):
        axes[j].set_visible(False)
        
    plt.show()
    
    print('='*100)
    
    if target.name not in df[cols]:
        df_plot = df[cols]
        df_plot[target.name] = target
    else:
        df_plot = df[cols]
    
    display(Markdown(f"### 📈 Comparación (target: {target.name})"))
    sns.pairplot(df_plot, hue=target.name)
    plt.show()
    
    sns.heatmap(df[cols].corr(), annot=True, vmin=-1, vmax=1, cmap="coolwarm")
    plt.show()
    
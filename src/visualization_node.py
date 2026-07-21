import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from src.custom_state import CustomState

def visualize(state: CustomState) -> CustomState:
    result = state.get('result')
    graph_type = state.get('graph_type', 'bar')

    if not result or not isinstance(result, list) or len(result[0]) < 2:
        return state

    df = pd.DataFrame(result)
    x_col, y_col = 0, 1

    plt.figure(figsize=(10, 5))
    try:
        df[y_col] = df[y_col].astype(float)

        if graph_type == "line":
            sns.lineplot(data=df, x=x_col, y=y_col, marker="o")
        elif graph_type == "pie":
            plt.pie(df[y_col], labels=df[x_col], autopct="%1.1f%%")
        else:
            sns.barplot(data=df, x=x_col, y=y_col)

        plt.title("Query Result Chart")
        plt.xticks(rotation=25, ha="right")
        plt.tight_layout()
        plt.savefig("latest_chart.png")
    except Exception as e:
        print(f"Chart generation failed: {e}")
    finally:
        plt.close()

    return state
import pandas as pd
import plotly.graph_objects as go

def map_area_to_color(area):
    if area >= 25:
        return "DarkGreen"  # 30-25: Dark Green Colour
    elif area >= 20:
        return "DarkOliveGreen"  # 24-20: One Level below Dark Green Colour
    elif area >= 15:
        return "OliveDrab"  # 19-15: Two-Level Below Dark Green
    elif area >= 10:
        return "LimeGreen"  # 14-10: Two-Level Above Light Green
    elif area >= 5:
        return "PaleGreen"  # 09-05: One Level Above Light Green
    else:
        return "LightGreen"  # 04-00: Light Green

def create_map_from_excel(file_path, sheet_name):
    ex_file = pd.read_excel(file_path, sheet_name=sheet_name)
    labels = ex_file['Area'].tolist()
    values = ex_file['Existing menbers proficient with this area'].tolist()
    colors = [map_area_to_color(area) for area in values]

    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=[''] * len(labels),
        values=values,
        texttemplate="%{label}<br>%{value}",
        textfont={"size": 15},
        hoverinfo="text",
        marker=dict(colors=colors)  # Corrected color assignment
    ))

    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    return fig

if __name__ == "__main__":
    file_path = 'C:\\Users\\Pavan Naik - 2789\\Downloads\\Heatmap_expertise.xlsx'
    sheet_name = 'Sheet1'
    map_fig = create_map_from_excel(file_path, sheet_name)
    map_fig.show()

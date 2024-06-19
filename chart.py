import streamlit as st
import streamlit.components.v1 as components
import json
import random

def get_chart_data():
    # This function returns the JSON data for various types of charts
    chart_type = random.choice(["line", "bar", "scatter", "pie"])
    labels = ["A", "B", "C", "D", "E"]
    data = [random.randint(1, 10) for _ in range(len(labels))]
    chart_title = f"Sample {chart_type.capitalize()} Chart"
    return {
        "type": chart_type,
        "labels": labels,
        "data": data,
        "chartTitle": chart_title,
        "xAxisTitle": "X Axis",
        "yAxisTitle": "Y Axis"
    }

def generate_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgba({r}, {g}, {b}, 0.2)')
    return colors

def generate_border_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgba({r}, {g}, {b}, 1)')
    return colors

# Fetch the chart data
chart_data = get_chart_data()

# Extract values from the chart data
chart_type = chart_data['type']
labels = json.dumps(chart_data['labels'])
data = json.dumps(chart_data['data'])
chart_title = chart_data['chartTitle']

# Generate dynamic colors based on chart type
if chart_type in ["bar", "pie"]:
    background_colors = json.dumps(generate_colors(len(chart_data['data'])))
    border_colors = json.dumps(generate_border_colors(len(chart_data['data'])))
else:
    background_colors = "'rgba(75, 192, 192, 0.2)'"
    border_colors = "'rgba(75, 192, 192, 1)'"

# HTML and JavaScript code for the Chart.js chart with dynamic values
chart_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chart_title}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .chart-container {{
            width: 80%;
            margin: auto;
            height: 400px; /* Adjust height as needed */
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        canvas {{
            max-width: 100%;
            max-height: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
    <div class="chart-container">
        <canvas id="myChart"></canvas>
    </div>
    <script>
        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {{
            type: '{chart_type}',
            data: {{
                labels: {labels},
                datasets: [{{
                    label: '{chart_title}',
                    data: {data},
                    backgroundColor: {background_colors},
                    borderColor: {border_colors},
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false, // Added to prevent chart from being cut off
                title: {{
                    display: true,
                    text: '{chart_title}',
                    position: 'top',
                    font: {{
                        weight: 'bold'
                    }}
                }},
                legend: {{
                    display: true,
                    position: 'right'
                }},
                scales: {{
                    x: {{
                        display: true,
                        title: {{
                            display: true,
                            text: '{chart_data['xAxisTitle']}',
                            font: {{
                                weight: 'bold'
                            }}
                        }}
                    }},
                    y: {{
                        display: true,
                        title: {{
                            display: true,
                            text: '{chart_data['yAxisTitle']}',
                            font: {{
                                weight: 'bold'
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

# Display the Chart.js chart in Streamlit using the components.html function
components.html(chart_code, height=500)

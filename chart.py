import streamlit as st
import streamlit.components.v1 as components
import json
import random


def get_chart_data(chart_type):
    # This function returns the JSON data for the specified chart type
    labels = ["A", "B", "C", "D", "E"]
    data = [random.randint(1, 10) for _ in range(len(labels))]
    chart_title = f"Sample {chart_type.capitalize()} Chart"
    x_axis_title = "X Axis"
    y_axis_title = "Y Axis"


    return {
        "type": chart_type,
        "labels": labels,
        "data": data,
        "chartTitle": chart_title,
        "xAxisTitle": x_axis_title,
        "yAxisTitle": y_axis_title
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

def generate_line_chart_code(chart_data):
    # Generate Chart.js code for line chart
    chart_type = chart_data['type']
    labels = json.dumps(chart_data['labels'])
    data = json.dumps(chart_data['data'])
    chart_title = chart_data['chartTitle']
    x_axis_title = chart_data['xAxisTitle']
    y_axis_title = chart_data['yAxisTitle']

    # Generate dynamic colors based on chart type
    background_colors = "'rgba(75, 192, 192, 0.2)'"
    border_colors = "'rgba(75, 192, 192, 1)'"

    # HTML and JavaScript code for the Chart.js line chart with dynamic values
    chart_code = f"""
    <canvas id="myChart" width="400" height="200"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
                            text: '{x_axis_title}',
                            font: {{
                                weight: 'bold'
                            }}
                        }}
                    }},
                    y: {{
                        display: true,
                        title: {{
                            display: true,
                            text: '{y_axis_title}',
                            font: {{
                                weight: 'bold'
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
    """
    return chart_code

def generate_bar_chart_code(chart_data):
    # Generate Chart.js code for bar chart
    chart_type = chart_data['type']
    labels = json.dumps(chart_data['labels'])
    data = json.dumps(chart_data['data'])
    chart_title = chart_data['chartTitle']
    x_axis_title = chart_data['xAxisTitle']
    y_axis_title = chart_data['yAxisTitle']

    # Generate dynamic colors for bar chart
    background_colors = json.dumps(generate_colors(len(chart_data['data'])))
    border_colors = json.dumps(generate_border_colors(len(chart_data['data'])))

    # HTML and JavaScript code for the Chart.js bar chart with dynamic values
    chart_code = f"""
    <canvas id="myChart" width="400" height="200"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
                            text: '{x_axis_title}',
                                               font: {{
                                weight: 'bold'
                            }}
                        }}
                    }},
                    y: {{
                        display: true,
                        title: {{
                            display: true,
                            text: '{y_axis_title}',
                            font: {{
                                weight: 'bold'
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
    """
    return chart_code

def generate_scatter_chart_code(chart_data):
    # Generate Chart.js code for scatter chart
    chart_type = chart_data['type']
    labels = json.dumps(chart_data['labels'])
    data = json.dumps(chart_data['data'])
    chart_title = chart_data['chartTitle']
    x_axis_title = chart_data['xAxisTitle']
    y_axis_title = chart_data['yAxisTitle']

    # Scatter chart uses the same color for all points
    background_colors = "'rgba(75, 192, 192, 0.2)'"
    border_colors = "'rgba(75, 192, 192, 1)'"

    # HTML and JavaScript code for the Chart.js scatter chart with dynamic values
    chart_code = f"""
    <canvas id="myChart" width="400" height="200"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
                            text: '{x_axis_title}',
                            font: {{
                                weight: 'bold'
                            }}
                        }}
                    }},
                    y: {{
                        display: true,
                        title: {{
                            display: true,
                            text: '{y_axis_title}',
                            font: {{
                                weight: 'bold'
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
    """
    return chart_code

def generate_pie_chart_code(chart_data):
    # Generate Chart.js code for pie chart
    chart_type = chart_data['type']
    labels = json.dumps(chart_data['labels'])
    data = json.dumps(chart_data['data'])
    chart_title = chart_data['chartTitle']

    # Generate dynamic colors for pie chart
    background_colors = json.dumps(generate_colors(len(chart_data['data'])))

    # HTML and JavaScript code for the Chart.js pie chart with dynamic values
    chart_code = f"""
    <canvas id="myChart" width="400" height="200"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
                    borderColor: 'white',
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
                }}
            }}
        }});
    </script>
    """
    return chart_code

# Sidebar to select chart type
chart_type = st.sidebar.selectbox("Select Chart Type", ["line", "bar", "scatter", "pie"])

# Get chart data based on selected chart type
chart_data = get_chart_data(chart_type)

# Generate Chart.js code based on chart data
if chart_type == "line":
    chart_code = generate_line_chart_code(chart_data)
elif chart_type == "bar":
    chart_code = generate_bar_chart_code(chart_data)
elif chart_type == "scatter":
    chart_code = generate_scatter_chart_code(chart_data)
else:
    chart_code = generate_pie_chart_code(chart_data)

# Display the Chart.js chart in Streamlit using the components.html function
components.html(chart_code, height=500)


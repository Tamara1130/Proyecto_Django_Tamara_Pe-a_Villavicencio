import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import io
import random
from matplotlib import pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
import base64

def generate_random_graph():
    """Generate a random graph."""
    fig, ax = plt.subplots()
    x = range(10)
    y = [random.randint(1, 20) for _ in x]
    ax.plot(x, y, marker='o', label="Random Data")
    ax.set_title("Random Graph")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    return fig

def get_graph_image(fig):
    """Convert matplotlib figure to a Base64 string."""
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return image_base64

def random_graphs(request):
    """View to display 6 random graphs."""
    graphs = []
    for _ in range(6):
        fig = generate_random_graph()
        image = get_graph_image(fig)
        graphs.append(image)

    return render(request, 'app/random_graphs.html', {'graphs': graphs})

import matplotlib.pyplot as plt


def plot_line_graph(x, y, title='Line Graph', xlabel='X-axis', ylabel='Y-axis'):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_bar_chart(categories, values, title='Bar Chart', xlabel='Categories', ylabel='Values'):
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_pie_chart(labels, sizes, title='Pie Chart'):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
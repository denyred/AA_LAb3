import time
import matplotlib.pyplot as plt
import math


def algorithm1(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1
    return c


def algorithm2(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    return c


def algorithm3(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
    return c


def algorithm4(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        j = 1
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


def algorithm5(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j <= int(math.sqrt(i)):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


def compare_algorithms():
    # define input sizes to test
    input_sizes = [10, 100, 1000, 10000]

    # define lists to store execution times for each algorithm
    times1, times2, times3, times4, times5 = [], [], [], [], []

    # loop over input sizes and measure execution times for each algorithm
    for n in input_sizes:
        start_time = time.time()
        algorithm1(n)
        times1.append(time.time() - start_time)

        start_time = time.time()
        algorithm2(n)
        times2.append(time.time() - start_time)

        start_time = time.time()
        algorithm3(n)
        times3.append(time.time() - start_time)

        start_time = time.time()
        algorithm4(n)
        times4.append(time.time() - start_time)

        start_time = time.time()
        algorithm5(n)
        times5.append(time.time() - start_time)

    # plot the execution times for each algorithm as a bar chart
    labels = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4', 'Algorithm 5']
    times = [times1, times2, times3, times4, times5]
    x = range(len(labels))
    fig, ax = plt.subplots()
    ax.bar(x, [sum(t) for t in times])
    ax.set_ylabel('Total Execution Time (Seconds)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.show()

compare_algorithms()
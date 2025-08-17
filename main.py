import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve, auc

from NeuralDecodingSDT.src.simulation import *
from NeuralDecodingSDT.src.analysis import *
from NeuralDecodingSDT.src.visualization import *

if __name__ == "__main__":
    stimulus_present, responses = simulate_neural_responses()

    signal_responses = responses[stimulus_present == 1]
    noise_responses  = responses[stimulus_present == 0]

    d_prime = compute_dprime(signal_responses, noise_responses)
    print(f"d’ estimado: {d_prime:.2f}")

    plot_histogram(signal_responses, noise_responses)
    plot_roc(stimulus_present, responses)
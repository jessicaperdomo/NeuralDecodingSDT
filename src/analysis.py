import numpy as np

def compute_dprime(signal_responses, noise_responses):
    mean_signal = np.mean(signal_responses)
    mean_noise = np.mean(noise_responses)
    std_all = np.sqrt(0.5 * (np.var(signal_responses) + np.var(noise_responses)))
    return (mean_signal - mean_noise) / std_all


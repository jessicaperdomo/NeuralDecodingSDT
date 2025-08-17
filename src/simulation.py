import numpy as np

def simulate_neural_responses(n_trials=1000, mu_signal=8, mu_noise=4, sigma=2):
    stimulus_present = np.random.choice([0,1], size=n_trials)  # 0 = ausência, 1 = presença
    responses = []

    for stim in stimulus_present:
        if stim == 1:
            responses.append(np.random.normal(loc=mu_signal, scale=sigma))
        else:
            responses.append(np.random.normal(loc=mu_noise, scale=sigma))

    return np.array(stimulus_present), np.array(responses)
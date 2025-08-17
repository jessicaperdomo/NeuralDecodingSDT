from src.simulation import *
from src.analysis import *
from src.visualization import *

language = "en"
# language = "pt"

if __name__ == "__main__":
    stimulus_present, responses = simulate_neural_responses()

    signal_responses = responses[stimulus_present == 1]
    noise_responses  = responses[stimulus_present == 0]

    d_prime = compute_dprime(signal_responses, noise_responses)
    
    if language == "pt":
        print(f"d’ estimado: {d_prime:.2f}")
    else:
        print(f"d’ estimated: {d_prime:.2f}")

    plot_histogram(signal_responses, noise_responses, language=language)
    plot_roc(stimulus_present, responses, language=language)
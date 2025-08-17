import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

def plot_histogram(signal_responses, noise_responses, language="en"):
    if language == "pt":
        labels = ["Com estímulo", "Sem estímulo"]
        xlabel = "Resposta Neural (spikes simulados)"
        ylabel = "Frequência"
        title  = "Distribuição de Disparos Neurais"
    else:
        labels = ["With stimulus", "Without stimulus"]
        xlabel = "Neural Response (simulated spikes)"
        ylabel = "Frequency"
        title  = "Neural Spike Distribution"

    plt.hist(signal_responses, bins=30, alpha=0.6, label=labels[0])
    plt.hist(noise_responses, bins=30, alpha=0.6, label=labels[1])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

def plot_roc(stimulus_present, responses, language="en"):
    fpr, tpr, _ = roc_curve(stimulus_present, responses)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6,6))
    plt.plot(fpr, tpr, label=f"ROC (AUC = {roc_auc:.2f})")
    plt.plot([0,1], [0,1], 'k--')

    if language == "pt":
        xlabel = "Taxa de Falsos Alarmes"
        ylabel = "Taxa de Acertos"
        title  = "Curva ROC - Teoria da Detecção de Sinais"
        legend_label = "ROC"
    else:
        xlabel = "False Alarm Rate"
        ylabel = "Hit Rate"
        title  = "ROC Curve - Signal Detection Theory"
        legend_label = "ROC"

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend([legend_label])
    plt.show()

def plot_histogram(signal_responses, noise_responses):
    plt.hist(signal_responses, bins=30, alpha=0.6, label="Com estímulo")
    plt.hist(noise_responses, bins=30, alpha=0.6, label="Sem estímulo")
    plt.xlabel("Resposta Neural (spikes simulados)")
    plt.ylabel("Frequência")
    plt.title("Distribuição de Disparos Neurais")
    plt.legend()
    plt.show()

def plot_roc(stimulus_present, responses):
    fpr, tpr, _ = roc_curve(stimulus_present, responses)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6,6))
    plt.plot(fpr, tpr, label=f"ROC (AUC = {roc_auc:.2f})")
    plt.plot([0,1], [0,1], 'k--')
    plt.xlabel("False Alarm Rate")
    plt.ylabel("Hit Rate")
    plt.title("Curva ROC - Teoria da Detecção de Sinais")
    plt.legend()
    plt.show()

    
import matplotlib.pyplot as plt

def plot_attempts(failed_attempts, save_as=None):
    ips = list(failed_attempts.keys())
    counts = [len(times) for times in failed_attempts.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(ips, counts, color='crimson')
    plt.xlabel('IP Address')
    plt.ylabel('Failed Attempts')
    plt.title('Brute Force Detection Report')
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_as:
        plt.savefig(save_as)
    else:
        plt.show()

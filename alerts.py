def check_brute_force(failed_attempts, threshold=3):
    alerts = []
    for ip, times in failed_attempts.items():
        if len(times) >= threshold:
            alerts.append((ip, len(times)))
    return alerts

import re
from collections import defaultdict

def parse_logs(file_path):
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\] "POST /login.*" (\d+)')
    failed_attempts = defaultdict(list)

    with open(file_path, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ip, timestamp, status = match.groups()
                if status == "401":
                    failed_attempts[ip].append(timestamp)
    return failed_attempts

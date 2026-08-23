import re
def scrub(t): return re.sub(r'\S+@\S+', '[REDACTED]', t)
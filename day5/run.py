
import re
from socket import create_connection
pat = re.compile(r"(UNION SELECT|<script>|xp_cmdshell|/etc/passwd|Failed password|SURICATA|ET )", re.I)
s = create_connection(("127.0.0.1", 5500))
with s, s.makefile() as f, open("suspicious_log.txt", "a") as out_file:
    for line in f:
        line=line.rstrip("\n")
        hit = "  <-- SUSPICIOUS" if pat.search(line) else ""
        with open("my_logs", "a") as file: 
            if hit in line : 
                file.write(line,"\n")

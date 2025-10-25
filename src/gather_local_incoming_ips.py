
interpreter = "python3"
command = "tcpdump"
interface = "-i eth0" # sudo tcpdump -D
ports = ["22", "21", "23", "25", "53", "80", "110", "123", "161", "443", "8080"]
count = "100"


def build_command():
    return f"{interpreter} {command} -i }"
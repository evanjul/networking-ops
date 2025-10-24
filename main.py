import sys
import src
import subprocess
import config

sys.dont_write_bytecode = True

@config.run_before_main()
def main(cmd=f"python3 src/{config.filename}.py"):
    subprocess.Popen([cmd], shell=True)

if __name__ == "__main__":
    main()

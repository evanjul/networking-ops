import sys
import src
import subprocess
import config

sys.dont_write_bytecode = True

@config.preprocess_main()
def main(config):
    cmd = f"echo Default config: {config.filename}"
    subprocess.Popen([cmd], shell=True)

if __name__ == "__main__":
    main()
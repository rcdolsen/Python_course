import subprocess

cmd = ['cmd.exe', '/c', 'dir']
encode = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encode,
    shell=False
)

print(proc.stdout)

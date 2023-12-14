import subprocess
from distutils import spawn

def is_command_available(command):
    try:
        subprocess.run([command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            
        return True
        
    except Exception:
        return False
    
def get_tool():
    try:
        subprocess.run(["go", "install", "github.com/1dayluo/subnya@latest"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False
    
def is_tool(name):
    spawn.find_executable(name) is not None

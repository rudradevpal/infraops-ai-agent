from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import paramiko

app = FastAPI()

class SSHRequest(BaseModel):
    host: str
    port: str  # changed to string
    username: str
    password: str
    command: str  # single command string

@app.post("/ssh/exec")
def ssh_exec(data: SSHRequest):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=data.host,
            port=int(data.port),  # convert string to int
            username=data.username,
            password=data.password
        )

        cmd = data.command.strip()
        if cmd.startswith("sudo"):
            full_cmd = f"sudo -S {cmd[5:].strip()}"
            stdin, stdout, stderr = client.exec_command(full_cmd)
            stdin.write(data.password + '\n')
            stdin.flush()
        else:
            stdin, stdout, stderr = client.exec_command(cmd)

        output = stdout.read().decode()
        error = stderr.read().decode()

        client.close()
        return {
            "command": cmd,
            "stdout": output,
            "stderr": error
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
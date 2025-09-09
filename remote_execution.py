#!/usr/bin/env python3
"""
Remote Currency Exchange Execution
Allows running the currency exchange library on remote Docker environments
while collecting logs locally for supply chain attack simulation.
"""

import subprocess
import sys
import json
import argparse
from datetime import datetime

def execute_remote_docker(remote_host, remote_user=None, ssh_key=None, docker_image="currency-backdoor-sim"):
    """
    Execute currency exchange on remote Docker environment via SSH.
    
    Args:
        remote_host (str): Remote host IP/hostname
        remote_user (str): SSH username (optional)
        ssh_key (str): SSH key path (optional)
        docker_image (str): Docker image name to run
    """
    
    # Build SSH command
    ssh_cmd = ["ssh"]
    
    if ssh_key:
        ssh_cmd.extend(["-i", ssh_key])
    
    if remote_user:
        ssh_host = f"{remote_user}@{remote_host}"
    else:
        ssh_host = remote_host
    
    ssh_cmd.append(ssh_host)
    
    # Docker command to run on remote host
    docker_cmd = f"docker run --rm {docker_image} python -c \"import currency_exchange; print('Remote execution completed')\""
    ssh_cmd.append(docker_cmd)
    
    print(f"[INFO] Executing on remote host: {remote_host}")
    print(f"[CMD] {' '.join(ssh_cmd)}")
    
    try:
        # Execute remote command
        result = subprocess.run(ssh_cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"[SUCCESS] Remote execution completed")
            print(f"[OUTPUT] {result.stdout.strip()}")
            
            # Log remote execution locally
            log_remote_execution(remote_host, "SUCCESS", result.stdout.strip())
            
        else:
            print(f"[ERROR] Remote execution failed: {result.stderr}")
            log_remote_execution(remote_host, "FAILED", result.stderr.strip())
            
    except subprocess.TimeoutExpired:
        print(f"[ERROR] Remote execution timeout")
        log_remote_execution(remote_host, "TIMEOUT", "Command timed out")
    except Exception as e:
        print(f"[ERROR] SSH connection failed: {e}")
        log_remote_execution(remote_host, "CONNECTION_FAILED", str(e))

def execute_remote_docker_compose(remote_host, remote_user=None, ssh_key=None, project_path="/tmp/currency-exchange"):
    """
    Execute currency exchange using docker-compose on remote environment.
    """
    
    # Build SSH command
    ssh_cmd = ["ssh"]
    
    if ssh_key:
        ssh_cmd.extend(["-i", ssh_key])
    
    if remote_user:
        ssh_host = f"{remote_user}@{remote_host}"
    else:
        ssh_host = remote_host
    
    ssh_cmd.append(ssh_host)
    
    # Docker-compose command sequence
    compose_cmd = f"cd {project_path} && docker-compose run --rm backdoor-simulation python -c \"import currency_exchange; print('Remote compose execution completed')\""
    ssh_cmd.append(compose_cmd)
    
    print(f"[INFO] Executing docker-compose on remote host: {remote_host}")
    print(f"[CMD] {' '.join(ssh_cmd)}")
    
    try:
        result = subprocess.run(ssh_cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print(f"[SUCCESS] Remote docker-compose execution completed")
            print(f"[OUTPUT] {result.stdout.strip()}")
            log_remote_execution(remote_host, "COMPOSE_SUCCESS", result.stdout.strip())
        else:
            print(f"[ERROR] Remote docker-compose execution failed: {result.stderr}")
            log_remote_execution(remote_host, "COMPOSE_FAILED", result.stderr.strip())
            
    except Exception as e:
        print(f"[ERROR] Remote docker-compose execution failed: {e}")
        log_remote_execution(remote_host, "COMPOSE_ERROR", str(e))

def log_remote_execution(remote_host, status, output):
    """Log remote execution details to local system metrics file."""
    try:
        with open(".remote_execution.log", "a", encoding="utf-8") as f:
            timestamp = datetime.now().isoformat()
            log_entry = f"{timestamp} - Remote Execution | Host: {remote_host} | Status: {status} | Output: {output}\n"
            f.write(log_entry)
        print(f"[LOG] Execution logged locally to .remote_execution.log")
    except Exception as e:
        print(f"[ERROR] Failed to log remote execution: {e}")

def deploy_to_remote(remote_host, remote_user=None, ssh_key=None, target_path="/tmp/currency-exchange"):
    """
    Deploy currency exchange project to remote host.
    """
    
    print(f"[INFO] Deploying project to remote host: {remote_host}")
    
    # Create target directory on remote
    ssh_cmd_mkdir = ["ssh"]
    if ssh_key:
        ssh_cmd_mkdir.extend(["-i", ssh_key])
    
    if remote_user:
        ssh_host = f"{remote_user}@{remote_host}"
    else:
        ssh_host = remote_host
    
    ssh_cmd_mkdir.extend([ssh_host, f"mkdir -p {target_path}"])
    
    try:
        subprocess.run(ssh_cmd_mkdir, check=True)
        print(f"[SUCCESS] Created directory {target_path} on remote host")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to create remote directory: {e}")
        return False
    
    # Copy project files to remote
    scp_cmd = ["scp", "-r"]
    if ssh_key:
        scp_cmd.extend(["-i", ssh_key])
    
    # Files to copy
    files_to_copy = [
        "currency_exchange.py",
        "requirements.txt", 
        "Dockerfile",
        "docker-compose.yml",
        "README.md",
        "LICENSE"
    ]
    
    scp_cmd.extend(files_to_copy)
    scp_cmd.append(f"{ssh_host}:{target_path}/")
    
    try:
        result = subprocess.run(scp_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[SUCCESS] Project files copied to {remote_host}:{target_path}")
            return True
        else:
            print(f"[ERROR] Failed to copy files: {result.stderr}")
            return False
    except Exception as e:
        print(f"[ERROR] SCP failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Remote Currency Exchange Execution")
    parser.add_argument("remote_host", help="Remote host IP or hostname")
    parser.add_argument("-u", "--user", help="SSH username")
    parser.add_argument("-k", "--key", help="SSH private key path")
    parser.add_argument("-i", "--image", default="currency-backdoor-sim", help="Docker image name")
    parser.add_argument("-p", "--path", default="/tmp/currency-exchange", help="Remote project path")
    parser.add_argument("--deploy", action="store_true", help="Deploy project files to remote host first")
    parser.add_argument("--compose", action="store_true", help="Use docker-compose instead of docker run")
    
    args = parser.parse_args()
    
    print(f"🎯 Remote Currency Exchange Execution")
    print(f"Target: {args.remote_host}")
    print("=" * 50)
    
    if args.deploy:
        print("\n📦 Deploying project to remote host...")
        if not deploy_to_remote(args.remote_host, args.user, args.key, args.path):
            print("❌ Deployment failed, aborting execution")
            return
    
    print("\n🚀 Executing currency exchange on remote host...")
    
    if args.compose:
        execute_remote_docker_compose(args.remote_host, args.user, args.key, args.path)
    else:
        execute_remote_docker(args.remote_host, args.user, args.key, args.image)
    
    print("\n✅ Remote execution completed")
    print(f"📋 Check .remote_execution.log for execution details")

if __name__ == "__main__":
    main()

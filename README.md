```markdown
# Code Fortress: Visual Vulnerability & Secret Auditor GUI

![Python](https://img.shields.io/badge/language-Python-blue)
![MIT](https://img.shields.io/badge/license-MIT-green)
![AI-Generated](https://img.shields.io/badge/AI-Assisted-orange)

## 🛡️ Architecture Overview
**Problem Statement:** Manual code audits fail to scale with modern codebases, while CLI tools lack visualization for nuanced security analysis. Code Fortress bridges this gap with a dynamic GUI that surfaces vulnerabilities through interactive exploration and contextual risk scoring.

## 🔍 Core Features
- **Multi-Engine Scanning:** Parallel executes Semgrep, TruffleHog, and custom regex rules with real-time results aggregation
- **Visual Risk Heatmaps:** D3.js-powered interactive treemaps highlighting high-risk files by CWE severity (CVSS v3.1)
- **Secret Context Weaver:** Reconstructs hardcoded secret lineages by tracing variable declarations through abstract syntax trees
- **Rule Playground:** Live-test custom detection rules with instant feedback (supports YAML/JSON rule imports)
- **Diff Analysis:** Git-integrated comparison between commits to track vulnerability introduction/resolution
- **Export-Ready:** Generate audit-ready PDFs with vulnerability details, code snippets, and remediation guidance

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9+ • Tkinter (sudo apt-get install python3-tk) • Graphviz
```

### Installation
```bash
git clone https://github.com/yourrepo/code-fortress.git
cd code-fortress
pip install -r requirements.txt  # Includes semgrep==1.32.0, trufflehog==3.4.0
```

### Usage
```bash
python gui_app.py  # Launches main interface
# OR for web mode:
streamlit run web_ui.py --server.port 8000
```

## 📊 Example Telemetry
```plaintext
[Code Fortress v1.2.0] Scanning /src...
✔ Loaded 18 detection rules (CWE-798, CWE-259, etc.)
❗ Found 4 criticals in auth_service.py:
  - Hardcoded AWS key (Confidence: 95%, Context: line 42)
  - SQL injection vector (Confidence: 88%, Context: lines 153-167)
📊 Risk distribution: 78% Secrets • 22% Injection
🛡️ Mitigation advisories generated (view in Reports tab)
```

## 📜 License
MIT © 2023 Code Fortress Team  
See [LICENSE](LICENSE) for full terms.
```
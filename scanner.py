import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
from google import genai
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

def add_colors_to_output(text):
    """Add colors to severity levels in the output."""
    text = text.replace("SEVERITY: CRITICAL", f"SEVERITY: {Fore.RED}{Style.BRIGHT}CRITICAL{Style.RESET_ALL}")
    text = text.replace("SEVERITY: HIGH", f"SEVERITY: {Fore.YELLOW}{Style.BRIGHT}HIGH{Style.RESET_ALL}")
    text = text.replace("SEVERITY: MEDIUM", f"SEVERITY: {Fore.BLUE}MEDIUM{Style.RESET_ALL}")
    text = text.replace("SEVERITY: LOW", f"SEVERITY: {Fore.GREEN}LOW{Style.RESET_ALL}")
    return text

def scan_file(filepath):
    """Read a file and analyze it for vulnerabilities."""
    try:
        with open(filepath, 'r') as f:
            code = f.read()

        print(f"\n{'=' * 60}")
        print(f"Scanning: {filepath}")
        print(f"{'=' * 60}\n")

        # Use the existing security prompt
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=security_prompt.format(code=code))
        output = add_colors_to_output(response.text)
        print(output)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{filepath}' not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")


# Configure with your API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

security_prompt = """
Analyze this code for security vulnerabilities. Be concise.

For each issue use this exact format:

---
SEVERITY: [CRITICAL/HIGH/MEDIUM/LOW]
TYPE: [Vulnerability Name]
DESCRIPTION: [One sentence explaining the issue]
IMPACT: [One sentence on potential damage]
FIX: [Code snippet only]
---

Code:
{code}
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Usage: python scanner.py <filepath>{Style.RESET_ALL}")
        print(f"Example: python scanner.py vulnerable.py")
        sys.exit(1)
    
    filepath = sys.argv[1]
    scan_file(filepath)
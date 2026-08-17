# Root Streamlit entrypoint for Streamlit Cloud & local execution
import os
import sys

# Add project root and GiveMeSomeCredit to python path
root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
give_me_dir = os.path.join(root_dir, 'GiveMeSomeCredit')
if give_me_dir not in sys.path:
    sys.path.insert(0, give_me_dir)

# Execute the application
with open(os.path.join(give_me_dir, 'app.py'), 'r') as f:
    code = f.read()

exec(code, globals())

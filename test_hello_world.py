import sys
from io import StringIO
from hello_world import main

def test_main():
    """Test that main() prints Hello, World!"""
    
    # Capture stdout
    captured = StringIO()
    sys.stdout = captured
    
    try:
        main()
    finally:
        sys.stdout = sys.__stdout__
    
    output = captured.getvalue().strip()
    assert output == "Hello, World!", f"Expected 'Hello, World!' but got '{output}'"
    print("Test passed: test_main()")

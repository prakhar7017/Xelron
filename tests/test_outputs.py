import os
import subprocess
import pytest

# Path to the compiled binary
BINARY_PATH = "./reverse"

def test_compilation():
    """Test that the program compiles successfully with make"""
    # Clean any previous build
    subprocess.run(["make", "clean"], check=False)
    
    # Compile the program
    result = subprocess.run(["make"], capture_output=True, text=True)
    
    # Check if compilation was successful
    assert result.returncode == 0, f"Compilation failed with error: {result.stderr}"
    assert os.path.exists(BINARY_PATH), f"Binary '{BINARY_PATH}' was not created"

def test_reverse_hello():
    """Test that 'hello' is correctly reversed to 'olleh'"""
    result = subprocess.run([BINARY_PATH, "hello"], capture_output=True, text=True)
    assert result.returncode == 0, f"Program crashed with error: {result.stderr}"
    assert result.stdout.strip() == "olleh", f"Expected 'olleh', got '{result.stdout.strip()}'"

def test_reverse_abcd():
    """Test that 'abcd' is correctly reversed to 'dcba'"""
    result = subprocess.run([BINARY_PATH, "abcd"], capture_output=True, text=True)
    assert result.returncode == 0, f"Program crashed with error: {result.stderr}"
    assert result.stdout.strip() == "dcba", f"Expected 'dcba', got '{result.stdout.strip()}'"

def test_empty_string():
    """Test that an empty string is handled correctly"""
    result = subprocess.run([BINARY_PATH, ""], capture_output=True, text=True)
    assert result.returncode == 0, f"Program crashed with error: {result.stderr}"
    assert result.stdout.strip() == "", f"Expected empty string, got '{result.stdout.strip()}'"

def test_single_character():
    """Test that a single character string is handled correctly"""
    result = subprocess.run([BINARY_PATH, "a"], capture_output=True, text=True)
    assert result.returncode == 0, f"Program crashed with error: {result.stderr}"
    assert result.stdout.strip() == "a", f"Expected 'a', got '{result.stdout.strip()}'"

def test_long_string():
    """Test that a long string is handled correctly"""
    long_string = "ThisIsALongStringToTestMemoryAllocation"
    expected = long_string[::-1]  # Python's way to reverse a string
    result = subprocess.run([BINARY_PATH, long_string], capture_output=True, text=True)
    assert result.returncode == 0, f"Program crashed with error: {result.stderr}"
    assert result.stdout.strip() == expected, f"Expected '{expected}', got '{result.stdout.strip()}'"

def test_no_memory_leaks():
    """Test that the program has no memory leaks using valgrind"""
    # Run valgrind to check for memory leaks
    result = subprocess.run(
        ["valgrind", "--leak-check=full", "--error-exitcode=1", BINARY_PATH, "hello"],
        capture_output=True,
        text=True
    )
    
    # Check if valgrind found any memory leaks
    assert result.returncode == 0, f"Memory leak detected: {result.stderr}"

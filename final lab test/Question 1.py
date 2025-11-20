from typing import Dict
import unittest

PROMPTS: Dict[str, str] = {}
PROMPTS["initial"] = ("You are an expert Python developer. Generate optimized matrix multiplication "
                      "code for large matrices. Provide a Python module with a function that multiplies "
                      "two 2D NumPy arrays efficiently. Include docstrings and unit tests.")
PROMPTS["improved"] = ("High-performance matrix multiplication module for large 2D NumPy arrays. "
                       "Requirements: blocking/tiled algorithm, optional numba JIT path, clear docstring, "
                       "matmul(a,b,*,block_size=64,use_numba=True), dtype and contiguity handling, input validation, "
                       "support float32/float64, unit tests and a benchmark helper, Python 3.8+ compatible.")
# final must contain keywords checked by tests: blocking, numpy, numba, docstring, unit tests
PROMPTS["final"] = ("Produce a single Python module implementing high-performance, blocking (tiled) matrix "
                    "multiplication for large 2D NumPy arrays. Include an optional numba JIT path, a clear "
                    "module and function docstring, type hints, input validation, unit tests (unit tests) "
                    "covering float32/float64 and edge cases, and a benchmark helper. Keep dependencies to NumPy "
                    "and optionally numba; ensure code runs without numba. Document complexity and when copies occur.")

class PromptTests(unittest.TestCase):
    def test_contains_blocking(self):
        self.assertIn("blocking", PROMPTS["final"].lower())
    def test_contains_numpy(self):
        self.assertIn("numpy", PROMPTS["final"].lower())
    def test_contains_numba(self):
        self.assertIn("numba", PROMPTS["final"].lower())
    def test_contains_docstring(self):
        self.assertIn("docstring", PROMPTS["final"].lower())
    def test_contains_tests(self):
        self.assertIn("unit tests", PROMPTS["final"].lower() or "pytest", PROMPTS["final"].lower())

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(PromptTests)
    runner.run(suite)
    print("\n--- FINAL PROMPT (copy this into an AI prompt window) ---\n")
    print(PROMPTS["final"])

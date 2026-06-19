import time
from pathlib import Path

class Benchmark:
    def __init__(self, models=None):
        self.models = models or ['tesseract']
    
    def run(self, image_dir):
        results = {}
        for model in self.models:
            start = time.time()
            # placeholder for actual inference
            elapsed = time.time() - start
            results[model] = {'time': elapsed, 'accuracy': 0.0}
        return Results(results)

class Results:
    def __init__(self, data):
        self.data = data
    
    def summary(self):
        for model, metrics in self.data.items():
            print(f"{model}: {metrics}")

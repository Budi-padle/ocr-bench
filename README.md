# ocr-bench

Lightweight OCR benchmarking toolkit for comparing Tesseract, TrOCR, and PaddleOCR.

## Install

```bash
pip install ocr-bench
```

## Usage

```python
from ocr_bench import Benchmark

bench = Benchmark(models=['tesseract', 'trocr'])
results = bench.run('test_images/')
results.summary()
```

from ocr_bench import Benchmark

def test_benchmark_init():
    bench = Benchmark(models=['tesseract'])
    assert bench.models == ['tesseract']

def test_benchmark_run():
    bench = Benchmark()
    # results = bench.run('test_images/')
    # assert results is not None

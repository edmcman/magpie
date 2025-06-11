import subprocess
import pathlib
import magpie.utils.known
from magpie.core import BasicFitness


class MetricFitness(BasicFitness):
    def process_test_exec(self, run_result, exec_result):
        super().process_test_exec(run_result, exec_result)
        # Call the custom metric.py script
        try:
            print(f"DEBUG: Calling metric.py from directory: {pathlib.Path.cwd()}")
            result = subprocess.run(
                ['python3', 'metric.py'], 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            print(f"DEBUG: metric.py return code: {result.returncode}")
            print(f"DEBUG: metric.py stdout: '{result.stdout.strip()}'")
            print(f"DEBUG: metric.py stderr: '{result.stderr.strip()}'")
            
            if result.returncode == 0:
                fitness_value = float(result.stdout.strip())
                print(f"DEBUG: Setting fitness to: {fitness_value}")
                run_result.fitness = fitness_value
            else:
                print("DEBUG: Setting fitness to infinity due to non-zero return code")
                run_result.fitness = float('inf')
        except Exception as e:
            print(f"DEBUG: Exception occurred: {e}")
            run_result.fitness = float('inf')

magpie.utils.known.fitness.append(MetricFitness)

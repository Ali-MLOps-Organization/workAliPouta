# submit_run.py
import kfp
import sys

sys.path.append('../src')
from pipelines.pipeline_definitions.pipeline_definition import pipeline
from pipelines.pipeline_arg.pipeline_arg import arguments

def submit_pipeline():

    client = kfp.Client() 
    

    # Define your experiment and run name
    experiment_name = "demo-experiment"
    run_name = "demo-run-through-github-actions-on-OSS-MLOps-platform-in-development-environment"

    # Submit the pipeline run
    client.create_run_from_pipeline_func(
        pipeline_func=pipeline,
        arguments=arguments,
        run_name=run_name,
        experiment_name=experiment_name,
        mode=kfp.dsl.PipelineExecutionMode.V2_COMPATIBLE,
        enable_caching=False,
    )

if __name__ == "__main__":
    submit_pipeline()
# Test commit for pipeline execution via GitHub Actions runner
# Test commit 2 for pipeline after forcing kfp==1.8.2
# Test commit 3 for pipeline. Last fix was not 1.8.2 but 1.8.3. Corrected
# now.
# Test commit 4 for pipeline. Changed git runner workflow to install kfp 1.8.2 also.
# Test commit 5. Fix previous.
# Test commit 6. Change runner to utilize python 3.11

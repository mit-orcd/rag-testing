import os

from unstructured_ingest.connector.local import SimpleLocalConfig
from unstructured_ingest.interfaces import PartitionConfig, ProcessorConfig, ReadConfig
from unstructured_ingest.runner import LocalRunner

output_path = "../unstructured_output/engaging"

runner = LocalRunner(
    processor_config=ProcessorConfig(
        # logs verbosity
        verbose=True,
        # the local directory to store outputs
        output_dir=output_path,
        num_processes=2,
    ),
    read_config=ReadConfig(),
    partition_config=PartitionConfig(
        encoding="latin1",
        partition_by_api=False        
    ),
    connector_config=SimpleLocalConfig(
        input_path="../engaging_docs",
        # whether to get the documents recursively from given directory
        recursive=False,
    ),
)
if __name__ == "__main__":
    runner.run()


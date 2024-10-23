import os

from unstructured.ingest.connector.local import SimpleLocalConfig
from unstructured.ingest.interfaces import PartitionConfig, ProcessorConfig, ReadConfig
from unstructured.ingest.runner import LocalRunner

output_path = "./unstructured-output"

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
        partition_by_api=True,
        api_key="BDGDwHkmiukv6lPU8SM4is90MWILF1",
    ),
    connector_config=SimpleLocalConfig(
        input_path="./orcd_docs",
        # whether to get the documents recursively from given directory
        recursive=False,
    ),
)
if __name__ == "__main__":
    runner.run()


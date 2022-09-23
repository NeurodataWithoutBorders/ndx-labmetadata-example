# ndx-labmetadata-example Extension for NWB

This is an example extension to illustrate how to extend the ``LabMetaData`` type from NWB to add lab-specific metadata. This extension is **NOT** intended for use in practice but is intended only as an example to illustrate how to generate an NWB extension using the ``LabMetaData`` type.

## Installation

```
pip install .
```

## Usage

```python

from pynwb.file import NWBFile, Subject
from ndx_labmetadata_example import LabMetaDataExtensionExample
from pynwb import NWBHDF5IO
from uuid import uuid4
from datetime import datetime

# create an example NWBFile
nwbfile = NWBFile(
    session_description="test session description",
    identifier=str(uuid4()),
    session_start_time=datetime(1970, 1, 1),
    subject=Subject(
        age="P50D",
        description="example mouse",
        sex="F",
        subject_id="test_id")
)

# create our custom lab metadata
lab_meta_data = LabMetaDataExtensionExample(tissue_preparation="Example tissue preparation")

# Add the test LabMetaDataExtensionExample to the NWBFile
nwbfile.add_lab_meta_data(lab_meta_data=lab_meta_data)

# Write the file to disk
with NWBHDF5IO(path=self.filename, mode='a') as io:
    io.write(nwbfile)

# Read the file from disk
with NWBHDF5IO(path=self.filename, mode='r') as io:
    in_nwbfile = io.read()
    in_lab_meta_data = in_nwbfile.get_lab_meta_data(lab_meta_data.name)
    assert lab_meta_data.tissue_preparation == in_lab_meta_data.tissue_preparation

```

---
This extension was created using [ndx-template](https://github.com/nwb-extensions/ndx-template).

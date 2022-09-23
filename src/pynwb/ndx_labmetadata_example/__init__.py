import os
from pynwb import load_namespaces, get_class

# Set path of the namespace.yaml file to the expected install location
ndx_labmetadata_example_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-labmetadata-example.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_labmetadata_example_specpath):
    ndx_labmetadata_example_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-labmetadata-example.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_labmetadata_example_specpath)

# them accessible at the package level
LabMetaDataExtensionExample = get_class('LabMetaDataExtensionExample', 'ndx-labmetadata-example')
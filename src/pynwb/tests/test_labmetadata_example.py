from pynwb.testing.mock.file import mock_NWBFile
from pynwb.testing import TestCase
from pynwb.testing.testh5io import NWBH5IOMixin

from ndx_labmetadata_example import LabMetaDataExtensionExample


class TestLabMetaDataExtensionExample(TestCase):

    def setUp(self):
        """Set up an NWB file. Necessary because TetrodeSeries requires references to electrodes."""
        self.nwbfile = mock_NWBFile()

    def test_constructor(self):
        """Test that the constructor for TetrodeSeries sets values as expected."""
        tissue_preparation = "Example tissue preparation"
        lmdee_object = LabMetaDataExtensionExample(tissue_preparation=tissue_preparation)
        self.assertEqual(lmdee_object.tissue_preparation, tissue_preparation)


class TestLabMetaDataExtensionExampleRoundtrip(NWBH5IOMixin, TestCase):
    """Roundtrip test for LabMetaDataExtensionExample pynwb.testing infrastructure."""

    def setUpContainer(self):
        """set up example LabMetaDataExtensionExample object"""
        self.lab_meta_data = LabMetaDataExtensionExample(tissue_preparation="Example tissue preparation")
        return self.lab_meta_data

    def addContainer(self, nwbfile):
        """Add the test LabMetaDataExtensionExample to the given NWBFile."""
        nwbfile.add_lab_meta_data(lab_meta_data=self.lab_meta_data)

    def getContainer(self, nwbfile):
        """Get the LabMetaDataExtensionExample object from the given NWBFile."""
        return nwbfile.get_lab_meta_data(self.lab_meta_data.name)

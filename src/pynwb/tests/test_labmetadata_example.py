from pynwb.testing.mock.file import mock_NWBFile
from pynwb.testing import TestCase
from pynwb.testing.testh5io import NWBH5IOMixin

from ndx_labmetadata_example import LabMetaDataExtensionExample


class TestLabMetaDataExtensionExample(TestCase):
    """Test basic functionality of LabMetaDataExtensionExample without read/write"""

    def setUp(self):
        """Set up an NWB file. Necessary because TetrodeSeries requires references to electrodes."""
        self.nwbfile = mock_NWBFile()

    def test_constructor(self):
        """Test that the constructor for TetrodeSeries sets values as expected."""
        tissue_preparation = "Example tissue preparation"
        lmdee_object = LabMetaDataExtensionExample(tissue_preparation=tissue_preparation)
        self.assertEqual(lmdee_object.tissue_preparation, tissue_preparation)


class TestLabMetaDataExtensionExampleRoundtrip(NWBH5IOMixin, TestCase):
    """
    Roundtrip test for LabMetaDataExtensionExample to test read/write

    This test class writes the LabMetaDataExtensionExample to an NWBFile, then
    reads the data back from the file, and compares that the data read from file
    is consistent with the original data. Using the pynwb.testing infrastructure
    simplifies this complex test greatly by allowing to simply define how to
    create the container, add to a file, and retrieve it form a file. The
    task of writing, reading, and comparing the data is then taken care of
    automatically by the NWBH5IOMixin.
    """

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


class TestReadmeExample(TestCase):
    """
    Run the example that is show in the README
    """

    def setUp(self) -> None:
        self.filename = 'testfile.nwb'

    def tearDown(self) -> None:
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_readme_script(self):
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
        filename = 'testfile.nwb'
        with NWBHDF5IO(path=filename, mode='a') as io:
            io.write(nwbfile)

        # Read the file from disk
        with NWBHDF5IO(path=filename, mode='r') as io:
            in_nwbfile = io.read()
            in_lab_meta_data = in_nwbfile.get_lab_meta_data(lab_meta_data.name)
            assert lab_meta_data.tissue_preparation == in_lab_meta_data.tissue_preparation


# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.contents_api import ContentsApi


class TestContentsApi(unittest.TestCase):
    """ContentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContentsApi()

    def tearDown(self) -> None:
        pass

    def test_api_contents_path_checkpoints_checkpoint_id_delete(self) -> None:
        """Test case for api_contents_path_checkpoints_checkpoint_id_delete

        Delete a checkpoint
        """
        pass

    def test_api_contents_path_checkpoints_checkpoint_id_post(self) -> None:
        """Test case for api_contents_path_checkpoints_checkpoint_id_post

        Restore a file to a particular checkpointed state
        """
        pass

    def test_api_contents_path_checkpoints_get(self) -> None:
        """Test case for api_contents_path_checkpoints_get

        Get a list of checkpoints for a file
        """
        pass

    def test_api_contents_path_checkpoints_post(self) -> None:
        """Test case for api_contents_path_checkpoints_post

        Create a new checkpoint for a file
        """
        pass

    def test_api_contents_path_delete(self) -> None:
        """Test case for api_contents_path_delete

        Delete a file in the given path
        """
        pass

    def test_api_contents_path_get(self) -> None:
        """Test case for api_contents_path_get

        Get contents of file or directory
        """
        pass

    def test_api_contents_path_patch(self) -> None:
        """Test case for api_contents_path_patch

        Rename a file or directory without re-uploading content
        """
        pass

    def test_api_contents_path_post(self) -> None:
        """Test case for api_contents_path_post

        Create a new file in the specified path
        """
        pass

    def test_api_contents_path_put(self) -> None:
        """Test case for api_contents_path_put

        Save or upload file.
        """
        pass


if __name__ == '__main__':
    unittest.main()
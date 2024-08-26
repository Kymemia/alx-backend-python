#!/usr/bin/env python3

"""
test_case for client.py file
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from typing import Dict, List
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    class definition for GithubOrgClient's test case
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json):
        """
        method definition that tests GithubOrg client
        """
        mock_get_json.return_value = {"org": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"org": org_name})
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )

    def test_public_repos_url(self):
        """
        this is a test that returns the required URL
        """
        with patch.object(
                GithubOrgClient, 'org',
                new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = {
                    "repos_url": "https://api.github.com/orgs/google/repos"
                    }
            client = GithubOrgClient("google")
            result = client._public_repos_url
            expected_result = "https://api.github.com/orgs/google/repos"
            self.assertEqual(result, expected_result)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        this is a test that returns a list of repositories
        based on mocked payload
        """
        test_payload = [{"name": "first_repo"}, {"name": "second_repo"}]
        mock_get_json.return_value = test_payload

        mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"
        client = GithubOrgClient("test")
        repos = client.public_repos()
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")
        self.assertEqual(repos, ["first_repo", "second_repo"])


if __name__ == "__main__":
    unittest.main()

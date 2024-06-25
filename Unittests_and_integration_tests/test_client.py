#!/usr/bin/env python3
""" Unittest Test client """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    '''Test class for GithubOrgClient'''

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''Test that GithubOrgClient.org returns the correct value'''
        endpoint = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.return_value = {"dummy_key": "dummy_value"}

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_get_json.return_value)

        mock_get_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, org_name, result):
        '''Test the _public_repos_url property'''
        with patch('client.GithubOrgClient.org', PropertyMock(return_value=result)):
            client = GithubOrgClient(org_name)
            self.assertEqual(client._public_repos_url, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        '''Test the public_repos method'''
        payload = [{"name": "Google"}, {"name": "TT"}]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://some_url.com"

            client = GithubOrgClient('test')
            self.assertEqual(client.public_repos(), ["Google", "TT"])

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://some_url.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''Test the has_license method'''
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class(['org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test for GithubOrgClient'''

    @classmethod
    def setUpClass(cls):
        '''Set up class'''
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''Tear down class'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Test public repos'''
        client = GithubOrgClient('test_org')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        '''Test public repos with license'''
        client = GithubOrgClient('test_org')
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == '__main__':
    unittest.main()

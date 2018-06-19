#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_ipify` package."""


import unittest
from unittest.mock import patch, Mock

from python_ipify.ip import my_ip


class TestPython_ipify(unittest.TestCase):
    """Tests for `python_ipify` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @patch('requests.get')
    def test_000_get_ip(self, get):
        """Test something."""
        req = Mock()
        req.ok = True
        req.text = '1.2.3.4'
        get.return_value = req
        s = my_ip()
        get.assert_called_with('http://members.3322.org/dyndns/getip')
        self.assertEqual(s, '1.2.3.4')

    @patch('requests.get')
    def test_001_network_failure(self, get):
        """Test something."""
        req = Mock()
        req.ok = False
        req.text = '1.2.3.4'
        get.return_value = req
        s = None
        with self.assertRaisesRegex(Exception, '^network error$'):
            s = my_ip()
        get.assert_called_with('http://members.3322.org/dyndns/getip')
        self.assertIsNone(s)

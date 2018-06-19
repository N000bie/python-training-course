#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_ipify` package."""


import unittest

from python_ipify.ip import my_ip
from requests_mock import Mocker


class TestPython_ipify(unittest.TestCase):
    """Tests for `python_ipify` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @Mocker()
    def test_000_get_ip(self, m):
        """Test something."""
        m.get('http://members.3322.org/dyndns/getip', text='1.2.3.4')
        s = my_ip()
        self.assertEqual(s, '1.2.3.4')

    @Mocker()
    def test_001_network_error(self, m):
        """Test something."""
        m.get('http://members.3322.org/dyndns/getip', text='1.2.3.4', status_code=404)
        s = None
        with self.assertRaisesRegex(Exception, '^network error$'):
            s = my_ip()
        self.assertIsNone(s)

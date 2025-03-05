# -*- coding: utf-8 -*-
import unittest

from a3exception.dynamic_error_factory import DynamicErrorFactory
from a3exception import errors


class T(unittest.TestCase):
    def test__build_error_by_status__success(self):
        error = DynamicErrorFactory.build_error_by_status(
            status=errors.NotFoundError.__name__
        )
        self.assertTrue(isinstance(error, errors.NotFoundError))

        error = DynamicErrorFactory.build_error_by_status(
            status=errors.NotAvailableError.__name__
        )
        self.assertTrue(isinstance(error, errors.NotAvailableError))

    def test__build_error_by_status__error(self):
        class CustomError(errors.Error):
            error_type = None

        with self.assertRaises(errors.PanicError):
            DynamicErrorFactory.build_error_by_status(status=CustomError.__name__)

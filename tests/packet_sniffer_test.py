import unittest
from unittest.mock import MagicMock
from model.PacketModel import PacketModel
from controller.PacketSnifferController import PacketSnifferController

class TestPacketSnifferController(unittest.TestCase):
    def setUp(self):
        self.view_mock = MagicMock()
        self.controller = PacketSnifferController(self.view_mock)

    def test_start_capture(self):
        # Mock the view's button configurations
        self.view_mock.start_button.configure = MagicMock()
        self.view_mock.stop_button.configure = MagicMock()

        # Call the method
        self.controller.start_capture()

        # Assert that the view's buttons were configured correctly
        self.view_mock.start_button.configure.assert_called_with(state='disabled')
        self.view_mock.stop_button.configure.assert_called_with(state='normal')

    def test_stop_capture(self):
        # Mock the view's button configurations
        self.view_mock.start_button.configure = MagicMock()
        self.view_mock.stop_button.configure = MagicMock()
        self.view_mock.filter.configure_button = MagicMock()

        # Mock the model's save_to_csv method
        self.controller.model.save_to_csv = MagicMock()

        # Call the method
        self.controller.stop_capture()

        # Assert that the view's buttons were configured correctly
        self.view_mock.start_button.configure.assert_called_with(state='normal')
        self.view_mock.stop_button.configure.assert_called_with(state='disabled')
        self.view_mock.filter.configure_button.assert_called_with(state='normal')

        # Assert that the model's save_to_csv method was called
        self.controller.model.save_to_csv.assert_called_with('captured_packets.csv')

    
    def test_set_filter_by(self):
        # Call the method
        self.controller.set_filter_by('src')

        # Assert that filter_by was set correctly
        self.assertEqual(self.controller.filter_by, 'src')

        # Call the method again with a different value
        self.controller.set_filter_by('dst')

        # Assert that filter_by was updated
        self.assertEqual(self.controller.filter_by, 'dst')

    def test_set_filter_value(self):
        # Call the method
        self.controller.set_filter_value('192.168.0.1')

        # Assert that filter_value was set correctly
        self.assertEqual(self.controller.filter_value, '192.168.0.1')

        # Call the method again with a different value
        self.controller.set_filter_value('10.0.0.1')

        # Assert that filter_value was updated
        self.assertEqual(self.controller.filter_value, '10.0.0.1')

if __name__ == '__main__':
    unittest.main()

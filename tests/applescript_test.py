import unittest
from i2ssh.layout import Layout
from i2ssh.applescript import AppleScript

class AppleScriptTest(unittest.TestCase):

    def test_layout_cmds(self):
        config = {'hosts': [''], 'layout': '3x2'}
        script = AppleScript(config, Layout(config))
        layout_cmds = script._namespace['layout_cmds']
        self.assertEqual(['d', '[', 'D', ']', 'd', '[', 'D', ']', 'D', ']'], layout_cmds)

    def test_panes(self):
        config = {'hosts': ['host1', 'host2', 'host3']}
        script = AppleScript(config, Layout(config))
        panes = script._namespace['panes']
        self.assertEqual(4, len(panes))
        self.assertEqual({'name': 'host1', 'cmd': 'ssh host1'}, panes[0])
        self.assertEqual({'name': 'host2', 'cmd': 'ssh host2'}, panes[1])
        self.assertEqual({'name': 'host3', 'cmd': 'ssh host3'}, panes[2])
        self.assertEqual({'name': 'Disabled', 'cmd': script._DISABLED_CMD}, panes[3])


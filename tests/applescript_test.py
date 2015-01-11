import unittest
from i2ssh.layout import Layout
from i2ssh.applescript import AppleScript

class AppleScriptTest(unittest.TestCase):

    def test_layout_cmds(self):
        config = {'hosts': [''], 'layout': '3x2'}
        script = AppleScript(config, Layout(config))
        layout_cmds = script._namespace['layout_cmds']
        self.assertEquals(['d', '[', 'D', ']', 'd', '[', 'D', ']', 'D', ']'], layout_cmds)

    def test_panes(self):
        config = {'hosts': ['host1', 'host2', 'host3']}
        script = AppleScript(config, Layout(config))
        panes = script._namespace['panes']
        self.assertEquals(3, len(panes))
        self.assertEquals({'name': 'host1', 'cmd': 'ssh host1'}, panes[0])
        self.assertEquals({'name': 'host2', 'cmd': 'ssh host2'}, panes[1])
        self.assertEquals({'name': 'host3', 'cmd': 'ssh host3'}, panes[2])


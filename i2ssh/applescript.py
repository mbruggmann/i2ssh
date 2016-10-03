#!/usr/bin/env python
import os
import logging
import sys
import subprocess
import tempfile
from quik import Template

# iTerm2 AppleScript adapted from
# https://github.com/luismartingil/per.scripts/blob/master/iterm_launcher02.applescript
# Author: Luis Martin Gil
# Website: http://www.luismartingil.com/

class AppleScript:
    '''Generates and launches a temporary AppleScript to configure iTerm2.'''

    _DEFAULT_CMD = 'ssh'
    _DEFAULT_DELAY = 0.1
    _DISABLED_CMD = 'stty -isig -icanon -echo && echo UNUSED && cat > /dev/null'
    _TEMPLATE = '''
        tell application "iTerm"
            -- panes
            set panes to {}
            #for @pane in @panes:
            set panes to panes & {{cmd:"unset HISTFILE && @pane.cmd", name:"@pane.name"}}
            #end

            -- layout @layout_name
            set layout to {} #for @layout_cmd in @layout_cmds: &{"@layout_cmd"}#end

            set myterm to (create window with default profile)

            tell myterm
                launch session 1
            end tell

            set the bounds of front window to {@window.x, @window.y, @window.tx, @window.ty}

            tell myterm
                -- set up layout
                repeat with currentLayout in items of layout
                    tell application "System Events" to keystroke currentLayout using command down
                    delay @delay
                end repeat
                -- execute commands in active tabs
                repeat with currentPane in items of panes
                    delay @delay
                    tell the current session
                        set name to name of currentPane
                        write text cmd of currentPane
                        tell application "System Events" to keystroke "]" using command down
                    end tell
                end repeat
            end tell
        end tell
    '''

    def __init__(self, config, layout, window):
        hosts = config['hosts']
        if 'user' in config.keys():
            hosts = map(lambda host: "{0}@{1}".format(config['user'], host), hosts)
        cmd = config.get('cmd', self._DEFAULT_CMD)
        delay = config.get('delay', self._DEFAULT_DELAY)

        namespace = {}
        namespace['panes'] = self._panes(layout, cmd, hosts)
        namespace['layout_name'] = layout
        namespace['layout_cmds'] = self._layout_cmds(layout)
        namespace['delay'] = delay
        namespace['window'] = self._window(window)
        self._namespace = namespace

    def _panes(self, layout, cmd, hosts):
        enabled = [{'cmd': '%s %s'%(cmd, hostname), 'name': hostname} for hostname in hosts]
        disabled = layout.disabled * [{'cmd': self._DISABLED_CMD, 'name': 'Disabled'}]
        return enabled + disabled

    def _layout_cmds(self, layout):
        cols = layout.cols
        rows = layout.rows

        splits = []
        for i in range(0, cols):
            if i < cols-1:
                splits.append('d')
                splits.append('[')
            for j in range(0, rows-1):
                splits.append('D')
            splits.append(']')
        return splits

    def _window(self, window):
        return {'x': window.origin.x, 'y': window.origin.y,
                'tx': window.origin.x + window.size.width,
                'ty': window.origin.y + window.size.height}

    def launch(self):
        template = Template(self._TEMPLATE)
        self.script = template.render(self._namespace)

        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(self.script)
        temp.close()

        logging.debug('Launch AppleScript at %s: %s', temp.name, self.script)
        subprocess.call('osascript %s' % temp.name, shell=True)
        os.unlink(temp.name)


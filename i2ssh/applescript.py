#!/usr/bin/env python
import os
import logging
import sys
import subprocess
import tempfile

# iTerm2 AppleScript adapted from
# https://github.com/luismartingil/per.scripts/blob/master/iterm_launcher02.applescript
# Author: Luis Martin Gil
# Website: http://www.luismartingil.com/

pane_template = '    set tab1 to tab1 & {{cmd:"%s", name:"%s", split:"%s"}}'

code_template = '''
tell application "iTerm"
    set tab1 to {}
%s
    set myterm to (make new terminal)
    tell myterm
        launch session 1
        repeat with currentPane in items of tab1
            tell the last session
                -- set name to name of currentPane
                write text cmd of currentPane
                if "h" is split of currentPane then
                    tell i term application "System Events" to keystroke "D" using command down
                else if "v" is split of currentPane then
                    tell i term application "System Events" to keystroke "d" using command down
                end if
            end tell
            delay 1
        end repeat
    end tell
end tell
'''


def pane_snippet(cmd=None, name="Default", split=None):
    return pane_template % (cmd, name, split)


def launch(config):
    # Construct the applescript
    panes = [pane_snippet('ls', hostname, 'v') for hostname in config['hosts']]
    body = code_template % ('\n'.join(panes))

    # Write it to a temporary file
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(body)
    temp.close()
    logging.debug('Applescript at %s: %s', temp.name, body)

    subprocess.call('osascript %s' % temp.name, shell=True)
    os.unlink(temp.name)


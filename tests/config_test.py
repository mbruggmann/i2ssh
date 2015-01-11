import os
from testfixtures import tempdir
import unittest
import yaml
from i2ssh.config import Config

FILENAME = '.i2sshrc'

class ConfigTest(unittest.TestCase):

    @tempdir()
    def test_cluster(self, tmpdir):
        cluster_config = {'hosts': ['host1']}
        full_config = {'mycluster': cluster_config}

        tmpdir.write(FILENAME, yaml.dump(full_config, default_flow_style=False).encode('utf-8'))
        config = Config(os.path.join(tmpdir.path, FILENAME))

        self.assertEqual(cluster_config, config.cluster('mycluster'))


import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HELPER = Path(__file__).with_name('stage.py')


class StageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.vault = self.root / 'vault'
        (self.vault / '.obsidian/plugins/work-log').mkdir(parents=True)
        (self.vault / 'References').mkdir()
        (self.vault / 'References/Alex Example.md').write_text('# Alex Example')
        self.config = self.root / 'config.json'
        self.config.write_text(json.dumps({'vault': str(self.vault)}))
        self.input = self.root / 'batch.json'
        self.batch = {
            'period': {'start': '2030-01-02', 'end': '2030-01-02'},
            'coverage': {'custom_meeting_provider': {'status': 'checked', 'detail': 'Synthetic evidence.'}},
            'entries': [{'event_key': 'fixture:one', 'title': 'Useful update', 'date': '2030-01-02',
                         'category': 'technical', 'related_notes': ['References/Alex Example.md'],
                         'sources': [{'label': 'Evidence', 'target': 'https://example.com/context'}],
                         'description': 'Shared a technical update.\n- https://example.com/context'}]}

    def tearDown(self):
        self.temp.cleanup()

    def run_helper(self, *args):
        self.input.write_text(json.dumps(self.batch))
        return subprocess.run([sys.executable, str(HELPER), '--config', str(self.config),
                               '--input', str(self.input), *args], capture_output=True, text=True)

    def test_custom_provider_config_dry_run_and_create_only(self):
        preview = self.run_helper('--dry-run')
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse((self.vault / 'Work Log Inbox').exists())
        result = self.run_helper()
        self.assertEqual(result.returncode, 0, result.stderr)
        path = self.vault / json.loads(result.stdout)['created'][0]
        original = path.read_text()
        self.assertIn('"pending"', original)
        self.assertIn(self.batch['entries'][0]['description'], original)
        path.write_text(original.replace('"pending"', '"dismissed"') + '\nUser edit\n')
        edited = path.read_bytes()
        self.batch['entries'][0]['description'] = 'Changed generated wording'
        repeated = self.run_helper()
        self.assertEqual(repeated.returncode, 0, repeated.stderr)
        self.assertEqual(json.loads(repeated.stdout)['created'], [])
        self.assertEqual(path.read_bytes(), edited)

    def test_missing_explicit_config_fails_without_writes(self):
        self.config.unlink()
        result = self.run_helper()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.vault / 'Work Log Inbox').exists())

    def test_invalid_coverage_fails_before_writes(self):
        self.batch['coverage'] = {}
        result = self.run_helper()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.vault / 'Work Log Inbox').exists())


if __name__ == '__main__':
    unittest.main()

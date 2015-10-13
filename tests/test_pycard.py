
from click.testing import CliRunner

from pycard.main import cli


def test_pycard_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['help'])

    assert 'USAGE: PicardCommandLine' in result.output
    assert result.exit_code == 0


def test_pycard_do():
    runner = CliRunner()
    result = runner.invoke(cli, ['do', 'FilterVcf'])

    assert 'USAGE: FilterVcf [options]' in result.output
    assert result.exit_code == 0

# def test

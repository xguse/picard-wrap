import os

import pytest

import click
from click.testing import CliRunner

import pycard.main as main

echo = click.echo


@pytest.fixture
def os_environ(request):
    environ_ = os.environ.copy()
    os.environ.clear()

    def reset_os():
        echo("resetting os module.")
        os.environ = environ_

    request.addfinalizer(reset_os)
    return os


def test_pycard_help():
    runner = CliRunner()
    result = runner.invoke(main.cli, ['help'])

    assert 'USAGE: PicardCommandLine' in result.output
    assert result.exit_code == 0


def test_pycard_do():
    runner = CliRunner()
    # jvm_args
    # h_flag
    # picard_arg

    result = runner.invoke(main.cli, ['do', 'FilterVcf'])

    assert 'USAGE: FilterVcf [options]' in result.output
    assert result.exit_code == 0


def test_get_picard_path_no_envvars(os_environ):

    with pytest.raises(click.BadParameter):
        # os = os_environ

        main.get_picard_path()


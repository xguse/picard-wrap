#!/usr/bin/env python

import os
import subprocess

import click


# Why does this file exist, and why __main__?
# For more info, read:
# - https://www.python.org/dev/peps/pep-0338/
# - https://docs.python.org/2/using/cmdline.html#cmdoption-m
# - https://docs.python.org/3/using/cmdline.html#cmdoption-m

echo = click.echo


class SystemCallError(StandardError):
    """Error raised when a problem occurs while attempting to run an external system call.

    Attributes:
        | ``err_number`` -- return code from system call
        | ``file_name`` -- file involved if any
        | ``err_msg`` -- error msg """

    def __init__(self, err_number, err_msg, file_name=None):
        self.err_number = err_number
        self.err_msg = err_msg
        self.file_name = file_name

    def __str__(self):
        if not self.file_name:
            return """ERROR: %s.\nRETURN_STATE: %s.""" % (self.err_msg.strip('\n'),
                                                          self.err_number)
        else:
            return """ERROR in %s: %s.\nRETURN_STATE: %s.""" % (self.file_name,
                                                                self.err_msg.strip('\n'),
                                                                self.err_number)


def whereis(program):
    """
    returns path of program if it exists in your ``$PATH`` variable or ``None`` otherwise
    """
    for path in os.environ.get('PATH', '').split(':'):
        if os.path.exists(os.path.join(path, program)) and not os.path.isdir(os.path.join(path, program)):
            return os.path.join(path, program)
    return None


def picard_process(arg_str):
    """
    func to handle calling and monitoring output of java/picard.
    """

    # Ensure program is callable.
    prog_path = whereis("java")
    if not prog_path:
        raise SystemCallError(None, '"%s" command not found in your PATH environmental variable.' % ("java"))

    # Construct shell command
    cmd_str = "%s %s" % (prog_path, arg_str)

    # Set up process obj
    process = subprocess.Popen(cmd_str,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # Get results
    result = process.communicate()

    # Check return code for success/failure
    if process.returncode == 1:
        if "USAGE: PicardCommandLine" in result[1]:
            return result

    elif process.returncode != 0:
        raise SystemCallError(process.returncode, result[1], "java")

    # Return result
    return result


def build_arg_string(picard_path, jvm_arg_str, picard_arg_str):
    arg_string = "{jvm_arg_str} -jar {picard_path} {picard_arg_str}".format(jvm_arg_str=jvm_arg_str,
                                                                            picard_path=picard_path,
                                                                            picard_arg_str=picard_arg_str)
    return arg_string


def call_picard(picard_path, jvm_arg_str='', picard_arg_str=''):
    arg_str = build_arg_string(picard_path=picard_path,
                               jvm_arg_str=jvm_arg_str,
                               picard_arg_str=picard_arg_str)

    stdout, stderr = picard_process(arg_str)

    if stdout:
        echo("STDOUT:\n{stdout}".format(stdout=stdout))
    if stderr:
        echo("STDERR:\n{stderr}".format(stderr=stderr))


def echo_picard_help(ctx):
    call_picard(picard_path=ctx.obj['PICARD'],
                jvm_arg_str='',
                picard_arg_str='')


def get_picard_path(path=None):
    if path is None:
        try:
            picard_path = "{conda_env}/picard/picard.jar".format(conda_env=os.environ['CONDA_ENV_PATH'])

        except KeyError:
            try:
                picard_path = os.environ['PICARD_JAR']

            except KeyError:
                pass

                msg = "If neither 'CONDA_ENV_PATH' or 'PICARD_JAR' have been set as environment variables, " \
                      "you MUST provide a value to '--use-path'."
                raise click.BadParameter(msg)

        return picard_path
    else:
        return path


@click.group()
@click.option('--use-path', type=click.Path(exists=True),
              default=None,
              show_default=True,
              help='Provide a path to override the default picard.jar location.')
@click.version_option()
@click.pass_context
def cli(ctx, use_path):
    """
    This script facilitates calling `/path/to/picard.jar`.

    Its purpose is to allow you to call picard without providing or even knowing the pull path to the executable far
    file.

    """
    ctx.obj = {}

    ctx.obj["PICARD"] = get_picard_path(path=use_path)
    ctx.obj["CONDA_ENV_PATH"] = os.environ["CONDA_ENV_PATH"]


@cli.command(short_help='runs picard', add_help_option=False)
@click.option('--jvm-args',
              default=u"'-Xmx2g'",
              show_default=True,
              help='a quoted string that contains the args you wish to pass to the java virtual machine.')
@click.option('--help', '-h', 'h_flag',
              is_flag=True)
@click.argument('picard-arg', nargs=-1)
@click.pass_context
def do(ctx, jvm_args, h_flag, picard_arg):
    """\b
    picard do PicardCommandName OPTION1=value1 OPTION2=value2...
    picard do --jvm-args '-Xmx6g' PicardCommandName OPTION1=value1 OPTION2=value2...
    picard do PicardCommandName OPTION1=value1 OPTION2=value2... --jvm-args '-Xmx6g'


    This command actually calls picard.

    The help text for picard can be accessed by providing zero PICARD_ARGs or "--help".

    \b
    PICARD_ARG\t\tThese will be passed directly to picard.

    """
    picard_arg = " ".join(picard_arg)
    if h_flag:
        echo_picard_help(ctx)

    else:
        call_picard(picard_path=ctx.obj['PICARD'],
                    jvm_arg_str=jvm_args,
                    picard_arg_str=picard_arg)


@cli.command(name='help', short_help='shows the picard.jar help text')
@click.pass_context
def help_(ctx):
    """
    This command is equivalent to:

    java -jar /path/to/picard.jar
    """
    echo_picard_help(ctx)

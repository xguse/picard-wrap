=====
Usage
=====

To use pycard in a from the command line::

    $ pycard --help
    Usage: pycard [OPTIONS] COMMAND [ARGS]...

      This script facilitates calling `/path/to/picard.jar`.

      Its purpose is to allow you to call picard without providing or even
      knowing the full path to the executable far file.

    Options:
      --use-path PATH  Provide a path to override the default picard.jar location.
      --version        Show the version and exit.
      --help           Show this message and exit.

    Commands:
      do    runs picard
      help  shows the picard.jar help text


::

    $ pycard do --help
    Usage: pycard do [OPTIONS] [PICARD_ARG]...

      This command actually calls picard.

      PICARD_ARG          These will be passed directly to picard.

      The help text for picard can be accessed by providing zero PICARD_ARGs.


      Example usages:

          picard do PicardCommandName OPTION1=value1 OPTION2=value2...
          picard do --jvm-args '-Xmx6g' PicardCommandName OPTION1=value1 OPTION2=value2...
          picard do PicardCommandName OPTION1=value1 OPTION2=value2... --jvm-args '-Xmx6g'

    Options:
      --jvm-args TEXT  a quoted string that contains the args you wish to pass to
                       the java virtual machine.  [default: '-Xmx2g']
      --help           Show this message and exit.


import click

"""
If run command in windows, do not use non-ascii char.
The type of encoding will make everything mass
"""


# convert function to a command
@click.command()
# # the help message for each parameter
@click.option("--count", default=1, help="Number of greeting.")
@click.option("--name", prompt="Your name", help="The person to grees.")
def hello(count, name):
    """
    simple demo for the click lib
    :param count:
    :param name:
    :return:
    """
    for i in range(count):
        click.echo(f"hello {name}! ")
        # click.echo("hello %s!" % name)

# convert function to a command
@click.command()
# # the help message for each parameter
@click.option("--count", default=1, help="Number of greeting.")
@click.option("--name", prompt="Your name", help="The person to grees.")
def bye(count, name):
    """
    simple demo for the click lib
    :param count:
    :param name:
    :return:
    """
    for i in range(count):
        click.echo(f"bye {name}! ")
        # click.echo("hello %s!" % name)


if __name__ == '__main__':
    bye()
    hello()

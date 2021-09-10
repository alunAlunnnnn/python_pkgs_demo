import click


@click.command()
# @click.option("-s", "--string-to-echo", default="demo", prompt="input a string")
@click.option("-s", default="demo", prompt="input a string", show_default=False )
def hello(s):
    click.echo(s)


if __name__ == '__main__':
    hello()

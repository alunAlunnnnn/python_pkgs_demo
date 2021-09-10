import click


@click.command()
@click.option("-t/-no-t")
def hello(t):
    if t:
        print("start")
        click.echo(t)
        print("finish")


if __name__ == '__main__':
    hello()

import click


@click.command()
@click.argument("src", nargs=-1)
@click.argument("dst", nargs=1)
def touch(src, dst):
    click.echo(src)
    click.echo(dst)


if __name__ == '__main__':
    touch()

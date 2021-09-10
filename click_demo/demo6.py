import click


@click.command()
@click.option("-i", type=click.Choice(["a", "b", "c"]))
def main(i):
    click.echo(i)


if __name__ == '__main__':
    main()

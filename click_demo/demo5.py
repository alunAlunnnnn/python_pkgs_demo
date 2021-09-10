import click


@click.command()
@click.argument("infile", type=click.File("r", encoding="utf-8"))
@click.argument("outfile", type=click.File("w", encoding="utf-8"))
def hello(infile, outfile):
    """
    hello demo 5
    :param infile:
    :param outfile:
    :return:
    """
    data = infile.read()
    outfile.write(data)


if __name__ == '__main__':
    hello()

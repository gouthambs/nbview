"""
The python notebook viewer

"""
import os
import sys
from nbconvert import HTMLExporter
import nbformat
import tempfile
import webbrowser

__author__ = "Goutham Balaraman"
__version__ = "1.0.0"


_tmpdir = tempfile.gettempdir()
_nbvudir = os.path.join(_tmpdir, "nbvu")
if not os.path.isdir(_nbvudir):
    os.mkdir(_nbvudir)


def create_html(nbfile):
    basename = os.path.basename(nbfile)
    htmlfile = basename.split(".")[0]+".html"
    htmlfile = os.path.join(_nbvudir, htmlfile)

    nb = nbformat.read(nbfile, as_version=4)
    html_exporter = HTMLExporter()
    # html_exporter.template_file = 'basic'
    (body, resources) = html_exporter.from_notebook_node(nb)
    f = open(htmlfile, "w")
    f.write(body)
    f.close()
    return htmlfile


if __name__ == '__main__':
    if len(sys.argv) == 2:
        nbfile = sys.argv[1]
        htmlfile = create_html(nbfile)
        w = webbrowser.open_new_tab(htmlfile)
    else:
        print "usage: nbvu <notebook file>"
# Usage

First, install the necessary requirements using pip: `pip install -r requirements.txt`.

Due to how some modules are installed differently across operating systems, these may not work as intended and may require the installation of OS-specific dependencies.

Everything else is numbered and labeled accordingly, and can be followed in that fashion. Thanks!

Note, if you wanted to do on-the-fly conversion of the Jupyter Notebooks into LaTeX, HTML, etc. one can use the command:

`jupyter nbconvert <notebook> --to slides --post serve`

This will convert the notebook into an HTML slideshow which will then be run locally on port 8000. When the server is terminated, a `notebook-name.slides.html` file will have been generated.

If you want to convert the notebook to PDFs, use the `to_pdf.sh` script which requires a LaTeX installation to work properly.



REFERENCES

1. Distributed Evolutionary Algorithms in Python (DEAP):
2. Marti, Luis; Advanced Evolutionary Computation: Theory and Practice - http://lmarti.com/aec-2014
3. https://scturtle.me/posts/2014-04-18-ga.html
4. https://github.com/pavitrakumar78/Python-Genetic-Cars-Box2D

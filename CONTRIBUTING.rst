.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/drkspace/stay/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation and examples
~~~~~~~~~~~~~~~~~~~

Stay could always use more documentation, whether as part of the
official Stay docs, in docstrings, or even on the web in blog posts,
articles, and such.

If you create a new feature or significantly change an existing one,
you should add an example to the examples folder or update existing
ones. Examples should always be working to make it easier for newcomers
to use stay.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/drkspace/stay/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

AI
------------

No AI generated code allowed.

Get Started!
------------

Ready to contribute? Here's how to set up `stay` for local development.

1. Fork the `stay` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:drkspace/stay.git

3. Install your local copy. Use a venv or conda as you see fit::

    $ cd stay/
    $ pip install ".[dev]"
    $ make pre-commit-install

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass ruff, the
   tests, and the type checker. Also, make sure that your code is formatted correctly::

    $ ruff check
    $ make test
    $ ruff format

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

    There is also a pre-commit hook added to automatically run ruff and some other checks.
    If there are any problems, fix them and try committing again.

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.com/drkspace/stay/pull_requests
   and make sure that the tests pass for all supported Python versions.


Code of Conduct
---------------

Please note that this project is released with a `Contributor Code of Conduct`_.
By participating in this project you agree to abide by its terms.

.. _`Contributor Code of Conduct`: CODE_OF_CONDUCT.rst

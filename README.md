# json-patch
A Python 2.7 implementation of [IETF RFC 6902](https://tools.ietf.org/html/rfc6902).

Please click [here](https://ermel272.github.io/json-patch-docs/) to go to the docs.

# Contributing
### Getting the code

Fork the repository, then:

```
git clone https://github.com/<username>/json-patch.git
cd json-patch
make install-full
```

The install-full make directive installs all module, test, and development external dependencies.
From there, simply open a PR against master (please add unit tests where applicable) and note that test coverage
must meet a certain percentage threshold, otherwise the unit test build will fail.

The install-full directive also initializes the the git submodule for the json-pointer docs
located [here](https://github.com/ermel272/json-patch-docs). To regenerate the documentation sources run the following
from the project root folder:

```
cd docs
make regen
```

Finally, running `make run-tests` will execute all unit tests for the module.
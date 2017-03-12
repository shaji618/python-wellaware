#!/bin/sh

rm -Rf build/ dist/ wellaware.egg-info coverage/ wellaware/tests/coverage/ html/ || true
echo -e 'y\n' | pip uninstall wellaware
nosetests -vv -w wellaware/tests --attr=unit

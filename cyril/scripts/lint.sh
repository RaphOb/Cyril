#!/usr/bin/env bash

set -e
set -x

ruff check cyril tests
ruff format cyril tests --check
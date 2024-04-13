#!/bin/sh -e
set -x
set -e

ruff check cyril tests scripts --fix
ruff format cyril tests scripts
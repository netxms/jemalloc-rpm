#!/bin/bash

set -e

mock -r rocky+epel-8-$(arch) --spec SPECS/*.spec --sources SOURCES
mock -r rocky+epel-9-$(arch) --spec SPECS/*.spec --sources SOURCES
mock -r fedora-36-$(arch) --spec SPECS/*.spec --sources SOURCES
mock -r fedora-37-$(arch) --spec SPECS/*.spec --sources SOURCES

cp /var/lib/mock/*/result/*.rpm /result/

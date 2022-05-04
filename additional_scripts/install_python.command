#!/bin/bash
cd -- "$(dirname "$0")"

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
brew install python
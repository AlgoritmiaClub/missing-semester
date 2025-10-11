#!/usr/bin/env bash

set -e

dprint_version='^0.50'
lychee_version='^0.19'
clang_format_version='^18'

# Check rust toolchain
if ! command -v cargo >/dev/null; then
    echo "Installing rust toolchain"
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Check dprint
if ! command -v dprint >/dev/null;then
    echo "Installing dprint"
    cargo install dprint --version "$dprint_version"
fi

# Check lychee
if ! command -v lychee >/dev/null;then
    echo "Installing lychee"
    cargo install lychee --version "$lychee_version"
fi

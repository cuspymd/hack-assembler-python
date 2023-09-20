# Hack Assembler in Python

![GitHub last commit](https://img.shields.io/github/last-commit/cuspymd/hack-assembler-python)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cuspymd/hack-assembler-python)

This repository contains a Python implementation of the Hack computer's assembler, as described in Chapter 6 of the [Nand to Tetris](https://www.nand2tetris.org/) course. With this assembler, you can translate Hack Assembly Language code into Hack Machine Language code.

## Prerequisites

- Python 3.11 or higher is required to run this assembler. You can download the latest version of Python from the [official Python website](https://www.python.org/downloads/).

## Installation

To use this assembler, you can clone this repository:

```bash
git clone https://github.com/cuspymd/hack-assembler-python.git
cd hack-assembler-python
```

## Usage

You can assemble Hack Assembly Language code using the following command:

```bash
python -m hack_assembler.assembler input.asm
```

This will generate an input.hack file in the same directory as your input assembly code (input.asm).

## Example

Suppose you have the following input.asm file:

```asm
// input.asm
@2
D=A
@3
D=D+A
@0
M=D
```

Running the assembler as shown above will create an input.hack file with the corresponding Hack Machine Language code.

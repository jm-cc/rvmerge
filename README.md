# RVmerge

Simple program to merge pdf. My scanner has an automatic document
feeder but no support for recto verso scanning.

So intead of rearanging myself the files, I wrote this simple script and made it available.
Just scan the recto as you would do normaly, scan the recto without reordering the pages 
and then merge the two pdf files with *rvmerge*.

## Installation and Usage

The modern way to use **rvmerge** without managing virtual environments manually is via [uv](https://docs.astral.sh/uv/).

### Run directly (No installation required)
You can run the tool instantly without installing it to your system:
```bash
uvx --from git+https://github.com/jm-cc/rvmerge.git rvmerge <recto.pdf> <verso.pdf> <output.pdf>
```

### Install as a permanent tool

If you use it frequently, install it as a standalone tool in an isolated environment:

```bash
uv tool install git+https://github.com/jm-cc/rvmerge.git
```

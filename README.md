# RVmerge

Simple program to merge pdf. My scanner has an automatic document
feeder but no support for recto verso scanning.

So intead of rearanging myself the files, I wrote this simple script and made it available.
Just scan the recto as you would do normaly, scan the recto without reordering the pages 
and then merge the two pdf files with *rvmerge*.

# Installation and Usage

Clone the depot then *pip install .* where it was cloned.
*rvmerge* command will then be available.

```
rvmerge <recto PDF> <verso PDF> <ouptut PDF>
```

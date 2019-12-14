# Whole genome alignment of an assembled genome to two possible reference genomes

## Prerequisites

This tool has the following dependencies:

python 3.6

Packages:
* biopython
* click

## Quick Setup for developers

Set up this project ready to run by copying it into your python working directory and installing the requirements.
1. <code>pip install -r requirements.txt</code>

**If need be**, change your python working directory using the following commands in your python shell:
1. <code>import os</code>
2. <code>os.getcwd()</code> (to check current working directory)
3. <code>os.chdir("<your_path_to_directory_containing_the_executable>")</code>
4. <code>exit()</code>

Afterwards run the executable as seen in the next paragraph.

## Usage

### The CLI - Command Line Interface
```
> python ClustalW.py [-i <inputfilepath>] [-o <inputfilepath>] [-a <"dna"/"amino_acid">] [-g <int>] [-h/-s]

-i, --input-filepath,   <arg> filepath to multiple-fasta-file for msa, default="data/supplement/BB11007_unaligned.fasta"
-o, --output-filepath,  <arg> filepath for outputfile in fasta format, default="data/output/BB11007_selfaligned.fasta"
-a, --alphabet,         <arg> either "dna" or "amino_acid" (is case sensitive) for respective alphabet, default="amino_acid"
-g, --gap-score,        <arg> positive value for gap-score, default="3"
-h/-s, --help/--silent        given -h or --help all usage options are displayed instead of a computation, default=False
```

### Example
The project can be run like this:
```
python ClustalW.py -i C:/users/MaryDoe/documents/multiFasta.fasta -o C:/users/JohnDoe/documents/msa.fasta -a "dna" -g 5
```

## Authors

* **Nantia Leonidou**
* **Florian Riedl**
* **Alexander Röhl**
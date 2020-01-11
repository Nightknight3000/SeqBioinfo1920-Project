# Whole genome alignment of an assembled genome to two possible reference genomes

## Prerequisites

This tool has the following dependencies:

python 3.6

Packages:
* biopython
* click
* pandas

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
> python start_project.py [INPUT_PATHS] [-cf/-nf]

Arguments:
    INPUT_PATHS,                                       <nargs> Path(s) for multiple/one wga inputfile, default=("data/mauve/WGA_Ref1_Assembly/wga_ref1.alignment", "data/mauve/WGA_Ref2_Assembly/wga_ref2.alignment", "data/MUMmer/NC_002695/out.maf", "data/MUMmer/NC_004431/out.maf")

Options:
    -cf/-nf, --collect-fastas/--not-collect-fastas,            Use '-cf' to collect fasta files from alignments, default=False
    --help  ,                                                  Show help message
```

### Example
The project can be run like this:
```
python start_project.py C:/users/MaryDoe/documents/mauve_wga.alignment C:/users/MaryDoe/documents/mumer_wga.maf -cf
```

## Authors

* **Nantia Leonidou**
* **Florian Riedl**
* **Alexander Röhl**
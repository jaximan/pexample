# Define a self-contained, relocatable binary that contains a complete Python environment
# (i.e., code and dependencies but not the interpreter itself). See https://pex.readthedocs.io

python_library(
  name='a_class',
  sources=globs('a.py'),
)

python_library(
  name='b_class',
  sources=globs('b.py'),
  dependencies=[
    'src/python/detailed:a_class',
  ],
)

python_library(
  name='c_class',
  sources=globs('c.py'),
  dependencies=[
    'src/python/detailed:a_class',
    'src/python/detailed:b_class',
  ],
)
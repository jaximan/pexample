# Define a self-contained, relocatable binary that contains a complete Python environment
# (i.e., code and dependencies but not the interpreter itself). See https://pex.readthedocs.io

python_library(
  name='_cli',
  dependencies=[
    '3rdparty/python:click',
    'src/python/hello_world/messages',
  ],
)

python_binary(
  name='hello_world',
  entry_point='hello_world.cli.main:main',
  dependencies=[
    ':_cli',
  ],
)

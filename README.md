# OX

The only recipe and automation package you will need.

## Installation

We have a few branches of installation

* Latest
You can install the Latest _Stable_ version via: `python -m pip install PyOx`

* Nightly
Nightly is a branch that is purely expermiental, you can install this unstable branch via: `python -m pip install PyOx[Nightly]`

* Dev
Dev is a slightly more stable branch than Nightly, you can install via: `python -m pip install PyOx[Dev]`

## Creating Recipes

Ox has a builtin gui editor for recipes, but you can also input files via cli.

Firstly, you would want to create your recipe file. Something like `test.ox` will suffice.
In test.ox you want to write your recipe using the [documentation](#OX)

You can try this simple recipe:

```recipe
%OX_RECIPE% 
Move Cursor to (0, 0)
Click
Move Cursor to (-250, -250)
Click
Exit
```

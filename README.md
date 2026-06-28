# The Frost Component Library

@johnzhou721's custom Toga component library.

This library will eventually expand to include frosted navigation bars on iOS hence the name.
You're welcome to guess but I'm not disclosing some other reasons I named this library until
later.

# Class Documentation

## RenderCanvas

```python
from togax_frost import RenderCanvas
```

A ``RenderCanvas`` is a regular ``toga.Canvas``, but without ``reset_transform`` for implementation reasons;
the functional difference is that its ``as_image`` function MUST accept a `size` parameter that is either a
``toga.Size`` or a ``tuple`` (type-checked as ``toga.types.SizeT``).  The vector graphic will be rendered at
the specified `size` in `as_image`, in pixels (not CSS points).

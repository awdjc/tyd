# tyd
Typing essentials that make the development process a bit faster.

**New**: `Optional` support.

```python
from tyd import *  # demo purposes only

value: Optional[str] = "Hello!"
nothing: Optional[str] = None

unwrap(value)
unwrap(nothing)  # raises an error because this is None

unwrap_or(value)  # "Hello!"
unwrap_or(nothing, "Hello again")  # "Hello again"

unwrap_or_else(nothing, lambda: str(10 + 10))  # "20"

# map() essentially transforms the data to another if it's not None
map(value, 100)  # 100 (int)
map(nothing, 100)  # None

# some other utilities
is_some(value)
is_none(nothing)
```

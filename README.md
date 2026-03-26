# BubbleUI

BubbleUI is a dual-target UI library workspace:

- `bubbleui/`: Python package for Flet desktop or packaged `exe` apps
- `packages/bubbleui-js/`: web package for JavaScript, TypeScript, and React

The repository is organized so the Python side and web side can evolve together while keeping their runtime-specific code separate.

## Project structure

```text
bubbleUI/
й└йд bubbleui/                 Python/Flet UI library
й└йд packages/bubbleui-js/     Web and React package
й└йд examples/python-exe/      Python showcase for all current Flet components
й└йд examples/web-react/       React showcase for the current web components
й╕йд tests/                    Python smoke tests
```

## Python package

Install in development mode:

```bash
pip install -e .
```

Run the Python example:

```bash
python examples/python-exe/all_components.py
```

Basic usage:

```python
import flet as ft
from bubbleui import BubbleButton, BubbleCard, BubbleInput, apply_bubble_theme


def main(page: ft.Page) -> None:
    apply_bubble_theme(page)
    page.add(
        BubbleCard(
            title="BubbleUI",
            content=ft.Column(
                controls=[
                    BubbleInput(label="Project"),
                    BubbleButton(text="Create"),
                ]
            ),
        )
    )


ft.run(main)
```

## Web and React package

Install from the local package folder:

```bash
npm install /absolute/path/to/bubbleUI/packages/bubbleui-js
```

Run the web example:

```bash
cd examples/web-react
npm install
npm run dev
```

Basic React usage:

```jsx
import { BubbleBadge, BubbleButton, BubbleCard } from "bubbleui-js/react";
import "bubbleui-js/styles.css";

export function Example() {
  return (
    <BubbleCard>
      <BubbleBadge tone="info">Preview</BubbleBadge>
      <BubbleButton>Submit</BubbleButton>
    </BubbleCard>
  );
}
```

## Notes

- `examples/python-exe/` is the desktop/Flet showcase.
- `examples/web-react/` is the web/React showcase.
- `dist/`, `*.egg-info`, and `__pycache__/` are build artifacts and should not be kept in the library.

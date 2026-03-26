# bubbleui-js

A framework-agnostic JavaScript package for BubbleUI design tokens and theme utilities.

## What it provides

- BubbleUI color, spacing, radius, and gradient tokens
- CSS variable generation
- Runtime theme variable injection
- A bundled CSS file with BubbleUI variables and utility classes
- TypeScript declaration files for editor autocomplete
- A React component entry for foundational UI primitives

## Install

### Install from local package folder

```bash
npm install /absolute/path/to/bubbleUI/packages/bubbleui-js
```

### Pack locally and install the tarball

Inside the package folder:

```bash
cd /absolute/path/to/bubbleUI/packages/bubbleui-js
npm pack
```

Then another project can install it with:

```bash
npm install /absolute/path/to/bubbleui-js-0.1.0.tgz
```

## Use tokens

```js
import { colors, radius, spacing, tokens } from "bubbleui-js";

console.log(colors.primary);
console.log(radius.lg);
console.log(spacing.md);
console.log(tokens.gradient.primary);
```

## Apply CSS variables

```js
import { applyThemeVariables } from "bubbleui-js";

applyThemeVariables(document.documentElement);
```

## Use bundled CSS

```js
import "bubbleui-js/styles.css";
```

## React usage

```jsx
import { BubbleBadge, BubbleButton, BubbleCard } from "bubbleui-js/react";
import "bubbleui-js/styles.css";

export function Example() {
  return (
    <BubbleCard>
      <h2>Feedback</h2>
      <BubbleBadge tone="info">Preview</BubbleBadge>
      <BubbleButton type="submit">Submit Feedback</BubbleButton>
      <BubbleButton variant="secondary">Cancel</BubbleButton>
      <BubbleButton variant="soft">Learn More</BubbleButton>
    </BubbleCard>
  );
}
```

## Exports

- `tokens`
- `colors`
- `radius`
- `spacing`
- `gradient`
- `createCssVariables()`
- `applyThemeVariables()`
- `createThemeObject()`
- `BubbleButton`
- `BubbleCard`
- `BubbleBadge`
- `styles.css`

## Files

- `src/index.js`
- `src/tokens.js`
- `src/theme.js`
- `src/react/index.js`
- `src/react/index.d.ts`
- `styles/bubbleui.css`

## Recommended workflow

- During local development: install directly from the package folder
- For sharing with other local web projects: run `npm pack` and install the generated `.tgz`
- If you later publish to npm, this package structure is already close to publish-ready
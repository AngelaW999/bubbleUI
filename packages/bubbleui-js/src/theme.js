import { colors, gradient, radius, spacing, tokens } from "./tokens.js";

export function createCssVariables(prefix = "bubble") {
  return {
    [`--${prefix}-color-primary`]: colors.primary,
    [`--${prefix}-color-primary-hover`]: colors.primaryHover,
    [`--${prefix}-color-primary-soft`]: colors.primarySoft,
    [`--${prefix}-color-secondary-soft`]: colors.secondarySoft,
    [`--${prefix}-color-accent-dark`]: colors.accentDark,
    [`--${prefix}-color-accent-deep`]: colors.accentDeep,
    [`--${prefix}-color-gray-50`]: colors.gray50,
    [`--${prefix}-color-gray-100`]: colors.gray100,
    [`--${prefix}-color-gray-200`]: colors.gray200,
    [`--${prefix}-color-gray-300`]: colors.gray300,
    [`--${prefix}-color-gray-500`]: colors.gray500,
    [`--${prefix}-color-gray-700`]: colors.gray700,
    [`--${prefix}-color-white`]: colors.white,
    [`--${prefix}-color-success`]: colors.success,
    [`--${prefix}-color-warning`]: colors.warning,
    [`--${prefix}-color-danger`]: colors.danger,
    [`--${prefix}-radius-sm`]: `${radius.sm}px`,
    [`--${prefix}-radius-md`]: `${radius.md}px`,
    [`--${prefix}-radius-lg`]: `${radius.lg}px`,
    [`--${prefix}-radius-xl`]: `${radius.xl}px`,
    [`--${prefix}-radius-pill`]: `${radius.pill}px`,
    [`--${prefix}-space-xs`]: `${spacing.xs}px`,
    [`--${prefix}-space-sm`]: `${spacing.sm}px`,
    [`--${prefix}-space-md`]: `${spacing.md}px`,
    [`--${prefix}-space-lg`]: `${spacing.lg}px`,
    [`--${prefix}-space-xl`]: `${spacing.xl}px`,
    [`--${prefix}-space-xxl`]: `${spacing.xxl}px`,
    [`--${prefix}-gradient-primary`]: `linear-gradient(135deg, ${gradient.primary.join(", ")})`
  };
}

export function applyThemeVariables(target = document.documentElement, prefix = "bubble") {
  if (!target || typeof target.style?.setProperty !== "function") {
    throw new Error("BubbleUI: target must support style.setProperty().");
  }

  const variables = createCssVariables(prefix);
  Object.entries(variables).forEach(([name, value]) => {
    target.style.setProperty(name, value);
  });

  return variables;
}

export function createThemeObject(prefix = "bubble") {
  return {
    prefix,
    tokens,
    variables: createCssVariables(prefix)
  };
}
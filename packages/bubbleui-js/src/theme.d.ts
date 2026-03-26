import type { tokens } from "./tokens.js";

export declare function createCssVariables(prefix?: string): Record<string, string>;
export declare function applyThemeVariables(target?: HTMLElement, prefix?: string): Record<string, string>;
export declare function createThemeObject(prefix?: string): {
  prefix: string;
  tokens: typeof tokens;
  variables: Record<string, string>;
};
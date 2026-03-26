export type BubbleColors = {
  primary: string;
  primaryHover: string;
  primarySoft: string;
  secondarySoft: string;
  accentDark: string;
  accentDeep: string;
  gray50: string;
  gray100: string;
  gray200: string;
  gray300: string;
  gray500: string;
  gray700: string;
  white: string;
  success: string;
  warning: string;
  danger: string;
};

export type BubbleRadius = {
  sm: number;
  md: number;
  lg: number;
  xl: number;
  pill: number;
};

export type BubbleSpacing = {
  xs: number;
  sm: number;
  md: number;
  lg: number;
  xl: number;
  xxl: number;
};

export type BubbleGradient = {
  primary: string[];
};

export declare const colors: BubbleColors;
export declare const radius: BubbleRadius;
export declare const spacing: BubbleSpacing;
export declare const gradient: BubbleGradient;
export declare const tokens: {
  colors: BubbleColors;
  radius: BubbleRadius;
  spacing: BubbleSpacing;
  gradient: BubbleGradient;
};
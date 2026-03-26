import * as React from "react";

export type BubbleButtonVariant = "primary" | "secondary" | "soft";
export type BubbleBadgeTone = "info" | "success" | "warning" | "danger";

export type BubbleButtonProps<C extends React.ElementType = "button"> = {
  as?: C;
  className?: string;
  variant?: BubbleButtonVariant;
  children?: React.ReactNode;
} & Omit<React.ComponentPropsWithoutRef<C>, "as" | "className" | "children">;

export type BubbleCardProps<C extends React.ElementType = "div"> = {
  as?: C;
  className?: string;
  children?: React.ReactNode;
} & Omit<React.ComponentPropsWithoutRef<C>, "as" | "className" | "children">;

export type BubbleBadgeProps<C extends React.ElementType = "span"> = {
  as?: C;
  className?: string;
  tone?: BubbleBadgeTone;
  children?: React.ReactNode;
} & Omit<React.ComponentPropsWithoutRef<C>, "as" | "className" | "children">;

export declare const BubbleButton: React.ForwardRefExoticComponent<BubbleButtonProps & React.RefAttributes<unknown>>;
export declare const BubbleCard: React.ForwardRefExoticComponent<BubbleCardProps & React.RefAttributes<unknown>>;
export declare const BubbleBadge: React.ForwardRefExoticComponent<BubbleBadgeProps & React.RefAttributes<unknown>>;
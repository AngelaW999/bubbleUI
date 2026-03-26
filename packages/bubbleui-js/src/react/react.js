import React from "react";

function joinClasses(...values) {
  return values.filter(Boolean).join(" ");
}

export const BubbleButton = React.forwardRef(function BubbleButton(
  {
    as = "button",
    children,
    className = "",
    variant = "primary",
    type,
    ...props
  },
  ref
) {
  const Component = as;
  const classes = joinClasses(
    "bubble-button",
    variant === "secondary" && "bubble-button--secondary",
    variant === "soft" && "bubble-button--soft",
    className
  );

  const componentProps = {
    ref,
    className: classes,
    ...props,
  };

  if (Component === "button" && !type) {
    componentProps.type = "button";
  } else if (type) {
    componentProps.type = type;
  }

  return React.createElement(Component, componentProps, children);
});

export const BubbleCard = React.forwardRef(function BubbleCard(
  { as = "div", children, className = "", ...props },
  ref
) {
  const Component = as;
  return React.createElement(
    Component,
    {
      ref,
      className: joinClasses("bubble-card", className),
      ...props,
    },
    children
  );
});

export const BubbleBadge = React.forwardRef(function BubbleBadge(
  { as = "span", children, className = "", tone = "info", ...props },
  ref
) {
  const Component = as;
  return React.createElement(
    Component,
    {
      ref,
      className: joinClasses("bubble-badge", tone !== "info" && `bubble-badge--${tone}`, className),
      ...props,
    },
    children
  );
});
import React from "react";

import { BubbleBadge, BubbleButton, BubbleCard } from "bubbleui-js/react";
import { colors, gradient, radius, spacing } from "bubbleui-js";
import "bubbleui-js/styles.css";

const buttonVariants = ["primary", "secondary", "soft"];
const badgeTones = ["info", "success", "warning", "danger"];

function Section({ title, description, children }) {
  return (
    <section className="example-section">
      <div className="example-section__header">
        <h2>{title}</h2>
        <p>{description}</p>
      </div>
      {children}
    </section>
  );
}

function TokenGrid({ items, valueType = "text" }) {
  return (
    <div className="token-grid">
      {items.map(([name, value]) => (
        <BubbleCard className="token-card" key={name}>
          {valueType === "color" ? <div className="token-swatch" style={{ background: value }} /> : null}
          <strong>{name}</strong>
          <span>{String(value)}</span>
        </BubbleCard>
      ))}
    </div>
  );
}

export default function App() {
  return (
    <main className="example-page bubble-page">
      <header className="hero">
        <div>
          <BubbleBadge>React</BubbleBadge>
          <h1>BubbleUI Web Components</h1>
          <p>One page that covers the current React primitives and shared design tokens.</p>
        </div>
        <div className="hero__actions">
          <BubbleButton>Primary Action</BubbleButton>
          <BubbleButton variant="secondary">Secondary</BubbleButton>
          <BubbleButton variant="soft">Soft</BubbleButton>
        </div>
      </header>

      <Section title="BubbleButton" description="The current React button variants.">
        <div className="inline-row">
          {buttonVariants.map((variant) => (
            <BubbleButton key={variant} variant={variant}>
              {variant}
            </BubbleButton>
          ))}
        </div>
      </Section>

      <Section title="BubbleBadge" description="Semantic badge tones exposed by the React package.">
        <div className="inline-row">
          {badgeTones.map((tone) => (
            <BubbleBadge key={tone} tone={tone}>
              {tone}
            </BubbleBadge>
          ))}
        </div>
      </Section>

      <Section title="BubbleCard" description="Cards are the base content container for the current web package.">
        <div className="card-grid">
          <BubbleCard>
            <h3>Feedback</h3>
            <p>Cards can wrap headings, body content, and actions.</p>
            <div className="inline-row">
              <BubbleButton>Submit</BubbleButton>
              <BubbleButton variant="secondary">Cancel</BubbleButton>
            </div>
          </BubbleCard>
          <BubbleCard>
            <h3>Status</h3>
            <div className="stack-sm">
              <BubbleBadge>Preview</BubbleBadge>
              <BubbleBadge tone="success">Ready</BubbleBadge>
            </div>
          </BubbleCard>
        </div>
      </Section>

      <Section title="Design Tokens" description="Shared web tokens from bubbleui-js.">
        <div className="stack-lg">
          <div className="gradient-card">
            <strong>gradient.primary</strong>
            <span>{gradient.primary.join(" -> ")}</span>
          </div>
          <TokenGrid items={Object.entries(colors)} valueType="color" />
          <TokenGrid items={Object.entries(radius)} />
          <TokenGrid items={Object.entries(spacing)} />
        </div>
      </Section>
    </main>
  );
}

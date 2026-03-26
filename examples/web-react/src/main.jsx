import React from "react";
import ReactDOM from "react-dom/client";

import { applyThemeVariables } from "bubbleui-js";

import App from "./App.jsx";

applyThemeVariables(document.documentElement);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

/**
 *  Light Switch @version v0.1.4
 */

(function () {
  let lightSwitch = document.getElementById("lightSwitch");
  if (!lightSwitch) {
    return;
  }

  /**
   * @function darkmode
   * @summary: changes the theme to 'dark mode' and save settings to local stroage.
   * Basically, replaces/toggles every CSS class that has '-light' class with '-dark'
   */
  function darkMode() {
    // sets the <html> attribute: data-bs-theme
    document.documentElement.setAttribute("data-bs-theme", "dark");

    // sets the head element href that styles the code-input
    document
      .querySelector("#import-theme")
      .setAttribute(
        "href",
        "https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/themes/prism-tomorrow.css"
      );

    if (!lightSwitch.checked) {
      lightSwitch.checked = true;
    }
    localStorage.setItem("lightSwitch", "dark");
  }

  /**
   * @function lightmode
   * @summary: changes the theme to 'light mode' and save settings to local stroage.
   */
  function lightMode() {
    // sets the <html> attribute: data-bs-theme
    document.documentElement.setAttribute("data-bs-theme", "light");

    // sets the head element href that styles the code-input
    document
      .querySelector("#import-theme")
      .setAttribute(
        "href",
        "https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/themes/prism.css"
      );

    if (lightSwitch.checked) {
      lightSwitch.checked = false;
    }
    localStorage.setItem("lightSwitch", "light");
  }

  /**
   * @function onToggleMode
   * @summary: the event handler attached to the switch. calling @darkMode or @lightMode depending on the checked state.
   */
  function onToggleMode() {
    if (lightSwitch.checked) {
      darkMode();
    } else {
      lightMode();
    }
  }

  /**
   * @function getSystemDefaultTheme
   * @summary: get system default theme by media query
   */
  function getSystemDefaultTheme() {
    const darkThemeMq = window.matchMedia("(prefers-color-scheme: dark)");
    if (darkThemeMq.matches) {
      return "dark";
    }
    return "light";
  }

  function setup() {
    var settings = localStorage.getItem("lightSwitch");
    if (settings == null) {
      settings = getSystemDefaultTheme();
    }

    if (settings == "dark") {
      lightSwitch.checked = true;
    }

    lightSwitch.addEventListener("change", onToggleMode);
    onToggleMode();
  }

  setup();
})();

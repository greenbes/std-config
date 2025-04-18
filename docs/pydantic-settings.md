<div md-component="skip">

<a href="#settings-management" class="md-skip">Skip to content</a>

</div>

<div md-component="announce">

<div class="md-banner__inner md-grid md-typeset">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE5IDYuNDEgMTcuNTkgNSAxMiAxMC41OSA2LjQxIDUgNSA2LjQxIDEwLjU5IDEyIDUgMTcuNTkgNi40MSAxOSAxMiAxMy40MSAxNy41OSAxOSAxOSAxNy41OSAxMy40MSAxMnoiIC8+PC9zdmc+)

What's new — we've launched [Pydantic
Logfire](https://pydantic.dev/articles/logfire-announcement) <img
src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg"
title=":fire:" class="twemoji" alt="🔥" /> to help you monitor and
understand your
<a href="https://logfire.pydantic.dev/docs/integrations/pydantic/"
id="logfire-app-type" target="_blank">Pydantic validations.</a>

</div>

</div>

<div md-color-scheme="default" md-component="outdated" hidden="">

</div>

<div class="md-header" md-component="header">

<a href="../.." class="md-header__button md-logo" aria-label="Pydantic"
data-md-component="logo" title="Pydantic"><img
src="../../logo-white.svg" alt="logo" /></a>
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTMgNmgxOHYySDN6bTAgNWgxOHYySDN6bTAgNWgxOHYySDN6IiAvPjwvc3ZnPg==)

<div class="md-header__title" md-component="header-title">

<div class="md-header__ellipsis">

<div class="md-header__topic">

<span class="md-ellipsis"> Pydantic </span>

</div>

<div class="md-header__topic" md-component="header-topic">

<span class="md-ellipsis"> Settings Management </span>

</div>

</div>

</div>

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJhNyA3IDAgMCAwLTcgN2MwIDIuMzggMS4xOSA0LjQ3IDMgNS43NFYxN2ExIDEgMCAwIDAgMSAxaDZhMSAxIDAgMCAwIDEtMXYtMi4yNmMxLjgxLTEuMjcgMy0zLjM2IDMtNS43NGE3IDcgMCAwIDAtNy03TTkgMjFhMSAxIDAgMCAwIDEgMWg0YTEgMSAwIDAgMCAxLTF2LTFIOXoiIC8+PC9zdmc+)
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJhNyA3IDAgMCAxIDcgN2MwIDIuMzgtMS4xOSA0LjQ3LTMgNS43NFYxN2ExIDEgMCAwIDEtMSAxSDlhMSAxIDAgMCAxLTEtMXYtMi4yNkM2LjE5IDEzLjQ3IDUgMTEuMzggNSA5YTcgNyAwIDAgMSA3LTdNOSAyMXYtMWg2djFhMSAxIDAgMCAxLTEgMWgtNGExIDEgMCAwIDEtMS0xbTMtMTdhNSA1IDAgMCAwLTUgNWMwIDIuMDUgMS4yMyAzLjgxIDMgNC41OFYxNmg0di0yLjQyYzEuNzctLjc3IDMtMi41MyAzLTQuNThhNSA1IDAgMCAwLTUtNSIgLz48L3N2Zz4=)
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkgMmMzLjg3IDAgNyAzLjEzIDcgNyAwIDIuMzgtMS4xOSA0LjQ3LTMgNS43NFYxN2MwIC41NS0uNDUgMS0xIDFINmMtLjU1IDAtMS0uNDUtMS0xdi0yLjI2QzMuMTkgMTMuNDcgMiAxMS4zOCAyIDljMC0zLjg3IDMuMTMtNyA3LTdNNiAyMXYtMWg2djFjMCAuNTUtLjQ1IDEtMSAxSDdjLS41NSAwLTEtLjQ1LTEtMU05IDRDNi4yNCA0IDQgNi4yNCA0IDljMCAyLjA1IDEuMjMgMy44MSAzIDQuNThWMTZoNHYtMi40MmMxLjc3LS43NyAzLTIuNTMgMy00LjU4IDAtMi43Ni0yLjI0LTUtNS01bTEwIDloLTJsLTMuMiA5aDEuOWwuNy0yaDMuMmwuNyAyaDEuOXptLTIuMTUgNS42NUwxOCAxNWwxLjE1IDMuNjV6IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkuNSAzQTYuNSA2LjUgMCAwIDEgMTYgOS41YzAgMS42MS0uNTkgMy4wOS0xLjU2IDQuMjNsLjI3LjI3aC43OWw1IDUtMS41IDEuNS01LTV2LS43OWwtLjI3LS4yN0E2LjUyIDYuNTIgMCAwIDEgOS41IDE2IDYuNSA2LjUgMCAwIDEgMyA5LjUgNi41IDYuNSAwIDAgMSA5LjUgM20wIDJDNyA1IDUgNyA1IDkuNVM3IDE0IDkuNSAxNCAxNCAxMiAxNCA5LjUgMTIgNSA5LjUgNSIgLz48L3N2Zz4=)

<div class="md-search" role="dialog">

<div class="md-search__inner" role="search">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkuNSAzQTYuNSA2LjUgMCAwIDEgMTYgOS41YzAgMS42MS0uNTkgMy4wOS0xLjU2IDQuMjNsLjI3LjI3aC43OWw1IDUtMS41IDEuNS01LTV2LS43OWwtLjI3LS4yN0E2LjUxNiA2LjUxNiAwIDAgMSA5LjUgMTYgNi41IDYuNSAwIDAgMSAzIDkuNSA2LjUgNi41IDAgMCAxIDkuNSAzbTAgMkM3IDUgNSA3IDUgOS41UzcgMTQgOS41IDE0IDE0IDEyIDE0IDkuNSAxMiA1IDkuNSA1WiIgLz48L3N2Zz4=)
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDExdjJIOGw1LjUgNS41LTEuNDIgMS40Mkw0LjE2IDEybDcuOTItNy45MkwxMy41IDUuNSA4IDExaDEyWiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE5IDYuNDEgMTcuNTkgNSAxMiAxMC41OSA2LjQxIDUgNSA2LjQxIDEwLjU5IDEyIDUgMTcuNTkgNi40MSAxOSAxMiAxMy40MSAxNy41OSAxOSAxOSAxNy41OSAxMy40MSAxMiAxOSA2LjQxWiIgLz48L3N2Zz4=)

<div class="md-search__suggest">

</div>

<div class="md-search__output">

<div class="md-search__scrollwrap" tabindex="0">

<div class="md-search-result">

<div id="type-to-start-searching" class="md-search-result__meta">

Type to start searching

</div>

</div>

</div>

</div>

</div>

</div>

<div class="md-header__source">

<a href="https://github.com/pydantic/pydantic" class="md-source"
data-md-component="source" title="Go to repository"></a>

<div class="md-source__icon md-icon">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA0NDggNTEyIj48IS0tISBGb250IEF3ZXNvbWUgRnJlZSA2LjcuMiBieSBAZm9udGF3ZXNvbWUgLSBodHRwczovL2ZvbnRhd2Vzb21lLmNvbSBMaWNlbnNlIC0gaHR0cHM6Ly9mb250YXdlc29tZS5jb20vbGljZW5zZS9mcmVlIChJY29uczogQ0MgQlkgNC4wLCBGb250czogU0lMIE9GTCAxLjEsIENvZGU6IE1JVCBMaWNlbnNlKSBDb3B5cmlnaHQgMjAyNCBGb250aWNvbnMsIEluYy4tLT48cGF0aCBkPSJNNDM5LjU1IDIzNi4wNSAyNDQgNDAuNDVhMjguODcgMjguODcgMCAwIDAtNDAuODEgMGwtNDAuNjYgNDAuNjMgNTEuNTIgNTEuNTJjMjcuMDYtOS4xNCA1Mi42OCAxNi43NyA0My4zOSA0My42OGw0OS42NiA0OS42NmMzNC4yMy0xMS44IDYxLjE4IDMxIDM1LjQ3IDU2LjY5LTI2LjQ5IDI2LjQ5LTcwLjIxLTIuODctNTYtMzcuMzRMMjQwLjIyIDE5OXYxMjEuODVjMjUuMyAxMi41NCAyMi4yNiA0MS44NSA5LjA4IDU1YTM0LjM0IDM0LjM0IDAgMCAxLTQ4LjU1IDBjLTE3LjU3LTE3LjYtMTEuMDctNDYuOTEgMTEuMjUtNTZ2LTEyM2MtMjAuOC04LjUxLTI0LjYtMzAuNzQtMTguNjQtNDVMMTQyLjU3IDEwMSA4LjQ1IDIzNS4xNGEyOC44NiAyOC44NiAwIDAgMCAwIDQwLjgxbDE5NS42MSAxOTUuNmEyOC44NiAyOC44NiAwIDAgMCA0MC44IDBsMTk0LjY5LTE5NC42OWEyOC44NiAyOC44NiAwIDAgMCAwLTQwLjgxIiAvPjwvc3ZnPg==)

</div>

<div class="md-source__repository">

pydantic/pydantic

</div>

</div>

</div>

<div class="md-container" md-component="container">

<div class="md-grid">

- <a href="../.." class="md-tabs__link">Get Started</a>
- <a href="../models/" class="md-tabs__link">Concepts</a>
- <a href="../../api/base_model/" class="md-tabs__link">API
  Documentation</a>
- <a href="../../internals/architecture/"
  class="md-tabs__link">Internals</a>
- <a href="../../examples/files/" class="md-tabs__link">Examples</a>
- <a href="../../errors/errors/" class="md-tabs__link">Error Messages</a>
- <a href="../../integrations/logfire/"
  class="md-tabs__link">Integrations</a>
- <a href="https://blog.pydantic.dev/" class="md-tabs__link">Blog</a>
- <a href="../../pydantic_people/" class="md-tabs__link">Pydantic
  People</a>

</div>

<div class="md-main" role="main" md-component="main">

<div class="md-main__inner md-grid">

<div class="md-sidebar md-sidebar--primary" md-component="sidebar"
md-type="navigation">

<div class="md-sidebar__scrollwrap">

<div class="md-sidebar__inner">

<a href="../.." class="md-nav__button md-logo" aria-label="Pydantic"
data-md-component="logo" title="Pydantic"><img
src="../../logo-white.svg" alt="logo" /></a> Pydantic

<div class="md-nav__source">

<a href="https://github.com/pydantic/pydantic" class="md-source"
data-md-component="source" title="Go to repository"></a>

<div class="md-source__icon md-icon">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA0NDggNTEyIj48IS0tISBGb250IEF3ZXNvbWUgRnJlZSA2LjcuMiBieSBAZm9udGF3ZXNvbWUgLSBodHRwczovL2ZvbnRhd2Vzb21lLmNvbSBMaWNlbnNlIC0gaHR0cHM6Ly9mb250YXdlc29tZS5jb20vbGljZW5zZS9mcmVlIChJY29uczogQ0MgQlkgNC4wLCBGb250czogU0lMIE9GTCAxLjEsIENvZGU6IE1JVCBMaWNlbnNlKSBDb3B5cmlnaHQgMjAyNCBGb250aWNvbnMsIEluYy4tLT48cGF0aCBkPSJNNDM5LjU1IDIzNi4wNSAyNDQgNDAuNDVhMjguODcgMjguODcgMCAwIDAtNDAuODEgMGwtNDAuNjYgNDAuNjMgNTEuNTIgNTEuNTJjMjcuMDYtOS4xNCA1Mi42OCAxNi43NyA0My4zOSA0My42OGw0OS42NiA0OS42NmMzNC4yMy0xMS44IDYxLjE4IDMxIDM1LjQ3IDU2LjY5LTI2LjQ5IDI2LjQ5LTcwLjIxLTIuODctNTYtMzcuMzRMMjQwLjIyIDE5OXYxMjEuODVjMjUuMyAxMi41NCAyMi4yNiA0MS44NSA5LjA4IDU1YTM0LjM0IDM0LjM0IDAgMCAxLTQ4LjU1IDBjLTE3LjU3LTE3LjYtMTEuMDctNDYuOTEgMTEuMjUtNTZ2LTEyM2MtMjAuOC04LjUxLTI0LjYtMzAuNzQtMTguNjQtNDVMMTQyLjU3IDEwMSA4LjQ1IDIzNS4xNGEyOC44NiAyOC44NiAwIDAgMCAwIDQwLjgxbDE5NS42MSAxOTUuNmEyOC44NiAyOC44NiAwIDAgMCA0MC44IDBsMTk0LjY5LTE5NC42OWEyOC44NiAyOC44NiAwIDAgMCAwLTQwLjgxIiAvPjwvc3ZnPg==)

</div>

<div class="md-source__repository">

pydantic/pydantic

</div>

</div>

<span class="md-ellipsis"> Get Started </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Get Started

- <a href="../.." class="md-nav__link"><span class="md-ellipsis"> Welcome
  to Pydantic </span></a>
- <a href="../../why/" class="md-nav__link"><span class="md-ellipsis"> Why
  use Pydantic </span></a>
- <a href="../../help_with_pydantic/" class="md-nav__link"><span
  class="md-ellipsis"> Help with Pydantic </span></a>
- <a href="../../install/" class="md-nav__link"><span class="md-ellipsis">
  Installation </span></a>
- <a href="../../migration/" class="md-nav__link"><span
  class="md-ellipsis"> Migration Guide </span></a>
- <a href="../../version-policy/" class="md-nav__link"><span
  class="md-ellipsis"> Version Policy </span></a>
- <a href="../../contributing/" class="md-nav__link"><span
  class="md-ellipsis"> Contributing </span></a>
- <a href="../../changelog/" class="md-nav__link"><span
  class="md-ellipsis"> Changelog </span></a>

<span class="md-ellipsis"> Concepts </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Concepts

<a href="../models/" class="md-nav__link"><span class="md-ellipsis">
Models </span></a>

<a href="../fields/" class="md-nav__link"><span class="md-ellipsis">
Fields </span></a>

<a href="../json_schema/" class="md-nav__link"><span
class="md-ellipsis"> JSON Schema </span></a>

<a href="../json/" class="md-nav__link"><span class="md-ellipsis"> JSON
</span></a>

<a href="../types/" class="md-nav__link"><span class="md-ellipsis">
Types </span></a>

<a href="../unions/" class="md-nav__link"><span class="md-ellipsis">
Unions </span></a>

<a href="../alias/" class="md-nav__link"><span class="md-ellipsis">
Alias </span></a>

<a href="../config/" class="md-nav__link"><span class="md-ellipsis">
Configuration </span></a>

<a href="../serialization/" class="md-nav__link"><span
class="md-ellipsis"> Serialization </span></a>

<a href="../validators/" class="md-nav__link"><span class="md-ellipsis">
Validators </span></a>

<a href="../dataclasses/" class="md-nav__link"><span
class="md-ellipsis"> Dataclasses </span></a>

<a href="../forward_annotations/" class="md-nav__link"><span
class="md-ellipsis"> Forward Annotations </span></a>

<a href="../strict_mode/" class="md-nav__link"><span
class="md-ellipsis"> Strict Mode </span></a>

<a href="../type_adapter/" class="md-nav__link"><span
class="md-ellipsis"> Type Adapter </span></a>

<a href="../validation_decorator/" class="md-nav__link"><span
class="md-ellipsis"> Validation Decorator </span></a>

<a href="../conversion_table/" class="md-nav__link"><span
class="md-ellipsis"> Conversion Table </span></a>

<span class="md-ellipsis"> Settings Management </span>
<span class="md-nav__icon md-icon"></span>
<a href="./" class="md-nav__link md-nav__link--active"><span
class="md-ellipsis"> Settings Management </span></a>

<span class="md-nav__icon md-icon"></span> Page contents

- <a href="#installation" class="md-nav__link"><span class="md-ellipsis">
  Installation </span></a>
- <a href="#usage" class="md-nav__link"><span class="md-ellipsis"> Usage
  </span></a>
- <a href="#validation-of-default-values" class="md-nav__link"><span
  class="md-ellipsis"> Validation of default values </span></a>
- <a href="#environment-variable-names" class="md-nav__link"><span
  class="md-ellipsis"> Environment variable names </span></a>
  - <a href="#case-sensitivity" class="md-nav__link"><span
    class="md-ellipsis"> Case-sensitivity </span></a>
- <a href="#parsing-environment-variable-values"
  class="md-nav__link"><span class="md-ellipsis"> Parsing environment
  variable values </span></a>
  - <a href="#disabling-json-parsing" class="md-nav__link"><span
    class="md-ellipsis"> Disabling JSON parsing </span></a>
- <a href="#nested-model-default-partial-updates"
  class="md-nav__link"><span class="md-ellipsis"> Nested model default
  partial updates </span></a>
- <a href="#dotenv-env-support" class="md-nav__link"><span
  class="md-ellipsis"> Dotenv (.env) support </span></a>
- <a href="#command-line-support" class="md-nav__link"><span
  class="md-ellipsis"> Command Line Support </span></a>
  - <a href="#the-basics" class="md-nav__link"><span class="md-ellipsis">
    The Basics </span></a>
    - <a href="#lists" class="md-nav__link"><span class="md-ellipsis"> Lists
      </span></a>
    - <a href="#dictionaries" class="md-nav__link"><span class="md-ellipsis">
      Dictionaries </span></a>
    - <a href="#literals-and-enums" class="md-nav__link"><span
      class="md-ellipsis"> Literals and Enums </span></a>
    - <a href="#aliases" class="md-nav__link"><span class="md-ellipsis">
      Aliases </span></a>
  - <a href="#subcommands-and-positional-arguments"
    class="md-nav__link"><span class="md-ellipsis"> Subcommands and
    Positional Arguments </span></a>
  - <a href="#creating-cli-applications" class="md-nav__link"><span
    class="md-ellipsis"> Creating CLI Applications </span></a>
  - <a href="#asynchronous-cli-commands" class="md-nav__link"><span
    class="md-ellipsis"> Asynchronous CLI Commands </span></a>
    - <a href="#asynchronous-subcommands" class="md-nav__link"><span
      class="md-ellipsis"> Asynchronous Subcommands </span></a>
  - <a href="#mutually-exclusive-groups" class="md-nav__link"><span
    class="md-ellipsis"> Mutually Exclusive Groups </span></a>
  - <a href="#customizing-the-cli-experience" class="md-nav__link"><span
    class="md-ellipsis"> Customizing the CLI Experience </span></a>
    - <a href="#change-the-displayed-program-name" class="md-nav__link"><span
      class="md-ellipsis"> Change the Displayed Program Name </span></a>
    - <a href="#cli-boolean-flags" class="md-nav__link"><span
      class="md-ellipsis"> CLI Boolean Flags </span></a>
    - <a href="#ignore-unknown-arguments" class="md-nav__link"><span
      class="md-ellipsis"> Ignore Unknown Arguments </span></a>
    - <a href="#cli-kebab-case-for-arguments" class="md-nav__link"><span
      class="md-ellipsis"> CLI Kebab Case for Arguments </span></a>
    - <a href="#change-whether-cli-should-exit-on-error"
      class="md-nav__link"><span class="md-ellipsis"> Change Whether CLI
      Should Exit on Error </span></a>
    - <a href="#enforce-required-arguments-at-cli" class="md-nav__link"><span
      class="md-ellipsis"> Enforce Required Arguments at CLI </span></a>
    - <a href="#change-the-none-type-parse-string" class="md-nav__link"><span
      class="md-ellipsis"> Change the None Type Parse String </span></a>
    - <a href="#hide-none-type-values" class="md-nav__link"><span
      class="md-ellipsis"> Hide None Type Values </span></a>
    - <a href="#avoid-adding-json-cli-options" class="md-nav__link"><span
      class="md-ellipsis"> Avoid Adding JSON CLI Options </span></a>
    - <a href="#use-class-docstring-for-group-help-text"
      class="md-nav__link"><span class="md-ellipsis"> Use Class Docstring for
      Group Help Text </span></a>
    - <a href="#change-the-cli-flag-prefix-character"
      class="md-nav__link"><span class="md-ellipsis"> Change the CLI Flag
      Prefix Character </span></a>
    - <a href="#suppressing-fields-from-cli-help-text"
      class="md-nav__link"><span class="md-ellipsis"> Suppressing Fields from
      CLI Help Text </span></a>
  - <a href="#integrating-with-existing-parsers" class="md-nav__link"><span
    class="md-ellipsis"> Integrating with Existing Parsers </span></a>
- <a href="#secrets" class="md-nav__link"><span class="md-ellipsis">
  Secrets </span></a>
  - <a href="#use-case-docker-secrets" class="md-nav__link"><span
    class="md-ellipsis"> Use Case: Docker Secrets </span></a>
- <a href="#aws-secrets-manager" class="md-nav__link"><span
  class="md-ellipsis"> AWS Secrets Manager </span></a>
- <a href="#azure-key-vault" class="md-nav__link"><span
  class="md-ellipsis"> Azure Key Vault </span></a>
- <a href="#other-settings-source" class="md-nav__link"><span
  class="md-ellipsis"> Other settings source </span></a>
  - <a href="#pyprojecttoml" class="md-nav__link"><span class="md-ellipsis">
    pyproject.toml </span></a>
- <a href="#field-value-priority" class="md-nav__link"><span
  class="md-ellipsis"> Field value priority </span></a>
- <a href="#customise-settings-sources" class="md-nav__link"><span
  class="md-ellipsis"> Customise settings sources </span></a>
  - <a href="#changing-priority" class="md-nav__link"><span
    class="md-ellipsis"> Changing Priority </span></a>
  - <a href="#adding-sources" class="md-nav__link"><span
    class="md-ellipsis"> Adding sources </span></a>
    - <a href="#accesing-the-result-of-previous-sources"
      class="md-nav__link"><span class="md-ellipsis"> Accesing the result of
      previous sources </span></a>
  - <a href="#removing-sources" class="md-nav__link"><span
    class="md-ellipsis"> Removing sources </span></a>
- <a href="#in-place-reloading" class="md-nav__link"><span
  class="md-ellipsis"> In-place reloading </span></a>

<a href="../performance/" class="md-nav__link"><span
class="md-ellipsis"> Performance </span></a>

<a href="../experimental/" class="md-nav__link"><span
class="md-ellipsis"> Experimental </span></a>

<span class="md-ellipsis"> API Documentation </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> API Documentation

<span class="md-ellipsis"> Pydantic </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Pydantic

- <a href="../../api/base_model/" class="md-nav__link"><span
  class="md-ellipsis"> BaseModel </span></a>
- <a href="../../api/root_model/" class="md-nav__link"><span
  class="md-ellipsis"> RootModel </span></a>
- <a href="../../api/dataclasses/" class="md-nav__link"><span
  class="md-ellipsis"> Pydantic Dataclasses </span></a>
- <a href="../../api/type_adapter/" class="md-nav__link"><span
  class="md-ellipsis"> TypeAdapter </span></a>
- <a href="../../api/validate_call/" class="md-nav__link"><span
  class="md-ellipsis"> Validate Call </span></a>
- <a href="../../api/fields/" class="md-nav__link"><span
  class="md-ellipsis"> Fields </span></a>
- <a href="../../api/aliases/" class="md-nav__link"><span
  class="md-ellipsis"> Aliases </span></a>
- <a href="../../api/config/" class="md-nav__link"><span
  class="md-ellipsis"> Configuration </span></a>
- <a href="../../api/json_schema/" class="md-nav__link"><span
  class="md-ellipsis"> JSON Schema </span></a>
- <a href="../../api/errors/" class="md-nav__link"><span
  class="md-ellipsis"> Errors </span></a>
- <a href="../../api/functional_validators/" class="md-nav__link"><span
  class="md-ellipsis"> Functional Validators </span></a>
- <a href="../../api/functional_serializers/" class="md-nav__link"><span
  class="md-ellipsis"> Functional Serializers </span></a>
- <a href="../../api/standard_library_types/" class="md-nav__link"><span
  class="md-ellipsis"> Standard Library Types </span></a>
- <a href="../../api/types/" class="md-nav__link"><span
  class="md-ellipsis"> Pydantic Types </span></a>
- <a href="../../api/networks/" class="md-nav__link"><span
  class="md-ellipsis"> Network Types </span></a>
- <a href="../../api/version/" class="md-nav__link"><span
  class="md-ellipsis"> Version Information </span></a>
- <a href="../../api/annotated_handlers/" class="md-nav__link"><span
  class="md-ellipsis"> Annotated Handlers </span></a>
- <a href="../../api/experimental/" class="md-nav__link"><span
  class="md-ellipsis"> Experimental </span></a>

<span class="md-ellipsis"> Pydantic Core </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Pydantic Core

- <a href="../../api/pydantic_core/" class="md-nav__link"><span
  class="md-ellipsis"> pydantic_core </span></a>
- <a href="../../api/pydantic_core_schema/" class="md-nav__link"><span
  class="md-ellipsis"> pydantic_core.core_schema </span></a>

<a href="../../api/pydantic_settings/" class="md-nav__link"><span
class="md-ellipsis"> Pydantic Settings </span></a>

<span class="md-ellipsis"> Pydantic Extra Types </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Pydantic Extra Types

- <a href="../../api/pydantic_extra_types_color/"
  class="md-nav__link"><span class="md-ellipsis"> Color </span></a>
- <a href="../../api/pydantic_extra_types_country/"
  class="md-nav__link"><span class="md-ellipsis"> Country </span></a>
- <a href="../../api/pydantic_extra_types_payment/"
  class="md-nav__link"><span class="md-ellipsis"> Payment </span></a>
- <a href="../../api/pydantic_extra_types_phone_numbers/"
  class="md-nav__link"><span class="md-ellipsis"> Phone Numbers
  </span></a>
- <a href="../../api/pydantic_extra_types_routing_numbers/"
  class="md-nav__link"><span class="md-ellipsis"> Routing Numbers
  </span></a>
- <a href="../../api/pydantic_extra_types_coordinate/"
  class="md-nav__link"><span class="md-ellipsis"> Coordinate </span></a>
- <a href="../../api/pydantic_extra_types_mac_address/"
  class="md-nav__link"><span class="md-ellipsis"> Mac Address </span></a>
- <a href="../../api/pydantic_extra_types_isbn/"
  class="md-nav__link"><span class="md-ellipsis"> ISBN </span></a>
- <a href="../../api/pydantic_extra_types_pendulum_dt/"
  class="md-nav__link"><span class="md-ellipsis"> Pendulum </span></a>
- <a href="../../api/pydantic_extra_types_currency_code/"
  class="md-nav__link"><span class="md-ellipsis"> Currency </span></a>
- <a href="../../api/pydantic_extra_types_language_code/"
  class="md-nav__link"><span class="md-ellipsis"> Language </span></a>
- <a href="../../api/pydantic_extra_types_script_code/"
  class="md-nav__link"><span class="md-ellipsis"> Script Code </span></a>
- <a href="../../api/pydantic_extra_types_semantic_version/"
  class="md-nav__link"><span class="md-ellipsis"> Semantic Version
  </span></a>
- <a href="../../api/pydantic_extra_types_timezone_name/"
  class="md-nav__link"><span class="md-ellipsis"> Timezone Name
  </span></a>
- <a href="../../api/pydantic_extra_types_ulid/"
  class="md-nav__link"><span class="md-ellipsis"> ULID </span></a>

<span class="md-ellipsis"> Internals </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Internals

- <a href="../../internals/architecture/" class="md-nav__link"><span
  class="md-ellipsis"> Architecture </span></a>
- <a href="../../internals/resolving_annotations/"
  class="md-nav__link"><span class="md-ellipsis"> Resolving Annotations
  </span></a>

<span class="md-ellipsis"> Examples </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Examples

- <a href="../../examples/files/" class="md-nav__link"><span
  class="md-ellipsis"> Validating File Data </span></a>
- <a href="../../examples/requests/" class="md-nav__link"><span
  class="md-ellipsis"> Web and API Requests </span></a>
- <a href="../../examples/queues/" class="md-nav__link"><span
  class="md-ellipsis"> Queues </span></a>
- <a href="../../examples/orms/" class="md-nav__link"><span
  class="md-ellipsis"> Databases </span></a>
- <a href="../../examples/custom_validators/" class="md-nav__link"><span
  class="md-ellipsis"> Custom Validators </span></a>

<span class="md-ellipsis"> Error Messages </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Error Messages

- <a href="../../errors/errors/" class="md-nav__link"><span
  class="md-ellipsis"> Error Handling </span></a>
- <a href="../../errors/validation_errors/" class="md-nav__link"><span
  class="md-ellipsis"> Validation Errors </span></a>
- <a href="../../errors/usage_errors/" class="md-nav__link"><span
  class="md-ellipsis"> Usage Errors </span></a>

<span class="md-ellipsis"> Integrations </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Integrations

<a href="../../integrations/logfire/" class="md-nav__link"><span
class="md-ellipsis"> Pydantic Logfire </span></a>

<a href="../../integrations/llms/" class="md-nav__link"><span
class="md-ellipsis"> LLMs </span></a>

<span class="md-ellipsis"> Dev Tools </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Dev Tools

- <a href="../../integrations/mypy/" class="md-nav__link"><span
  class="md-ellipsis"> Mypy </span></a>
- <a href="../../integrations/pycharm/" class="md-nav__link"><span
  class="md-ellipsis"> PyCharm </span></a>
- <a href="../../integrations/hypothesis/" class="md-nav__link"><span
  class="md-ellipsis"> Hypothesis </span></a>
- <a href="../../integrations/visual_studio_code/"
  class="md-nav__link"><span class="md-ellipsis"> Visual Studio Code
  </span></a>
- <a href="../../integrations/datamodel_code_generator/"
  class="md-nav__link"><span class="md-ellipsis"> datamodel-code-generator
  </span></a>
- <a href="../../integrations/devtools/" class="md-nav__link"><span
  class="md-ellipsis"> devtools </span></a>
- <a href="../../integrations/rich/" class="md-nav__link"><span
  class="md-ellipsis"> Rich </span></a>
- <a href="../../integrations/linting/" class="md-nav__link"><span
  class="md-ellipsis"> Linting </span></a>
- <a href="../../integrations/documentation/" class="md-nav__link"><span
  class="md-ellipsis"> Documentation </span></a>

<span class="md-ellipsis"> Production Tools </span>
<span class="md-nav__icon md-icon"></span>

<span class="md-nav__icon md-icon"></span> Production Tools

- <a href="../../integrations/aws_lambda/" class="md-nav__link"><span
  class="md-ellipsis"> AWS Lambda </span></a>

<a href="https://blog.pydantic.dev/" class="md-nav__link"><span
class="md-ellipsis"> Blog </span></a>

<a href="../../pydantic_people/" class="md-nav__link"><span
class="md-ellipsis"> Pydantic People </span></a>

</div>

</div>

</div>

<div class="md-sidebar md-sidebar--secondary" md-component="sidebar"
md-type="toc">

<div class="md-sidebar__scrollwrap">

<div class="md-sidebar__inner">

<span class="md-nav__icon md-icon"></span> Page contents

- <a href="#installation" class="md-nav__link"><span class="md-ellipsis">
  Installation </span></a>
- <a href="#usage" class="md-nav__link"><span class="md-ellipsis"> Usage
  </span></a>
- <a href="#validation-of-default-values" class="md-nav__link"><span
  class="md-ellipsis"> Validation of default values </span></a>
- <a href="#environment-variable-names" class="md-nav__link"><span
  class="md-ellipsis"> Environment variable names </span></a>
  - <a href="#case-sensitivity" class="md-nav__link"><span
    class="md-ellipsis"> Case-sensitivity </span></a>
- <a href="#parsing-environment-variable-values"
  class="md-nav__link"><span class="md-ellipsis"> Parsing environment
  variable values </span></a>
  - <a href="#disabling-json-parsing" class="md-nav__link"><span
    class="md-ellipsis"> Disabling JSON parsing </span></a>
- <a href="#nested-model-default-partial-updates"
  class="md-nav__link"><span class="md-ellipsis"> Nested model default
  partial updates </span></a>
- <a href="#dotenv-env-support" class="md-nav__link"><span
  class="md-ellipsis"> Dotenv (.env) support </span></a>
- <a href="#command-line-support" class="md-nav__link"><span
  class="md-ellipsis"> Command Line Support </span></a>
  - <a href="#the-basics" class="md-nav__link"><span class="md-ellipsis">
    The Basics </span></a>
    - <a href="#lists" class="md-nav__link"><span class="md-ellipsis"> Lists
      </span></a>
    - <a href="#dictionaries" class="md-nav__link"><span class="md-ellipsis">
      Dictionaries </span></a>
    - <a href="#literals-and-enums" class="md-nav__link"><span
      class="md-ellipsis"> Literals and Enums </span></a>
    - <a href="#aliases" class="md-nav__link"><span class="md-ellipsis">
      Aliases </span></a>
  - <a href="#subcommands-and-positional-arguments"
    class="md-nav__link"><span class="md-ellipsis"> Subcommands and
    Positional Arguments </span></a>
  - <a href="#creating-cli-applications" class="md-nav__link"><span
    class="md-ellipsis"> Creating CLI Applications </span></a>
  - <a href="#asynchronous-cli-commands" class="md-nav__link"><span
    class="md-ellipsis"> Asynchronous CLI Commands </span></a>
    - <a href="#asynchronous-subcommands" class="md-nav__link"><span
      class="md-ellipsis"> Asynchronous Subcommands </span></a>
  - <a href="#mutually-exclusive-groups" class="md-nav__link"><span
    class="md-ellipsis"> Mutually Exclusive Groups </span></a>
  - <a href="#customizing-the-cli-experience" class="md-nav__link"><span
    class="md-ellipsis"> Customizing the CLI Experience </span></a>
    - <a href="#change-the-displayed-program-name" class="md-nav__link"><span
      class="md-ellipsis"> Change the Displayed Program Name </span></a>
    - <a href="#cli-boolean-flags" class="md-nav__link"><span
      class="md-ellipsis"> CLI Boolean Flags </span></a>
    - <a href="#ignore-unknown-arguments" class="md-nav__link"><span
      class="md-ellipsis"> Ignore Unknown Arguments </span></a>
    - <a href="#cli-kebab-case-for-arguments" class="md-nav__link"><span
      class="md-ellipsis"> CLI Kebab Case for Arguments </span></a>
    - <a href="#change-whether-cli-should-exit-on-error"
      class="md-nav__link"><span class="md-ellipsis"> Change Whether CLI
      Should Exit on Error </span></a>
    - <a href="#enforce-required-arguments-at-cli" class="md-nav__link"><span
      class="md-ellipsis"> Enforce Required Arguments at CLI </span></a>
    - <a href="#change-the-none-type-parse-string" class="md-nav__link"><span
      class="md-ellipsis"> Change the None Type Parse String </span></a>
    - <a href="#hide-none-type-values" class="md-nav__link"><span
      class="md-ellipsis"> Hide None Type Values </span></a>
    - <a href="#avoid-adding-json-cli-options" class="md-nav__link"><span
      class="md-ellipsis"> Avoid Adding JSON CLI Options </span></a>
    - <a href="#use-class-docstring-for-group-help-text"
      class="md-nav__link"><span class="md-ellipsis"> Use Class Docstring for
      Group Help Text </span></a>
    - <a href="#change-the-cli-flag-prefix-character"
      class="md-nav__link"><span class="md-ellipsis"> Change the CLI Flag
      Prefix Character </span></a>
    - <a href="#suppressing-fields-from-cli-help-text"
      class="md-nav__link"><span class="md-ellipsis"> Suppressing Fields from
      CLI Help Text </span></a>
  - <a href="#integrating-with-existing-parsers" class="md-nav__link"><span
    class="md-ellipsis"> Integrating with Existing Parsers </span></a>
- <a href="#secrets" class="md-nav__link"><span class="md-ellipsis">
  Secrets </span></a>
  - <a href="#use-case-docker-secrets" class="md-nav__link"><span
    class="md-ellipsis"> Use Case: Docker Secrets </span></a>
- <a href="#aws-secrets-manager" class="md-nav__link"><span
  class="md-ellipsis"> AWS Secrets Manager </span></a>
- <a href="#azure-key-vault" class="md-nav__link"><span
  class="md-ellipsis"> Azure Key Vault </span></a>
- <a href="#other-settings-source" class="md-nav__link"><span
  class="md-ellipsis"> Other settings source </span></a>
  - <a href="#pyprojecttoml" class="md-nav__link"><span class="md-ellipsis">
    pyproject.toml </span></a>
- <a href="#field-value-priority" class="md-nav__link"><span
  class="md-ellipsis"> Field value priority </span></a>
- <a href="#customise-settings-sources" class="md-nav__link"><span
  class="md-ellipsis"> Customise settings sources </span></a>
  - <a href="#changing-priority" class="md-nav__link"><span
    class="md-ellipsis"> Changing Priority </span></a>
  - <a href="#adding-sources" class="md-nav__link"><span
    class="md-ellipsis"> Adding sources </span></a>
    - <a href="#accesing-the-result-of-previous-sources"
      class="md-nav__link"><span class="md-ellipsis"> Accesing the result of
      previous sources </span></a>
  - <a href="#removing-sources" class="md-nav__link"><span
    class="md-ellipsis"> Removing sources </span></a>
- <a href="#in-place-reloading" class="md-nav__link"><span
  class="md-ellipsis"> In-place reloading </span></a>

</div>

</div>

</div>

<div class="md-content" md-component="content">

# Settings Management<a href="#settings-management" class="headerlink"
title="Permanent link">¶</a>

[Pydantic Settings](https://github.com/pydantic/pydantic-settings)
provides optional Pydantic features for loading a settings or config
class from environment variables or secrets files.

## Installation<a href="#installation" class="headerlink" title="Permanent link">¶</a>

Installation is as simple as:

<div class="language-bash highlight">

    pip install pydantic-settings

</div>

## Usage<a href="#usage" class="headerlink" title="Permanent link">¶</a>

If you create a model that inherits from `BaseSettings`, the model
initialiser will attempt to determine the values of any fields not
passed as keyword arguments by reading from the environment. (Default
values will still be used if the matching environment variable is not
set.)

This makes it easy to:

- Create a clearly-defined, type-hinted application configuration class
- Automatically read modifications to the configuration from environment
  variables
- Manually override specific settings in the initialiser where desired
  (e.g. in unit tests)

For example:

<div class="language-py highlight">

    from collections.abc import Callable
    from typing import Any

    from pydantic import (
        AliasChoices,
        AmqpDsn,
        BaseModel,
        Field,
        ImportString,
        PostgresDsn,
        RedisDsn,
    )

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class SubModel(BaseModel):
        foo: str = 'bar'
        apple: int = 1


    class Settings(BaseSettings):
        auth_key: str = Field(validation_alias='my_auth_key')  # (1)!

        api_key: str = Field(alias='my_api_key')  # (2)!

        redis_dsn: RedisDsn = Field(
            'redis://user:pass@localhost:6379/1',
            validation_alias=AliasChoices('service_redis_dsn', 'redis_url'),  # (3)!
        )
        pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
        amqp_dsn: AmqpDsn = 'amqp://user:pass@localhost:5672/'

        special_function: ImportString[Callable[[Any], Any]] = 'math.cos'  # (4)!

        # to override domains:
        # export my_prefix_domains='["foo.com", "bar.com"]'
        domains: set[str] = set()

        # to override more_settings:
        # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
        more_settings: SubModel = SubModel()

        model_config = SettingsConfigDict(env_prefix='my_prefix_')  # (5)!


    print(Settings().model_dump())
    """
    {
        'auth_key': 'xxx',
        'api_key': 'xxx',
        'redis_dsn': RedisDsn('redis://user:pass@localhost:6379/1'),
        'pg_dsn': PostgresDsn('postgres://user:pass@localhost:5432/foobar'),
        'amqp_dsn': AmqpDsn('amqp://user:pass@localhost:5672/'),
        'special_function': math.cos,
        'domains': set(),
        'more_settings': {'foo': 'bar', 'apple': 1},
    }
    """

</div>

1.  The environment variable name is overridden using
    `validation_alias`. In this case, the environment variable
    `my_auth_key` will be read instead of `auth_key`.

    Check the [`Field` documentation](../fields/) for more information.

2.  The environment variable name is overridden using `alias`. In this
    case, the environment variable `my_api_key` will be used for both
    validation and serialization instead of `api_key`.

    Check the [`Field` documentation](../fields/#field-aliases) for more
    information.

3.  The <a href="../../api/aliases/#pydantic.aliases.AliasChoices"
    class="autorefs autorefs-internal"><code>AliasChoices</code></a>
    class allows to have multiple environment variable names for a
    single field. The first environment variable that is found will be
    used.

    Check the [documentation on alias
    choices](../alias/#aliaspath-and-aliaschoices) for more information.

4.  The <a href="../../api/types/#pydantic.types.ImportString"
    class="autorefs autorefs-internal"><code>ImportString</code></a>
    class allows to import an object from a string. In this case, the
    environment variable `special_function` will be read and the
    function
    <a href="https://docs.python.org/3/library/math.html#math.cos"
    class="autorefs autorefs-external"><code>math.cos</code></a> will be
    imported.

5.  The `env_prefix` config setting allows to set a prefix for all
    environment variables.

    Check the [Environment variable names
    documentation](#environment-variable-names) for more information.

## Validation of default values<a href="#validation-of-default-values" class="headerlink"
title="Permanent link">¶</a>

Unlike pydantic `BaseModel`, default values of `BaseSettings` fields are
validated by default. You can disable this behaviour by setting
`validate_default=False` either in `model_config` or on field level by
`Field(validate_default=False)`:

<div class="language-py highlight">

    from pydantic import Field

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(validate_default=False)

        # default won't be validated
        foo: int = 'test'


    print(Settings())
    #> foo='test'


    class Settings1(BaseSettings):
        # default won't be validated
        foo: int = Field('test', validate_default=False)


    print(Settings1())
    #> foo='test'

</div>

Check the [validation of default
values](../fields/#validate-default-values) for more information.

## Environment variable names<a href="#environment-variable-names" class="headerlink"
title="Permanent link">¶</a>

By default, the environment variable name is the same as the field name.

You can change the prefix for all environment variables by setting the
`env_prefix` config setting, or via the `_env_prefix` keyword argument
on instantiation:

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_prefix='my_prefix_')

        auth_key: str = 'xxx'  # will be read from `my_prefix_auth_key`

</div>

<div class="admonition note">

Note

The default `env_prefix` is `''` (empty string). `env_prefix` is not
only for env settings but also for dotenv files, secrets, and other
sources.

</div>

If you want to change the environment variable name for a single field,
you can use an alias.

There are two ways to do this:

- Using `Field(alias=...)` (see `api_key` above)
- Using `Field(validation_alias=...)` (see `auth_key` above)

Check the [`Field` aliases documentation](../fields/#field-aliases) for
more information about aliases.

`env_prefix` does not apply to fields with alias. It means the
environment variable name is the same as field alias:

<div class="language-py highlight">

    from pydantic import Field

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_prefix='my_prefix_')

        foo: str = Field('xxx', alias='FooAlias')  # (1)!

</div>

1.  `env_prefix` will be ignored and the value will be read from
    `FooAlias` environment variable.

### Case-sensitivity<a href="#case-sensitivity" class="headerlink"
title="Permanent link">¶</a>

By default, environment variable names are case-insensitive.

If you want to make environment variable names case-sensitive, you can
set the `case_sensitive` config setting:

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(case_sensitive=True)

        redis_host: str = 'localhost'

</div>

When `case_sensitive` is `True`, the environment variable names must
match field names (optionally with a prefix), so in this example
`redis_host` could only be modified via `export redis_host`. If you want
to name environment variables all upper-case, you should name attribute
all upper-case too. You can still name environment variables anything
you like through `Field(validation_alias=...)`.

Case-sensitivity can also be set via the `_case_sensitive` keyword
argument on instantiation.

In case of nested models, the `case_sensitive` setting will be applied
to all nested models.

<div class="language-py highlight">

    import os

    from pydantic import BaseModel, ValidationError

    from pydantic_settings import BaseSettings


    class RedisSettings(BaseModel):
        host: str
        port: int


    class Settings(BaseSettings, case_sensitive=True):
        redis: RedisSettings


    os.environ['redis'] = '{"host": "localhost", "port": 6379}'
    print(Settings().model_dump())
    #> {'redis': {'host': 'localhost', 'port': 6379}}
    os.environ['redis'] = '{"HOST": "localhost", "port": 6379}'  # (1)!
    try:
        Settings()
    except ValidationError as e:
        print(e)
        """
        1 validation error for Settings
        redis.host
          Field required [type=missing, input_value={'HOST': 'localhost', 'port': 6379}, input_type=dict]
            For further information visit https://errors.pydantic.dev/2/v/missing
        """

</div>

1.  Note that the `host` field is not found because the environment
    variable name is `HOST` (all upper-case).

<div class="admonition note">

Note

On Windows, Python's `os` module always treats environment variables as
case-insensitive, so the `case_sensitive` config setting will have no
effect - settings will always be updated ignoring case.

</div>

## Parsing environment variable values<a href="#parsing-environment-variable-values" class="headerlink"
title="Permanent link">¶</a>

By default environment variables are parsed verbatim, including if the
value is empty. You can choose to ignore empty environment variables by
setting the `env_ignore_empty` config setting to `True`. This can be
useful if you would prefer to use the default value for a field rather
than an empty value from the environment.

For most simple field types (such as `int`, `float`, `str`, etc.), the
environment variable value is parsed the same way it would be if passed
directly to the initialiser (as a string).

Complex types like `list`, `set`, `dict`, and sub-models are populated
from the environment by treating the environment variable's value as a
JSON-encoded string.

Another way to populate nested complex variables is to configure your
model with the `env_nested_delimiter` config setting, then use an
environment variable with a name pointing to the nested module fields.
What it does is simply explodes your variable into nested models or
dicts. So if you define a variable `FOO__BAR__BAZ=123` it will convert
it into `FOO={'BAR': {'BAZ': 123}}` If you have multiple variables with
the same structure they will be merged.

<div class="admonition note">

Note

Sub model has to inherit from `pydantic.BaseModel`, Otherwise
`pydantic-settings` will initialize sub model, collects values for sub
model fields separately, and you may get unexpected results.

</div>

As an example, given the following environment variables:

<div class="language-bash highlight">

    # your environment
    export V0=0
    export SUB_MODEL='{"v1": "json-1", "v2": "json-2"}'
    export SUB_MODEL__V2=nested-2
    export SUB_MODEL__V3=3
    export SUB_MODEL__DEEP__V4=v4

</div>

You could load them into the following settings model:

<div class="language-py highlight">

    from pydantic import BaseModel

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class DeepSubModel(BaseModel):  # (1)!
        v4: str


    class SubModel(BaseModel):  # (2)!
        v1: str
        v2: bytes
        v3: int
        deep: DeepSubModel


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_nested_delimiter='__')

        v0: str
        sub_model: SubModel


    print(Settings().model_dump())
    """
    {
        'v0': '0',
        'sub_model': {'v1': 'json-1', 'v2': b'nested-2', 'v3': 3, 'deep': {'v4': 'v4'}},
    }
    """

</div>

1.  Sub model has to inherit from `pydantic.BaseModel`.

2.  Sub model has to inherit from `pydantic.BaseModel`.

`env_nested_delimiter` can be configured via the `model_config` as shown
above, or via the `_env_nested_delimiter` keyword argument on
instantiation.

By default environment variables are split by `env_nested_delimiter`
into arbitrarily deep nested fields. You can limit the depth of the
nested fields with the `env_nested_max_split` config setting. A common
use case this is particularly useful is for two-level deep settings,
where the `env_nested_delimiter` (usually a single `_`) may be a
substring of model field names. For example:

<div class="language-bash highlight">

    # your environment
    export GENERATION_LLM_PROVIDER='anthropic'
    export GENERATION_LLM_API_KEY='your-api-key'
    export GENERATION_LLM_API_VERSION='2024-03-15'

</div>

You could load them into the following settings model:

<div class="language-py highlight">

    from pydantic import BaseModel

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class LLMConfig(BaseModel):
        provider: str = 'openai'
        api_key: str
        api_type: str = 'azure'
        api_version: str = '2023-03-15-preview'


    class GenerationConfig(BaseSettings):
        model_config = SettingsConfigDict(
            env_nested_delimiter='_', env_nested_max_split=1, env_prefix='GENERATION_'
        )

        llm: LLMConfig
        ...


    print(GenerationConfig().model_dump())
    """
    {
        'llm': {
            'provider': 'anthropic',
            'api_key': 'your-api-key',
            'api_type': 'azure',
            'api_version': '2024-03-15',
        }
    }
    """

</div>

Without `env_nested_max_split=1` set, `GENERATION_LLM_API_KEY` would be
parsed as `llm.api.key` instead of `llm.api_key` and it would raise a
`ValidationError`.

Nested environment variables take precedence over the top-level
environment variable JSON (e.g. in the example above, `SUB_MODEL__V2`
trumps `SUB_MODEL`).

You may also populate a complex type by providing your own source class.

<div class="language-py highlight">

    import json
    import os
    from typing import Any

    from pydantic.fields import FieldInfo

    from pydantic_settings import (
        BaseSettings,
        EnvSettingsSource,
        PydanticBaseSettingsSource,
    )


    class MyCustomSource(EnvSettingsSource):
        def prepare_field_value(
            self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
        ) -> Any:
            if field_name == 'numbers':
                return [int(x) for x in value.split(',')]
            return json.loads(value)


    class Settings(BaseSettings):
        numbers: list[int]

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return (MyCustomSource(settings_cls),)


    os.environ['numbers'] = '1,2,3'
    print(Settings().model_dump())
    #> {'numbers': [1, 2, 3]}

</div>

### Disabling JSON parsing<a href="#disabling-json-parsing" class="headerlink"
title="Permanent link">¶</a>

pydantic-settings by default parses complex types from environment
variables as JSON strings. If you want to disable this behavior for a
field and parse the value in your own validator, you can annotate the
field with
[`NoDecode`](../../api/pydantic_settings/#pydantic_settings.NoDecode):

<div class="language-py highlight">

    import os
    from typing import Annotated

    from pydantic import field_validator

    from pydantic_settings import BaseSettings, NoDecode


    class Settings(BaseSettings):
        numbers: Annotated[list[int], NoDecode]  # (1)!

        @field_validator('numbers', mode='before')
        @classmethod
        def decode_numbers(cls, v: str) -> list[int]:
            return [int(x) for x in v.split(',')]


    os.environ['numbers'] = '1,2,3'
    print(Settings().model_dump())
    #> {'numbers': [1, 2, 3]}

</div>

1.  The `NoDecode` annotation disables JSON parsing for the `numbers`
    field. The `decode_numbers` field validator will be called to parse
    the value.

You can also disable JSON parsing for all fields by setting the
`enable_decoding` config setting to `False`:

<div class="language-py highlight">

    import os

    from pydantic import field_validator

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(enable_decoding=False)

        numbers: list[int]

        @field_validator('numbers', mode='before')
        @classmethod
        def decode_numbers(cls, v: str) -> list[int]:
            return [int(x) for x in v.split(',')]


    os.environ['numbers'] = '1,2,3'
    print(Settings().model_dump())
    #> {'numbers': [1, 2, 3]}

</div>

You can force JSON parsing for a field by annotating it with
[`ForceDecode`](../../api/pydantic_settings/#pydantic_settings.ForceDecode).
This will bypass the `enable_decoding` config setting:

<div class="language-py highlight">

    import os
    from typing import Annotated

    from pydantic import field_validator

    from pydantic_settings import BaseSettings, ForceDecode, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(enable_decoding=False)

        numbers: Annotated[list[int], ForceDecode]
        numbers1: list[int]  # (1)!

        @field_validator('numbers1', mode='before')
        @classmethod
        def decode_numbers1(cls, v: str) -> list[int]:
            return [int(x) for x in v.split(',')]


    os.environ['numbers'] = '["1","2","3"]'
    os.environ['numbers1'] = '1,2,3'
    print(Settings().model_dump())
    #> {'numbers': [1, 2, 3], 'numbers1': [1, 2, 3]}

</div>

1.  The `numbers1` field is not annotated with `ForceDecode`, so it will
    not be parsed as JSON. and we have to provide a custom validator to
    parse the value.

## Nested model default partial updates<a href="#nested-model-default-partial-updates" class="headerlink"
title="Permanent link">¶</a>

By default, Pydantic settings does not allow partial updates to nested
model default objects. This behavior can be overriden by setting the
`nested_model_default_partial_update` flag to `True`, which will allow
partial updates on nested model default object fields.

<div class="language-py highlight">

    import os

    from pydantic import BaseModel

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class SubModel(BaseModel):
        val: int = 0
        flag: bool = False


    class SettingsPartialUpdate(BaseSettings):
        model_config = SettingsConfigDict(
            env_nested_delimiter='__', nested_model_default_partial_update=True
        )

        nested_model: SubModel = SubModel(val=1)


    class SettingsNoPartialUpdate(BaseSettings):
        model_config = SettingsConfigDict(
            env_nested_delimiter='__', nested_model_default_partial_update=False
        )

        nested_model: SubModel = SubModel(val=1)


    # Apply a partial update to the default object using environment variables
    os.environ['NESTED_MODEL__FLAG'] = 'True'

    # When partial update is enabled, the existing SubModel instance is updated
    # with nested_model.flag=True change
    assert SettingsPartialUpdate().model_dump() == {
        'nested_model': {'val': 1, 'flag': True}
    }

    # When partial update is disabled, a new SubModel instance is instantiated
    # with nested_model.flag=True change
    assert SettingsNoPartialUpdate().model_dump() == {
        'nested_model': {'val': 0, 'flag': True}
    }

</div>

## Dotenv (.env) support<a href="#dotenv-env-support" class="headerlink"
title="Permanent link">¶</a>

Dotenv files (generally named `.env`) are a common pattern that make it
easy to use environment variables in a platform-independent manner.

A dotenv file follows the same general principles of all environment
variables, and it looks like this:

<div class="language-bash highlight">

<span class="filename">.env</span>

    # ignore comment
    ENVIRONMENT="production"
    REDIS_ADDRESS=localhost:6379
    MEANING_OF_LIFE=42
    MY_VAR='Hello world'

</div>

Once you have your `.env` file filled with variables, *pydantic*
supports loading it in two ways:

1.  Setting the `env_file` (and `env_file_encoding` if you don't want
    the default encoding of your OS) on `model_config` in the
    `BaseSettings` class:
    <div class="language-py highlight">

        from pydantic_settings import BaseSettings, SettingsConfigDict


        class Settings(BaseSettings):
            model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    </div>
2.  Instantiating the `BaseSettings` derived class with the `_env_file`
    keyword argument (and the `_env_file_encoding` if needed):
    <div class="language-py highlight">

        from pydantic_settings import BaseSettings, SettingsConfigDict


        class Settings(BaseSettings):
            model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


        settings = Settings(_env_file='prod.env', _env_file_encoding='utf-8')

    </div>

    In either case, the value of the passed argument can be any valid
    path or filename, either absolute or relative to the current working
    directory. From there, *pydantic* will handle everything for you by
    loading in your variables and validating them.

<div class="admonition note">

Note

If a filename is specified for `env_file`, Pydantic will only check the
current working directory and won't check any parent directories for the
`.env` file.

</div>

Even when using a dotenv file, *pydantic* will still read environment
variables as well as the dotenv file, **environment variables will
always take priority over values loaded from a dotenv file**.

Passing a file path via the `_env_file` keyword argument on
instantiation (method 2) will override the value (if any) set on the
`model_config` class. If the above snippets were used in conjunction,
`prod.env` would be loaded while `.env` would be ignored.

If you need to load multiple dotenv files, you can pass multiple file
paths as a tuple or list. The files will be loaded in order, with each
file overriding the previous one.

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(
            # `.env.prod` takes priority over `.env`
            env_file=('.env', '.env.prod')
        )

</div>

You can also use the keyword argument override to tell Pydantic not to
load any file at all (even if one is set in the `model_config` class) by
passing `None` as the instantiation keyword argument, e.g.
`settings = Settings(_env_file=None)`.

Because python-dotenv is used to parse the file, bash-like semantics
such as `export` can be used which (depending on your OS and
environment) may allow your dotenv file to also be used with `source`,
see [python-dotenv's
documentation](https://saurabh-kumar.com/python-dotenv/#usages) for more
details.

Pydantic settings consider `extra` config in case of dotenv file. It
means if you set the `extra=forbid` (*default*) on `model_config` and
your dotenv file contains an entry for a field that is not defined in
settings model, it will raise `ValidationError` in settings
construction.

For compatibility with pydantic 1.x BaseSettings you should use
`extra=ignore`:

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_file='.env', extra='ignore')

</div>

<div class="admonition note">

Note

Pydantic settings loads all the values from dotenv file and passes it to
the model, regardless of the model's `env_prefix`. So if you provide
extra values in a dotenv file, whether they start with `env_prefix` or
not, a `ValidationError` will be raised.

</div>

## Command Line Support<a href="#command-line-support" class="headerlink"
title="Permanent link">¶</a>

Pydantic settings provides integrated CLI support, making it easy to
quickly define CLI applications using Pydantic models. There are two
primary use cases for Pydantic settings CLI:

1.  When using a CLI to override fields in Pydantic models.
2.  When using Pydantic models to define CLIs.

By default, the experience is tailored towards use case \#1 and builds
on the foundations established in [parsing environment
variables](#parsing-environment-variable-values). If your use case
primarily falls into \#2, you will likely want to enable most of the
defaults outlined at the end of [creating CLI
applications](#creating-cli-applications).

### The Basics<a href="#the-basics" class="headerlink" title="Permanent link">¶</a>

To get started, let's revisit the example presented in [parsing
environment variables](#parsing-environment-variable-values) but using a
Pydantic settings CLI:

<div class="language-py highlight">

    import sys

    from pydantic import BaseModel

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class DeepSubModel(BaseModel):
        v4: str


    class SubModel(BaseModel):
        v1: str
        v2: bytes
        v3: int
        deep: DeepSubModel


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(cli_parse_args=True)

        v0: str
        sub_model: SubModel


    sys.argv = [
        'example.py',
        '--v0=0',
        '--sub_model={"v1": "json-1", "v2": "json-2"}',
        '--sub_model.v2=nested-2',
        '--sub_model.v3=3',
        '--sub_model.deep.v4=v4',
    ]

    print(Settings().model_dump())
    """
    {
        'v0': '0',
        'sub_model': {'v1': 'json-1', 'v2': b'nested-2', 'v3': 3, 'deep': {'v4': 'v4'}},
    }
    """

</div>

To enable CLI parsing, we simply set the `cli_parse_args` flag to a
valid value, which retains similar connotations as defined in
`argparse`.

Note that a CLI settings source is [**the topmost
source**](#field-value-priority) by default unless its [priority value
is customised](#customise-settings-sources):

<div class="language-py highlight">

    import os
    import sys

    from pydantic_settings import (
        BaseSettings,
        CliSettingsSource,
        PydanticBaseSettingsSource,
    )


    class Settings(BaseSettings):
        my_foo: str

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return env_settings, CliSettingsSource(settings_cls, cli_parse_args=True)


    os.environ['MY_FOO'] = 'from environment'

    sys.argv = ['example.py', '--my_foo=from cli']

    print(Settings().model_dump())
    #> {'my_foo': 'from environment'}

</div>

#### Lists<a href="#lists" class="headerlink" title="Permanent link">¶</a>

CLI argument parsing of lists supports intermixing of any of the below
three styles:

- JSON style `--field='[1,2]'`
- Argparse style `--field 1 --field 2`
- Lazy style `--field=1,2`

<div class="language-py highlight">

    import sys

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True):
        my_list: list[int]


    sys.argv = ['example.py', '--my_list', '[1,2]']
    print(Settings().model_dump())
    #> {'my_list': [1, 2]}

    sys.argv = ['example.py', '--my_list', '1', '--my_list', '2']
    print(Settings().model_dump())
    #> {'my_list': [1, 2]}

    sys.argv = ['example.py', '--my_list', '1,2']
    print(Settings().model_dump())
    #> {'my_list': [1, 2]}

</div>

#### Dictionaries<a href="#dictionaries" class="headerlink" title="Permanent link">¶</a>

CLI argument parsing of dictionaries supports intermixing of any of the
below two styles:

- JSON style `--field='{"k1": 1, "k2": 2}'`
- Environment variable style `--field k1=1 --field k2=2`

These can be used in conjunction with list forms as well, e.g:

- `--field k1=1,k2=2 --field k3=3 --field '{"k4": 4}'` etc.

<div class="language-py highlight">

    import sys

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True):
        my_dict: dict[str, int]


    sys.argv = ['example.py', '--my_dict', '{"k1":1,"k2":2}']
    print(Settings().model_dump())
    #> {'my_dict': {'k1': 1, 'k2': 2}}

    sys.argv = ['example.py', '--my_dict', 'k1=1', '--my_dict', 'k2=2']
    print(Settings().model_dump())
    #> {'my_dict': {'k1': 1, 'k2': 2}}

</div>

#### Literals and Enums<a href="#literals-and-enums" class="headerlink"
title="Permanent link">¶</a>

CLI argument parsing of literals and enums are converted into CLI
choices.

<div class="language-py highlight">

    import sys
    from enum import IntEnum
    from typing import Literal

    from pydantic_settings import BaseSettings


    class Fruit(IntEnum):
        pear = 0
        kiwi = 1
        lime = 2


    class Settings(BaseSettings, cli_parse_args=True):
        fruit: Fruit
        pet: Literal['dog', 'cat', 'bird']


    sys.argv = ['example.py', '--fruit', 'lime', '--pet', 'cat']
    print(Settings().model_dump())
    #> {'fruit': <Fruit.lime: 2>, 'pet': 'cat'}

</div>

#### Aliases<a href="#aliases" class="headerlink" title="Permanent link">¶</a>

Pydantic field aliases are added as CLI argument aliases. Aliases of
length one are converted into short options.

<div class="language-py highlight">

    import sys

    from pydantic import AliasChoices, AliasPath, Field

    from pydantic_settings import BaseSettings


    class User(BaseSettings, cli_parse_args=True):
        first_name: str = Field(
            validation_alias=AliasChoices('f', 'fname', AliasPath('name', 0))
        )
        last_name: str = Field(
            validation_alias=AliasChoices('l', 'lname', AliasPath('name', 1))
        )


    sys.argv = ['example.py', '--fname', 'John', '--lname', 'Doe']
    print(User().model_dump())
    #> {'first_name': 'John', 'last_name': 'Doe'}

    sys.argv = ['example.py', '-f', 'John', '-l', 'Doe']
    print(User().model_dump())
    #> {'first_name': 'John', 'last_name': 'Doe'}

    sys.argv = ['example.py', '--name', 'John,Doe']
    print(User().model_dump())
    #> {'first_name': 'John', 'last_name': 'Doe'}

    sys.argv = ['example.py', '--name', 'John', '--lname', 'Doe']
    print(User().model_dump())
    #> {'first_name': 'John', 'last_name': 'Doe'}

</div>

### Subcommands and Positional Arguments<a href="#subcommands-and-positional-arguments" class="headerlink"
title="Permanent link">¶</a>

Subcommands and positional arguments are expressed using the
`CliSubCommand` and `CliPositionalArg` annotations. The subcommand
annotation can only be applied to required fields (i.e. fields that do
not have a default value). Furthermore, subcommands must be a valid type
derived from either a pydantic `BaseModel` or pydantic.dataclasses
`dataclass`.

Parsed subcommands can be retrieved from model instances using the
`get_subcommand` utility function. If a subcommand is not required, set
the `is_required` flag to `False` to disable raising an error if no
subcommand is found.

<div class="admonition note">

Note

CLI settings subcommands are limited to a single subparser per model. In
other words, all subcommands for a model are grouped under a single
subparser; it does not allow for multiple subparsers with each subparser
having its own set of subcommands. For more information on subparsers,
see [argparse
subcommands](https://docs.python.org/3/library/argparse.html#sub-commands).

</div>

<div class="admonition note">

Note

`CliSubCommand` and `CliPositionalArg` are always case sensitive.

</div>

<div class="language-py highlight">

    import sys

    from pydantic import BaseModel

    from pydantic_settings import (
        BaseSettings,
        CliPositionalArg,
        CliSubCommand,
        SettingsError,
        get_subcommand,
    )


    class Init(BaseModel):
        directory: CliPositionalArg[str]


    class Clone(BaseModel):
        repository: CliPositionalArg[str]
        directory: CliPositionalArg[str]


    class Git(BaseSettings, cli_parse_args=True, cli_exit_on_error=False):
        clone: CliSubCommand[Clone]
        init: CliSubCommand[Init]


    # Run without subcommands
    sys.argv = ['example.py']
    cmd = Git()
    assert cmd.model_dump() == {'clone': None, 'init': None}

    try:
        # Will raise an error since no subcommand was provided
        get_subcommand(cmd).model_dump()
    except SettingsError as err:
        assert str(err) == 'Error: CLI subcommand is required {clone, init}'

    # Will not raise an error since subcommand is not required
    assert get_subcommand(cmd, is_required=False) is None


    # Run the clone subcommand
    sys.argv = ['example.py', 'clone', 'repo', 'dest']
    cmd = Git()
    assert cmd.model_dump() == {
        'clone': {'repository': 'repo', 'directory': 'dest'},
        'init': None,
    }

    # Returns the subcommand model instance (in this case, 'clone')
    assert get_subcommand(cmd).model_dump() == {
        'directory': 'dest',
        'repository': 'repo',
    }

</div>

The `CliSubCommand` and `CliPositionalArg` annotations also support
union operations and aliases. For unions of Pydantic models, it is
important to remember the
[nuances](https://docs.pydantic.dev/latest/concepts/unions/) that can
arise during validation. Specifically, for unions of subcommands that
are identical in content, it is recommended to break them out into
separate `CliSubCommand` fields to avoid any complications. Lastly, the
derived subcommand names from unions will be the names of the Pydantic
model classes themselves.

When assigning aliases to `CliSubCommand` or `CliPositionalArg` fields,
only a single alias can be assigned. For non-union subcommands, aliasing
will change the displayed help text and subcommand name. Conversely, for
union subcommands, aliasing will have no tangible effect from the
perspective of the CLI settings source. Lastly, for positional
arguments, aliasing will change the CLI help text displayed for the
field.

<div class="language-py highlight">

    import sys
    from typing import Union

    from pydantic import BaseModel, Field

    from pydantic_settings import (
        BaseSettings,
        CliPositionalArg,
        CliSubCommand,
        get_subcommand,
    )


    class Alpha(BaseModel):
        """Apha Help"""

        cmd_alpha: CliPositionalArg[str] = Field(alias='alpha-cmd')


    class Beta(BaseModel):
        """Beta Help"""

        opt_beta: str = Field(alias='opt-beta')


    class Gamma(BaseModel):
        """Gamma Help"""

        opt_gamma: str = Field(alias='opt-gamma')


    class Root(BaseSettings, cli_parse_args=True, cli_exit_on_error=False):
        alpha_or_beta: CliSubCommand[Union[Alpha, Beta]] = Field(alias='alpha-or-beta-cmd')
        gamma: CliSubCommand[Gamma] = Field(alias='gamma-cmd')


    sys.argv = ['example.py', 'Alpha', 'hello']
    assert get_subcommand(Root()).model_dump() == {'cmd_alpha': 'hello'}

    sys.argv = ['example.py', 'Beta', '--opt-beta=hey']
    assert get_subcommand(Root()).model_dump() == {'opt_beta': 'hey'}

    sys.argv = ['example.py', 'gamma-cmd', '--opt-gamma=hi']
    assert get_subcommand(Root()).model_dump() == {'opt_gamma': 'hi'}

</div>

### Creating CLI Applications<a href="#creating-cli-applications" class="headerlink"
title="Permanent link">¶</a>

The `CliApp` class provides two utility methods, `CliApp.run` and
`CliApp.run_subcommand`, that can be used to run a Pydantic
`BaseSettings`, `BaseModel`, or `pydantic.dataclasses.dataclass` as a
CLI application. Primarily, the methods provide structure for running
`cli_cmd` methods associated with models.

`CliApp.run` can be used in directly providing the `cli_args` to be
parsed, and will run the model `cli_cmd` method (if defined) after
instantiation:

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, CliApp


    class Settings(BaseSettings):
        this_foo: str

        def cli_cmd(self) -> None:
            # Print the parsed data
            print(self.model_dump())
            #> {'this_foo': 'is such a foo'}

            # Update the parsed data showing cli_cmd ran
            self.this_foo = 'ran the foo cli cmd'


    s = CliApp.run(Settings, cli_args=['--this_foo', 'is such a foo'])
    print(s.model_dump())
    #> {'this_foo': 'ran the foo cli cmd'}

</div>

Similarly, the `CliApp.run_subcommand` can be used in recursive fashion
to run the `cli_cmd` method of a subcommand:

<div class="language-py highlight">

    from pydantic import BaseModel

    from pydantic_settings import CliApp, CliPositionalArg, CliSubCommand


    class Init(BaseModel):
        directory: CliPositionalArg[str]

        def cli_cmd(self) -> None:
            print(f'git init "{self.directory}"')
            #> git init "dir"
            self.directory = 'ran the git init cli cmd'


    class Clone(BaseModel):
        repository: CliPositionalArg[str]
        directory: CliPositionalArg[str]

        def cli_cmd(self) -> None:
            print(f'git clone from "{self.repository}" into "{self.directory}"')
            self.directory = 'ran the clone cli cmd'


    class Git(BaseModel):
        clone: CliSubCommand[Clone]
        init: CliSubCommand[Init]

        def cli_cmd(self) -> None:
            CliApp.run_subcommand(self)


    cmd = CliApp.run(Git, cli_args=['init', 'dir'])
    assert cmd.model_dump() == {
        'clone': None,
        'init': {'directory': 'ran the git init cli cmd'},
    }

</div>

<div class="admonition note">

Note

Unlike `CliApp.run`, `CliApp.run_subcommand` requires the subcommand
model to have a defined `cli_cmd` method.

</div>

For `BaseModel` and `pydantic.dataclasses.dataclass` types, `CliApp.run`
will internally use the following `BaseSettings` configuration defaults:

- `nested_model_default_partial_update=True`
- `case_sensitive=True`
- `cli_hide_none_type=True`
- `cli_avoid_json=True`
- `cli_enforce_required=True`
- `cli_implicit_flags=True`
- `cli_kebab_case=True`

### Asynchronous CLI Commands<a href="#asynchronous-cli-commands" class="headerlink"
title="Permanent link">¶</a>

Pydantic settings supports running asynchronous CLI commands via
`CliApp.run` and `CliApp.run_subcommand`. With this feature, you can
define async def methods within your Pydantic models (including
subcommands) and have them executed just like their synchronous
counterparts. Specifically:

1.  Asynchronous methods are supported: You can now mark your cli_cmd or
    similar CLI entrypoint methods as async def and have CliApp execute
    them.
2.  Subcommands may also be asynchronous: If you have nested CLI
    subcommands, the final (lowest-level) subcommand methods can
    likewise be asynchronous.
3.  Limit asynchronous methods to final subcommands: Defining parent
    commands as asynchronous is not recommended, because it can result
    in additional threads and event loops being created. For best
    performance and to avoid unnecessary resource usage, only implement
    your deepest (child) subcommands as async def.

Below is a simple example demonstrating an asynchronous top-level
command:

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, CliApp


    class AsyncSettings(BaseSettings):
        async def cli_cmd(self) -> None:
            print('Hello from an async CLI method!')
            #> Hello from an async CLI method!


    # If an event loop is already running, a new thread will be used;
    # otherwise, asyncio.run() is used to execute this async method.
    assert CliApp.run(AsyncSettings, cli_args=[]).model_dump() == {}

</div>

#### Asynchronous Subcommands<a href="#asynchronous-subcommands" class="headerlink"
title="Permanent link">¶</a>

As mentioned above, you can also define subcommands as async. However,
only do so for the leaf (lowest-level) subcommand to avoid spawning new
threads and event loops unnecessarily in parent commands:

<div class="language-py highlight">

    from pydantic import BaseModel

    from pydantic_settings import (
        BaseSettings,
        CliApp,
        CliPositionalArg,
        CliSubCommand,
    )


    class Clone(BaseModel):
        repository: CliPositionalArg[str]
        directory: CliPositionalArg[str]

        async def cli_cmd(self) -> None:
            # Perform async tasks here, e.g. network or I/O operations
            print(f'Cloning async from "{self.repository}" into "{self.directory}"')
            #> Cloning async from "repo" into "dir"


    class Git(BaseSettings):
        clone: CliSubCommand[Clone]

        def cli_cmd(self) -> None:
            # Run the final subcommand (clone/init). It is recommended to define async methods only at the deepest level.
            CliApp.run_subcommand(self)


    CliApp.run(Git, cli_args=['clone', 'repo', 'dir']).model_dump() == {
        'repository': 'repo',
        'directory': 'dir',
    }

</div>

When executing a subcommand with an asynchronous cli_cmd, Pydantic
settings automatically detects whether the current thread already has an
active event loop. If so, the async command is run in a fresh thread to
avoid conflicts. Otherwise, it uses asyncio.run() in the current thread.
This handling ensures your asynchronous subcommands “just work” without
additional manual setup.

### Mutually Exclusive Groups<a href="#mutually-exclusive-groups" class="headerlink"
title="Permanent link">¶</a>

CLI mutually exclusive groups can be created by inheriting from the
`CliMutuallyExclusiveGroup` class.

<div class="admonition note">

Note

A `CliMutuallyExclusiveGroup` cannot be used in a union or contain
nested models.

</div>

<div class="language-py highlight">

    from typing import Optional

    from pydantic import BaseModel

    from pydantic_settings import CliApp, CliMutuallyExclusiveGroup, SettingsError


    class Circle(CliMutuallyExclusiveGroup):
        radius: Optional[float] = None
        diameter: Optional[float] = None
        perimeter: Optional[float] = None


    class Settings(BaseModel):
        circle: Circle


    try:
        CliApp.run(
            Settings,
            cli_args=['--circle.radius=1', '--circle.diameter=2'],
            cli_exit_on_error=False,
        )
    except SettingsError as e:
        print(e)
        """
        error parsing CLI: argument --circle.diameter: not allowed with argument --circle.radius
        """

</div>

### Customizing the CLI Experience<a href="#customizing-the-cli-experience" class="headerlink"
title="Permanent link">¶</a>

The below flags can be used to customise the CLI experience to your
needs.

#### Change the Displayed Program Name<a href="#change-the-displayed-program-name" class="headerlink"
title="Permanent link">¶</a>

Change the default program name displayed in the help text usage by
setting `cli_prog_name`. By default, it will derive the name of the
currently executing program from `sys.argv[0]`, just like argparse.

<div class="language-py highlight">

    import sys

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True, cli_prog_name='appdantic'):
        pass


    try:
        sys.argv = ['example.py', '--help']
        Settings()
    except SystemExit as e:
        print(e)
        #> 0
    """
    usage: appdantic [-h]

    options:
      -h, --help  show this help message and exit
    """

</div>

#### CLI Boolean Flags<a href="#cli-boolean-flags" class="headerlink"
title="Permanent link">¶</a>

Change whether boolean fields should be explicit or implicit by default
using the `cli_implicit_flags` setting. By default, boolean fields are
"explicit", meaning a boolean value must be explicitly provided on the
CLI, e.g. `--flag=True`. Conversely, boolean fields that are "implicit"
derive the value from the flag itself, e.g. `--flag,--no-flag`, which
removes the need for an explicit value to be passed.

Additionally, the provided `CliImplicitFlag` and `CliExplicitFlag`
annotations can be used for more granular control when necessary.

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, CliExplicitFlag, CliImplicitFlag


    class ExplicitSettings(BaseSettings, cli_parse_args=True):
        """Boolean fields are explicit by default."""

        explicit_req: bool
        """
        --explicit_req bool   (required)
        """

        explicit_opt: bool = False
        """
        --explicit_opt bool   (default: False)
        """

        # Booleans are explicit by default, so must override implicit flags with annotation
        implicit_req: CliImplicitFlag[bool]
        """
        --implicit_req, --no-implicit_req (required)
        """

        implicit_opt: CliImplicitFlag[bool] = False
        """
        --implicit_opt, --no-implicit_opt (default: False)
        """


    class ImplicitSettings(BaseSettings, cli_parse_args=True, cli_implicit_flags=True):
        """With cli_implicit_flags=True, boolean fields are implicit by default."""

        # Booleans are implicit by default, so must override explicit flags with annotation
        explicit_req: CliExplicitFlag[bool]
        """
        --explicit_req bool   (required)
        """

        explicit_opt: CliExplicitFlag[bool] = False
        """
        --explicit_opt bool   (default: False)
        """

        implicit_req: bool
        """
        --implicit_req, --no-implicit_req (required)
        """

        implicit_opt: bool = False
        """
        --implicit_opt, --no-implicit_opt (default: False)
        """

</div>

#### Ignore Unknown Arguments<a href="#ignore-unknown-arguments" class="headerlink"
title="Permanent link">¶</a>

Change whether to ignore unknown CLI arguments and only parse known ones
using `cli_ignore_unknown_args`. By default, the CLI does not ignore any
args.

<div class="language-py highlight">

    import sys

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True, cli_ignore_unknown_args=True):
        good_arg: str


    sys.argv = ['example.py', '--bad-arg=bad', 'ANOTHER_BAD_ARG', '--good_arg=hello world']
    print(Settings().model_dump())
    #> {'good_arg': 'hello world'}

</div>

#### CLI Kebab Case for Arguments<a href="#cli-kebab-case-for-arguments" class="headerlink"
title="Permanent link">¶</a>

Change whether CLI arguments should use kebab case by enabling
`cli_kebab_case`.

<div class="language-py highlight">

    import sys

    from pydantic import Field

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True, cli_kebab_case=True):
        my_option: str = Field(description='will show as kebab case on CLI')


    try:
        sys.argv = ['example.py', '--help']
        Settings()
    except SystemExit as e:
        print(e)
        #> 0
    """
    usage: example.py [-h] [--my-option str]

    options:
      -h, --help       show this help message and exit
      --my-option str  will show as kebab case on CLI (required)
    """

</div>

#### Change Whether CLI Should Exit on Error<a href="#change-whether-cli-should-exit-on-error" class="headerlink"
title="Permanent link">¶</a>

Change whether the CLI internal parser will exit on error or raise a
`SettingsError` exception by using `cli_exit_on_error`. By default, the
CLI internal parser will exit on error.

<div class="language-py highlight">

    import sys

    from pydantic_settings import BaseSettings, SettingsError


    class Settings(BaseSettings, cli_parse_args=True, cli_exit_on_error=False): ...


    try:
        sys.argv = ['example.py', '--bad-arg']
        Settings()
    except SettingsError as e:
        print(e)
        #> error parsing CLI: unrecognized arguments: --bad-arg

</div>

#### Enforce Required Arguments at CLI<a href="#enforce-required-arguments-at-cli" class="headerlink"
title="Permanent link">¶</a>

Pydantic settings is designed to pull values in from various sources
when instantating a model. This means a field that is required is not
strictly required from any single source (e.g. the CLI). Instead, all
that matters is that one of the sources provides the required value.

However, if your use case [aligns more with \#2](#command-line-support),
using Pydantic models to define CLIs, you will likely want required
fields to be *strictly required at the CLI*. We can enable this behavior
by using `cli_enforce_required`.

<div class="admonition note">

Note

A required `CliPositionalArg` field is always strictly required
(enforced) at the CLI.

</div>

<div class="language-py highlight">

    import os
    import sys

    from pydantic import Field

    from pydantic_settings import BaseSettings, SettingsError


    class Settings(
        BaseSettings,
        cli_parse_args=True,
        cli_enforce_required=True,
        cli_exit_on_error=False,
    ):
        my_required_field: str = Field(description='a top level required field')


    os.environ['MY_REQUIRED_FIELD'] = 'hello from environment'

    try:
        sys.argv = ['example.py']
        Settings()
    except SettingsError as e:
        print(e)
        #> error parsing CLI: the following arguments are required: --my_required_field

</div>

#### Change the None Type Parse String<a href="#change-the-none-type-parse-string" class="headerlink"
title="Permanent link">¶</a>

Change the CLI string value that will be parsed (e.g. "null", "void",
"None", etc.) into `None` by setting `cli_parse_none_str`. By default it
will use the `env_parse_none_str` value if set. Otherwise, it will
default to "null" if `cli_avoid_json` is `False`, and "None" if
`cli_avoid_json` is `True`.

<div class="language-py highlight">

    import sys
    from typing import Optional

    from pydantic import Field

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True, cli_parse_none_str='void'):
        v1: Optional[int] = Field(description='the top level v0 option')


    sys.argv = ['example.py', '--v1', 'void']
    print(Settings().model_dump())
    #> {'v1': None}

</div>

#### Hide None Type Values<a href="#hide-none-type-values" class="headerlink"
title="Permanent link">¶</a>

Hide `None` values from the CLI help text by enabling
`cli_hide_none_type`.

<div class="language-py highlight">

    import sys
    from typing import Optional

    from pydantic import Field

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True, cli_hide_none_type=True):
        v0: Optional[str] = Field(description='the top level v0 option')


    try:
        sys.argv = ['example.py', '--help']
        Settings()
    except SystemExit as e:
        print(e)
        #> 0
    """
    usage: example.py [-h] [--v0 str]

    options:
      -h, --help  show this help message and exit
      --v0 str    the top level v0 option (required)
    """

</div>

#### Avoid Adding JSON CLI Options<a href="#avoid-adding-json-cli-options" class="headerlink"
title="Permanent link">¶</a>

Avoid adding complex fields that result in JSON strings at the CLI by
enabling `cli_avoid_json`.

<div class="language-py highlight">

    import sys

    from pydantic import BaseModel, Field

    from pydantic_settings import BaseSettings


    class SubModel(BaseModel):
        v1: int = Field(description='the sub model v1 option')


    class Settings(BaseSettings, cli_parse_args=True, cli_avoid_json=True):
        sub_model: SubModel = Field(
            description='The help summary for SubModel related options'
        )


    try:
        sys.argv = ['example.py', '--help']
        Settings()
    except SystemExit as e:
        print(e)
        #> 0
    """
    usage: example.py [-h] [--sub_model.v1 int]

    options:
      -h, --help          show this help message and exit

    sub_model options:
      The help summary for SubModel related options

      --sub_model.v1 int  the sub model v1 option (required)
    """

</div>

#### Use Class Docstring for Group Help Text<a href="#use-class-docstring-for-group-help-text" class="headerlink"
title="Permanent link">¶</a>

By default, when populating the group help text for nested models it
will pull from the field descriptions. Alternatively, we can also
configure CLI settings to pull from the class docstring instead.

<div class="admonition note">

Note

If the field is a union of nested models the group help text will always
be pulled from the field description; even if
`cli_use_class_docs_for_groups` is set to `True`.

</div>

<div class="language-py highlight">

    import sys

    from pydantic import BaseModel, Field

    from pydantic_settings import BaseSettings


    class SubModel(BaseModel):
        """The help text from the class docstring."""

        v1: int = Field(description='the sub model v1 option')


    class Settings(BaseSettings, cli_parse_args=True, cli_use_class_docs_for_groups=True):
        """My application help text."""

        sub_model: SubModel = Field(description='The help text from the field description')


    try:
        sys.argv = ['example.py', '--help']
        Settings()
    except SystemExit as e:
        print(e)
        #> 0
    """
    usage: example.py [-h] [--sub_model JSON] [--sub_model.v1 int]

    My application help text.

    options:
      -h, --help          show this help message and exit

    sub_model options:
      The help text from the class docstring.

      --sub_model JSON    set sub_model from JSON string
      --sub_model.v1 int  the sub model v1 option (required)
    """

</div>

#### Change the CLI Flag Prefix Character<a href="#change-the-cli-flag-prefix-character" class="headerlink"
title="Permanent link">¶</a>

Change The CLI flag prefix character used in CLI optional arguments by
settings `cli_flag_prefix_char`.

<div class="language-py highlight">

    import sys

    from pydantic import AliasChoices, Field

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings, cli_parse_args=True, cli_flag_prefix_char='+'):
        my_arg: str = Field(validation_alias=AliasChoices('m', 'my-arg'))


    sys.argv = ['example.py', '++my-arg', 'hi']
    print(Settings().model_dump())
    #> {'my_arg': 'hi'}

    sys.argv = ['example.py', '+m', 'hi']
    print(Settings().model_dump())
    #> {'my_arg': 'hi'}

</div>

#### Suppressing Fields from CLI Help Text<a href="#suppressing-fields-from-cli-help-text" class="headerlink"
title="Permanent link">¶</a>

To suppress a field from the CLI help text, the `CliSuppress` annotation
can be used for field types, or the `CLI_SUPPRESS` string constant can
be used for field descriptions.

<div class="language-py highlight">

    import sys

    from pydantic import Field

    from pydantic_settings import CLI_SUPPRESS, BaseSettings, CliSuppress


    class Settings(BaseSettings, cli_parse_args=True):
        """Suppress fields from CLI help text."""

        field_a: CliSuppress[int] = 0
        field_b: str = Field(default=1, description=CLI_SUPPRESS)


    try:
        sys.argv = ['example.py', '--help']
        Settings()
    except SystemExit as e:
        print(e)
        #> 0
    """
    usage: example.py [-h]

    Suppress fields from CLI help text.

    options:
      -h, --help          show this help message and exit
    """

</div>

### Integrating with Existing Parsers<a href="#integrating-with-existing-parsers" class="headerlink"
title="Permanent link">¶</a>

A CLI settings source can be integrated with existing parsers by
overriding the default CLI settings source with a user defined one that
specifies the `root_parser` object.

<div class="language-py highlight">

    import sys
    from argparse import ArgumentParser

    from pydantic_settings import BaseSettings, CliApp, CliSettingsSource

    parser = ArgumentParser()
    parser.add_argument('--food', choices=['pear', 'kiwi', 'lime'])


    class Settings(BaseSettings):
        name: str = 'Bob'


    # Set existing `parser` as the `root_parser` object for the user defined settings source
    cli_settings = CliSettingsSource(Settings, root_parser=parser)

    # Parse and load CLI settings from the command line into the settings source.
    sys.argv = ['example.py', '--food', 'kiwi', '--name', 'waldo']
    s = CliApp.run(Settings, cli_settings_source=cli_settings)
    print(s.model_dump())
    #> {'name': 'waldo'}

    # Load CLI settings from pre-parsed arguments. i.e., the parsing occurs elsewhere and we
    # just need to load the pre-parsed args into the settings source.
    parsed_args = parser.parse_args(['--food', 'kiwi', '--name', 'ralph'])
    s = CliApp.run(Settings, cli_args=parsed_args, cli_settings_source=cli_settings)
    print(s.model_dump())
    #> {'name': 'ralph'}

</div>

A `CliSettingsSource` connects with a `root_parser` object by using
parser methods to add `settings_cls` fields as command line arguments.
The `CliSettingsSource` internal parser representation is based on the
`argparse` library, and therefore, requires parser methods that support
the same attributes as their `argparse` counterparts. The available
parser methods that can be customised, along with their argparse
counterparts (the defaults), are listed below:

- `parse_args_method` - (`argparse.ArgumentParser.parse_args`)
- `add_argument_method` - (`argparse.ArgumentParser.add_argument`)
- `add_argument_group_method` -
  (`argparse.ArgumentParser.add_argument_group`)
- `add_parser_method` - (`argparse._SubParsersAction.add_parser`)
- `add_subparsers_method` - (`argparse.ArgumentParser.add_subparsers`)
- `formatter_class` - (`argparse.RawDescriptionHelpFormatter`)

For a non-argparse parser the parser methods can be set to `None` if not
supported. The CLI settings will only raise an error when connecting to
the root parser if a parser method is necessary but set to `None`.

<div class="admonition note">

Note

The `formatter_class` is only applied to subcommands. The
`CliSettingsSource` never touches or modifies any of the external parser
settings to avoid breaking changes. Since subcommands reside on their
own internal parser trees, we can safely apply the `formatter_class`
settings without breaking the external parser logic.

</div>

## Secrets<a href="#secrets" class="headerlink" title="Permanent link">¶</a>

Placing secret values in files is a common pattern to provide sensitive
configuration to an application.

A secret file follows the same principal as a dotenv file except it only
contains a single value and the file name is used as the key. A secret
file will look like the following:

<div class="language-text highlight">

<span class="filename">/var/run/database_password</span>

    super_secret_database_password

</div>

Once you have your secret files, *pydantic* supports loading it in two
ways:

1.  Setting the `secrets_dir` on `model_config` in a `BaseSettings`
    class to the directory where your secret files are stored.
    <div class="language-py highlight">

        from pydantic_settings import BaseSettings, SettingsConfigDict


        class Settings(BaseSettings):
            model_config = SettingsConfigDict(secrets_dir='/var/run')

            database_password: str

    </div>
2.  Instantiating the `BaseSettings` derived class with the
    `_secrets_dir` keyword argument:
    <div class="language-text highlight">

        settings = Settings(_secrets_dir='/var/run')

    </div>

In either case, the value of the passed argument can be any valid
directory, either absolute or relative to the current working directory.
**Note that a non existent directory will only generate a warning**.
From there, *pydantic* will handle everything for you by loading in your
variables and validating them.

Even when using a secrets directory, *pydantic* will still read
environment variables from a dotenv file or the environment, **a dotenv
file and environment variables will always take priority over values
loaded from the secrets directory**.

Passing a file path via the `_secrets_dir` keyword argument on
instantiation (method 2) will override the value (if any) set on the
`model_config` class.

If you need to load settings from multiple secrets directories, you can
pass multiple paths as a tuple or list. Just like for `env_file`, values
from subsequent paths override previous ones.

<div class="language-python highlight">

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        # files in '/run/secrets' take priority over '/var/run'
        model_config = SettingsConfigDict(secrets_dir=('/var/run', '/run/secrets'))

        database_password: str

</div>

If any of `secrets_dir` is missing, it is ignored, and warning is shown.
If any of `secrets_dir` is a file, error is raised.

### Use Case: Docker Secrets<a href="#use-case-docker-secrets" class="headerlink"
title="Permanent link">¶</a>

Docker Secrets can be used to provide sensitive configuration to an
application running in a Docker container. To use these secrets in a
*pydantic* application the process is simple. More information regarding
creating, managing and using secrets in Docker see the official [Docker
documentation](https://docs.docker.com/engine/reference/commandline/secret/).

First, define your `Settings` class with a `SettingsConfigDict` that
specifies the secrets directory.

<div class="language-py highlight">

    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(secrets_dir='/run/secrets')

        my_secret_data: str

</div>

<div class="admonition note">

Note

By default [Docker uses
`/run/secrets`](https://docs.docker.com/engine/swarm/secrets/#how-docker-manages-secrets)
as the target mount point. If you want to use a different location,
change `Config.secrets_dir` accordingly.

</div>

Then, create your secret via the Docker CLI

<div class="language-bash highlight">

    printf "This is a secret" | docker secret create my_secret_data -

</div>

Last, run your application inside a Docker container and supply your
newly created secret

<div class="language-bash highlight">

    docker service create --name pydantic-with-secrets --secret my_secret_data pydantic-app:latest

</div>

## AWS Secrets Manager<a href="#aws-secrets-manager" class="headerlink"
title="Permanent link">¶</a>

You must set one parameter:

- `secret_id`: The AWS secret id

You must have the same naming convention in the key value in secret as
in the field name. For example, if the key in secret is named
`SqlServerPassword`, the field name must be the same. You can use an
alias too.

In AWS Secrets Manager, nested models are supported with the `--`
separator in the key name. For example, `SqlServer--Password`.

Arrays (e.g. `MySecret--0`, `MySecret--1`) are not supported.

<div class="language-py highlight">

    import os

    from pydantic import BaseModel

    from pydantic_settings import (
        AWSSecretsManagerSettingsSource,
        BaseSettings,
        PydanticBaseSettingsSource,
    )


    class SubModel(BaseModel):
        a: str


    class AWSSecretsManagerSettings(BaseSettings):
        foo: str
        bar: int
        sub: SubModel

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            aws_secrets_manager_settings = AWSSecretsManagerSettingsSource(
                settings_cls,
                os.environ['AWS_SECRETS_MANAGER_SECRET_ID'],
            )
            return (
                init_settings,
                env_settings,
                dotenv_settings,
                file_secret_settings,
                aws_secrets_manager_settings,
            )

</div>

## Azure Key Vault<a href="#azure-key-vault" class="headerlink"
title="Permanent link">¶</a>

You must set two parameters:

- `url`: For example, `https://my-resource.vault.azure.net/`.
- `credential`: If you use `DefaultAzureCredential`, in local you can
  execute `az login` to get your identity credentials. The identity must
  have a role assignment (the recommended one is
  `Key Vault Secrets User`), so you can access the secrets.

You must have the same naming convention in the field name as in the Key
Vault secret name. For example, if the secret is named
`SqlServerPassword`, the field name must be the same. You can use an
alias too.

In Key Vault, nested models are supported with the `--` separator. For
example, `SqlServer--Password`.

Key Vault arrays (e.g. `MySecret--0`, `MySecret--1`) are not supported.

<div class="language-py highlight">

    import os

    from azure.identity import DefaultAzureCredential
    from pydantic import BaseModel

    from pydantic_settings import (
        AzureKeyVaultSettingsSource,
        BaseSettings,
        PydanticBaseSettingsSource,
    )


    class SubModel(BaseModel):
        a: str


    class AzureKeyVaultSettings(BaseSettings):
        foo: str
        bar: int
        sub: SubModel

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            az_key_vault_settings = AzureKeyVaultSettingsSource(
                settings_cls,
                os.environ['AZURE_KEY_VAULT_URL'],
                DefaultAzureCredential(),
            )
            return (
                init_settings,
                env_settings,
                dotenv_settings,
                file_secret_settings,
                az_key_vault_settings,
            )

</div>

## Other settings source<a href="#other-settings-source" class="headerlink"
title="Permanent link">¶</a>

Other settings sources are available for common configuration files:

- `JsonConfigSettingsSource` using `json_file` and `json_file_encoding`
  arguments
- `PyprojectTomlConfigSettingsSource` using *(optional)*
  `pyproject_toml_depth` and *(optional)* `pyproject_toml_table_header`
  arguments
- `TomlConfigSettingsSource` using `toml_file` argument
- `YamlConfigSettingsSource` using `yaml_file` and yaml_file_encoding
  arguments

You can also provide multiple files by providing a list of path:

<div class="language-py highlight">

    toml_file = ['config.default.toml', 'config.custom.toml']

</div>

To use them, you can use the same mechanism described
[here](#customise-settings-sources)

<div class="language-py highlight">

    from pydantic import BaseModel

    from pydantic_settings import (
        BaseSettings,
        PydanticBaseSettingsSource,
        SettingsConfigDict,
        TomlConfigSettingsSource,
    )


    class Nested(BaseModel):
        nested_field: str


    class Settings(BaseSettings):
        foobar: str
        nested: Nested
        model_config = SettingsConfigDict(toml_file='config.toml')

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return (TomlConfigSettingsSource(settings_cls),)

</div>

This will be able to read the following "config.toml" file, located in
your working directory:

<div class="language-toml highlight">

    foobar = "Hello"
    [nested]
    nested_field = "world!"

</div>

### pyproject.toml<a href="#pyprojecttoml" class="headerlink" title="Permanent link">¶</a>

"pyproject.toml" is a standardized file for providing configuration
values in Python projects. [PEP
518](https://peps.python.org/pep-0518/#tool-table) defines a `[tool]`
table that can be used to provide arbitrary tool configuration. While
encouraged to use the `[tool]` table,
`PyprojectTomlConfigSettingsSource` can be used to load variables from
any location with in "pyproject.toml" file.

This is controlled by providing
`SettingsConfigDict(pyproject_toml_table_header=tuple[str, ...])` where
the value is a tuple of header parts. By default,
`pyproject_toml_table_header=('tool', 'pydantic-settings')` which will
load variables from the `[tool.pydantic-settings]` table.

<div class="language-python highlight">

    from pydantic_settings import (
        BaseSettings,
        PydanticBaseSettingsSource,
        PyprojectTomlConfigSettingsSource,
        SettingsConfigDict,
    )


    class Settings(BaseSettings):
        """Example loading values from the table used by default."""

        field: str

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return (PyprojectTomlConfigSettingsSource(settings_cls),)


    class SomeTableSettings(Settings):
        """Example loading values from a user defined table."""

        model_config = SettingsConfigDict(
            pyproject_toml_table_header=('tool', 'some-table')
        )


    class RootSettings(Settings):
        """Example loading values from the root of a pyproject.toml file."""

        model_config = SettingsConfigDict(extra='ignore', pyproject_toml_table_header=())

</div>

This will be able to read the following "pyproject.toml" file, located
in your working directory, resulting in
`Settings(field='default-table')`,
`SomeTableSettings(field='some-table')`, & `RootSettings(field='root')`:

<div class="language-toml highlight">

    field = "root"

    [tool.pydantic-settings]
    field = "default-table"

    [tool.some-table]
    field = "some-table"

</div>

By default, `PyprojectTomlConfigSettingsSource` will only look for a
"pyproject.toml" in the your current working directory. However, there
are two options to change this behavior.

- `SettingsConfigDict(pyproject_toml_depth=<int>)` can be provided to
  check `<int>` number of directories **up** in the directory tree for a
  "pyproject.toml" if one is not found in the current working directory.
  By default, no parent directories are checked.
- An explicit file path can be provided to the source when it is
  instantiated (e.g.
  `PyprojectTomlConfigSettingsSource(settings_cls, Path('~/.config').resolve() / 'pyproject.toml')`).
  If a file path is provided this way, it will be treated as absolute
  (no other locations are checked).

<div class="language-python highlight">

    from pathlib import Path

    from pydantic_settings import (
        BaseSettings,
        PydanticBaseSettingsSource,
        PyprojectTomlConfigSettingsSource,
        SettingsConfigDict,
    )


    class DiscoverSettings(BaseSettings):
        """Example of discovering a pyproject.toml in parent directories in not in `Path.cwd()`."""

        model_config = SettingsConfigDict(pyproject_toml_depth=2)

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return (PyprojectTomlConfigSettingsSource(settings_cls),)


    class ExplicitFilePathSettings(BaseSettings):
        """Example of explicitly providing the path to the file to load."""

        field: str

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return (
                PyprojectTomlConfigSettingsSource(
                    settings_cls, Path('~/.config').resolve() / 'pyproject.toml'
                ),
            )

</div>

## Field value priority<a href="#field-value-priority" class="headerlink"
title="Permanent link">¶</a>

In the case where a value is specified for the same `Settings` field in
multiple ways, the selected value is determined as follows (in
descending order of priority):

1.  If `cli_parse_args` is enabled, arguments passed in at the CLI.
2.  Arguments passed to the `Settings` class initialiser.
3.  Environment variables, e.g. `my_prefix_special_function` as
    described above.
4.  Variables loaded from a dotenv (`.env`) file.
5.  Variables loaded from the secrets directory.
6.  The default field values for the `Settings` model.

## Customise settings sources<a href="#customise-settings-sources" class="headerlink"
title="Permanent link">¶</a>

If the default order of priority doesn't match your needs, it's possible
to change it by overriding the `settings_customise_sources` method of
your `Settings` .

`settings_customise_sources` takes four callables as arguments and
returns any number of callables as a tuple. In turn these callables are
called to build the inputs to the fields of the settings class.

Each callable should take an instance of the settings class as its sole
argument and return a `dict`.

### Changing Priority<a href="#changing-priority" class="headerlink"
title="Permanent link">¶</a>

The order of the returned callables decides the priority of inputs;
first item is the highest priority.

<div class="language-py highlight">

    from pydantic import PostgresDsn

    from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


    class Settings(BaseSettings):
        database_dsn: PostgresDsn

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return env_settings, init_settings, file_secret_settings


    print(Settings(database_dsn='postgres://postgres@localhost:5432/kwargs_db'))
    #> database_dsn=PostgresDsn('postgres://postgres@localhost:5432/kwargs_db')

</div>

By flipping `env_settings` and `init_settings`, environment variables
now have precedence over `__init__` kwargs.

### Adding sources<a href="#adding-sources" class="headerlink"
title="Permanent link">¶</a>

As explained earlier, *pydantic* ships with multiples built-in settings
sources. However, you may occasionally need to add your own custom
sources, `settings_customise_sources` makes this very easy:

<div class="language-py highlight">

    import json
    from pathlib import Path
    from typing import Any

    from pydantic.fields import FieldInfo

    from pydantic_settings import (
        BaseSettings,
        PydanticBaseSettingsSource,
        SettingsConfigDict,
    )


    class JsonConfigSettingsSource(PydanticBaseSettingsSource):
        """
        A simple settings source class that loads variables from a JSON file
        at the project's root.

        Here we happen to choose to use the `env_file_encoding` from Config
        when reading `config.json`
        """

        def get_field_value(
            self, field: FieldInfo, field_name: str
        ) -> tuple[Any, str, bool]:
            encoding = self.config.get('env_file_encoding')
            file_content_json = json.loads(
                Path('tests/example_test_config.json').read_text(encoding)
            )
            field_value = file_content_json.get(field_name)
            return field_value, field_name, False

        def prepare_field_value(
            self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
        ) -> Any:
            return value

        def __call__(self) -> dict[str, Any]:
            d: dict[str, Any] = {}

            for field_name, field in self.settings_cls.model_fields.items():
                field_value, field_key, value_is_complex = self.get_field_value(
                    field, field_name
                )
                field_value = self.prepare_field_value(
                    field_name, field, field_value, value_is_complex
                )
                if field_value is not None:
                    d[field_key] = field_value

            return d


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_file_encoding='utf-8')

        foobar: str

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return (
                init_settings,
                JsonConfigSettingsSource(settings_cls),
                env_settings,
                file_secret_settings,
            )


    print(Settings())
    #> foobar='test'

</div>

#### Accesing the result of previous sources<a href="#accesing-the-result-of-previous-sources" class="headerlink"
title="Permanent link">¶</a>

Each source of settings can access the output of the previous ones.

<div class="language-python highlight">

    from typing import Any

    from pydantic.fields import FieldInfo

    from pydantic_settings import PydanticBaseSettingsSource


    class MyCustomSource(PydanticBaseSettingsSource):
        def get_field_value(
            self, field: FieldInfo, field_name: str
        ) -> tuple[Any, str, bool]: ...

        def __call__(self) -> dict[str, Any]:
            # Retrieve the aggregated settings from previous sources
            current_state = self.current_state
            current_state.get('some_setting')

            # Retrive settings from all sources individually
            # self.settings_sources_data["SettingsSourceName"]: dict[str, Any]
            settings_sources_data = self.settings_sources_data
            settings_sources_data['SomeSettingsSource'].get('some_setting')

            # Your code here...

</div>

### Removing sources<a href="#removing-sources" class="headerlink"
title="Permanent link">¶</a>

You might also want to disable a source:

<div class="language-py highlight">

    from pydantic import ValidationError

    from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


    class Settings(BaseSettings):
        my_api_key: str

        @classmethod
        def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            # here we choose to ignore arguments from init_settings
            return env_settings, file_secret_settings


    try:
        Settings(my_api_key='this is ignored')
    except ValidationError as exc_info:
        print(exc_info)
        """
        1 validation error for Settings
        my_api_key
          Field required [type=missing, input_value={}, input_type=dict]
            For further information visit https://errors.pydantic.dev/2/v/missing
        """

</div>

## In-place reloading<a href="#in-place-reloading" class="headerlink"
title="Permanent link">¶</a>

In case you want to reload in-place an existing setting, you can do it
by using its `__init__` method :

<div class="language-py highlight">

    import os

    from pydantic import Field

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings):
        foo: str = Field('foo')


    mutable_settings = Settings()

    print(mutable_settings.foo)
    #> foo

    os.environ['foo'] = 'bar'
    print(mutable_settings.foo)
    #> foo

    mutable_settings.__init__()
    print(mutable_settings.foo)
    #> bar

    os.environ.pop('foo')
    mutable_settings.__init__()
    print(mutable_settings.foo)
    #> foo

</div>

Was this page helpful?

<div class="md-feedback__inner">

<div class="md-feedback__list">

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTUgOXYxMkgxVjl6bTQgMTJhMiAyIDAgMCAxLTItMlY5YzAtLjU1LjIyLTEuMDUuNTktMS40MUwxNC4xNyAxbDEuMDYgMS4wNmMuMjcuMjcuNDQuNjQuNDQgMS4wNWwtLjAzLjMyTDE0LjY5IDhIMjFhMiAyIDAgMCAxIDIgMnYyYzAgLjI2LS4wNS41LS4xNC43M2wtMy4wMiA3LjA1QzE5LjU0IDIwLjUgMTguODMgMjEgMTggMjF6bTAtMmg5LjAzTDIxIDEydi0yaC04Ljc5bDEuMTMtNS4zMkw5IDkuMDN6IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE5IDE1VjNoNHYxMnpNMTUgM2EyIDIgMCAwIDEgMiAydjEwYzAgLjU1LS4yMiAxLjA1LS41OSAxLjQxTDkuODMgMjNsLTEuMDYtMS4wNmMtLjI3LS4yNy0uNDQtLjY0LS40NC0xLjA2bC4wMy0uMzEuOTUtNC41N0gzYTIgMiAwIDAgMS0yLTJ2LTJjMC0uMjYuMDUtLjUuMTQtLjczbDMuMDItNy4wNUM0LjQ2IDMuNSA1LjE3IDMgNiAzem0wIDJINS45N0wzIDEydjJoOC43OGwtMS4xMyA1LjMyTDE1IDE0Ljk3eiIgLz48L3N2Zz4=)

</div>

<div class="md-feedback__note">

<div md-value="1" hidden="">

Thanks for your feedback!

</div>

<div md-value="0" hidden="">

Thanks for your feedback!

</div>

</div>

</div>

</div>

</div>

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=)
Back to top

</div>

<div class="md-footer-meta md-typeset">

<div class="md-footer-meta__inner md-grid">

<div class="md-copyright">

Made with
<a href="https://squidfunk.github.io/mkdocs-material/" target="_blank"
rel="noopener">Material for MkDocs</a>

</div>

</div>

</div>

</div>

<div class="md-dialog" md-component="dialog">

<div class="md-dialog__inner md-typeset">

</div>

</div>

<div class="md-progress" md-component="progress" role="progressbar">

</div>

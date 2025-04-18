<div md-component="skip">

<a href="#the-annotated-pattern" class="md-skip">Skip to content</a>



<div md-component="announce">

<div class="md-banner__inner md-grid md-typeset">


What's new — we've launched [Pydantic
Logfire](https://pydantic.dev/articles/logfire-announcement) <img
src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg"
title=":fire:" class="twemoji" alt="🔥" /> to help you monitor and
understand your
<a href="https://logfire.pydantic.dev/docs/integrations/pydantic/"
id="logfire-app-type" target="_blank">Pydantic validations.</a>





<div md-color-scheme="default" md-component="outdated" hidden="">



<div class="md-header" md-component="header">

<a href="../.." class="md-header__button md-logo" aria-label="Pydantic"
data-md-component="logo" title="Pydantic"><img
src="../../logo-white.svg" alt="logo" /></a>

<div class="md-header__title" md-component="header-title">

<div class="md-header__ellipsis">

<div class="md-header__topic">

<span class="md-ellipsis"> Pydantic </span>



<div class="md-header__topic" md-component="header-topic">

<span class="md-ellipsis"> Fields </span>








<div class="md-search" role="dialog">

<div class="md-search__inner" role="search">



<div class="md-search__suggest">



<div class="md-search__output">

<div class="md-search__scrollwrap" tabindex="0">

<div class="md-search-result">

<div id="type-to-start-searching" class="md-search-result__meta">

Type to start searching













<div class="md-header__source">

<a href="https://github.com/pydantic/pydantic" class="md-source"
data-md-component="source" title="Go to repository"></a>

<div class="md-source__icon md-icon">




<div class="md-source__repository">

pydantic/pydantic







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




<div class="md-source__repository">

pydantic/pydantic





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

<span class="md-ellipsis"> Fields </span>
<span class="md-nav__icon md-icon"></span>
<a href="./" class="md-nav__link md-nav__link--active"><span
class="md-ellipsis"> Fields </span></a>

<span class="md-nav__icon md-icon"></span> Page contents

- <a href="#the-annotated-pattern" class="md-nav__link"><span
  class="md-ellipsis"> The annotated pattern </span></a>
- <a href="#default-values" class="md-nav__link"><span
  class="md-ellipsis"> Default values </span></a>
- <a href="#validate-default-values" class="md-nav__link"><span
  class="md-ellipsis"> Validate default values </span></a>
  - <a href="#mutable-default-values" class="md-nav__link"><span
    class="md-ellipsis"> Mutable default values </span></a>
- <a href="#field-aliases" class="md-nav__link"><span class="md-ellipsis">
  Field aliases </span></a>
- <a href="#numeric-constraints" class="md-nav__link"><span
  class="md-ellipsis"> Numeric Constraints </span></a>
- <a href="#string-constraints" class="md-nav__link"><span
  class="md-ellipsis"> String Constraints </span></a>
- <a href="#decimal-constraints" class="md-nav__link"><span
  class="md-ellipsis"> Decimal Constraints </span></a>
- <a href="#dataclass-constraints" class="md-nav__link"><span
  class="md-ellipsis"> Dataclass Constraints </span></a>
- <a href="#field-representation" class="md-nav__link"><span
  class="md-ellipsis"> Field Representation </span></a>
- <a href="#discriminator" class="md-nav__link"><span class="md-ellipsis">
  Discriminator </span></a>
- <a href="#strict-mode" class="md-nav__link"><span class="md-ellipsis">
  Strict Mode </span></a>
- <a href="#immutability" class="md-nav__link"><span class="md-ellipsis">
  Immutability </span></a>
- <a href="#exclude" class="md-nav__link"><span class="md-ellipsis">
  Exclude </span></a>
- <a href="#deprecated-fields" class="md-nav__link"><span
  class="md-ellipsis"> Deprecated fields </span></a>
  - <a href="#deprecated-as-a-string" class="md-nav__link"><span
    class="md-ellipsis"> deprecated as a string </span></a>
  - <a href="#deprecated-via-the-warningsdeprecated-decorator"
    class="md-nav__link"><span class="md-ellipsis"> deprecated via the
    warnings.deprecated decorator </span></a>
  - <a href="#deprecated-as-a-boolean" class="md-nav__link"><span
    class="md-ellipsis"> deprecated as a boolean </span></a>
- <a href="#customizing-json-schema" class="md-nav__link"><span
  class="md-ellipsis"> Customizing JSON Schema </span></a>
- <a href="#the-computed_field-decorator" class="md-nav__link"><span
  class="md-ellipsis"> The computed_field decorator </span></a>

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

<a href="../pydantic_settings/" class="md-nav__link"><span
class="md-ellipsis"> Settings Management </span></a>

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







<div class="md-sidebar md-sidebar--secondary" md-component="sidebar"
md-type="toc">

<div class="md-sidebar__scrollwrap">

<div class="md-sidebar__inner">

<span class="md-nav__icon md-icon"></span> Page contents

- <a href="#the-annotated-pattern" class="md-nav__link"><span
  class="md-ellipsis"> The annotated pattern </span></a>
- <a href="#default-values" class="md-nav__link"><span
  class="md-ellipsis"> Default values </span></a>
- <a href="#validate-default-values" class="md-nav__link"><span
  class="md-ellipsis"> Validate default values </span></a>
  - <a href="#mutable-default-values" class="md-nav__link"><span
    class="md-ellipsis"> Mutable default values </span></a>
- <a href="#field-aliases" class="md-nav__link"><span class="md-ellipsis">
  Field aliases </span></a>
- <a href="#numeric-constraints" class="md-nav__link"><span
  class="md-ellipsis"> Numeric Constraints </span></a>
- <a href="#string-constraints" class="md-nav__link"><span
  class="md-ellipsis"> String Constraints </span></a>
- <a href="#decimal-constraints" class="md-nav__link"><span
  class="md-ellipsis"> Decimal Constraints </span></a>
- <a href="#dataclass-constraints" class="md-nav__link"><span
  class="md-ellipsis"> Dataclass Constraints </span></a>
- <a href="#field-representation" class="md-nav__link"><span
  class="md-ellipsis"> Field Representation </span></a>
- <a href="#discriminator" class="md-nav__link"><span class="md-ellipsis">
  Discriminator </span></a>
- <a href="#strict-mode" class="md-nav__link"><span class="md-ellipsis">
  Strict Mode </span></a>
- <a href="#immutability" class="md-nav__link"><span class="md-ellipsis">
  Immutability </span></a>
- <a href="#exclude" class="md-nav__link"><span class="md-ellipsis">
  Exclude </span></a>
- <a href="#deprecated-fields" class="md-nav__link"><span
  class="md-ellipsis"> Deprecated fields </span></a>
  - <a href="#deprecated-as-a-string" class="md-nav__link"><span
    class="md-ellipsis"> deprecated as a string </span></a>
  - <a href="#deprecated-via-the-warningsdeprecated-decorator"
    class="md-nav__link"><span class="md-ellipsis"> deprecated via the
    warnings.deprecated decorator </span></a>
  - <a href="#deprecated-as-a-boolean" class="md-nav__link"><span
    class="md-ellipsis"> deprecated as a boolean </span></a>
- <a href="#customizing-json-schema" class="md-nav__link"><span
  class="md-ellipsis"> Customizing JSON Schema </span></a>
- <a href="#the-computed_field-decorator" class="md-nav__link"><span
  class="md-ellipsis"> The computed_field decorator </span></a>







<div class="md-content" md-component="content">

# Fields

API Documentation

<a href="../../api/fields/#pydantic.fields.Field"
class="autorefs autorefs-internal"><code>pydantic.fields.Field</code></a>  

In this section, we will go through the available mechanisms to
customize Pydantic model fields: default values, JSON Schema metadata,
constraints, etc.

To do so, the <a href="../../api/fields/#pydantic.fields.Field"
class="autorefs autorefs-internal"><code>Field()</code></a> function is
used a lot, and behaves the same way as the standard library <a
href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field"
class="autorefs autorefs-external"><code>field()</code></a> function for
dataclasses:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class Model(BaseModel):
        name: str = Field(frozen=True)



<div class="admonition note">

Note

Even though `name` is assigned a value, it is still required and has no
default value. If you want to emphasize on the fact that a value must be
provided, you can use the
<a href="https://docs.python.org/3/library/constants.html#Ellipsis"
class="autorefs autorefs-external">ellipsis</a>:

<div class="language-python highlight">

    class Model(BaseModel):
        name: str = Field(..., frozen=True)



However, its usage is discouraged as it doesn't play well with static
type checkers.



## The annotated pattern<a href="#the-annotated-pattern" class="headerlink"
title="Permanent link">¶</a>

To apply constraints or attach
<a href="../../api/fields/#pydantic.fields.Field"
class="autorefs autorefs-internal"><code>Field()</code></a> functions to
a model field, Pydantic supports the
<a href="https://docs.python.org/3/library/typing.html#typing.Annotated"
class="autorefs autorefs-external"><code>Annotated</code></a> typing
construct to attach metadata to an annotation:

<div class="language-python highlight">

    from typing import Annotated

    from pydantic import BaseModel, Field, WithJsonSchema


    class Model(BaseModel):
        name: Annotated[str, Field(strict=True), WithJsonSchema({'extra': 'data'})]



As far as static type checkers are concerned, `name` is still typed as
`str`, but Pydantic leverages the available metadata to add validation
logic, type constraints, etc.

Using this pattern has some advantages:

- Using the `f: <type> = Field(...)` form can be confusing and might
  trick users into thinking `f` has a default value, while in reality it
  is still required.
- You can provide an arbitrary amount of metadata elements for a field.
  As shown in the example above, the
  <a href="../../api/fields/#pydantic.fields.Field"
  class="autorefs autorefs-internal"><code>Field()</code></a> function
  only supports a limited set of constraints/metadata, and you may have
  to use different Pydantic utilities such as
  <a href="../../api/json_schema/#pydantic.json_schema.WithJsonSchema"
  class="autorefs autorefs-internal"><code>WithJsonSchema</code></a> in
  some cases.
- Types can be made reusable (see the documentation on [custom
  types](../types/#using-the-annotated-pattern) using this pattern).

However, note that certain arguments to the
<a href="../../api/fields/#pydantic.fields.Field"
class="autorefs autorefs-internal"><code>Field()</code></a> function
(namely, `default`, `default_factory`, and `alias`) are taken into
account by static type checkers to synthesize a correct `__init__`
method. The annotated pattern is *not* understood by them, so you should
use the normal assignment form instead.

<div class="admonition tip">

Tip

The annotated pattern can also be used to add metadata to specific parts
of the type. For instance, [validation constraints](#field-constraints)
can be added this way:

<div class="language-python highlight">

    from typing import Annotated

    from pydantic import BaseModel, Field


    class Model(BaseModel):
        int_list: list[Annotated[int, Field(gt=0)]]
        # Valid: [1, 3]
        # Invalid: [-1, 2]





## Default values<a href="#default-values" class="headerlink"
title="Permanent link">¶</a>

Default values for fields can be provided using the normal assignment
syntax or by providing a value to the `default` argument:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        # Both fields aren't required:
        name: str = 'John Doe'
        age: int = Field(default=20)



<div class="admonition warning">

Warning

[In Pydantic
V1](../../migration/#required-optional-and-nullable-fields), a type
annotated as
<a href="https://docs.python.org/3/library/typing.html#typing.Any"
class="autorefs autorefs-external"><code>Any</code></a> or wrapped by
<a href="https://docs.python.org/3/library/typing.html#typing.Optional"
class="autorefs autorefs-external"><code>Optional</code></a> would be
given an implicit default of `None` even if no default was explicitly
specified. This is no longer the case in Pydantic V2.



You can also pass a callable to the `default_factory` argument that will
be called to generate a default value:

<div class="language-python highlight">

    from uuid import uuid4

    from pydantic import BaseModel, Field


    class User(BaseModel):
        id: str = Field(default_factory=lambda: uuid4().hex)



The default factory can also take a single required argument, in which
case the already validated data will be passed as a dictionary.

<div class="language-python highlight">

    from pydantic import BaseModel, EmailStr, Field


    class User(BaseModel):
        email: EmailStr
        username: str = Field(default_factory=lambda data: data['email'])


    user = User(email='[email protected]')
    print(user.username)
    #> [email protected]



The `data` argument will *only* contain the already validated data,
based on the [order of model fields](../models/#field-ordering) (the
above example would fail if `username` were to be defined before
`email`).

## Validate default values<a href="#validate-default-values" class="headerlink"
title="Permanent link">¶</a>

By default, Pydantic will *not* validate default values. The
`validate_default` field parameter (or the
<a href="../../api/config/#pydantic.config.ConfigDict.validate_default"
class="autorefs autorefs-internal"><code>validate_default</code></a>
configuration value) can be used to enable this behavior:

<div class="language-python highlight">

    from pydantic import BaseModel, Field, ValidationError


    class User(BaseModel):
        age: int = Field(default='twelve', validate_default=True)


    try:
        user = User()
    except ValidationError as e:
        print(e)
        """
        1 validation error for User
        age
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='twelve', input_type=str]
        """



### Mutable default values<a href="#mutable-default-values" class="headerlink"
title="Permanent link">¶</a>

A common source of bugs in Python is to use a mutable object as a
default value for a function or method argument, as the same instance
ends up being reused in each call.

The <a
href="https://docs.python.org/3/library/dataclasses.html#module-dataclasses"
class="autorefs autorefs-external"><code>dataclasses</code></a> module
actually raises an error in this case, indicating that you should use a
[default
factory](https://docs.python.org/3/library/dataclasses.html#default-factory-functions)
instead.

While the same thing can be done in Pydantic, it is not required. In the
event that the default value is not hashable, Pydantic will create a
deep copy of the default value when creating each instance of the model:

<div class="language-python highlight">

    from pydantic import BaseModel


    class Model(BaseModel):
        item_counts: list[dict[str, int]] = [{}]


    m1 = Model()
    m1.item_counts[0]['a'] = 1
    print(m1.item_counts)
    #> [{'a': 1}]

    m2 = Model()
    print(m2.item_counts)
    #> [{}]



## Field aliases<a href="#field-aliases" class="headerlink" title="Permanent link">¶</a>

<div class="admonition tip">

Tip

Read more about aliases in the [dedicated section](../alias/).



For validation and serialization, you can define an alias for a field.

There are three ways to define an alias:

- `Field(alias='foo')`
- `Field(validation_alias='foo')`
- `Field(serialization_alias='foo')`

The `alias` parameter is used for both validation *and* serialization.
If you want to use *different* aliases for validation and serialization
respectively, you can use the `validation_alias` and
`serialization_alias` parameters, which will apply only in their
respective use cases.

Here is an example of using the `alias` parameter:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str = Field(alias='username')


    user = User(username='johndoe')  # (1)!
    print(user)
    #> name='johndoe'
    print(user.model_dump(by_alias=True))  # (2)!
    #> {'username': 'johndoe'}



1.  The alias `'username'` is used for instance creation and validation.

2.  We are using
    <a href="../../api/base_model/#pydantic.BaseModel.model_dump"
    class="autorefs autorefs-internal"><code>model_dump()</code></a> to
    convert the model into a serializable format.

    Note that the `by_alias` keyword argument defaults to `False`, and
    must be specified explicitly to dump models using the field
    (serialization) aliases.

    You can also use <a
    href="../../api/config/#pydantic.config.ConfigDict.serialize_by_alias"
    class="autorefs autorefs-internal"><code>ConfigDict.serialize_by_alias</code></a>
    to configure this behavior at the model level.

    When `by_alias=True`, the alias `'username'` used during
    serialization.

If you want to use an alias *only* for validation, you can use the
`validation_alias` parameter:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str = Field(validation_alias='username')


    user = User(username='johndoe')  # (1)!
    print(user)
    #> name='johndoe'
    print(user.model_dump(by_alias=True))  # (2)!
    #> {'name': 'johndoe'}



1.  The validation alias `'username'` is used during validation.
2.  The field name `'name'` is used during serialization.

If you only want to define an alias for *serialization*, you can use the
`serialization_alias` parameter:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str = Field(serialization_alias='username')


    user = User(name='johndoe')  # (1)!
    print(user)
    #> name='johndoe'
    print(user.model_dump(by_alias=True))  # (2)!
    #> {'username': 'johndoe'}



1.  The field name `'name'` is used for validation.
2.  The serialization alias `'username'` is used for serialization.

<div class="admonition note">

Alias precedence and priority

In case you use `alias` together with `validation_alias` or
`serialization_alias` at the same time, the `validation_alias` will have
priority over `alias` for validation, and `serialization_alias` will
have priority over `alias` for serialization.

If you provide a value for the
<a href="../../api/config/#pydantic.config.ConfigDict.alias_generator"
class="autorefs autorefs-internal"><code>alias_generator</code></a>
model setting, you can control the order of precedence for field alias
and generated aliases via the `alias_priority` field parameter. You can
read more about alias precedence [here](../alias/#alias-precedence).



Static type checking/IDE support

If you provide a value for the `alias` field parameter, static type
checkers will use this alias instead of the actual field name to
synthesize the `__init__` method:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str = Field(alias='username')


    user = User(username='johndoe')  # (1)!



1.  Accepted by type checkers.

This means that when using the
<a href="../../api/config/#pydantic.config.ConfigDict.validate_by_name"
class="autorefs autorefs-internal"><code>validate_by_name</code></a>
model setting (which allows both the field name and alias to be used
during model validation), type checkers will error when the actual field
name is used:

<div class="language-python highlight">

    from pydantic import BaseModel, ConfigDict, Field


    class User(BaseModel):
        model_config = ConfigDict(validate_by_name=True)

        name: str = Field(alias='username')


    user = User(name='johndoe')  # (1)!



1.  *Not* accepted by type checkers.

If you still want type checkers to use the field name and not the alias,
the [annotated pattern](#the-annotated-pattern) can be used (which is
only understood by Pydantic):

<div class="language-python highlight">

    from typing import Annotated

    from pydantic import BaseModel, ConfigDict, Field


    class User(BaseModel):
        model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

        name: Annotated[str, Field(alias='username')]


    user = User(name='johndoe')  # (1)!
    user = User(username='johndoe')  # (2)!



1.  Accepted by type checkers.
2.  *Not* accepted by type checkers.

### Validation Alias

Even though Pydantic treats `alias` and `validation_alias` the same when
creating model instances, type checkers only understand the `alias`
field parameter. As a workaround, you can instead specify both an
`alias` and
serialization_alias`(identical to the field name), as the`serialization_alias`will override the`alias\`
during serialization:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class MyModel(BaseModel):
        my_field: int = Field(validation_alias='myValidationAlias')



with:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class MyModel(BaseModel):
        my_field: int = Field(
            alias='myValidationAlias',
            serialization_alias='my_field',
        )


    m = MyModel(myValidationAlias=1)
    print(m.model_dump(by_alias=True))
    #> {'my_field': 1}



<a href="" id="field-constraints"></a>

## Numeric Constraints<a href="#numeric-constraints" class="headerlink"
title="Permanent link">¶</a>

There are some keyword arguments that can be used to constrain numeric
values:

- `gt` - greater than
- `lt` - less than
- `ge` - greater than or equal to
- `le` - less than or equal to
- `multiple_of` - a multiple of the given number
- `allow_inf_nan` - allow `'inf'`, `'-inf'`, `'nan'` values

Here's an example:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class Foo(BaseModel):
        positive: int = Field(gt=0)
        non_negative: int = Field(ge=0)
        negative: int = Field(lt=0)
        non_positive: int = Field(le=0)
        even: int = Field(multiple_of=2)
        love_for_pydantic: float = Field(allow_inf_nan=True)


    foo = Foo(
        positive=1,
        non_negative=0,
        negative=-1,
        non_positive=0,
        even=2,
        love_for_pydantic=float('inf'),
    )
    print(foo)
    """
    positive=1 non_negative=0 negative=-1 non_positive=0 even=2 love_for_pydantic=inf
    """



JSON Schema

In the generated JSON schema:

- `gt` and `lt` constraints will be translated to `exclusiveMinimum` and
  `exclusiveMaximum`.
- `ge` and `le` constraints will be translated to `minimum` and
  `maximum`.
- `multiple_of` constraint will be translated to `multipleOf`.

The above snippet will generate the following JSON Schema:

<div class="language-json highlight">

    {
      "title": "Foo",
      "type": "object",
      "properties": {
        "positive": {
          "title": "Positive",
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "non_negative": {
          "title": "Non Negative",
          "type": "integer",
          "minimum": 0
        },
        "negative": {
          "title": "Negative",
          "type": "integer",
          "exclusiveMaximum": 0
        },
        "non_positive": {
          "title": "Non Positive",
          "type": "integer",
          "maximum": 0
        },
        "even": {
          "title": "Even",
          "type": "integer",
          "multipleOf": 2
        },
        "love_for_pydantic": {
          "title": "Love For Pydantic",
          "type": "number"
        }
      },
      "required": [
        "positive",
        "non_negative",
        "negative",
        "non_positive",
        "even",
        "love_for_pydantic"
      ]
    }



See the [JSON Schema Draft
2020-12](https://json-schema.org/understanding-json-schema/reference/numeric.html#numeric-types)
for more details.

<div class="admonition warning">

Constraints on compound types

In case you use field constraints with compound types, an error can
happen in some cases. To avoid potential issues, you can use
`Annotated`:

<div class="language-python highlight">

    from typing import Annotated, Optional

    from pydantic import BaseModel, Field


    class Foo(BaseModel):
        positive: Optional[Annotated[int, Field(gt=0)]]
        # Can error in some cases, not recommended:
        non_negative: Optional[int] = Field(ge=0)





## String Constraints<a href="#string-constraints" class="headerlink"
title="Permanent link">¶</a>

API Documentation

<a href="../../api/types/#pydantic.types.StringConstraints"
class="autorefs autorefs-internal"><code>pydantic.types.StringConstraints</code></a>  

There are fields that can be used to constrain strings:

- `min_length`: Minimum length of the string.
- `max_length`: Maximum length of the string.
- `pattern`: A regular expression that the string must match.

Here's an example:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class Foo(BaseModel):
        short: str = Field(min_length=3)
        long: str = Field(max_length=10)
        regex: str = Field(pattern=r'^\d*$')  # (1)!


    foo = Foo(short='foo', long='foobarbaz', regex='123')
    print(foo)
    #> short='foo' long='foobarbaz' regex='123'



1.  Only digits are allowed.

JSON Schema

In the generated JSON schema:

- `min_length` constraint will be translated to `minLength`.
- `max_length` constraint will be translated to `maxLength`.
- `pattern` constraint will be translated to `pattern`.

The above snippet will generate the following JSON Schema:

<div class="language-json highlight">

    {
      "title": "Foo",
      "type": "object",
      "properties": {
        "short": {
          "title": "Short",
          "type": "string",
          "minLength": 3
        },
        "long": {
          "title": "Long",
          "type": "string",
          "maxLength": 10
        },
        "regex": {
          "title": "Regex",
          "type": "string",
          "pattern": "^\\d*$"
        }
      },
      "required": [
        "short",
        "long",
        "regex"
      ]
    }



## Decimal Constraints<a href="#decimal-constraints" class="headerlink"
title="Permanent link">¶</a>

There are fields that can be used to constrain decimals:

- `max_digits`: Maximum number of digits within the `Decimal`. It does
  not include a zero before the decimal point or trailing decimal
  zeroes.
- `decimal_places`: Maximum number of decimal places allowed. It does
  not include trailing decimal zeroes.

Here's an example:

<div class="language-python highlight">

    from decimal import Decimal

    from pydantic import BaseModel, Field


    class Foo(BaseModel):
        precise: Decimal = Field(max_digits=5, decimal_places=2)


    foo = Foo(precise=Decimal('123.45'))
    print(foo)
    #> precise=Decimal('123.45')



## Dataclass Constraints<a href="#dataclass-constraints" class="headerlink"
title="Permanent link">¶</a>

There are fields that can be used to constrain dataclasses:

- `init`: Whether the field should be included in the `__init__` of the
  dataclass.
- `init_var`: Whether the field should be seen as an [init-only
  field](https://docs.python.org/3/library/dataclasses.html#init-only-variables)
  in the dataclass.
- `kw_only`: Whether the field should be a keyword-only argument in the
  constructor of the dataclass.

Here's an example:

<div class="language-python highlight">

    from pydantic import BaseModel, Field
    from pydantic.dataclasses import dataclass


    @dataclass
    class Foo:
        bar: str
        baz: str = Field(init_var=True)
        qux: str = Field(kw_only=True)


    class Model(BaseModel):
        foo: Foo


    model = Model(foo=Foo('bar', baz='baz', qux='qux'))
    print(model.model_dump())  # (1)!
    #> {'foo': {'bar': 'bar', 'qux': 'qux'}}



1.  The `baz` field is not included in the `model_dump()` output, since
    it is an init-only field.

## Field Representation<a href="#field-representation" class="headerlink"
title="Permanent link">¶</a>

The parameter `repr` can be used to control whether the field should be
included in the string representation of the model.

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str = Field(repr=True)  # (1)!
        age: int = Field(repr=False)


    user = User(name='John', age=42)
    print(user)
    #> name='John'



1.  This is the default value.

## Discriminator<a href="#discriminator" class="headerlink" title="Permanent link">¶</a>

The parameter `discriminator` can be used to control the field that will
be used to discriminate between different models in a union. It takes
either the name of a field or a `Discriminator` instance. The
`Discriminator` approach can be useful when the discriminator fields
aren't the same for all the models in the `Union`.

The following example shows how to use `discriminator` with a field
name:

<div class="tabbed-set tabbed-alternate" tabs="1:2">

<div class="tabbed-labels">

Python 3.9 and abovePython 3.10 and above



<div class="tabbed-content">

<div class="tabbed-block">

<div class="language-python highlight">

    from typing import Literal, Union

    from pydantic import BaseModel, Field


    class Cat(BaseModel):
        pet_type: Literal['cat']
        age: int


    class Dog(BaseModel):
        pet_type: Literal['dog']
        age: int


    class Model(BaseModel):
        pet: Union[Cat, Dog] = Field(discriminator='pet_type')


    print(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}}))  # (1)!
    #> pet=Cat(pet_type='cat', age=12)



1.  See more about [Validating data](../models/#validating-data) in the
    [Models](../models/) page.



<div class="tabbed-block">

<div class="language-python highlight">

    from typing import Literal

    from pydantic import BaseModel, Field


    class Cat(BaseModel):
        pet_type: Literal['cat']
        age: int


    class Dog(BaseModel):
        pet_type: Literal['dog']
        age: int


    class Model(BaseModel):
        pet: Cat | Dog = Field(discriminator='pet_type')


    print(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}}))  # (1)!
    #> pet=Cat(pet_type='cat', age=12)



1.  See more about [Validating data](../models/#validating-data) in the
    [Models](../models/) page.







The following example shows how to use the `discriminator` keyword
argument with a `Discriminator` instance:

<div class="tabbed-set tabbed-alternate" tabs="2:2">

<div class="tabbed-labels">

Python 3.9 and abovePython 3.10 and above



<div class="tabbed-content">

<div class="tabbed-block">

<div class="language-python highlight">

    from typing import Annotated, Literal, Union

    from pydantic import BaseModel, Discriminator, Field, Tag


    class Cat(BaseModel):
        pet_type: Literal['cat']
        age: int


    class Dog(BaseModel):
        pet_kind: Literal['dog']
        age: int


    def pet_discriminator(v):
        if isinstance(v, dict):
            return v.get('pet_type', v.get('pet_kind'))
        return getattr(v, 'pet_type', getattr(v, 'pet_kind', None))


    class Model(BaseModel):
        pet: Union[Annotated[Cat, Tag('cat')], Annotated[Dog, Tag('dog')]] = Field(
            discriminator=Discriminator(pet_discriminator)
        )


    print(repr(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}})))
    #> Model(pet=Cat(pet_type='cat', age=12))

    print(repr(Model.model_validate({'pet': {'pet_kind': 'dog', 'age': 12}})))
    #> Model(pet=Dog(pet_kind='dog', age=12))





<div class="tabbed-block">

<div class="language-python highlight">

    from typing import Annotated, Literal

    from pydantic import BaseModel, Discriminator, Field, Tag


    class Cat(BaseModel):
        pet_type: Literal['cat']
        age: int


    class Dog(BaseModel):
        pet_kind: Literal['dog']
        age: int


    def pet_discriminator(v):
        if isinstance(v, dict):
            return v.get('pet_type', v.get('pet_kind'))
        return getattr(v, 'pet_type', getattr(v, 'pet_kind', None))


    class Model(BaseModel):
        pet: Annotated[Cat, Tag('cat')] | Annotated[Dog, Tag('dog')] = Field(
            discriminator=Discriminator(pet_discriminator)
        )


    print(repr(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}})))
    #> Model(pet=Cat(pet_type='cat', age=12))

    print(repr(Model.model_validate({'pet': {'pet_kind': 'dog', 'age': 12}})))
    #> Model(pet=Dog(pet_kind='dog', age=12))









You can also take advantage of `Annotated` to define your discriminated
unions. See the [Discriminated Unions](../unions/#discriminated-unions)
docs for more details.

## Strict Mode<a href="#strict-mode" class="headerlink" title="Permanent link">¶</a>

The `strict` parameter on a
<a href="../../api/fields/#pydantic.fields.Field"
class="autorefs autorefs-internal"><code>Field</code></a> specifies
whether the field should be validated in "strict mode". In strict mode,
Pydantic throws an error during validation instead of coercing data on
the field where `strict=True`.

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str = Field(strict=True)
        age: int = Field(strict=False)  # (1)!


    user = User(name='John', age='42')  # (2)!
    print(user)
    #> name='John' age=42



1.  This is the default value.
2.  The `age` field is not validated in the strict mode. Therefore, it
    can be assigned a string.

See [Strict Mode](../strict_mode/) for more details.

See [Conversion Table](../conversion_table/) for more details on how
Pydantic converts data in both strict and lax modes.

## Immutability<a href="#immutability" class="headerlink" title="Permanent link">¶</a>

The parameter `frozen` is used to emulate the frozen dataclass
behaviour. It is used to prevent the field from being assigned a new
value after the model is created (immutability).

See the [frozen dataclass
documentation](https://docs.python.org/3/library/dataclasses.html#frozen-instances)
for more details.

<div class="language-python highlight">

    from pydantic import BaseModel, Field, ValidationError


    class User(BaseModel):
        name: str = Field(frozen=True)
        age: int


    user = User(name='John', age=42)

    try:
        user.name = 'Jane'  # (1)!
    except ValidationError as e:
        print(e)
        """
        1 validation error for User
        name
          Field is frozen [type=frozen_field, input_value='Jane', input_type=str]
        """



1.  Since `name` field is frozen, the assignment is not allowed.

## Exclude<a href="#exclude" class="headerlink" title="Permanent link">¶</a>

The `exclude` parameter can be used to control which fields should be
excluded from the model when exporting the model.

See the following example:

<div class="language-python highlight">

    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str
        age: int = Field(exclude=True)


    user = User(name='John', age=42)
    print(user.model_dump())  # (1)!
    #> {'name': 'John'}



1.  The `age` field is not included in the `model_dump()` output, since
    it is excluded.

See the
[Serialization](../serialization/#model-and-field-level-include-and-exclude)
section for more details.

## Deprecated fields<a href="#deprecated-fields" class="headerlink"
title="Permanent link">¶</a>

The `deprecated` parameter can be used to mark a field as being
deprecated. Doing so will result in:

- a runtime deprecation warning emitted when accessing the field.
- `"deprecated": true` being set in the generated JSON schema.

You can set the `deprecated` parameter as one of:

- A string, which will be used as the deprecation message.
- An instance of the `warnings.deprecated` decorator (or the
  `typing_extensions` backport).
- A boolean, which will be used to mark the field as deprecated with a
  default `'deprecated'` deprecation message.

### `deprecated` as a string<a href="#deprecated-as-a-string" class="headerlink"
title="Permanent link">¶</a>

<div class="language-python highlight">

    from typing import Annotated

    from pydantic import BaseModel, Field


    class Model(BaseModel):
        deprecated_field: Annotated[int, Field(deprecated='This is deprecated')]


    print(Model.model_json_schema()['properties']['deprecated_field'])
    #> {'deprecated': True, 'title': 'Deprecated Field', 'type': 'integer'}



### `deprecated` via the `warnings.deprecated` decorator<a href="#deprecated-via-the-warningsdeprecated-decorator"
class="headerlink" title="Permanent link">¶</a>

<div class="admonition note">

Note

You can only use the `deprecated` decorator in this way if you have
`typing_extensions` \>= 4.9.0 installed.



<div class="language-python highlight">

    import importlib.metadata
    from typing import Annotated, deprecated

    from packaging.version import Version

    from pydantic import BaseModel, Field

    if Version(importlib.metadata.version('typing_extensions')) >= Version('4.9'):

        class Model(BaseModel):
            deprecated_field: Annotated[int, deprecated('This is deprecated')]

            # Or explicitly using `Field`:
            alt_form: Annotated[
                int, Field(deprecated=deprecated('This is deprecated'))
            ]



### `deprecated` as a boolean<a href="#deprecated-as-a-boolean" class="headerlink"
title="Permanent link">¶</a>

<div class="language-python highlight">

    from typing import Annotated

    from pydantic import BaseModel, Field


    class Model(BaseModel):
        deprecated_field: Annotated[int, Field(deprecated=True)]


    print(Model.model_json_schema()['properties']['deprecated_field'])
    #> {'deprecated': True, 'title': 'Deprecated Field', 'type': 'integer'}



<div class="admonition note">

Support for `category` and `stacklevel`

The current implementation of this feature does not take into account
the `category` and `stacklevel` arguments to the `deprecated` decorator.
This might land in a future version of Pydantic.



<div class="admonition warning">

Accessing a deprecated field in validators

When accessing a deprecated field inside a validator, the deprecation
warning will be emitted. You can use <a
href="https://docs.python.org/3/library/warnings.html#warnings.catch_warnings"
class="autorefs autorefs-external"><code>catch_warnings</code></a> to
explicitly ignore it:

<div class="language-python highlight">

    import warnings

    from typing_extensions import Self

    from pydantic import BaseModel, Field, model_validator


    class Model(BaseModel):
        deprecated_field: int = Field(deprecated='This is deprecated')

        @model_validator(mode='after')
        def validate_model(self) -> Self:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', DeprecationWarning)
                self.deprecated_field = self.deprecated_field * 2





## Customizing JSON Schema<a href="#customizing-json-schema" class="headerlink"
title="Permanent link">¶</a>

Some field parameters are used exclusively to customize the generated
JSON schema. The parameters in question are:

- `title`
- `description`
- `examples`
- `json_schema_extra`

Read more about JSON schema customization / modification with fields in
the [Customizing JSON Schema](../json_schema/#field-level-customization)
section of the JSON schema docs.

## The `computed_field` decorator<a href="#the-computed_field-decorator" class="headerlink"
title="Permanent link">¶</a>

API Documentation

<a href="../../api/fields/#pydantic.fields.computed_field"
class="autorefs autorefs-internal"><code>computed_field</code></a>  

The <a href="../../api/fields/#pydantic.fields.computed_field"
class="autorefs autorefs-internal"><code>computed_field</code></a>
decorator can be used to include
<a href="https://docs.python.org/3/library/functions.html#property"
class="autorefs autorefs-external"><code>property</code></a> or <a
href="https://docs.python.org/3/library/functools.html#functools.cached_property"
class="autorefs autorefs-external"><code>cached_property</code></a>
attributes when serializing a model or dataclass. The property will also
be taken into account in the JSON Schema (in serialization mode).

<div class="admonition note">

Note

Properties can be useful for fields that are computed from other fields,
or for fields that are expensive to be computed (and thus, are cached if
using <a
href="https://docs.python.org/3/library/functools.html#functools.cached_property"
class="autorefs autorefs-external"><code>cached_property</code></a>).

However, note that Pydantic will *not* perform any additional logic on
the wrapped property (validation, cache invalidation, etc.).



Here's an example of the JSON schema (in serialization mode) generated
for a model with a computed field:

<div class="language-python highlight">

    from pydantic import BaseModel, computed_field


    class Box(BaseModel):
        width: float
        height: float
        depth: float

        @computed_field
        @property  # (1)!
        def volume(self) -> float:
            return self.width * self.height * self.depth


    print(Box.model_json_schema(mode='serialization'))
    """
    {
        'properties': {
            'width': {'title': 'Width', 'type': 'number'},
            'height': {'title': 'Height', 'type': 'number'},
            'depth': {'title': 'Depth', 'type': 'number'},
            'volume': {'readOnly': True, 'title': 'Volume', 'type': 'number'},
        },
        'required': ['width', 'height', 'depth', 'volume'],
        'title': 'Box',
        'type': 'object',
    }
    """



1.  If not specified,
    <a href="../../api/fields/#pydantic.fields.computed_field"
    class="autorefs autorefs-internal"><code>computed_field</code></a>
    will implicitly convert the method to a
    <a href="https://docs.python.org/3/library/functions.html#property"
    class="autorefs autorefs-external"><code>property</code></a>.
    However, it is preferable to explicitly use the
    <a href="https://docs.python.org/3/library/functions.html#property"
    class="autorefs autorefs-external"><code>@property</code></a>
    decorator for type checking purposes.

Here's an example using the `model_dump` method with a computed field:

<div class="language-python highlight">

    from pydantic import BaseModel, computed_field


    class Box(BaseModel):
        width: float
        height: float
        depth: float

        @computed_field
        @property
        def volume(self) -> float:
            return self.width * self.height * self.depth


    b = Box(width=1, height=2, depth=3)
    print(b.model_dump())
    #> {'width': 1.0, 'height': 2.0, 'depth': 3.0, 'volume': 6.0}



As with regular fields, computed fields can be marked as being
deprecated:

<div class="language-python highlight">

    from typing_extensions import deprecated

    from pydantic import BaseModel, computed_field


    class Box(BaseModel):
        width: float
        height: float
        depth: float

        @computed_field
        @property
        @deprecated("'volume' is deprecated")
        def volume(self) -> float:
            return self.width * self.height * self.depth



Was this page helpful?

<div class="md-feedback__inner">

<div class="md-feedback__list">





<div class="md-feedback__note">

<div md-value="1" hidden="">

Thanks for your feedback!



<div md-value="0" hidden="">

Thanks for your feedback!















<div class="md-footer-meta md-typeset">

<div class="md-footer-meta__inner md-grid">

<div class="md-copyright">

Made with
<a href="https://squidfunk.github.io/mkdocs-material/" target="_blank"
rel="noopener">Material for MkDocs</a>









<div class="md-dialog" md-component="dialog">

<div class="md-dialog__inner md-typeset">





<div class="md-progress" md-component="progress" role="progressbar">



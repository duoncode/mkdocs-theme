Home Page
=========

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem
ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing
elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna
aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo
dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus
est Lorem ipsum dolor sit amet.

## Code Block

```php
<?php

declare(strict_types=1);

namespace Conia\Boiler;


class Layout extends Template
{
    protected string $str = 'Chuck';
    protected int $number = 666;
    protected bool $is = false;

    public function __construct(
        Engine $engine,
        string $path,
        array $context,
        protected readonly string $body,
    ) {
        parent::__construct($engine, $path, $context);
    }

    /**
     * Used in the layout template to get the content of the wrapped template
     */
    public function body(): string
    {
        $s = "hans";
        return $this->body;
    }
}
```

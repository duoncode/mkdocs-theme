<?php

declare(strict_types=1);

namespace Conia\Boiler;

use Conia\Boiler\Engine;

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
     * The colors match the album cover of Scream Bloody Gore very well
     */
    public function body(): string
    {
        $s = "hans";
        return $this->body . $this->pad($s) . $this::class;
    }

    protected function pad(string $value): string
    {
        // Strange comment
        $text = <<<EOF
            Images of the forgotten past
            Your first life revealed at last
        EOF;

        return $text . str_pad($value, 10, '-');
    }
}


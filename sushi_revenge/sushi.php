<?php

highlight_file(__FILE__);

$waf = Array("'", "\"", "^", "|", "l", "p");

$_ = $_GET['🍣'];

if(isset($_)) {

    sort($_);

    $s = '';
    for($i = 0; $i < count($_); $i++)
        $s .= chr($_[$i]);

    if(preg_match("/[\w]{5,}/is", $s))
        die("GG");

    for($i = 0; $i < count($waf); $i++)
        if(strpos($s, $waf[$i]) !== FALSE)
            die("GG");

    eval(substr($s, 0, 25));
}
?>

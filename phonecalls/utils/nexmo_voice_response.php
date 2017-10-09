<?php
$text = trim(htmlspecialchars($_GET['text']));

$talk = Array();
$talk["action"] = "talk";
$talk["voiceName"] = "Russell";
$talk["text"] = "$text";

$response = [$talk];
file_put_contents('answer.json', json_encode($response, JSON_PRETTY_PRINT));

echo json_encode($response, JSON_PRETTY_PRINT);
?>
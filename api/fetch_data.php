<?php
header('Content-Type: application/json');

$data = json_decode(file_get_contents("php://input"));

$name = $data->name;
$email = $data->email;

$response = ["message" => "Hello, $name! Email $email received successfully."];
echo json_encode($response);
?>

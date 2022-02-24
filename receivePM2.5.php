<?php
header("Content-type:text/html;charset=utf-8");
$pm = $_GET['pm'];
$dsn = 'mysql:dbname=pm;host=127.0.0.1;port=3306';
$username = '';
$password = '';
try {
    $pdo = new PDO($dsn, $username, $password);
} catch(PDOException $e) {
    die('Could not connect to the database:
' . $e);
}
$pdo->query('set names utf8');
$sql = "insert into pm(data) values(\"".$pm."\")";
$result = $pdo->exec($sql);
print_R($result);
?>

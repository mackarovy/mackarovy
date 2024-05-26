<?php
$file = "/home/admin1/mackarovy/r.txt";

if(isset($_POST["content"])) {
    $newContent = $_POST["content"];

    $fp = fopen($file, "w");

    if ($fp) {
        fwrite($fp, $newContent);
    
        fclose($fp);

        echo "Содержимое файла успешно изменено на $newContent";
    } else {
        echo "Ошибка открытия файла для записи";
    }
} else {
    echo "Произошла ошибка при изменении файла";
}
?>



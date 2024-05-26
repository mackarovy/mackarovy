<?php
$fileLight = "/home/admin1/mackarovy/light_sensor_pin.txt";
if(isset($_POST["brightness"])) {
    $brightness = $_POST["brightness"];

    $fp = fopen($fileLight, "w");

    if ($fp) {
        fwrite($fp, $brightness);
    
        fclose($fp);

        echo "Уровень освещенности успешно установлен на $brightness";
    } else {
        echo "Ошибка открытия файла lightsensorpin.txt для записи";
    }
} else {
    echo "Произошла ошибка при установке уровня освещенности";
}
?>

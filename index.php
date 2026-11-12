<?php
$NamaNasabah = $_POST['nama'];
$SaldoAwal = $_POST['saldo'];
$hasil = "Nama Nasabah adalah " . $NamaNasabah . "<br>Saldo Awal adalah " . $SaldoAwal;
$hasilDeposit = $SaldoAwal - (($SaldoAwal * 0.03) * 11);
echo $hasil;
echo "<p>Hasil Deposit adalah " . $hasilDeposit . "</p>";
?>
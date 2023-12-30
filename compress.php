<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Get file and compression level
  $file = $_FILES['pdf_file'];
  $compressionLevel = $_POST['compression_level'];
  $compressionPercentage = $_POST['compression_percentage'];

  // Check if file is a PDF
  if ($file['type'] !== 'application/pdf') {
    echo json_encode(['error' => 'File must be a PDF.']);
    exit;
  }

  // Get original file size
  $originalFileSize = $file['size'];

  // Set compression options based on compression level
  switch ($compressionLevel) {
    case 'high':
      $compressionOptions = '-q 0';
      break;
    case 'medium':
      $compressionOptions = '-q 5';
      break;
    case 'low':
      $compressionOptions = '-q 10';
      break;
    case 'percentage':
      $compressionOptions = '-q ' . (100 - $compressionPercentage);
      break;
  }

  // Create temporary file name
  $tempFileName = tempnam(sys_get_temp_dir(), 'pdf');

  // Compress PDF using ghostscript
  exec("gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 $compressionOptions -o $tempFileName {$file['tmp_name']}", $output, $returnCode);

  // Check if compression was successful
  if ($returnCode !== 0) {
    echo json_encode(['error' => 'Error compressing PDF.']);
    exit;
  }

  // Get compressed file size
  $compressedFileSize = filesize($tempFileName);

  // Generate download link for compressed file
  $compressedFilePath = 'compressed.pdf';
  copy($tempFileName, $compressedFilePath);
  $downloadLink = 'http://' . $_SERVER['HTTP_HOST'] . '/' . $compressedFilePath;

  // Delete temporary file
  unlink($tempFileName);

  // Return results as JSON
  echo json_encode([
    'originalFileSize' => $originalFileSize,
    'compressedFileSize' => $compressedFileSize,
    'compressedFilePath' => $downloadLink
  ]);
} else {
  echo 'Invalid request method.';
  }
  ?>
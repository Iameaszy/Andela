def binary_converter(k):
  if not (isinstance(k, int) and k >= 0 and k <= 255):
    return "Invalid input"
  return bin(k)[2:]
import math

def main():
  print('#1 Picnic')
  can_radious = 6.83
  can_height = 10.16
  can_volume = compute_volume(can_radious, can_height)
  can_surface = compute_surface_area(can_radious, can_height)
  storage_efficiency = compute_storage_efficiency(can_volume, can_surface)
  print(f'The can has Radius: {can_radious} - Height: {can_height} - Volume: {can_volume:.2f}')
  print(f'Surface: {can_surface:.2f} - Storage Efficiency: {storage_efficiency:.2f}')
        
def compute_volume(radious, height):
  """Calculates the volume by using
  the radious and the height"""
  volume = math.pi * radious **2 * height
  return volume

def compute_surface_area(radious, height):
  """Calculates the surface area using
  the volume and height"""
  surface_area = 2 * math.pi * radious * (radious + height)
  return surface_area 
  
def compute_storage_efficiency(volume, surface_area):
  """Calculates the storage efficiency 
  using the volume and and surface"""
  storage_efficiency = volume / surface_area
  return storage_efficiency

main()
import math

def main():
  # print('#1 Picnic')
  # can_radious = 6.83
  # can_height = 10.16
  # can_volume = compute_volume(can_radious, can_height)
  # can_surface = compute_surface_area(can_radious, can_height)
  # storage_efficiency = compute_storage_efficiency(can_volume, can_surface)
  # print(f'The can has Radius: {can_radious} - Height: {can_height} - Volume: {can_volume:.2f}')
  # print(f'Surface: {can_surface:.2f} - Storage Efficiency: {storage_efficiency:.2f}')
  can_efficiency('#1 Picnic', 6.83, 10.16)
  can_efficiency('#1 Tall', 7.78, 11.91)
  can_efficiency('#2', 8.73, 11.59)
  can_efficiency('#2.5', 10.32, 11.91)
  can_efficiency('#3 Cylinder', 10.79, 17.78)
  can_efficiency('#5', 13.02, 14.29)
  can_efficiency('#6Z', 5.40,8.89)
  can_efficiency('#8Z short', 6.83, 7.62)
  can_efficiency('#10', 15.72, 17.78)
  can_efficiency('#211', 6.83, 12.38)
  can_efficiency('#300', 7.62, 11.27)
  can_efficiency('#303', 8.10, 11.11)
        
def can_efficiency(name, radious, height):
  can_volume = compute_volume(radious, height)
  can_surface = compute_surface_area(radious, height)
  storage_efficiency = compute_storage_efficiency(can_volume, can_surface)
  print(f'-----------------------{name}-----------------------')
  print(f'The can has Radius: {radious} - Height: {height} - Volume: {can_volume:.2f}')
  print(f'Surface: {can_surface:.2f} - Storage Efficiency: {storage_efficiency:.2f}')
  print('--------------------------------------------------------------')
  
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
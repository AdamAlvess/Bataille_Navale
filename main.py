from map import Map

def main():
    map_obj = Map(10, 10)
    map_obj.place_boat(3, 5, 1, 'v')
    map_obj.display()
    
if __name__ == '__main__':
    main()
